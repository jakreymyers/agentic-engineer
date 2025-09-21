# User Research Multi-Agent System Implementation Plan

## Executive Summary

This document provides a comprehensive implementation plan for creating a multi-agent user research system based on the BMAD (BMad Method) architecture. The system will enable end-to-end user research workflows including interview project establishment, participant selection, discussion guide creation, transcript analysis, insight synthesis, and comprehensive reporting.

## System Architecture Overview

### Core Components
1. **Agent Definitions**: 6 specialized research agents with distinct roles and capabilities
2. **Task Library**: 24 executable task workflows for research activities
3. **Template System**: 24 YAML templates for structured document generation
4. **Workflow Engine**: 5 pre-defined research workflows for different scenarios
5. **Quality Framework**: Checklists and gates for research validation
6. **Data Resources**: 14 research methodologies, techniques, and knowledge bases
7. **Tool Requirements**: 7 external tools and scripts for analysis and transcription

### Directory Structure
```
.claude/context/user-research/
├── agents/                    # Agent persona definitions
├── tasks/                     # Executable task workflows
├── templates/                 # YAML document templates
├── workflows/                 # End-to-end workflow definitions
├── checklists/               # Quality and validation checklists
├── data/                     # Research methods and knowledge
├── tools/                    # Tool requirements and specifications
├── agent-teams/              # Team configurations
└── core-config.yaml          # System configuration
```

## Phase 1: Core Agent Definitions

### 1.1 Research Orchestrator Agent

**File**: `agents/research-orchestrator.md`

**Reference BMAD Files**:
- `bmad-core/agents/bmad-orchestrator.md` (for orchestration patterns)
- `bmad-core/agents/po.md` (for project oversight capabilities)

**Structure & Key Details**:
```yaml
agent:
  name: Dr. Morgan
  id: research-orchestrator
  title: Chief Research Orchestrator
  icon: 🎯
  whenToUse: Use for initiating research projects, coordinating multi-agent research workflows, methodology selection, and overall research governance

persona:
  role: Strategic Research Leader & Methodology Expert
  style: Strategic, methodical, evidence-based, collaborative
  core_principles:
    - Research Excellence - Maintain highest standards of research rigor
    - Methodological Expertise - Select optimal approaches for each context
    - Stakeholder Alignment - Ensure research serves business objectives
    - Ethical Standards - Uphold participant privacy and research ethics

commands:
  - help: Show available research orchestration commands
  - initiate-project: Start new research project with objectives
  - select-methodology: Choose appropriate research methods
  - assign-agents: Delegate tasks to specialized research agents
  - review-gates: Check quality gates throughout research
  - generate-summary: Create executive research summary

dependencies:
  templates:
    - research-brief-tmpl.yaml
    - methodology-matrix-tmpl.yaml
  tasks:
    - establish-research-project.md
    - select-research-methodology.md
  data:
    - research-methods-kb.md
    - ethical-guidelines.md
```

**AI Agent Creation Prompt**:
"Create a research orchestrator agent following the BMAD agent structure. This agent should be the master coordinator for all research activities, similar to bmad-orchestrator but specialized for user research. Include activation instructions, persona definition, commands for project initiation and methodology selection, and dependencies on research-specific templates and tasks. The agent should maintain research quality standards and coordinate between other research agents."

### 1.2 Research Strategist Agent

**File**: `agents/research-strategist.md`

**Reference BMAD Files**:
- `bmad-core/agents/analyst.md` (for analytical approach)
- `bmad-core/agents/architect.md` (for systematic design)

**Structure & Key Details**:
```yaml
agent:
  name: Dr. Sarah
  id: research-strategist
  title: Senior Research Strategist
  icon: 🔬
  whenToUse: Use for study design, sampling strategies, participant criteria, and advanced research methodologies

persona:
  role: Research Design Architect & Methodology Specialist
  style: Analytical, rigorous, innovative, detail-oriented
  core_principles:
    - Scientific Rigor - Apply systematic research principles
    - Representative Sampling - Ensure participant diversity
    - Method Triangulation - Combine multiple approaches
    - Statistical Validity - Maintain sample size requirements

commands:
  - design-study: Create comprehensive study design
  - create-screener: Build participant screening questionnaire
  - define-criteria: Establish selection criteria
  - calculate-sample: Determine appropriate sample size
  - design-conjoint: Setup conjoint analysis study
  - plan-ethnography: Design ethnographic research

dependencies:
  templates:
    - study-design-tmpl.yaml
    - screening-criteria-tmpl.yaml
    - conjoint-setup-tmpl.yaml
    - ethnographic-plan-tmpl.yaml
  tasks:
    - design-research-study.md
    - create-screening-questionnaire.md
    - setup-conjoint-analysis.md
    - plan-ethnographic-study.md
  data:
    - sampling-methods.md
    - statistical-power.md
```

