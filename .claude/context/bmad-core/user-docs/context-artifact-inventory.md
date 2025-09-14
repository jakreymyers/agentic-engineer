# Agents, Commands, and Tasks Inventory

*Complete guide to commands, tasks, and workflows*

---

## Overview

The Agentic Engineer repository implements a sophisticated command framework built on two primary bundles:
- **BMAD Core**: Business, Management, Architecture & Development framework
- **Content Creation**: Specialized content development and marketing tools

All commands follow a consistent structure with agents, tasks, templates, checklists, and workflows orchestrating complex development processes.

## Command Architecture

### Command Structure
```
.claude/
├── commands/               # Executable command entry points
│   ├── general/            # General-purpose utilities
│   ├── bmad-core/          # BMAD framework commands
│   └── content-creation/   # Content creation commands
├── context/                # Supporting framework files
│   ├── bmad-core/          # BMAD context and configuration
│   └── content-creation/   # Content creation context
└── agents/                 # Specialized agent definitions
```

### Command Prefixes
All orchestrator commands require a `*` prefix:
- `*help` - Show available commands
- `*agent [name]` - Transform into specialized agent
- `*task [name]` - Run specific task
- `*workflow [name]` - Start workflow
- `*status` - Show current context

## General Commands

### Core Utilities

#### `prime-cc` - Prime Claude Code
**Description**: Gain understanding of codebase with Claude Code focus
**Usage**:
- Reads `.claude/commands/**`, output styles, hooks, settings
- Provides codebase summary and understanding

#### `prime-full` - General Codebase Primer
**Description**: Basic codebase understanding
**Usage**:
- Runs `git ls-files`, reads README.md

#### `background-agent` - Background Claude Code Instance
**Description**: Fires off autonomous Claude Code instance

**Syntax**: `background-agent [prompt] [model] [report-file]`
- **Parameters**:
  - `prompt`: Task to execute
  - `model`: 'sonnet' (default) or 'opus'
  - `report-file`: Output location (auto-generated if not provided)
**Features**:
- Runs in background with full autonomy
- Creates progress reports in `reports/background-agent/`
- Auto-renames on completion/failure

#### `git-commit` - Git Commit Automation
**Description**: Automated git commit workflow
**Features**:
- Analyzes staged changes
- Drafts contextual commit messages
- Handles pre-commit hooks

#### `load-ai-docs` - Load AI Documentation
**Description**: Load AI documentation context for analysis

## BMAD Core Framework

### Orchestrator Commands

#### `*bmad-orchestrator` - Master Orchestrator
**Role**: Workflow coordination & BMAD method orchestration
**Key Features**:
- Transforms into any specialized agent on demand
- Loads configuration from `bmad-core/core-config.yaml`
- Provides workflow guidance and agent recommendations

**Core Commands**:
```
*help               # Show command guide
*agent [name]       # Transform to specialist
*workflow [name]    # Start workflow
*task [name]        # Run specific task
*checklist [name]   # Execute checklist
*kb-mode           # Load knowledge base
*status            # Show current state
```

### Specialized Agents

#### Business & Strategy Agents

**`*analyst`** - Business Analyst & Research Expert
- **When to use**: Market research, requirements gathering, project briefs
- **Key deliverables**: project-brief.md, market research, competitive analysis
- **Dependencies**: brainstorming-techniques, market-research templates

**`*pm`** - Product Manager (John)
- **When to use**: PRD creation, product strategy, feature prioritization
- **Key deliverables**: prd.md, product roadmaps, feature specifications
- **Commands**: `*create-prd`, `*create-brownfield-prd`, `*shard-prd`

**`*po`** - Product Owner
- **When to use**: Story validation, acceptance criteria, backlog management
- **Key deliverables**: Validated stories, acceptance criteria, epic management

#### Technical Agents

**`*architect`** - Technical Architect
- **When to use**: System design, technical specifications, architecture decisions
- **Key deliverables**: architecture.md, technical specifications, tech stack decisions
- **Commands**: `*create-architecture`, `*review-architecture`

**`*dev`** - Development Agent
- **When to use**: Code implementation, technical problem solving, code review
- **Key deliverables**: Implementation files, code documentation, technical solutions

**`*qa`** - Quality Assurance Engineer
- **When to use**: Code review, test strategy, quality gates
- **Key deliverables**: Test plans, QA reviews, quality assessments
- **Commands**: `*review-story`, `*qa-gate`, `*apply-qa-fixes`

#### Project Management Agents

**`*sm`** - Scrum Master
- **When to use**: Story creation, agile ceremonies, team coordination
- **Key deliverables**: User stories, sprint planning, team facilitation
- **Commands**: `*create-story`, `*validate-story`

**`*ux-expert`** - UX Expert
- **When to use**: UI/UX design, user research, interface specifications
- **Key deliverables**: front-end-spec.md, UI designs, user experience guidelines

### Core Tasks

#### Document Creation Tasks

`create-doc` - Template-driven document creation
- **Purpose**: Create any document using YAML templates
- **Features**:
  - Interactive elicitation with 1-9 format
  - Agent permission handling
  - Step-by-step validation
- **Usage**: Mandatory user interaction for `elicit: true` sections

`shard-doc` - Document sharding for IDE development
- **Purpose**: Break large documents into manageable pieces
- **Usage**: Typically used on PRD and architecture docs

#### Story Management Tasks

- `brownfield-create-epic` - Create epics for existing projects
- `brownfield-create-story` - Create stories for brownfield projects
- `create-next-story` - Generate next story in sequence
- `review-story` - Validate story completeness
- `validate-next-story` - Ensure story readiness

