---
description: Load documentation from their respective websites into local markdown files our agents can use as context
allowed-tools: Task, WebFetch, Write, Edit, Bash (ls*), mcp__firecrawl__firecrawl_scrape
---

# Load AI Docs

Load documentation from their respective websites into local markdown files our agents can use as context.

## Variables

DELETE_OLD_AI_DOCS_AFTER_HOURS: 24

## Workflow

1. Read the @docs/ai-docs/README.md file

2. See if any ai-docs/<some-filename>.md file already exists
   1. If it does, see if it was created within the last `DELETE_OLD_AI_DOCS_AFTER_HOURS` hours
   2. If it was, skip it - take a note that it was skipped
   3. If it was not, delete it - take a note that it was deleted

3. For each URL in ai-docs/README.md that was not skipped, Use the Task tool in parallel and use the `scrape_loop_prompt` as the exact prompt for each Task
   
   <scrape_loop_prompt>
   Use @.claude/agents/docs-scraper agent - pass in the URL as an arugment to the agent
   </scrape_loop_prompt>

4. After all Tasks are complete, respond in the `Report Format`

## Report Format

```
AI Docs Report:
- <✅ Success or ❌ Failure or ⚠️ Skipped >: <url> - <markdown file path>
```