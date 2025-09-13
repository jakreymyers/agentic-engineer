"""Command-line interface for Claude Code Python SDK wrapper."""

import asyncio
import json
import sys
from pathlib import Path
from typing import Optional

import click

from .types import WrapperSettings, SlashCommandConfig, ModelType, PermissionMode
from .wrapper import (
    adhoc_prompt,
    reusable_prompt,
    stream_adhoc_prompt,
    register_slash_command,
    get_registered_command,
    list_registered_commands,
    WrapperException
)


@click.group()
@click.version_option(version="0.1.0")
def main():
    """Claude Code Python SDK Wrapper CLI.
    
    A simple interface for executing prompts and managing slash commands.
    """
    pass


@main.command()
@click.argument("prompt", required=True)
@click.option("--model", type=click.Choice([m.value for m in ModelType]), default=ModelType.CLAUDE_3_5_SONNET.value)
@click.option("--max-turns", type=int, default=20, help="Maximum conversation turns")
@click.option("--system-prompt", type=str, help="System prompt for the agent")
@click.option("--tools", type=str, help="Comma-separated list of allowed tools")
@click.option("--permission-mode", type=click.Choice([p.value for p in PermissionMode]), default=PermissionMode.ASK.value)
@click.option("--working-dir", type=click.Path(exists=True), help="Working directory for the agent")
@click.option("--timeout", type=int, default=300, help="Timeout in seconds")
@click.option("--stream", is_flag=True, help="Stream responses in real-time")
@click.option("--debug", is_flag=True, help="Enable debug mode")
def prompt(
    prompt: str,
    model: str,
    max_turns: int,
    system_prompt: Optional[str],
    tools: Optional[str],
    permission_mode: str,
    working_dir: Optional[str],
    timeout: int,
    stream: bool,
    debug: bool
):
    """Execute an adhoc prompt with Claude Code agent."""
    
    # Build settings
    settings = WrapperSettings(
        model=ModelType(model),
        max_turns=max_turns,
        system_prompt=system_prompt,
        allowed_tools=tools.split(",") if tools else None,
        permission_mode=PermissionMode(permission_mode),
        working_directory=working_dir,
        timeout_seconds=timeout,
        debug_mode=debug
    )
    
    if stream:
        asyncio.run(_stream_prompt(prompt, settings))
    else:
        asyncio.run(_execute_prompt(prompt, settings))


async def _execute_prompt(prompt: str, settings: WrapperSettings):
    """Execute a prompt and display results."""
    try:
        response = await adhoc_prompt(prompt, settings)
        
        if response.success:
            click.echo("=== Agent Response ===")
            for msg in response.messages:
                click.echo(msg.content)
            
            if response.execution_time:
                click.echo(f"\n--- Execution time: {response.execution_time:.2f}s ---")
        else:
            click.echo(f"Error: {response.error_message}", err=True)
            sys.exit(1)
            
    except WrapperException as e:
        click.echo(f"Wrapper Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected Error: {e}", err=True)
        sys.exit(1)


async def _stream_prompt(prompt: str, settings: WrapperSettings):
    """Stream a prompt and display results in real-time."""
    try:
        click.echo("=== Streaming Agent Response ===")
        async for message in stream_adhoc_prompt(prompt, settings):
            if message.metadata and message.metadata.get("error"):
                click.echo(f"Error: {message.content}", err=True)
                sys.exit(1)
            else:
                click.echo(message.content, nl=False)
        click.echo("")  # Final newline
        
    except WrapperException as e:
        click.echo(f"Wrapper Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected Error: {e}", err=True)
        sys.exit(1)


@main.group()
def commands():
    """Manage slash commands."""
    pass


@commands.command("create")
@click.argument("config_file", type=click.Path(exists=True))
def create_command(config_file: str):
    """Create a slash command from a JSON configuration file."""
    try:
        with open(config_file, 'r') as f:
            config_data = json.load(f)
        
        command = SlashCommandConfig(**config_data)
        register_slash_command(command)
        
        click.echo(f"Registered slash command: {command.command_name}")
        
    except Exception as e:
        click.echo(f"Error creating command: {e}", err=True)
        sys.exit(1)


@commands.command("list")
def list_commands():
    """List all registered slash commands."""
    commands = list_registered_commands()
    
    if not commands:
        click.echo("No slash commands registered.")
        return
    
    click.echo("Registered Slash Commands:")
    click.echo("=" * 40)
    
    for name, config in commands.items():
        click.echo(f"/{name}")
        click.echo(f"  Description: {config.description}")
        if config.required_tools:
            click.echo(f"  Required Tools: {', '.join(config.required_tools)}")
        click.echo("")


@commands.command("run")
@click.argument("command_name")
@click.argument("user_input")
@click.option("--model", type=click.Choice([m.value for m in ModelType]))
@click.option("--max-turns", type=int)
@click.option("--stream", is_flag=True)
def run_command(command_name: str, user_input: str, model: Optional[str], max_turns: Optional[int], stream: bool):
    """Run a registered slash command."""
    command = get_registered_command(command_name)
    
    if not command:
        click.echo(f"Slash command '{command_name}' not found.", err=True)
        sys.exit(1)
    
    # Build override settings
    override_settings = None
    if model or max_turns:
        override_dict = {}
        if model:
            override_dict["model"] = ModelType(model)
        if max_turns:
            override_dict["max_turns"] = max_turns
        override_settings = WrapperSettings(**override_dict)
    
    asyncio.run(_execute_slash_command(command, user_input, override_settings, stream))


async def _execute_slash_command(
    command: SlashCommandConfig, 
    user_input: str, 
    override_settings: Optional[WrapperSettings],
    stream: bool
):
    """Execute a slash command."""
    try:
        response = await reusable_prompt(command, user_input, override_settings)
        
        if response.success:
            click.echo(f"=== /{command.command_name} Response ===")
            for msg in response.messages:
                click.echo(msg.content)
            
            if response.execution_time:
                click.echo(f"\n--- Execution time: {response.execution_time:.2f}s ---")
        else:
            click.echo(f"Error: {response.error_message}", err=True)
            sys.exit(1)
            
    except WrapperException as e:
        click.echo(f"Wrapper Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected Error: {e}", err=True)
        sys.exit(1)


@commands.command("example")
@click.argument("output_file", type=click.Path())
def create_example_config(output_file: str):
    """Create an example slash command configuration file."""
    example_config = {
        "command_name": "code_review",
        "description": "Perform a thorough code review focusing on best practices, security, and performance",
        "system_prompt": "You are a senior code reviewer with expertise in multiple programming languages. Analyze the provided code for:\n1. Code quality and best practices\n2. Security vulnerabilities\n3. Performance optimizations\n4. Documentation completeness\n\nProvide actionable feedback with specific suggestions for improvement.",
        "default_settings": {
            "model": "claude-3-5-sonnet-20241022",
            "max_turns": 10,
            "permission_mode": "ask"
        },
        "required_tools": ["Read", "Grep", "Bash"],
        "examples": [
            "Review the authentication module in src/auth/",
            "Check the API endpoints for security issues",
            "Analyze the database queries for performance problems"
        ]
    }
    
    with open(output_file, 'w') as f:
        json.dump(example_config, f, indent=2)
    
    click.echo(f"Example configuration written to: {output_file}")


if __name__ == "__main__":
    main()