---
description: Gain a general understanding of the agentic system with a focus on the BMAD (Core) workflow
allowed-tools: Read, Bash
---

# Prime BMAD System

Execute the `Workflow` and `Report` sections to understand the codebase and then summarize your understanding

## Variables

CONTEXT_LOCATION: ./.claude/context/bmad-core/

## Workflow

### 1. Understanding of BMAD System Components

Read these context files located in the `CONTEXT_LOCATION` directory. This is a representative sample of the full BMAD system.
  1. `user-docs/user-guide.md`
  2. `agent-teams/team-all.yaml`
  3. `agents/pm.md` and `agents/architect.md` and `agents/qa.md`
  4. `checklists/pm-checklist.md` and `checklists/architect-checklist.md`
  5. `tasks/document-project.md` and `tasks/advanced-elicitation.md` and `tasks/execute-checklist.md`

### 2. Inventory of Essential Context Files

Take note of the other context files in the `CONTEXT_LOCATION` directory by running `ls -a [path_to_folder]` for the following subfolders
  1. `agents`
  2. `checklists`
  3. `data`
  4. `tasks`
  5. `templates`
  6. `utils`
  7. `workflows`

## Report

Summarize your understanding of the codebase with a focus on the BMAD (Core) workflow and functionality