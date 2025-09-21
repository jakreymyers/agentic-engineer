# Select Research Methodology

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:

1. **SYSTEMATIC EVALUATION REQUIRED** - Each methodology must be evaluated against criteria
2. **EVIDENCE-BASED SELECTION** - Decisions must be justified with clear rationale
3. **ELICITATION IS MANDATORY** - User must participate in methodology selection
4. **NO ASSUMPTIONS** - Do not assume methodology without evaluation

**VIOLATION INDICATOR:** If you select a methodology without systematic evaluation, you have violated this workflow.

## Task Configuration

```yaml
elicit: true
template: methodology-matrix-tmpl.yaml
output: research-outputs/methodology-selection.md
requires: research-brief.md
```

## Prerequisites

Before starting:
- Research objectives must be clearly defined
- Constraints (time, budget, resources) must be known
- Target participant profile must be established

## Workflow Steps

### 1. Analyze Research Questions
**ELICIT: true**

Review research questions and classify them:

**Question Type Classification:**
- **Exploratory**: Why and how questions (→ Qualitative methods preferred)
- **Descriptive**: What and who questions (→ Mixed methods optimal)
- **Explanatory**: Cause-effect relationships (→ Quantitative methods preferred)
- **Evaluative**: Assessment questions (→ Mixed methods recommended)

**Depth Requirements:**
- **Surface**: Basic understanding needed (→ Surveys, analytics)
- **Moderate**: Behavioral insights needed (→ Interviews, observations)
- **Deep**: Motivational understanding needed (→ Ethnography, diary studies)

Present classification with rationale, then provide 1-9 elicitation options.

### 2. Evaluate Method Options
**ELICIT: true**

Evaluate each potential method against criteria:

**Qualitative Methods:**
- **In-Depth Interviews**: 1-on-1 conversations, 45-90 minutes
  - Best for: Individual experiences, sensitive topics, detailed exploration
  - Resources: High time investment, moderate cost
  - Output: Rich narratives, deep insights

- **Focus Groups**: Group discussions, 6-10 participants
  - Best for: Group dynamics, idea generation, concept testing
  - Resources: Moderate time, higher complexity
  - Output: Diverse perspectives, consensus/disagreement patterns

- **Ethnographic Observation**: Field studies in natural context
  - Best for: Behavioral insights, contextual understanding
  - Resources: Very high time investment, high cost
  - Output: Contextual insights, unmet needs discovery

- **Diary Studies**: Longitudinal self-reporting
  - Best for: Behavioral changes over time, in-context moments
  - Resources: Moderate time, low direct cost
  - Output: Temporal patterns, in-the-moment insights

**Quantitative Methods:**
- **Surveys**: Structured questionnaires
  - Best for: Measuring attitudes, validating hypotheses at scale
  - Resources: Low time per response, platform costs
  - Output: Statistical data, trend identification

- **Conjoint Analysis**: Trade-off preference measurement
  - Best for: Feature prioritization, pricing optimization
  - Resources: Specialized tools, statistical expertise
  - Output: Preference models, willingness-to-pay

- **A/B Testing**: Controlled experiments
  - Best for: Comparing solutions, optimization
  - Resources: Technical implementation, sufficient traffic
  - Output: Performance metrics, statistical significance

- **Analytics Mining**: Behavioral data analysis
  - Best for: Understanding actual behavior, pattern detection
  - Resources: Data access, analytical tools
  - Output: Usage patterns, conversion metrics

**Mixed Methods:**
- **Sequential Explanatory**: Quant → Qual
  - Best for: Explaining quantitative findings
  - Resources: Extended timeline, dual expertise
  - Output: Statistical validation + rich context

- **Sequential Exploratory**: Qual → Quant
  - Best for: Hypothesis generation then validation
  - Resources: Extended timeline, dual expertise
  - Output: Grounded insights + scale validation