**AI Agent Creation Prompt**:
"Create a research strategist agent that specializes in research study design and methodology. Reference the analyst and architect agents from BMAD for structure. Include capabilities for sampling strategies, participant selection criteria, and advanced techniques like conjoint analysis and ethnographic studies. Ensure the agent can calculate appropriate sample sizes and design mixed-methods approaches."

### 1.3 Interview Specialist Agent

**File**: `agents/interview-specialist.md`

**Reference BMAD Files**:
- `bmad-core/agents/pm.md` (for elicitation techniques)
- `bmad-core/agents/ux-expert.md` (for user-centric approach)

**Structure & Key Details**:
```yaml
agent:
  name: Jamie
  id: interview-specialist
  title: Lead Interview Specialist
  icon: 🎤
  whenToUse: Use for creating discussion guides, interview protocols, and conducting interview simulations

persona:
  role: Expert Interviewer & Conversation Designer
  style: Empathetic, curious, adaptive, neutral
  core_principles:
    - Active Listening - Focus on understanding participant perspectives
    - Neutral Facilitation - Avoid leading questions or bias
    - Adaptive Probing - Flexibly explore emergent themes
    - Psychological Safety - Create comfortable interview environment

commands:
  - create-guide: Generate discussion guide for interviews
  - generate-probes: Create follow-up questions and probes
  - simulate-interview: Run practice interview session
  - refine-questions: Improve question clarity and flow
  - create-protocol: Build interview execution protocol

dependencies:
  templates:
    - discussion-guide-tmpl.yaml
    - interview-protocol-tmpl.yaml
    - probe-bank-tmpl.yaml
    - consent-form-tmpl.yaml
  tasks:
    - create-discussion-guide.md
    - generate-interview-probes.md
    - simulate-interview-session.md
    - create-interview-protocol.md
  data:
    - interview-techniques.md
    - cognitive-biases.md
    - rapport-building.md
```

**AI Agent Creation Prompt**:
"Create an interview specialist agent focused on interview guide creation and execution. Use the PM agent's elicitation approach and UX expert's empathy as references. Include capabilities for generating unbiased questions, creating follow-up probes, and simulating interviews. The agent should understand various interview techniques and cognitive biases to avoid."

### 1.4 Data Analyst Agent

**File**: `agents/data-analyst.md`

**Reference BMAD Files**:
- `bmad-core/agents/qa.md` (for systematic analysis)
- `bmad-core/agents/architect.md` (for structured approach)

**Structure & Key Details**:
```yaml
agent:
  name: Alex
  id: data-analyst
  title: Senior Research Analyst
  icon: 📊
  whenToUse: Use for transcript analysis, thematic coding, statistical analysis, and pattern identification

persona:
  role: Qualitative & Quantitative Analysis Expert
  style: Systematic, thorough, objective, detail-oriented
  core_principles:
    - Systematic Coding - Apply consistent analysis frameworks
    - Inter-rater Reliability - Ensure coding consistency
    - Data Saturation - Identify when themes are exhausted
    - Mixed Methods - Integrate qual and quant insights

commands:
  - analyze-transcript: Process interview transcripts
  - extract-themes: Identify recurring themes
  - code-responses: Apply coding framework
  - create-affinity: Build affinity diagrams
  - calculate-stats: Perform statistical analysis
  - sentiment-analysis: Analyze emotional patterns

dependencies:
  templates:
    - transcript-analysis-tmpl.yaml
    - coding-framework-tmpl.yaml
    - affinity-map-tmpl.yaml
    - statistical-summary-tmpl.yaml
  tasks:
    - analyze-transcript.md
    - extract-themes.md
    - create-affinity-diagram.md
    - perform-statistical-analysis.md
    - conduct-sentiment-analysis.md
  data:
    - coding-frameworks.md
    - analysis-methods.md
    - statistical-tests.md
```

**AI Agent Creation Prompt**:
"Create a data analyst agent specialized in qualitative and quantitative research analysis. Reference the QA agent's systematic review approach. Include capabilities for transcript coding, theme extraction, affinity mapping, and statistical analysis. The agent should understand various coding frameworks and maintain inter-rater reliability standards."

### 1.5 Insight Synthesizer Agent

**File**: `agents/insight-synthesizer.md`

**Reference BMAD Files**:
- `bmad-core/agents/architect.md` (for synthesis patterns)
- `bmad-core/agents/pm.md` (for requirement extraction)

**Structure & Key Details**:
```yaml
agent:
  name: Dr. Riley
  id: insight-synthesizer
  title: Principal Insight Synthesizer
  icon: 💡
  whenToUse: Use for cross-interview synthesis, pattern recognition, persona creation, and requirement extraction

persona:
  role: Pattern Recognition & Insight Generation Specialist
  style: Insightful, creative, systematic, strategic
  core_principles:
    - Pattern Recognition - Identify cross-cutting themes
    - Insight Depth - Go beyond surface observations
    - Actionable Findings - Generate practical recommendations
    - User Centricity - Maintain focus on user needs

commands:
  - synthesize-findings: Integrate findings across interviews
  - extract-requirements: Identify user requirements
  - create-personas: Generate user personas
  - identify-jtbd: Extract jobs-to-be-done
  - map-journey: Create customer journey maps
  - find-opportunities: Identify innovation opportunities

dependencies:
  templates:
    - synthesis-framework-tmpl.yaml
    - persona-profile-tmpl.yaml
    - journey-map-tmpl.yaml
    - requirements-matrix-tmpl.yaml
    - jtbd-framework-tmpl.yaml
  tasks:
    - synthesize-cross-interview.md
    - extract-user-requirements.md
    - create-user-personas.md
    - map-customer-journey.md
    - identify-jobs-to-be-done.md
  data:
    - persona-frameworks.md
    - jtbd-methodology.md
```

