"""Pydantic types for Claude Code Python SDK wrapper system."""

from typing import List, Optional, Dict, Any, Literal, Union
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum


class PermissionMode(str, Enum):
    """Permission modes for Claude Code agents."""
    ASK = "ask"
    ALLOW_ALL = "allow_all"
    DENY_ALL = "deny_all"


class ModelType(str, Enum):
    """Available Claude models."""
    CLAUDE_3_5_SONNET = "claude-3-5-sonnet-20241022"
    CLAUDE_3_5_HAIKU = "claude-3-5-haiku-20241022"
    CLAUDE_3_OPUS = "claude-3-opus-20240229"


class WrapperSettings(BaseModel):
    """Configuration settings for Claude Code wrapper."""
    model_config = ConfigDict(extra="forbid")
    
    # Core settings
    system_prompt: Optional[str] = None
    model: ModelType = ModelType.CLAUDE_3_5_SONNET
    max_turns: int = Field(default=20, ge=1, le=100)
    max_thinking_tokens: Optional[int] = Field(default=None, ge=0)
    
    # Tool configuration
    allowed_tools: Optional[List[str]] = None
    permission_mode: PermissionMode = PermissionMode.ASK
    
    # Environment settings
    working_directory: Optional[str] = None
    environment_variables: Optional[Dict[str, str]] = None
    
    # Advanced settings
    debug_mode: bool = False
    timeout_seconds: Optional[int] = Field(default=300, ge=1)
    
    # MCP server configuration
    mcp_servers: Optional[List[Dict[str, Any]]] = None


class PromptRequest(BaseModel):
    """Request model for prompt execution."""
    model_config = ConfigDict(extra="forbid")
    
    prompt: str = Field(..., min_length=1)
    settings: Optional[WrapperSettings] = None
    session_id: Optional[str] = None


class AgentMessage(BaseModel):
    """Individual message from the agent."""
    model_config = ConfigDict(extra="forbid")
    
    content: str
    message_type: Literal["text", "tool_use", "tool_result", "thinking"] = "text"
    timestamp: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class AgentResponse(BaseModel):
    """Response from Claude Code agent."""
    model_config = ConfigDict(extra="forbid")
    
    messages: List[AgentMessage]
    session_id: Optional[str] = None
    total_tokens: Optional[int] = None
    thinking_tokens: Optional[int] = None
    success: bool = True
    error_message: Optional[str] = None
    execution_time: Optional[float] = None


class SlashCommandConfig(BaseModel):
    """Configuration for custom slash commands."""
    model_config = ConfigDict(extra="forbid")
    
    command_name: str = Field(..., regex=r"^[a-zA-Z][a-zA-Z0-9_-]*$")
    description: str
    system_prompt: str
    default_settings: Optional[WrapperSettings] = None
    required_tools: Optional[List[str]] = None
    examples: Optional[List[str]] = None


class WrapperError(BaseModel):
    """Error response from wrapper system."""
    model_config = ConfigDict(extra="forbid")
    
    error_type: str
    error_message: str
    details: Optional[Dict[str, Any]] = None
    session_id: Optional[str] = None