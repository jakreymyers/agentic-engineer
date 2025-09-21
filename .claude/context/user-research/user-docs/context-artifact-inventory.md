# User Research System - Agents, Commands, and Tasks Inventory

*Complete guide to commands, tasks, and workflows in the User Research Multi-Agent System*

---

## Overview

The User Research Multi-Agent System implements a sophisticated research orchestration framework with:
- **6 Specialized Agents**: Each with deep expertise in specific research domains
- **5 Research Workflows**: From rapid discovery to comprehensive ethnography
- **24+ Executable Tasks**: Systematic workflows with mandatory elicitation
- **24+ YAML Templates**: Structured documents for consistent outputs
- **18 Data Resources**: Knowledge bases and methodological guidance
- **3 Quality Checklists**: Comprehensive validation frameworks

All commands follow a consistent structure with agents orchestrating tasks, templates, and workflows to deliver professional research outcomes.

## Command Architecture

### Command Structure
```
.claude/context/user-research/
├── agents/                # Agent persona definitions
├── tasks/                 # Executable task workflows
├── templates/             # YAML document templates
├── workflows/             # End-to-end research workflows
├── checklists/            # Quality validation checklists
├── data/                  # Research methods and knowledge
├── tools/                 # Tool requirements and specs
├── agent-teams/           # Team configurations
└── core-config.yaml       # System configuration
```

### Command Prefixes
All agent commands require a `*` prefix:
- `*help` - Show available commands
- `*agent [name]` - Transform into specialized agent
- `*task [name]` - Run specific task
- `*workflow [name]` - Start research workflow
- `*status` - Show current context

## Research Agents

### Agent Roster

#### `*research-orchestrator` - Dr. Morgan 🎯
**Role**: Chief Research Orchestrator
**Key Features**:
- Master coordinator for all research activities
- Ensures quality standards and alignment
- Manages agent handoffs and workflow progression

**Core Commands**:
```
*help                    # Show research commands
*initiate-project        # Start new research
*select-methodology      # Choose approach
*assign-agents          # Delegate tasks
*review-gates           # Check quality
*generate-summary       # Executive summary
*workflow [name]        # Start workflow
*checklist [name]       # Run checklist
*status                 # Show progress
```

#### `*research-strategist` - Dr. Sarah 🔬
**Role**: Senior Research Strategist
**Key Features**:
- Study design and sampling expert
- Advanced methodology specialist
- Statistical power calculations

**Core Commands**:
```
*design-study           # Comprehensive design
*create-screener        # Participant screening
*calculate-sample       # Sample size
*design-conjoint        # Conjoint analysis
*plan-ethnography       # Field research
*select-method          # Method selection
*create-protocol        # Research protocol
```

#### `*interview-specialist` - Jamie 🎤
**Role**: Lead Interview Specialist
**Key Features**:
- Master of elicitation techniques
- Bias prevention and rapport building
- Conversation flow optimization

**Core Commands**:
```
*create-guide           # Discussion guide
*generate-probes        # Follow-up questions
*simulate-interview     # Practice session
*refine-questions       # Improve clarity
*create-protocol        # Interview protocol
*check-bias            # Bias detection
*build-rapport         # Rapport strategies
```

#### `*data-analyst` - Alex 📊
**Role**: Senior Research Analyst
**Key Features**:
- Qualitative coding expertise
- Statistical analysis capabilities
- Theme extraction and validation

**Core Commands**:
```
*analyze-transcript     # Process transcripts
*extract-themes         # Identify patterns
*code-responses        # Apply coding
*create-affinity       # Affinity diagrams
*calculate-stats       # Statistical analysis
*sentiment-analysis    # Emotion patterns
*saturation-check      # Data saturation
*reliability-test      # IRR calculation
```

#### `*insight-synthesizer` - Dr. Riley 💡
**Role**: Principal Insight Synthesizer
**Key Features**:
- Cross-interview pattern recognition
- Strategic insight generation
- Persona and journey development

**Core Commands**:
```
*synthesize            # Cross-interview synthesis
*extract-requirements  # User requirements
*create-personas       # User personas
*map-journey          # Customer journeys
*identify-jtbd        # Jobs-to-be-done
*find-opportunities   # Innovation areas
*validate-insights    # Cross-check findings
```