**AI Agent Creation Prompt**:
"Create an insight synthesizer agent that specializes in pattern recognition and insight generation. Use the architect's synthesis capabilities and PM's requirement extraction as references. Include abilities to create personas, identify jobs-to-be-done, and generate actionable recommendations from research findings."

### 1.6 Research Reporter Agent

**File**: `agents/research-reporter.md`

**Reference BMAD Files**:
- `bmad-core/agents/pm.md` (for document creation)
- `bmad-core/agents/analyst.md` (for reporting structure)

**Structure & Key Details**:
```yaml
agent:
  name: Taylor
  id: research-reporter
  title: Lead Research Reporter
  icon: 📝
  whenToUse: Use for creating research reports, executive summaries, and data visualizations

persona:
  role: Research Communication & Visualization Expert
  style: Clear, compelling, visual, strategic
  core_principles:
    - Clarity First - Make findings accessible to all audiences
    - Visual Storytelling - Use data visualization effectively
    - Executive Focus - Highlight strategic implications
    - Evidence-Based - Support all claims with data

commands:
  - generate-report: Create comprehensive research report
  - create-summary: Build executive summary
  - design-visuals: Generate data visualizations
  - draft-recommendations: Formulate strategic recommendations
  - export-findings: Package deliverables

dependencies:
  templates:
    - research-report-tmpl.yaml
    - executive-summary-tmpl.yaml
    - visualization-specs-tmpl.yaml
    - recommendations-tmpl.yaml
  tasks:
    - generate-research-report.md
    - create-executive-summary.md
    - design-visualizations.md
    - formulate-recommendations.md
  data:
    - visualization-guidelines.md
    - reporting-standards.md
```

**AI Agent Creation Prompt**:
"Create a research reporter agent focused on report generation and communication. Reference PM's document creation and analyst's reporting approaches. Include capabilities for creating comprehensive reports, executive summaries, and data visualizations. The agent should translate complex findings into clear, actionable insights."

## Phase 2: Complete Task Definitions (24 Tasks)

### 2.1 Project Establishment Tasks

#### Task: establish-research-project.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a task workflow for establishing a research project. Follow the create-doc.md pattern from BMAD with mandatory elicitation points. Include steps for defining objectives, mapping stakeholders, and planning resources. Each section should require user confirmation before proceeding."

**Full Task Definition**:
```markdown
# Establish Research Project

## Task Configuration
elicit: true
template: research-brief-tmpl.yaml
output: docs/research/project-brief.md

## Workflow Steps
1. Define Research Objectives
   - Business goals alignment
   - Research questions formulation
   - Success criteria definition

2. Stakeholder Mapping
   - Identify key stakeholders
   - Define communication plan
   - Set review gates

3. Resource Planning
   - Timeline establishment
   - Budget allocation
   - Team assignment

## Elicitation Points
- After objectives: Review and refine research questions
- After stakeholder map: Validate coverage and priorities
- After resource plan: Confirm feasibility
```

#### Task: select-research-methodology.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a methodology selection task that guides users through choosing appropriate research methods based on objectives, constraints, and requirements. Include systematic evaluation criteria and decision frameworks."

**Full Task Definition**:
```markdown
# Select Research Methodology

## Task Configuration
elicit: true
template: methodology-matrix-tmpl.yaml
output: docs/research/methodology-selection.md

## Workflow Steps
1. Analyze Research Questions
   - Question type classification
   - Required depth of insight
   - Stakeholder expectations

2. Evaluate Method Options
   - Qualitative vs quantitative
   - Resource requirements
   - Timeline considerations

3. Create Methodology Matrix
   - Score methods against criteria
   - Document trade-offs
   - Justify final selection

## Decision Framework
- Exploratory: Qualitative methods preferred
- Descriptive: Quantitative methods preferred
- Explanatory: Mixed methods optimal
```

### 2.2 Study Design Tasks

#### Task: design-research-study.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a comprehensive study design task that covers all aspects of research planning including participants, data collection, and analysis frameworks. Use systematic design principles."

#### Task: create-screening-questionnaire.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a screening questionnaire development task that helps identify and recruit appropriate research participants. Include bias reduction and validation techniques."

#### Task: setup-conjoint-analysis.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a conjoint analysis setup task that guides the configuration of attributes, levels, choice sets, and sample size calculations for preference research."

