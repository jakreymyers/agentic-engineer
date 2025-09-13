"""Basic usage examples for Claude Code Python SDK wrapper."""

import asyncio
from cc_py_wrapper import (
    adhoc_prompt,
    reusable_prompt,
    stream_adhoc_prompt,
    WrapperSettings,
    SlashCommandConfig,
    ModelType,
    PermissionMode
)


async def basic_adhoc_example():
    """Example of basic adhoc prompt usage."""
    print("=== Basic Adhoc Prompt ===")
    
    response = await adhoc_prompt("What is the current time and date?")
    
    if response.success:
        for msg in response.messages:
            print(msg.content)
        print(f"Execution time: {response.execution_time:.2f}s")
    else:
        print(f"Error: {response.error_message}")


async def advanced_adhoc_example():
    """Example of adhoc prompt with custom settings."""
    print("\n=== Advanced Adhoc Prompt ===")
    
    settings = WrapperSettings(
        system_prompt="You are a helpful assistant specializing in file system operations",
        model=ModelType.CLAUDE_3_5_SONNET,
        max_turns=10,
        allowed_tools=["Bash", "Read", "Glob"],
        permission_mode=PermissionMode.ASK,
        debug_mode=True
    )
    
    response = await adhoc_prompt(
        "List all Python files in the current directory and show their sizes",
        settings
    )
    
    if response.success:
        for msg in response.messages:
            print(msg.content)
    else:
        print(f"Error: {response.error_message}")


async def streaming_example():
    """Example of streaming responses."""
    print("\n=== Streaming Example ===")
    
    settings = WrapperSettings(
        system_prompt="You are a code analysis expert",
        allowed_tools=["Read", "Grep"]
    )
    
    print("Streaming response:")
    async for message in stream_adhoc_prompt(
        "Analyze the structure of this Python package", 
        settings
    ):
        print(message.content, end="", flush=True)
    print("\n")


async def slash_command_example():
    """Example of using slash commands."""
    print("\n=== Slash Command Example ===")
    
    # Create a code review command
    code_review_command = SlashCommandConfig(
        command_name="code_review",
        description="Perform comprehensive code review",
        system_prompt="""You are a senior software engineer and code reviewer. 
        Analyze the provided code for:
        1. Code quality and best practices
        2. Potential bugs or issues
        3. Performance considerations
        4. Security concerns
        5. Documentation quality
        
        Provide specific, actionable feedback.""",
        default_settings=WrapperSettings(
            model=ModelType.CLAUDE_3_5_SONNET,
            max_turns=15,
            permission_mode=PermissionMode.ASK
        ),
        required_tools=["Read", "Grep", "Bash"],
        examples=[
            "Review the authentication module",
            "Check API endpoints for security issues",
            "Analyze database query performance"
        ]
    )
    
    # Use the command
    response = await reusable_prompt(
        code_review_command,
        "Review the wrapper.py file in this directory",
        # Optional settings override
        WrapperSettings(debug_mode=True)
    )
    
    if response.success:
        print(f"Command: /{code_review_command.command_name}")
        print("Response:")
        for msg in response.messages:
            print(msg.content)
            if msg.metadata:
                print(f"Metadata: {msg.metadata}")
    else:
        print(f"Error: {response.error_message}")


async def main():
    """Run all examples."""
    try:
        await basic_adhoc_example()
        await advanced_adhoc_example()
        await streaming_example()
        await slash_command_example()
        
    except Exception as e:
        print(f"Example failed: {e}")


if __name__ == "__main__":
    asyncio.run(main())