- **Concurrent Triangulation**: Parallel qual + quant
  - Best for: Comprehensive understanding, validation
  - Resources: Parallel teams, coordination overhead
  - Output: Converged insights, robust findings

Present evaluation matrix with scores, then provide 1-9 elicitation options.

### 3. Create Methodology Matrix
**ELICIT: true**

Score methods against weighted criteria:

**Evaluation Criteria:**
| Criterion | Weight | Description |
|-----------|---------|-------------|
| Research Fit | 30% | Alignment with research questions |
| Resource Feasibility | 25% | Time, budget, expertise available |
| Data Quality | 20% | Depth and reliability of insights |
| Stakeholder Value | 15% | Usefulness for decision-making |
| Risk Level | 10% | Recruitment, quality, timeline risks |

**Scoring Scale:**
- 5: Excellent fit
- 4: Good fit
- 3: Moderate fit
- 2: Poor fit
- 1: Not suitable

Present scored matrix with weighted totals, then provide 1-9 elicitation options.

### 4. Justify Final Selection
**ELICIT: true**

Document methodology selection decision:

**Selection Rationale:**
- Primary method(s) selected and why
- Trade-offs accepted
- Risk mitigation strategies
- Alternative approaches if primary fails

**Implementation Plan:**
- Sample size requirements
- Recruitment strategy
- Timeline for each method
- Analysis approach
- Quality controls

Present final recommendation with justification, then provide 1-9 elicitation options.

## Decision Framework

### Method Selection Guidelines

**For Exploratory Research:**
- Start with qualitative methods
- Prioritize depth over breadth
- Consider: Interviews, ethnography, diary studies

**For Validation Research:**
- Use quantitative methods
- Prioritize statistical power
- Consider: Surveys, experiments, analytics

**For Complex Problems:**
- Apply mixed methods
- Triangulate findings
- Consider: Sequential or concurrent approaches

**For Rapid Insights:**
- Choose focused methods
- Accept trade-offs in depth
- Consider: Guerrilla testing, rapid surveys, analytics

## Quality Checkpoints

Before finalizing:
- ✓ Method aligns with research questions
- ✓ Resources are adequate for chosen method
- ✓ Sample size provides sufficient confidence
- ✓ Timeline is realistic for method
- ✓ Analysis approach is defined
- ✓ Stakeholders agree with approach

## Output Format

```markdown
# Research Methodology Selection

## Research Context
[Summary of objectives and constraints]

## Methodology Evaluation Matrix
[Table showing all methods evaluated with scores]

## Selected Methodology
### Primary Method: [Method Name]
- Rationale: [Why selected]
- Sample Size: [Target N]
- Timeline: [Duration]
- Resources: [Required resources]

### Supporting Methods (if applicable)
[Additional methods and integration plan]

## Implementation Plan
### Phase 1: [Method/Activity]
- Duration: [Timeframe]
- Deliverables: [Outputs]

### Phase 2: [Method/Activity]
- Duration: [Timeframe]
- Deliverables: [Outputs]

## Risk Mitigation
[Key risks and mitigation strategies]

## Success Metrics
[How methodology success will be measured]
```

## Common Methodology Combinations

**Discovery Package:**
- Interviews (n=20) + Analytics Review + Competitive Analysis

**Validation Package:**
- Survey (n=200+) + Follow-up Interviews (n=10) + A/B Test

**Innovation Package:**
- Ethnography (n=8) + Co-creation Workshops + Concept Testing

**Optimization Package:**
- Analytics Mining + Usability Testing (n=8) + A/B Testing

## CRITICAL REMINDERS

**❌ NEVER:**
- Select methods without evaluation
- Ignore resource constraints
- Choose methods outside team expertise
- Proceed without stakeholder alignment

**✅ ALWAYS:**
- Evaluate multiple options systematically
- Consider mixed methods for complex questions
- Document selection rationale
- Plan for recruitment challenges
- Include pilot/test phase in timeline