#### Task: plan-ethnographic-study.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create an ethnographic research planning task that addresses observation protocols, cultural considerations, and longitudinal data collection approaches."

### 2.3 Interview Tasks

#### Task: create-discussion-guide.md
**Reference**: `bmad-core/tasks/create-doc.md`, `bmad-core/tasks/advanced-elicitation.md`

**AI Agent Creation Prompt**:
"Create a task for generating interview discussion guides. Use create-doc.md as the base pattern and incorporate advanced-elicitation.md techniques. Include sections for opening, core questions, and closing. Implement the 9-option elicitation format for user interaction."

#### Task: generate-interview-probes.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a probe generation task that helps create effective follow-up questions for interviews. Include different probe types and usage guidelines."

#### Task: simulate-interview-session.md
**Reference**: `bmad-core/tasks/execute-checklist.md`

**AI Agent Creation Prompt**:
"Create an interview simulation task that allows practice and refinement of interview techniques before actual data collection."

#### Task: create-interview-protocol.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a comprehensive interview protocol task covering pre-interview, during-interview, and post-interview procedures."

### 2.4 Analysis Tasks

#### Task: analyze-transcript.md
**Reference**: `bmad-core/tasks/review-story.md`, `bmad-core/tasks/trace-requirements.md`

**AI Agent Creation Prompt**:
"Create a transcript analysis task following review-story.md's systematic approach. Include multi-pass coding, thematic grouping, and insight extraction. Add quality checks for coding consistency and theme saturation."

#### Task: extract-themes.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a theme extraction task that systematically identifies patterns and themes from coded data. Include validation and refinement processes."

#### Task: create-affinity-diagram.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create an affinity diagramming task that organizes research insights into meaningful clusters and hierarchies."

#### Task: perform-statistical-analysis.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a statistical analysis task for quantitative research data including descriptive statistics, hypothesis testing, and effect size calculations."

#### Task: conduct-sentiment-analysis.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a sentiment analysis task specifically designed for user research data that can identify emotional patterns and intensity."

### 2.5 Synthesis Tasks

#### Task: synthesize-cross-interview.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a cross-interview synthesis task that identifies patterns and insights across multiple data sources."

#### Task: extract-user-requirements.md
**Reference**: `bmad-core/tasks/trace-requirements.md`

**AI Agent Creation Prompt**:
"Create a requirements extraction task that translates user research findings into actionable product requirements."

#### Task: create-user-personas.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a persona development task that builds evidence-based user personas from research data."

#### Task: map-customer-journey.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a customer journey mapping task that visualizes the end-to-end user experience based on research insights."

#### Task: identify-jobs-to-be-done.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a jobs-to-be-done identification task that uncovers the underlying jobs users are trying to accomplish."

### 2.6 Reporting Tasks

#### Task: generate-research-report.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a comprehensive research report generation task that compiles all findings into a professional, actionable document."

#### Task: create-executive-summary.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create an executive summary task that distills key findings and recommendations for senior stakeholders."

#### Task: design-visualizations.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a data visualization task that transforms research findings into clear, compelling visual presentations."

#### Task: formulate-recommendations.md
**Reference**: `bmad-core/tasks/create-doc.md`

**AI Agent Creation Prompt**:
"Create a recommendations formulation task that translates insights into prioritized, actionable strategic recommendations."

## Phase 3: Complete Template Library (24 Templates)

### 3.1 Project Templates

#### Template: research-brief-tmpl.yaml
**Reference**: `bmad-core/templates/prd-tmpl.yaml`, `bmad-core/templates/project-brief-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a research brief template following the structure of prd-tmpl.yaml and project-brief-tmpl.yaml. Include sections for executive summary, research questions, methodology, and deliverables. Each section should have elicit:true for user interaction and clear instructions."

#### Template: methodology-matrix-tmpl.yaml
**Reference**: `bmad-core/templates/project-brief-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a methodology selection matrix template that helps evaluate and compare different research approaches systematically."

### 3.2 Study Design Templates

#### Template: study-design-tmpl.yaml
**Reference**: `bmad-core/templates/architecture-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a comprehensive study design template that covers all aspects of research planning and execution."

#### Template: screening-criteria-tmpl.yaml
**Reference**: `bmad-core/templates/story-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a participant screening template that defines inclusion/exclusion criteria and screening procedures."

#### Template: conjoint-setup-tmpl.yaml
**Reference**: `bmad-core/templates/architecture-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a conjoint analysis setup template covering attributes, levels, choice sets, and analysis planning."

#### Template: ethnographic-plan-tmpl.yaml
**Reference**: `bmad-core/templates/architecture-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create an ethnographic research planning template for observational studies and cultural research."

### 3.3 Interview Templates

#### Template: discussion-guide-tmpl.yaml
**Reference**: `bmad-core/templates/story-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a discussion guide template structured like story-tmpl.yaml but for interview guides. Include sections for logistics, opening, context exploration, deep dive topics, and future state discussion. Add elicitation points for iterative refinement of questions."

#### Template: interview-protocol-tmpl.yaml
**Reference**: `bmad-core/templates/qa-gate-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create an interview protocol template covering all procedural aspects of interview execution."