#### Quality & Testing Tasks

- `qa-gate` - Quality gate assessment
- `apply-qa-fixes` - Address QA feedback
- `test-design` - Create test strategies
- `nfr-assess` - Non-functional requirements assessment

#### Research & Analysis Tasks

- `advanced-elicitation` - Deep requirements gathering
- `create-deep-research-prompt` - Generate research prompts
- `trace-requirements` - Requirements traceability
- `risk-profile` - Risk assessment and mitigation

#### Utilities

- `execute-checklist` - Run any checklist with validation
- `kb-mode-interaction` - Knowledge base interaction
- `index-docs` - Document indexing and organization
- `document-project` - Comprehensive project documentation

### Templates

**Architecture Templates**:
- `fullstack-architecture-tmpl.yaml` - Full-stack architecture
- `front-end-architecture-tmpl.yaml` - Frontend architecture
- `brownfield-architecture-tmpl.yaml` - Existing system architecture

**Product Templates**:
- `prd-tmpl.yaml` - Product Requirements Document
- `brownfield-prd-tmpl.yaml` - PRD for existing projects
- `story-tmpl.yaml` - User story template
- `project-brief-tmpl.yaml` - Project brief template

**Research Templates**:
- `market-research-tmpl.yaml` - Market research
- `competitor-analysis-tmpl.yaml` - Competitive analysis
- `brainstorming-output-tmpl.yaml` - Brainstorming results

### Workflows

#### Greenfield Development
`greenfield-fullstack` - Complete full-stack development
**Sequence**:
1. analyst → project-brief.md
2. pm → prd.md
3. ux-expert → front-end-spec.md
4. ux-expert → v0 prompt (optional AI generation)
5. architect → fullstack-architecture.md
6. po → validation
7. Development cycle (sm → dev → qa)

#### Brownfield Development
- `brownfield-fullstack` - Enhance existing applications
- `brownfield-ui` - Frontend improvements
- `brownfield-service` - Backend service enhancement

## Content Creation Framework

### Orchestrator

**`*bmad-orchestrator`** (Content Creation variant)
- **Role**: Content workflow coordination
- **Focus**: Content strategy, thought leadership, LinkedIn optimization

### Specialized Content Agents

#### Writing Specialists

**`*linkedin-writer`** - LinkedIn Content Expert (Alex Chen)
- **Specialization**: Viral LinkedIn posts, engagement optimization
- **Voice**: Jak's authentic style - direct, conversational, data-driven
- **Commands**: `*create-post`, `*optimize-hook`, `*viral-check`, `*format`
- **Features**:
  - Saves to `/Users/kthkellogg/Documents/Obsidian Vault/LinkedIn Posts/`
  - Anti-AI humanization techniques
  - Engagement optimization

**`*blog-writer`** - Blog Content Specialist
- **Focus**: Long-form content, SEO optimization, thought leadership articles
- **Deliverables**: Blog posts, articles, SEO-optimized content

**`*data-product-writer`** - Data Products Content Expert
- **Specialization**: Technical content about data products, healthcare tech
- **Focus**: Complex technical concepts made accessible

#### Strategic Content Agents

**`*narrative-architect`** - Story Structure Expert
- **Role**: Content strategy, narrative flow, story development
- **Deliverables**: Content frameworks, narrative structures

**`*thought-partner`** - Strategic Content Consultant
- **Role**: Idea development, strategic thinking, content positioning
- **Focus**: High-level content strategy and positioning

**`*hook-optimizer`** - Engagement Specialist
- **Focus**: Headlines, hooks, opening lines optimization
- **Deliverables**: Multiple hook variations, A/B testing suggestions

**`*content-editor`** - Editorial Expert
- **Role**: Content polishing, quality assurance, style consistency
- **Focus**: Final review and optimization

**`*microsaas-advisor`** - MicroSaaS Content Strategy
- **Focus**: Solo entrepreneur content, product positioning, growth strategies

### Content Creation Tasks

#### Content Development
- `write-linkedin-post` - Create LinkedIn posts with Jak's voice
- `create-blog-article` - Long-form content creation
- `craft-microsaas-narrative` - Product storytelling for solo entrepreneurs
- `develop-content-idea` - Idea development and expansion
- `refine-messaging` - Message optimization and clarity

#### Strategic Tasks
- `build-thought-leadership` - Establish expertise and authority
- `advanced-elicitation` - Deep content research and planning
- `execute-checklist` - Quality control processes

### Content Templates

**Social Media Templates**:
- `linkedin-post-tmpl.yaml` - LinkedIn post structure
- `hook-framework-tmpl.yaml` - Hook creation framework
- `blog-structure-tmpl.yaml` - Blog post structure

**Business Templates**:
- `microsaas-pitch-tmpl.yaml` - Product positioning
- `data-story-tmpl.yaml` - Data-driven narratives

### Content Workflows

- `thought-leadership-development` - Build expertise and authority
- `microsaas-content-strategy` - Solo entrepreneur content pipeline
- `content-creation-pipeline` - End-to-end content creation

## Advanced Features

### Multi-Agent Collaboration
- `*party-mode` enables group chat with all agents
- Seamless agent-to-agent handoffs in workflows
- Context preservation across transformations

### Knowledge Base Integration
- `*kb-mode` loads full domain knowledge
- Context-aware responses based on loaded knowledge
- Topic-specific expertise areas

### Workflow Planning
- `*plan` creates detailed workflow plans
- `*plan-status` tracks progress
- `*plan-update` maintains current state

---