#### `*research-reporter` - Taylor 📝
**Role**: Lead Research Reporter
**Key Features**:
- Multi-format report generation
- Stakeholder-specific communication
- Data visualization expertise

**Core Commands**:
```
*generate-report       # Full report
*create-summary       # Executive summary
*design-visuals       # Visualizations
*draft-recommendations # Strategic recs
*create-presentation  # Stakeholder deck
*quick-wins          # Immediate actions
*stakeholder-report  # Audience versions
```

## Specialized Tasks

### Task Categories & Usage

#### Project Establishment Tasks
| Task | Agent | Purpose | Elicitation |
|------|-------|---------|-------------|
| `establish-research-project.md` | Orchestrator | Define objectives and scope | Yes (4 phases) |
| `select-research-methodology.md` | Orchestrator | Choose research approach | Yes (3 phases) |

#### Study Design Tasks
| Task | Agent | Purpose | Elicitation |
|------|-------|---------|-------------|
| `design-research-study.md` | Strategist | Comprehensive study planning | Yes (6 phases) |
| `create-screening-questionnaire.md` | Strategist | Participant recruitment | Yes (4 phases) |
| `setup-conjoint-analysis.md` | Strategist | Conjoint study setup | Yes (8 phases) |
| `plan-ethnographic-study.md` | Strategist | Field research planning | Yes (10 phases) |

#### Interview Tasks
| Task | Agent | Purpose | Elicitation |
|------|-------|---------|-------------|
| `create-discussion-guide.md` | Specialist | Interview guide creation | Yes (11 points) |
| `generate-interview-probes.md` | Specialist | Follow-up questions | Yes (3 phases) |
| `simulate-interview-session.md` | Specialist | Practice interviews | Interactive |
| `create-interview-protocol.md` | Specialist | Execution procedures | Yes (4 phases) |

#### Analysis Tasks
| Task | Agent | Purpose | Elicitation |
|------|-------|---------|-------------|
| `analyze-transcript.md` | Analyst | Transcript coding | Yes (5 passes) |
| `extract-themes.md` | Analyst | Pattern identification | Yes (3 phases) |
| `create-affinity-diagram.md` | Analyst | Insight clustering | Yes (4 phases) |
| `perform-statistical-analysis.md` | Analyst | Quantitative analysis | Yes (5 phases) |
| `conduct-sentiment-analysis.md` | Analyst | Emotion analysis | Yes (4 phases) |

#### Synthesis Tasks
| Task | Agent | Purpose | Elicitation |
|------|-------|---------|-------------|
| `synthesize-cross-interview.md` | Synthesizer | Pattern integration | Yes (5 phases) |
| `extract-user-requirements.md` | Synthesizer | Requirements extraction | Yes (4 phases) |
| `create-user-personas.md` | Synthesizer | Persona development | Yes (5 phases) |
| `map-customer-journey.md` | Synthesizer | Journey mapping | Yes (6 phases) |
| `identify-jobs-to-be-done.md` | Synthesizer | JTBD framework | Yes (4 phases) |

#### Reporting Tasks
| Task | Agent | Purpose | Elicitation |
|------|-------|---------|-------------|
| `generate-research-report.md` | Reporter | Comprehensive report | Yes (7 sections) |
| `create-executive-summary.md` | Reporter | C-level summary | Yes (4 sections) |
| `design-visualizations.md` | Reporter | Data graphics | Yes (3 phases) |
| `formulate-recommendations.md` | Reporter | Strategic guidance | Yes (4 phases) |

### The Elicitation System

**Critical**: All tasks with `elicit: true` require mandatory user interaction using the 1-9 format:

```
1. Proceed to next section
2. [Contextual elicitation method]
3. [Contextual elicitation method]
4. [Contextual elicitation method]
5. [Contextual elicitation method]
6. [Contextual elicitation method]
7. [Contextual elicitation method]
8. [Contextual elicitation method]
9. [Contextual elicitation method]

Select 1-9 or just type your question/feedback:
```

**Violation Indicators**:
- Creating complete documents without user interaction
- Skipping elicitation points
- Not using the 1-9 format exactly