#### Template: probe-bank-tmpl.yaml
**Reference**: `bmad-core/templates/brainstorming-output-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a probe bank template with categorized follow-up questions for different interview situations."

#### Template: consent-form-tmpl.yaml
**Reference**: `bmad-core/templates/project-brief-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a research consent form template ensuring ethical compliance and participant rights protection."

### 3.4 Analysis Templates

#### Template: transcript-analysis-tmpl.yaml
**Reference**: `bmad-core/templates/qa-gate-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a transcript analysis framework template for systematic qualitative data processing."

#### Template: coding-framework-tmpl.yaml
**Reference**: `bmad-core/templates/architecture-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a qualitative coding framework template for consistent data analysis."

#### Template: affinity-map-tmpl.yaml
**Reference**: `bmad-core/templates/brainstorming-output-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create an affinity mapping template for organizing and clustering research insights."

#### Template: statistical-summary-tmpl.yaml
**Reference**: `bmad-core/templates/competitor-analysis-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a statistical analysis summary template for quantitative research reporting."

#### Template: sentiment-analysis-tmpl.yaml
**Reference**: `bmad-core/templates/market-research-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a sentiment analysis template for emotional pattern identification in user research."

### 3.5 Synthesis Templates

#### Template: synthesis-framework-tmpl.yaml
**Reference**: `bmad-core/templates/architecture-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a cross-interview synthesis framework template for pattern identification across data sources."

#### Template: persona-profile-tmpl.yaml
**Reference**: `bmad-core/templates/front-end-spec-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a user persona profile template with evidence-based characteristics and behaviors."

#### Template: journey-map-tmpl.yaml
**Reference**: `bmad-core/templates/fullstack-architecture-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a customer journey mapping template visualizing touchpoints, emotions, and opportunities."

#### Template: requirements-matrix-tmpl.yaml
**Reference**: `bmad-core/templates/prd-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a user requirements matrix template linking research findings to product requirements."

#### Template: jtbd-framework-tmpl.yaml
**Reference**: `bmad-core/templates/story-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a jobs-to-be-done framework template for understanding user motivations and contexts."

### 3.6 Reporting Templates

#### Template: research-report-tmpl.yaml
**Reference**: `bmad-core/templates/prd-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a comprehensive research report template with executive summary, methodology, findings, and recommendations."

#### Template: executive-summary-tmpl.yaml
**Reference**: `bmad-core/templates/project-brief-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create an executive summary template focused on strategic insights and actionable recommendations."

