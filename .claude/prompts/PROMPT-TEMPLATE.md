---
name: # Short, memorable agent identifier (e.g., "test-runner", "code-reviewer")
description: # One-line description of what this agent does
argument-hint: [argument 1] [argument 2] # Optional: Show users expected arguments (e.g., "[file-path]", "[test-name] [--verbose]")
tools: # Optional: Comma-separated list of required tools (e.g., "Read, Write, Bash")
model: # Optional: Specific model to use (e.g., "claude-3-opus", "gpt-4")
color: # Optional: Terminal color for agent output (e.g., "blue", "green", "yellow")
---

# Agent Name

Brief overview of the agent's purpose, capabilities, and when to use it.

## Relevant Files

List critical files or patterns this agent commonly interacts with:
- `src/**/*.ts` - TypeScript source files
- `tests/**/*.test.ts` - Test files
- `package.json` - Dependencies and scripts
- `.env` - Environment configuration

## Codebase Structure

Describe the expected project structure this agent operates on:
```
project-root/
├── src/           # Source code
├── tests/         # Test files
├── docs/          # Documentation
└── config/        # Configuration files
```

## Variables

**Static Variables** - hardcoded paths or values

CONFIG_PATH: `./config/settings.json`  <!--- Path to configuration file -->

**Dynamic Variables** - passed by user at runtime

DYNAMIC_VARIABLE: $1   <!--- First argument (e.g., file path to analyze) --> 

## Instructions

Core behavioral guidelines and constraints:
- Always validate inputs before processing
- Follow project coding standards
- Preserve existing formatting unless fixing issues
- Handle errors gracefully with clear messages
- Respect .gitignore and other exclusion patterns

## Workflow

When invoked, you must follow these steps:

1. **Initialize**: Validate environment and prerequisites
   - Check required tools are available
   - Verify target files/directories exist
   - Load any necessary configurations

2. **Analyze**: Gather information about the task
   - Read relevant files using appropriate tools
   - Understand existing patterns and conventions
   - Identify potential issues or conflicts

3. **Execute**: Perform the main task
   - Apply changes systematically
   - Follow established patterns
   - Document significant decisions

4. **Verify**: Ensure quality and correctness
   - Run validation checks
   - Test changes if applicable
   - Generate summary report

## Examples

### Example 1: Basic Usage
```bash
# Command
claude agent <agent-name> "src/utils.ts"

# Expected behavior
- Reads the specified file
- Performs analysis
- Outputs results
```

### Example 2: With Options
```bash
# Command
claude agent <agent-name> "src/" "--fix --verbose"

# Expected behavior
- Processes all files in directory
- Applies automatic fixes
- Shows detailed output
```

## Template

*Optional:* Provide a reusable structure for outputs or configurations:

```yaml
# Agent configuration template
agent:
  name: ${AGENT_NAME}
  version: 1.0.0
  tasks:
    - task: ${TASK_NAME}
      input: ${INPUT_PATH}
      output: ${OUTPUT_PATH}
      options:
        verbose: ${VERBOSE}
        autofix: ${AUTOFIX}
  results:
    status: ${STATUS}
    summary: ${SUMMARY}
    errors: ${ERROR_COUNT}
```

## Output Format

Specify the expected output structure:
- **Summary**: Brief overview of actions taken
- **Changes**: List of modified files with descriptions
- **Issues**: Any problems encountered
- **Next Steps**: Recommended follow-up actions

Example output:
```
✅ Analysis Complete
- Files analyzed: 15
- Issues found: 3
- Auto-fixed: 2
- Manual review needed: 1

See detailed report in: ./reports/analysis-TIMESTAMP.md
```