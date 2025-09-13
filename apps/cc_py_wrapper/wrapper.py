"""Core wrapper functions for Claude Code Python SDK."""

import asyncio
import time
import logging
from typing import AsyncGenerator, Optional, Dict, Any
from contextlib import asynccontextmanager

try:
    from claude_code_sdk import ClaudeSDKClient, ClaudeCodeOptions
except ImportError:
    # Fallback for development/testing
    ClaudeSDKClient = None
    ClaudeCodeOptions = None

from .types import (
    WrapperSettings,
    PromptRequest,
    AgentResponse,
    AgentMessage,
    SlashCommandConfig,
    WrapperError
)

logger = logging.getLogger(__name__)


class WrapperException(Exception):
    """Custom exception for wrapper operations."""
    pass


def _convert_settings_to_options(settings: Optional[WrapperSettings]) -> Optional[Dict[str, Any]]:
    """Convert WrapperSettings to ClaudeCodeOptions format."""
    if not settings:
        return None
    
    options = {}
    
    # Core settings
    if settings.system_prompt:
        options["system_prompt"] = settings.system_prompt
    if settings.model:
        options["model"] = settings.model.value
    if settings.max_turns:
        options["max_turns"] = settings.max_turns
    if settings.max_thinking_tokens is not None:
        options["max_thinking_tokens"] = settings.max_thinking_tokens
    
    # Tool configuration
    if settings.allowed_tools:
        options["allowed_tools"] = settings.allowed_tools
    if settings.permission_mode:
        options["permission_mode"] = settings.permission_mode.value
    
    # Environment settings
    if settings.working_directory:
        options["working_directory"] = settings.working_directory
    if settings.environment_variables:
        options["environment_variables"] = settings.environment_variables
    
    # MCP servers
    if settings.mcp_servers:
        options["mcp_servers"] = settings.mcp_servers
    
    return options


@asynccontextmanager
async def _create_client(settings: Optional[WrapperSettings]):
    """Create and manage Claude SDK client lifecycle."""
    if ClaudeSDKClient is None:
        raise WrapperException("claude-code-sdk not installed. Run: uv add claude-code-sdk")
    
    options_dict = _convert_settings_to_options(settings)
    options = ClaudeCodeOptions(**options_dict) if options_dict else ClaudeCodeOptions()
    
    async with ClaudeSDKClient(options=options) as client:
        yield client


async def adhoc_prompt(prompt: str, settings: Optional[WrapperSettings] = None) -> AgentResponse:
    """
    Execute an adhoc prompt with Claude Code agent.
    
    Args:
        prompt: The prompt text to send to the agent
        settings: Optional configuration settings for the agent
        
    Returns:
        AgentResponse containing the agent's response and metadata
        
    Raises:
        WrapperException: If there's an error executing the prompt
    """
    start_time = time.time()
    
    try:
        async with _create_client(settings) as client:
            # Send query
            await client.query(prompt)
            
            messages = []
            async for message in client.receive_response():
                # Convert SDK message to our format
                agent_msg = AgentMessage(
                    content=str(message),
                    message_type="text",  # Could be enhanced to detect type
                    timestamp=None,
                    metadata=None
                )
                messages.append(agent_msg)
            
            execution_time = time.time() - start_time
            
            return AgentResponse(
                messages=messages,
                session_id=None,  # Could be enhanced with session tracking
                success=True,
                execution_time=execution_time
            )
            
    except Exception as e:
        execution_time = time.time() - start_time
        logger.error(f"Error in adhoc_prompt: {e}")
        
        return AgentResponse(
            messages=[],
            success=False,
            error_message=str(e),
            execution_time=execution_time
        )


async def reusable_prompt(
    custom_slash_command: SlashCommandConfig, 
    user_input: str,
    settings: Optional[WrapperSettings] = None
) -> AgentResponse:
    """
    Execute a reusable prompt using a custom slash command configuration.
    
    Args:
        custom_slash_command: Configuration for the custom command
        user_input: User input to process with the command
        settings: Optional additional settings (merged with command defaults)
        
    Returns:
        AgentResponse containing the agent's response and metadata
        
    Raises:
        WrapperException: If there's an error executing the prompt
    """
    start_time = time.time()
    
    try:
        # Merge settings
        merged_settings = custom_slash_command.default_settings or WrapperSettings()
        if settings:
            # Override with provided settings
            merged_dict = merged_settings.model_dump()
            override_dict = settings.model_dump(exclude_unset=True)
            merged_dict.update(override_dict)
            merged_settings = WrapperSettings(**merged_dict)
        
        # Set system prompt from slash command
        merged_settings.system_prompt = custom_slash_command.system_prompt
        
        # Add required tools if specified
        if custom_slash_command.required_tools:
            if merged_settings.allowed_tools:
                merged_settings.allowed_tools.extend(custom_slash_command.required_tools)
            else:
                merged_settings.allowed_tools = custom_slash_command.required_tools.copy()
        
        # Create the full prompt
        full_prompt = f"Command: {custom_slash_command.command_name}\nDescription: {custom_slash_command.description}\n\nUser Input: {user_input}"
        
        # Execute using adhoc_prompt
        response = await adhoc_prompt(full_prompt, merged_settings)
        
        # Add command metadata
        if response.messages:
            for msg in response.messages:
                if msg.metadata is None:
                    msg.metadata = {}
                msg.metadata["slash_command"] = custom_slash_command.command_name
        
        return response
        
    except Exception as e:
        execution_time = time.time() - start_time
        logger.error(f"Error in reusable_prompt: {e}")
        
        return AgentResponse(
            messages=[],
            success=False,
            error_message=str(e),
            execution_time=execution_time
        )


async def stream_adhoc_prompt(
    prompt: str, 
    settings: Optional[WrapperSettings] = None
) -> AsyncGenerator[AgentMessage, None]:
    """
    Execute an adhoc prompt and stream responses in real-time.
    
    Args:
        prompt: The prompt text to send to the agent
        settings: Optional configuration settings for the agent
        
    Yields:
        AgentMessage objects as they are received from the agent
        
    Raises:
        WrapperException: If there's an error executing the prompt
    """
    try:
        async with _create_client(settings) as client:
            await client.query(prompt)
            
            async for message in client.receive_response():
                yield AgentMessage(
                    content=str(message),
                    message_type="text",
                    timestamp=None,
                    metadata=None
                )
                
    except Exception as e:
        logger.error(f"Error in stream_adhoc_prompt: {e}")
        yield AgentMessage(
            content=f"Error: {str(e)}",
            message_type="text",
            metadata={"error": True}
        )


# Utility functions for command management
_registered_commands: Dict[str, SlashCommandConfig] = {}


def register_slash_command(command: SlashCommandConfig) -> None:
    """Register a slash command for reuse."""
    _registered_commands[command.command_name] = command


def get_registered_command(command_name: str) -> Optional[SlashCommandConfig]:
    """Get a registered slash command by name."""
    return _registered_commands.get(command_name)


def list_registered_commands() -> Dict[str, SlashCommandConfig]:
    """List all registered slash commands."""
    return _registered_commands.copy()


def unregister_slash_command(command_name: str) -> bool:
    """Unregister a slash command."""
    if command_name in _registered_commands:
        del _registered_commands[command_name]
        return True
    return False