## Template System

### Template Categories

#### Project Templates
| Template | Purpose | Sections | Elicitation |
|---------|---------|----------|-------------|
| `research-brief-tmpl.yaml` | Project foundation | 11 | Yes |
| `methodology-matrix-tmpl.yaml` | Method selection | 5 | Yes |

#### Study Design Templates
| Template | Purpose | Sections | Elicitation |
|---------|---------|----------|-------------|
| `study-design-tmpl.yaml` | Research planning | 10 | Yes |
| `screening-criteria-tmpl.yaml` | Recruitment | 6 | Yes |
| `conjoint-setup-tmpl.yaml` | Conjoint config | 14 | Yes |
| `ethnographic-plan-tmpl.yaml` | Field research | 11 | Yes |

#### Interview Templates
| Template | Purpose | Sections | Elicitation |
|---------|---------|----------|-------------|
| `discussion-guide-tmpl.yaml` | Interview guide | 11 | Yes |
| `interview-protocol-tmpl.yaml` | Procedures | 8 | Yes |
| `probe-bank-tmpl.yaml` | Follow-ups | 5 | Yes |
| `consent-form-tmpl.yaml` | Ethics | 7 | Required |

#### Analysis Templates
| Template | Purpose | Sections | Elicitation |
|---------|---------|----------|-------------|
| `transcript-analysis-tmpl.yaml` | Coding framework | 8 | Yes |
| `coding-framework-tmpl.yaml` | Code structure | 6 | Yes |
| `affinity-map-tmpl.yaml` | Clustering | 7 | Yes |
| `statistical-summary-tmpl.yaml` | Stats output | 9 | Yes |
| `sentiment-analysis-tmpl.yaml` | Emotion analysis | 8 | Yes |

#### Synthesis Templates
| Template | Purpose | Sections | Elicitation |
|---------|---------|----------|-------------|
| `synthesis-framework-tmpl.yaml` | Cross-analysis | 9 | Yes |
| `persona-profile-tmpl.yaml` | User personas | 12 | Yes |
| `journey-map-tmpl.yaml` | Experience map | 10 | Yes |
| `requirements-matrix-tmpl.yaml` | Requirements | 7 | Yes |
| `jtbd-framework-tmpl.yaml` | Jobs framework | 8 | Yes |

#### Reporting Templates
| Template | Purpose | Sections | Elicitation |
|---------|---------|----------|-------------|
| `research-report-tmpl.yaml` | Full report | 12 | Yes |
| `executive-summary-tmpl.yaml` | Executive brief | 6 | Yes |
| `visualization-specs-tmpl.yaml` | Graphics specs | 8 | Yes |
| `recommendations-tmpl.yaml` | Strategic recs | 7 | Yes |
| `presentation-deck-tmpl.yaml` | Stakeholder deck | 10 | Yes |
| `insight-cards-tmpl.yaml` | Insight summaries | 6 | Yes |
| `dashboard-specs-tmpl.yaml` | Dashboard design | 9 | Yes |
| `handoff-doc-tmpl.yaml` | Transition docs | 8 | Yes |

## Research Workflows

### Workflow Command Reference

#### `*workflow rapid-discovery`
**Duration**: 5 days
**Agents**: Orchestrator, Specialist, Analyst
**Best For**: Quick insights, urgent decisions
**Key Phases**:
- Day 1: Plan & Recruit
- Day 2-3: Interview (8-10 participants)
- Day 4: Analyze & Synthesize
- Day 5: Report & Present

#### `*workflow user-interview-research`
**Duration**: 3-6 weeks
**Agents**: All 6 agents
**Best For**: Deep behavioral understanding
**Key Phases**:
1. Planning (3-4 days)
2. Preparation (2-3 days)
3. Collection (5-10 days)
4. Analysis (4-5 days)
5. Synthesis (3-4 days)
6. Reporting (3-4 days)
7. Delivery (1-2 days)

#### `*workflow conjoint-analysis`
**Duration**: 2-3 weeks
**Agents**: Orchestrator, Strategist, Analyst, Reporter
**Best For**: Feature/pricing preferences
**Technical Requirements**:
- 4-7 attributes
- 200+ respondents
- D-efficiency >0.85

