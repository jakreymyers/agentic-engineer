# Design Research Study

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:

1. **COMPREHENSIVE DESIGN REQUIRED** - All aspects of study must be specified
2. **SYSTEMATIC PLANNING** - Each component must build on previous decisions
3. **ELICITATION IS MANDATORY** - User must approve key design decisions
4. **NO SHORTCUTS** - Complete study design cannot be created without this workflow

**VIOLATION INDICATOR:** If you create a study design without systematic planning, you have violated this workflow.

## Task Configuration

```yaml
elicit: true
template: study-design-tmpl.yaml
output: research-outputs/study-design.md
requires:
  - research-brief.md
  - methodology-selection.md
```

## Prerequisites

Before starting:
- Research objectives must be defined
- Methodology must be selected
- Resources and constraints must be known
- Ethical guidelines must be reviewed

## Workflow Steps

### 1. Study Foundation
**ELICIT: true**

Establish the foundation for the study design:

**Study Overview:**
- Study title and identifier
- Research type (exploratory/descriptive/explanatory/evaluative)
- Primary methodology (qual/quant/mixed)
- Expected duration (start to final report)
- Key stakeholders and their roles

**Research Objectives Mapping:**
- Map each research question to specific study components
- Define how each objective will be measured/assessed
- Specify expected insights for each objective
- Identify dependencies between objectives

Present foundation with rationale, then provide 1-9 elicitation options.

### 2. Participant Design
**ELICIT: true**

Define comprehensive participant strategy:

**Target Population:**
- **Primary Characteristics**: Demographics, behaviors, needs
- **Inclusion Criteria**: Must-have characteristics
- **Exclusion Criteria**: Disqualifying factors
- **Segmentation Strategy**: How to ensure diversity

**Sampling Strategy:**
- **Method**: Probability/purposive/convenience/snowball
- **Sample Size**: Target N with justification
- **Recruitment Channels**: Where to find participants
- **Screening Process**: How to verify eligibility

**Recruitment Plan:**
```
Week 1-2: Channel setup and initial outreach
Week 2-3: Screening and qualification
Week 3-4: Scheduling and confirmation
Buffer: 25% over-recruitment for no-shows
```

Present participant design with rationale, then provide 1-9 elicitation options.

### 3. Data Collection Design
**ELICIT: true**

Specify detailed data collection approach:

**Collection Methods:**
For each method selected:
- **Protocol**: Step-by-step process
- **Duration**: Time per session/participant
- **Setting**: Location/environment requirements
- **Materials**: Guides, prompts, stimuli needed
- **Recording**: Audio/video/notes approach

**Interview/Session Structure** (if applicable):
```
1. Introduction & Consent (5 min)
   - Welcome and rapport building
   - Consent review and signing
   - Permission for recording

2. Warm-up (5-10 min)
   - Context-setting questions
   - Participant background

3. Core Exploration (30-45 min)
   - Main research topics
   - Probing and follow-ups

4. Deep Dives (15-20 min)
   - Specific areas of interest
   - Scenarios or exercises

5. Wrap-up (5 min)
   - Final thoughts
   - Next steps explanation
```

**Quality Controls:**
- Pilot testing plan (minimum 2 sessions)
- Inter-rater reliability measures
- Data quality checkpoints
- Contingency for poor quality data

Present data collection design with details, then provide 1-9 elicitation options.

### 4. Analysis Framework
**ELICIT: true**

Define comprehensive analysis approach:

**Qualitative Analysis** (if applicable):
- **Approach**: Thematic/content/narrative/grounded theory
- **Coding Strategy**:
  - Round 1: Open coding for emergence
  - Round 2: Axial coding for relationships
  - Round 3: Selective coding for themes
- **Tools**: Software and frameworks to use
- **Validation**: Member checking, peer debriefing

**Quantitative Analysis** (if applicable):
- **Descriptive Statistics**: Means, frequencies, distributions
- **Inferential Tests**: T-tests, ANOVA, regression as needed
- **Effect Sizes**: Cohen's d, r-squared calculations
- **Confidence Levels**: 95% CI standard

