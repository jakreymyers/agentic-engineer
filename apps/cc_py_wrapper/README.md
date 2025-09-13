# Claude Code Python SDK Wrapper

A reusable, three-file wrapper system for calling agents via the Claude Code Python SDK. Provides simple functions for adhoc prompts and reusable slash commands with full Pydantic type safety.

## Features

- **Simple API**: Two main functions - `adhoc_prompt()` and `reusable_prompt()`
- **Type Safety**: Full Pydantic validation for all inputs and outputs
- **CLI Interface**: Command-line tool for quick testing and automation
- **Streaming Support**: Real-time response streaming
- **Slash Commands**: Create reusable command configurations
- **Error Handling**: Comprehensive error handling with detailed responses

## Installation

```bash
cd apps/cc_py_wrapper
uv install
```

## Quick Start

### Basic Usage

```python
import asyncio
from cc_py_wrapper import adhoc_prompt, WrapperSettings

async def main():
    # Simple prompt
    response = await adhoc_prompt("What is the capital of France?")
    print(response.messages[0].content)
    
    # With custom settings
    settings = WrapperSettings(
        system_prompt="You are a helpful coding assistant",
        allowed_tools=["Read", "Bash", "Grep"],
        max_turns=10
    )
    
    response = await adhoc_prompt("Analyze this Python file", settings)
    for msg in response.messages:
        print(msg.content)

asyncio.run(main())
```

### Slash Commands

```python
from cc_py_wrapper import reusable_prompt, SlashCommandConfig, WrapperSettings

# Create a reusable command
code_review_command = SlashCommandConfig(
    command_name="code_review",
    description="Perform thorough code review",
    system_prompt="You are a senior code reviewer...",
    default_settings=WrapperSettings(
        allowed_tools=["Read", "Grep", "Bash"],
        max_turns=15
    ),
    required_tools=["Read"]
)

# Use the command
response = await reusable_prompt(
    code_review_command, 
    "Review the authentication module in src/auth/"
)
```

## CLI Usage

### Basic Prompts

```bash
# Simple prompt
cc-wrapper prompt "What is the current directory structure?"

# With custom settings
cc-wrapper prompt "Analyze the code quality" \
  --system-prompt "You are a code quality expert" \
  --tools "Read,Grep,Bash" \
  --max-turns 15 \
  --stream
```

### Slash Commands

```bash
# Create example command config
cc-wrapper commands example code_review.json

# Create command from config
cc-wrapper commands create code_review.json

# List registered commands
cc-wrapper commands list

# Run a command
cc-wrapper commands run code_review "Check the API endpoints"
```

## API Reference

### Core Functions

#### `adhoc_prompt(prompt: str, settings: Optional[WrapperSettings] = None) -> AgentResponse`

Execute a one-time prompt with the Claude Code agent.

**Parameters:**
- `prompt`: The text prompt to send
- `settings`: Optional configuration settings

**Returns:** `AgentResponse` with messages and metadata

#### `reusable_prompt(custom_slash_command: SlashCommandConfig, user_input: str, settings: Optional[WrapperSettings] = None) -> AgentResponse`

Execute a reusable slash command with user input.

**Parameters:**
- `custom_slash_command`: The slash command configuration
- `user_input`: User input to process
- `settings`: Optional settings override

**Returns:** `AgentResponse` with messages and metadata

#### `stream_adhoc_prompt(prompt: str, settings: Optional[WrapperSettings] = None) -> AsyncGenerator[AgentMessage, None]`

Stream responses from an adhoc prompt in real-time.

### Type Models

#### `WrapperSettings`
Configuration for Claude Code agents:
- `system_prompt`: Custom system prompt
- `model`: Claude model to use
- `max_turns`: Maximum conversation turns
- `allowed_tools`: List of permitted tools
- `permission_mode`: Tool permission mode
- `working_directory`: Working directory
- `environment_variables`: Environment variables
- `debug_mode`: Enable debug output
- `timeout_seconds`: Request timeout
- `mcp_servers`: MCP server configurations

#### `SlashCommandConfig`
Configuration for reusable commands:
- `command_name`: Unique command identifier
- `description`: Command description
- `system_prompt`: Command-specific system prompt
- `default_settings`: Default settings for the command
- `required_tools`: Tools required by the command
- `examples`: Usage examples

#### `AgentResponse`
Response from agent execution:
- `messages`: List of agent messages
- `session_id`: Session identifier
- `total_tokens`: Token usage
- `success`: Success status
- `error_message`: Error details if failed
- `execution_time`: Execution duration

## File Structure

```
apps/cc_py_wrapper/
├── __init__.py          # Package exports
├── types.py             # Pydantic type definitions
├── wrapper.py           # Core wrapper functions
├── cli.py               # Command-line interface
├── pyproject.toml       # Project configuration
└── README.md            # This file
```

## Examples

See the `examples/` directory for more detailed usage examples and slash command configurations.

## Development

```bash
# Install development dependencies
uv install --dev

# Run tests
uv run pytest

# Format code
uv run black .
uv run isort .
```

## License

This project is licensed under the MIT License.