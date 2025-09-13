"""Simple test file for Claude Code Python SDK wrapper."""

import pytest
import asyncio
from unittest.mock import AsyncMock, patch

from cc_py_wrapper.types import WrapperSettings, SlashCommandConfig, ModelType, AgentResponse
from cc_py_wrapper.wrapper import (
    _convert_settings_to_options,
    register_slash_command,
    get_registered_command,
    list_registered_commands,
    unregister_slash_command
)


def test_convert_settings_to_options():
    """Test settings conversion to options format."""
    settings = WrapperSettings(
        system_prompt="Test prompt",
        model=ModelType.CLAUDE_3_5_SONNET,
        max_turns=10,
        allowed_tools=["Read", "Bash"],
        debug_mode=True
    )
    
    options = _convert_settings_to_options(settings)
    
    assert options["system_prompt"] == "Test prompt"
    assert options["model"] == "claude-3-5-sonnet-20241022"
    assert options["max_turns"] == 10
    assert options["allowed_tools"] == ["Read", "Bash"]


def test_convert_settings_none():
    """Test None settings conversion."""
    options = _convert_settings_to_options(None)
    assert options is None


def test_slash_command_registration():
    """Test slash command registration and retrieval."""
    command = SlashCommandConfig(
        command_name="test_command",
        description="Test command",
        system_prompt="Test system prompt"
    )
    
    # Test registration
    register_slash_command(command)
    
    # Test retrieval
    retrieved = get_registered_command("test_command")
    assert retrieved is not None
    assert retrieved.command_name == "test_command"
    assert retrieved.description == "Test command"
    
    # Test listing
    commands = list_registered_commands()
    assert "test_command" in commands
    
    # Test unregistration
    success = unregister_slash_command("test_command")
    assert success is True
    
    # Verify removal
    retrieved_after = get_registered_command("test_command")
    assert retrieved_after is None
    
    # Test unregistering non-existent command
    success_nonexistent = unregister_slash_command("nonexistent")
    assert success_nonexistent is False


def test_wrapper_settings_validation():
    """Test WrapperSettings validation."""
    # Valid settings
    settings = WrapperSettings(
        max_turns=10,
        timeout_seconds=300
    )
    assert settings.max_turns == 10
    assert settings.timeout_seconds == 300
    
    # Test default values
    default_settings = WrapperSettings()
    assert default_settings.max_turns == 20
    assert default_settings.timeout_seconds == 300
    assert default_settings.model == ModelType.CLAUDE_3_5_SONNET


def test_slash_command_config_validation():
    """Test SlashCommandConfig validation."""
    # Valid config
    config = SlashCommandConfig(
        command_name="valid_command",
        description="A valid command",
        system_prompt="System prompt"
    )
    assert config.command_name == "valid_command"
    
    # Test with invalid command name (should raise validation error)
    with pytest.raises(ValueError):
        SlashCommandConfig(
            command_name="invalid-command-with-spaces and symbols!",
            description="Invalid command",
            system_prompt="System prompt"
        )


@pytest.mark.asyncio
async def test_adhoc_prompt_mock():
    """Test adhoc_prompt with mocked Claude SDK."""
    from cc_py_wrapper.wrapper import adhoc_prompt
    
    # Mock the Claude SDK components
    with patch('cc_py_wrapper.wrapper.ClaudeSDKClient') as mock_client_class:
        mock_client = AsyncMock()
        mock_client_class.return_value.__aenter__.return_value = mock_client
        
        # Mock the response stream
        async def mock_receive_response():
            yield "Test response message"
            yield "Second message part"
        
        mock_client.receive_response.return_value = mock_receive_response()
        
        # Test the function
        response = await adhoc_prompt("Test prompt")
        
        # Verify the response
        assert response.success is True
        assert len(response.messages) == 2
        assert response.messages[0].content == "Test response message"
        assert response.messages[1].content == "Second message part"
        assert response.execution_time is not None


if __name__ == "__main__":
    pytest.main([__file__])