**Mixed Methods Integration**:
- **Integration Points**: Where qual and quant merge
- **Triangulation Strategy**: How to compare findings
- **Weight of Evidence**: How to resolve conflicts

Present analysis framework with justification, then provide 1-9 elicitation options.

### 5. Project Management
**ELICIT: true**

Create detailed project plan:

**Timeline & Milestones:**
```markdown
| Phase | Week | Activities | Deliverables |
|-------|------|------------|--------------|
| Setup | 1-2 | IRB, materials prep | Study protocol |
| Recruitment | 2-4 | Outreach, screening | Participant roster |
| Data Collection | 4-8 | Sessions, quality checks | Raw data |
| Analysis | 8-10 | Coding, statistics | Findings document |
| Synthesis | 10-11 | Integration, insights | Draft report |
| Reporting | 11-12 | Review, finalization | Final report |
```

**Resource Allocation:**
- **Team Roles**: Who does what
- **Time Commitment**: Hours per week per role
- **Budget Distribution**: Breakdown by category
- **Tools & Infrastructure**: What's needed when

**Risk Management:**
```markdown
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Low recruitment | Medium | High | Multiple channels, increased incentive |
| Data quality | Low | High | Pilot testing, quality checks |
| Timeline slip | Medium | Medium | Buffer time, parallel work streams |
| Analysis complexity | Low | Medium | External expertise on standby |
```

Present project management plan, then provide 1-9 elicitation options.

### 6. Ethical Considerations
**ELICIT: true**

Address all ethical requirements:

**Consent Process:**
- Informed consent form development
- Process for obtaining consent
- Handling of vulnerable populations
- Right to withdraw procedures

**Data Protection:**
- Data anonymization approach
- Storage and security measures
- Retention and deletion policies
- Access control protocols

**Participant Welfare:**
- Compensation structure and rationale
- Handling of sensitive topics
- Support resources if needed
- Debriefing procedures

Present ethical framework with compliance notes, then provide 1-9 elicitation options.

## Decision Points

### Critical Design Decisions

**Sample Size Determination:**
- Qualitative: Saturation typically at 12-20
- Quantitative: Power analysis for effect size
- Mixed: Larger of the two requirements

**Session Duration:**
- Interviews: 45-90 minutes optimal
- Surveys: 15-20 minutes maximum
- Observations: 2-4 hours per session
- Diary studies: 1-4 weeks duration

**Incentive Guidelines:**
- Professional: $100-200/hour
- Consumer: $50-100/hour
- Students: $25-50/hour
- Diary studies: $10-20/day

## Quality Checkpoints

Before finalizing:
- ✓ All research questions have collection methods
- ✓ Sample size provides adequate confidence
- ✓ Timeline includes adequate buffers
- ✓ Budget covers all anticipated costs
- ✓ Team has required expertise
- ✓ Ethical requirements are addressed
- ✓ Analysis plan matches data type
- ✓ Deliverables meet stakeholder needs

## Output Format

```markdown
# Research Study Design

## Study Overview
- **Title**: [Study name]
- **Duration**: [Total weeks]
- **Methodology**: [Primary approach]
- **Sample Size**: [Target N]

## Research Design
### Objectives & Questions
[Mapped objectives to methods]

### Participant Strategy
[Detailed recruitment and sampling plan]

### Data Collection Protocol
[Step-by-step procedures]

### Analysis Framework
[Detailed analysis approach]

## Project Plan
### Timeline
[Gantt chart or phase table]

### Resources
[Team, budget, tools breakdown]

### Risk Management
[Risk matrix with mitigations]

## Ethical Framework
[Consent, privacy, welfare measures]

## Quality Assurance
[Validation and reliability measures]

## Appendices
- A: Screening questionnaire
- B: Discussion guides
- C: Consent forms
- D: Analysis codebook
```

## CRITICAL REMINDERS

**❌ NEVER:**
- Skip pilot testing
- Underestimate recruitment time
- Ignore ethical requirements
- Proceed without clear analysis plan

**✅ ALWAYS:**
- Build in timeline buffers
- Over-recruit by 20-25%
- Document all decisions
- Prepare contingency plans
- Get stakeholder sign-off