#### Template: visualization-specs-tmpl.yaml
**Reference**: `bmad-core/templates/front-end-spec-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a data visualization specification template for research-appropriate charts and graphics."

#### Template: recommendations-tmpl.yaml
**Reference**: `bmad-core/templates/prd-tmpl.yaml`

**AI Agent Creation Prompt**:
"Create a strategic recommendations template with prioritization and implementation guidance."

## Phase 4: Complete Data Resources

### 4.1 Research Methods Knowledge Base
**File**: `data/research-methods-kb.md`
**Reference**: `bmad-core/data/bmad-kb.md`

**AI Agent Creation Prompt**:
"Create a comprehensive research methods knowledge base covering quantitative methods (conjoint, surveys), qualitative methods (interviews, ethnography), and mixed methods approaches. Include practical guidance, sample sizes, timelines, and best practices for each method."

### 4.2 Interview Techniques Resource
**File**: `data/interview-techniques.md`

**AI Agent Creation Prompt**:
"Create a detailed interview techniques reference covering question types, probing strategies, bias avoidance, rapport building, and cultural sensitivity considerations."

### 4.3 Cognitive Biases Reference
**File**: `data/cognitive-biases.md`

**AI Agent Creation Prompt**:
"Create a comprehensive cognitive biases reference specifically for user research, including researcher biases, participant biases, and mitigation strategies."

### 4.4 Sampling Methods Reference
**File**: `data/sampling-methods.md`

**AI Agent Creation Prompt**:
"Create a detailed sampling methods guide covering probability and non-probability sampling, sample size calculations, and recruitment strategies."

### 4.5 Statistical Power Reference
**File**: `data/statistical-power.md`

**AI Agent Creation Prompt**:
"Create a statistical power and sample size calculation guide for user research applications, including tools and practical examples."

### 4.6 Ethical Guidelines
**File**: `data/ethical-guidelines.md`

**AI Agent Creation Prompt**:
"Create comprehensive ethical guidelines for user research including consent procedures, privacy protection, and compliance requirements."

### 4.7 Rapport Building Techniques
**File**: `data/rapport-building.md`

**AI Agent Creation Prompt**:
"Create a rapport building guide for user research interviews focusing on trust establishment and comfortable environments."

### 4.8 Coding Frameworks Reference
**File**: `data/coding-frameworks.md`

**AI Agent Creation Prompt**:
"Create a comprehensive coding frameworks reference for qualitative analysis including different approaches and selection criteria."

### 4.9 Analysis Methods Guide
**File**: `data/analysis-methods.md`

**AI Agent Creation Prompt**:
"Create an analysis methods guide covering both qualitative and quantitative techniques for user research data."

### 4.10 Statistical Tests Reference
**File**: `data/statistical-tests.md`

**AI Agent Creation Prompt**:
"Create a statistical tests reference guide for user research applications including selection criteria and interpretation."

### 4.11 Persona Frameworks
**File**: `data/persona-frameworks.md`

**AI Agent Creation Prompt**:
"Create a persona development frameworks guide covering different approaches and validation methods."

### 4.12 Jobs-to-be-Done Methodology
**File**: `data/jtbd-methodology.md`

**AI Agent Creation Prompt**:
"Create a jobs-to-be-done methodology guide for user research applications and insight generation."

### 4.13 Visualization Guidelines
**File**: `data/visualization-guidelines.md`

**AI Agent Creation Prompt**:
"Create data visualization guidelines specifically for user research reporting and stakeholder communication."

### 4.14 Reporting Standards
**File**: `data/reporting-standards.md`

**AI Agent Creation Prompt**:
"Create reporting standards for user research including structure, evidence requirements, and quality criteria."

## Phase 5: Tool Requirements

### 5.1 Transcription Tools
**Tool Name**: `intelligent-transcription-service`

**Requirements**:
- Audio/video file input support (MP3, WAV, MP4, MOV)
- Speaker diarization (identify and separate speakers)
- Timestamp accuracy to 1-second precision
- Confidence scoring for transcription quality
- Export formats: TXT, JSON, SRT, VTT
- API access for batch processing
- Privacy/security compliance

**AI Agent Creation Prompt**:
"Create specifications for an intelligent transcription service that can process research interviews with speaker identification and high accuracy. Include technical requirements, output formats, and integration capabilities."

### 5.2 Statistical Analysis Scripts
**Tool Name**: `research-stats-analyzer`

**Requirements**:
- Descriptive statistics calculation
- Hypothesis testing capabilities
- Effect size calculations
- Power analysis functions
- Data visualization generation
- Multiple input format support

**AI Agent Creation Prompt**:
"Create a statistical analysis toolkit specifically designed for user research data. Include functions for descriptive statistics, group comparisons, effect size calculations, and power analysis."

### 5.3 Affinity Mapping Tool
**Tool Name**: `digital-affinity-mapper`

**Requirements**:
- Import coded data from analysis tools
- Drag-and-drop interface for grouping
- Hierarchical clustering capabilities
- Real-time collaboration support
- Export capabilities (images, structured data)

**AI Agent Creation Prompt**:
"Design a digital affinity mapping tool that can import coded research data and provide an intuitive interface for grouping and clustering insights."

### 5.4 Sentiment Analysis Engine
**Tool Name**: `research-sentiment-analyzer`

**Requirements**:
- Process interview transcripts and open-ended responses
- Multi-dimensional sentiment scoring
- Context-aware analysis
- Temporal pattern tracking
- Export structured sentiment data

**AI Agent Creation Prompt**:
"Create a sentiment analysis engine optimized for user research data that can detect nuanced emotions and track sentiment changes over time."

### 5.5 Data Visualization Generator
**Tool Name**: `research-viz-generator`

**Requirements**:
- Template library for research charts
- Brand-compliant styling options
- Interactive visualization capabilities
- Multiple export formats
- Accessibility compliance

**AI Agent Creation Prompt**:
"Design a visualization generator specifically for user research outputs that can create publication-ready charts and graphs with accessibility features."

### 5.6 Research Data Pipeline
**Tool Name**: `research-data-orchestrator`

**Requirements**:
- Workflow orchestration capabilities
- Data quality validation
- Error handling and recovery
- Progress monitoring and reporting
- Integration with all analysis tools

**AI Agent Creation Prompt**:
"Create a data pipeline orchestrator that can automatically process user research data through multiple analysis stages while maintaining quality controls."

### 5.7 Participant Management System
**Tool Name**: `research-participant-manager`

**Requirements**:
- Participant database with screening criteria
- Scheduling and calendar integration
- Consent form management
- Incentive tracking and distribution
- Privacy and compliance features

**AI Agent Creation Prompt**:
"Design a comprehensive participant management system that can handle recruitment, screening, scheduling, and compliance for user research studies."

## Phase 6: Workflow Definitions

### 6.1 End-to-End User Interview Research Workflow
**File**: `workflows/user-interview-research.yaml`
**Reference**: `bmad-core/workflows/greenfield-fullstack.yaml`

**AI Agent Creation Prompt**:
"Create a complete user interview research workflow following greenfield-fullstack.yaml structure. Include sequential agent actions from project establishment through report generation with quality gates."

### 6.2 Rapid Discovery Sprint Workflow
**File**: `workflows/rapid-discovery.yaml`

**AI Agent Creation Prompt**:
"Create a 5-day rapid discovery workflow for quick insights generation with compressed timelines."

### 6.3 Conjoint Analysis Workflow
**File**: `workflows/conjoint-analysis.yaml`

**AI Agent Creation Prompt**:
"Create a quantitative conjoint analysis workflow for preference research and trade-off analysis."

### 6.4 Ethnographic Research Workflow
**File**: `workflows/ethnographic-research.yaml`

**AI Agent Creation Prompt**:
"Create an ethnographic research workflow for in-depth observational studies and cultural insights."

### 6.5 Mixed Methods Research Workflow
**File**: `workflows/mixed-methods-research.yaml`

**AI Agent Creation Prompt**:
"Create a mixed methods research workflow that integrates qualitative and quantitative approaches systematically."

## Phase 7: Quality Framework

### 7.1 Research Quality Checklist
**File**: `checklists/research-quality-checklist.md`
**Reference**: `bmad-core/checklists/po-master-checklist.md`

**AI Agent Creation Prompt**:
"Create a comprehensive research quality checklist covering pre-research, data collection, analysis, and reporting phases with specific, verifiable criteria."

### 7.2 Interview Quality Checklist
**File**: `checklists/interview-quality-checklist.md`
**Reference**: `bmad-core/checklists/story-draft-checklist.md`

**AI Agent Creation Prompt**:
"Create an interview quality checklist covering preparation, execution, and post-interview procedures."

### 7.3 Analysis Quality Checklist
**File**: `checklists/analysis-quality-checklist.md`
**Reference**: `bmad-core/checklists/architect-checklist.md`

**AI Agent Creation Prompt**:
"Create an analysis quality checklist ensuring systematic coding, theme development, and insight generation standards."

## Implementation Roadmap

### Week 1: Foundation Architecture & Core Infrastructure
**Priority**: System Foundation | **Team**: Core Development + Research Lead
**Deliverables**:
- Complete directory structure implementation (`user-research/` with all 8 subdirectories)
- Core configuration file (`core-config.yaml`) with agent registry and dependencies
- Research Orchestrator Agent (Dr. Morgan) - fully functional with all 6 commands
- Primary task: `establish-research-project.md` with elicitation framework
- Primary template: `research-brief-tmpl.yaml` with all sections

**Quality Checkpoint**:
- All directory paths accessible
- Agent loads without errors
- Basic project creation workflow functional
- Configuration validates against schema

**Resource Allocation**: 2 developers, 1 research expert, 40 hours total

### Week 2: Research Strategy & Methodology Foundation
**Priority**: Strategic Agents | **Team**: Research Strategy + Development
**Deliverables**:
- Research Strategist Agent (Dr. Sarah) - complete with 6 specialized commands
- Tasks: `select-research-methodology.md`, `design-research-study.md`, `create-screening-questionnaire.md`
- Templates: `methodology-matrix-tmpl.yaml`, `study-design-tmpl.yaml`, `screening-criteria-tmpl.yaml`
- Data resources: `research-methods-kb.md`, `sampling-methods.md`, `statistical-power.md`

**Quality Checkpoint**:
- Agent commands execute successfully
- Methodology selection matrix functional
- Study design workflow validates
- Cross-agent communication established

**Resource Allocation**: 1 senior developer, 1 research methodologist, 45 hours total

### Week 3: Interview Capabilities & Interaction Design
**Priority**: Core Interview System | **Team**: UX Research + Development
**Deliverables**:
- Interview Specialist Agent (Jamie) - complete with 5 interaction commands
- Tasks: `create-discussion-guide.md`, `generate-interview-probes.md`, `simulate-interview-session.md`
- Templates: `discussion-guide-tmpl.yaml`, `interview-protocol-tmpl.yaml`, `probe-bank-tmpl.yaml`, `consent-form-tmpl.yaml`
- Data resources: `interview-techniques.md`, `cognitive-biases.md`, `rapport-building.md`

**Quality Checkpoint**:
- Discussion guide generation functional
- Interview simulation capability working
- Probe generation producing quality outputs
- Bias detection and mitigation active

**Resource Allocation**: 1 developer, 1 interview specialist, 1 UX researcher, 50 hours total

### Week 4: Analysis Engine & Data Processing
**Priority**: Data Analysis Core | **Team**: Data Science + Development
**Deliverables**:
- Data Analyst Agent (Alex) - complete with 6 analysis commands
- Tasks: `analyze-transcript.md`, `extract-themes.md`, `create-affinity-diagram.md`, `perform-statistical-analysis.md`
- Templates: `transcript-analysis-tmpl.yaml`, `coding-framework-tmpl.yaml`, `affinity-map-tmpl.yaml`, `statistical-summary-tmpl.yaml`
- Data resources: `coding-frameworks.md`, `analysis-methods.md`, `statistical-tests.md`

**Quality Checkpoint**:
- Transcript processing pipeline functional
- Theme extraction accuracy >85%
- Statistical analysis capabilities validated
- Coding consistency measures implemented

**Resource Allocation**: 1 senior developer, 1 data scientist, 1 qualitative researcher, 55 hours total

### Week 5: Insight Synthesis & Pattern Recognition
**Priority**: Intelligence Layer | **Team**: Research Intelligence + Development
**Deliverables**:
- Insight Synthesizer Agent (Dr. Riley) - complete with 6 synthesis commands
- Tasks: `synthesize-cross-interview.md`, `extract-user-requirements.md`, `create-user-personas.md`, `map-customer-journey.md`, `identify-jobs-to-be-done.md`
- Templates: `synthesis-framework-tmpl.yaml`, `persona-profile-tmpl.yaml`, `journey-map-tmpl.yaml`, `requirements-matrix-tmpl.yaml`, `jtbd-framework-tmpl.yaml`
- Data resources: `persona-frameworks.md`, `jtbd-methodology.md`

**Quality Checkpoint**:
- Cross-interview synthesis producing coherent insights
- Persona generation based on evidence
- Journey mapping capabilities functional
- Requirements extraction accuracy >90%

**Resource Allocation**: 1 developer, 1 senior researcher, 1 product strategist, 50 hours total

### Week 6: Reporting & Communication Systems
**Priority**: Output Generation | **Team**: Communication + Development
**Deliverables**:
- Research Reporter Agent (Taylor) - complete with 5 reporting commands
- Tasks: `generate-research-report.md`, `create-executive-summary.md`, `design-visualizations.md`, `formulate-recommendations.md`
- Templates: `research-report-tmpl.yaml`, `executive-summary-tmpl.yaml`, `visualization-specs-tmpl.yaml`, `recommendations-tmpl.yaml`
- Data resources: `visualization-guidelines.md`, `reporting-standards.md`

**Quality Checkpoint**:
- Report generation producing publication-ready outputs
- Executive summaries meeting C-level standards
- Visualizations accessible and compelling
- Recommendations actionable and prioritized

**Resource Allocation**: 1 developer, 1 technical writer, 1 design specialist, 45 hours total

### Week 7: Workflow Integration & End-to-End Testing
**Priority**: System Integration | **Team**: Full Team Coordination
**Deliverables**:
- 5 complete workflow definitions: `user-interview-research.yaml`, `rapid-discovery.yaml`, `conjoint-analysis.yaml`, `ethnographic-research.yaml`, `mixed-methods-research.yaml`
- Remaining specialized tasks (conjoint, ethnographic, sentiment analysis)
- Advanced templates for specialized methods
- Tool requirement specifications for all 7 external tools

**Integration Testing Phase**:
- End-to-end workflow execution testing
- Agent handoff validation between all 6 agents
- Template/task dependency verification
- Performance benchmarking against success metrics

**Quality Checkpoint**:
- All 5 workflows execute without errors
- Agent coordination seamless
- Data flows correctly between stages
- Performance meets >90% completion rate target

**Resource Allocation**: 3 developers, 2 researchers, 1 QA specialist, 60 hours total

### Week 8: Quality Framework & Validation Systems
**Priority**: Quality Assurance | **Team**: QA + Research Standards
**Deliverables**:
- 3 comprehensive checklists: `research-quality-checklist.md`, `interview-quality-checklist.md`, `analysis-quality-checklist.md`
- Quality gate implementations at each workflow stage
- Validation protocols for all 24 templates
- Error handling and recovery mechanisms
- Remaining data resources (ethical guidelines, advanced frameworks)

**Validation Testing**:
- Research quality standards verification
- Template output validation against industry standards
- Agent response accuracy testing (target >95%)
- Stakeholder acceptance testing

**Quality Checkpoint**:
- Quality gates functional and catching issues
- All checklists comprehensive and actionable
- Error recovery mechanisms working
- System ready for production use

**Resource Allocation**: 2 developers, 1 QA lead, 2 senior researchers, 50 hours total

## AI Agent Orchestration Instructions

### For Primary Orchestrator Agent
1. **Start with agents/research-orchestrator.md** as it coordinates all others
2. **Create agents in dependency order**: Orchestrator → Strategist → Others
3. **Test each component before integration**: Agent → Tasks → Templates → Workflows
4. **Use BMAD reference files as patterns** but adapt for research context
5. **Maintain consistency** in YAML structure and command patterns
6. **Implement elicitation points** strictly as defined
7. **Validate quality gates** at each phase transition

### For Individual Builder Agents
1. **Follow BMAD patterns exactly** from reference files
2. **Maintain YAML structure integrity** for system compatibility
3. **Include all required sections** (activation, persona, commands, dependencies)
4. **Test outputs** against quality checklists
5. **Document any deviations** from reference patterns
6. **Preserve elicitation requirements** without optimization

### Dependency Validation Protocol
1. **Verify all dependencies exist** with exact names as referenced
2. **Test dependency loading** in isolation
3. **Validate dependency relationships** work as intended
4. **Check for circular dependencies** and resolve
5. **Document dependency hierarchy** for maintenance