#### `*workflow ethnographic-research`
**Duration**: 4-8 weeks
**Agents**: All agents except Reporter
**Best For**: Cultural/contextual insights
**Key Features**:
- Participant observation
- Multi-method collection
- Thick description
- Member checking

#### `*workflow mixed-methods-research`
**Duration**: 4-6 weeks
**Agents**: All 6 agents
**Best For**: Validation & triangulation
**Design Types**:
- Convergent parallel
- Explanatory sequential
- Exploratory sequential

## Quality Framework

### Quality Checklists

#### `research-quality-checklist.md`
**Scope**: Entire research lifecycle
**Validation Points**: 400+
**Phases**: 8 major phases
**Adapts To**: Research methodology type

#### `interview-quality-checklist.md`
**Scope**: Interview preparation and execution
**Critical Items**: 15 blockers
**Phases**: Pre/During/Post interview
**Focus**: Technique and bias prevention

#### `analysis-quality-checklist.md`
**Scope**: Data analysis and coding
**Key Metrics**: IRR >0.70, Coverage >95%
**Phases**: 10 quality dimensions
**Focus**: Systematic rigor

### Quality Gates

| Gate | Threshold | Measurement |
|------|-----------|-------------|
| **Planning Gate** | >75% | Stakeholder approval |
| **Collection Gate** | >95% | Recording quality |
| **Analysis Gate** | >0.70 | Inter-rater reliability |
| **Delivery Gate** | >80% | Stakeholder understanding |

## Data Resources

### Knowledge Bases

| Resource | Lines | Purpose |
|----------|-------|---------|
| `research-methods-kb.md` | 679 | Comprehensive methodology guide |
| `sampling-methods.md` | 673 | Sampling strategies and calculations |
| `statistical-power.md` | 635 | Power analysis and sample sizing |
| `interview-techniques.md` | 459 | Elicitation and rapport building |
| `cognitive-biases.md` | 512 | Bias identification and mitigation |
| `ethical-guidelines.md` | 359 | Research ethics and compliance |
| `coding-frameworks.md` | 423 | Qualitative analysis approaches |
| `analysis-methods.md` | 387 | Analysis technique selection |
| `statistical-tests.md` | 402 | Statistical test selection guide |
| `persona-frameworks.md` | 396 | Persona development methods |
| `jtbd-methodology.md` | 418 | Jobs-to-be-done framework |
| `visualization-guidelines.md` | 445 | Data visualization best practices |
| `reporting-standards.md` | 467 | Report structure and quality |
| `rapport-building.md` | 589 | Interview relationship techniques |

## Team Configurations

### Available Teams

| Team | Agents | Workflows | Use Case |
|------|--------|-----------|----------|
| `team-all` | All 6 agents | All 5 workflows | Comprehensive research |
| `team-minimal` | 3 agents | Rapid discovery | Quick insights |
| `team-qualitative` | 4 agents | Interviews, Ethnography | Behavioral research |
| `team-quantitative` | 4 agents | Conjoint, Surveys | Statistical research |
| `team-mixed` | 6 agents | Mixed methods | Triangulated insights |

### Team Loading

```bash
# Load specific team
*team-all           # Full capabilities
*team-minimal       # Rapid research
*team-qualitative   # Qual focus
*team-quantitative  # Quant focus
*team-mixed         # Combined approach
```

## Tool Integrations

### Research Tools

| Tool | Purpose | Integration |
|------|---------|-------------|
| `intelligent-transcription-service` | Audio transcription | >95% accuracy |
| `research-stats-analyzer` | Statistical analysis | Agent commands |
| `digital-affinity-mapper` | Insight clustering | 2000+ insights |
| `research-sentiment-analyzer` | Emotion analysis | Multi-dimensional |
| `research-viz-generator` | Visualizations | 50+ chart types |
| `research-data-orchestrator` | Workflow management | All workflows |
| `research-participant-manager` | Recruitment | 10,000+ database |

## Output Specifications

### Standard Output Paths

```text
# Planning Documents
docs/research/brief.md
docs/research/methodology-matrix.md
docs/research/study-design.md

# Data Collection
docs/research/discussion-guide.md
docs/research/screening-questionnaire.md
data/recordings/
data/transcripts/

# Analysis Artifacts
data/analysis/coded-transcripts/
data/analysis/themes.json
data/analysis/affinity-map.md

# Synthesis Outputs
docs/research/synthesis.md
docs/research/personas/
docs/research/journey-maps/

# Final Deliverables
docs/research/reports/full-report.md
docs/research/reports/executive-summary.md
docs/research/presentations/
```

## Configuration

### Core Configuration (`core-config.yaml`)

```yaml
research_system:
  agents:
    - research-orchestrator
    - research-strategist
    - interview-specialist
    - data-analyst
    - insight-synthesizer
    - research-reporter

  workflows:
    - rapid-discovery
    - user-interview-research
    - conjoint-analysis
    - ethnographic-research
    - mixed-methods-research

  quality_thresholds:
    irr_minimum: 0.70
    stakeholder_approval: 75
    recording_quality: 95
    code_coverage: 95

  elicitation:
    required: true
    format: 1-9
    violation_check: enabled

  output_paths:
    research: ./docs/research/
    data: ./data/
    analysis: ./data/analysis/
    reports: ./docs/research/reports/
```

## Quick Reference Matrix

### Task → Agent → Template → Output

| Task | Agent | Template | Output |
|------|-------|----------|---------|
| establish-research-project | Orchestrator | research-brief-tmpl | docs/research/brief.md |
| select-research-methodology | Orchestrator | methodology-matrix-tmpl | docs/research/methodology-matrix.md |
| design-research-study | Strategist | study-design-tmpl | docs/research/study-design.md |
| create-screening-questionnaire | Strategist | screening-criteria-tmpl | docs/research/screener.md |
| create-discussion-guide | Specialist | discussion-guide-tmpl | docs/research/guide.md |
| analyze-transcript | Analyst | transcript-analysis-tmpl | data/analysis/coded/ |
| synthesize-cross-interview | Synthesizer | synthesis-framework-tmpl | docs/research/synthesis.md |
| generate-research-report | Reporter | research-report-tmpl | docs/research/reports/full.md |

## System Integration Flow

```mermaid
graph LR
    A[Orchestrator] --> B[Strategist]
    B --> C[Specialist]
    C --> D[Data Collection]
    D --> E[Analyst]
    E --> F[Synthesizer]
    F --> G[Reporter]
    G --> H[Stakeholders]

    style A fill:#f9ab00,color:#fff
    style B fill:#fff3e0,color:#000
    style C fill:#e1f5fe,color:#000
    style D fill:#e8f5e9,color:#000
    style E fill:#e3f2fd,color:#000
    style F fill:#f3e5f5,color:#000
    style G fill:#fff3e0,color:#000
    style H fill:#34a853,color:#fff
```

## Best Practices

### Command Usage
1. Always start with `*help` to see available options
2. Use `*status` to check current progress
3. Run `*checklist` at phase transitions
4. Document decisions with elicitation system

### Workflow Selection
1. Match methodology to research questions
2. Consider time and resource constraints
3. Default to mixed methods for complex questions
4. Use rapid discovery for urgent needs

### Quality Assurance
1. Never skip elicitation points
2. Maintain evidence chains throughout
3. Achieve IRR >0.70 for all coding
4. Validate with multiple data sources

## Getting Started

### Quick Start Commands

```bash
# Start new research project
*research-orchestrator
*initiate-project

# Quick 5-day discovery
*team-minimal
*workflow rapid-discovery

# Comprehensive user research
*team-all
*workflow user-interview-research

# Check system status
*status
*review-gates
```

### First Project Checklist

1. [ ] Load appropriate team configuration
2. [ ] Run `*initiate-project` to define objectives
3. [ ] Use `*select-methodology` to choose approach
4. [ ] Select workflow with `*workflow [name]`
5. [ ] Follow elicitation prompts at each phase
6. [ ] Run quality checklists at gates
7. [ ] Generate reports for stakeholders

---

*This inventory provides complete reference documentation for all commands, tasks, and workflows in the User Research Multi-Agent System.*