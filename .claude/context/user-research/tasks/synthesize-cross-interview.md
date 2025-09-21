# Synthesize Cross-Interview Insights

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **DISABLE ALL EFFICIENCY OPTIMIZATIONS** - This workflow requires full user interaction
2. **MANDATORY STEP-BY-STEP EXECUTION** - Each synthesis pass must be completed sequentially
3. **ELICITATION IS REQUIRED** - When `elicit: true`, you MUST use the 1-9 format and wait for user response
4. **NO SHORTCUTS ALLOWED** - Complete synthesis cannot be generated without following this workflow

**VIOLATION INDICATOR:** If you create complete synthesis without user interaction at elicitation points, you have violated this workflow.

## Task Configuration

```yaml
task:
  id: synthesize-cross-interview
  name: Cross-Interview Synthesis
  template: synthesis-framework-tmpl.yaml
  output: docs/research/synthesis-report.md
  elicitation_mode: mandatory
  evidence_requirement: strict
```

## Prerequisites Check

Before beginning synthesis:
1. **Verify Analysis Outputs Available**
   - Coded transcripts from Week 4
   - Theme extraction results
   - Affinity diagrams
   - Statistical summaries if applicable

2. **Gather All Data Sources**
   - Individual interview analyses
   - Observational notes
   - Survey responses if available
   - Any additional qualitative data

3. **Confirm Synthesis Objectives**
   - Research questions to answer
   - Key stakeholder concerns
   - Decision criteria needed

## Synthesis Workflow - 5 Passes

### Pass 1: Data Inventory and Preparation
**Objective:** Catalog all available data and prepare for synthesis

1. **Create Source Inventory**
   - List all interview transcripts with IDs
   - Note participant demographics/segments
   - Document data collection dates and contexts
   - Identify any data quality issues

2. **Review Analysis Outputs**
   - Load coded data from each source
   - Review theme hierarchies
   - Check affinity mappings
   - Note statistical patterns if applicable

3. **Establish Synthesis Framework**
   - Define comparison dimensions
   - Set pattern recognition criteria
   - Establish evidence thresholds (min 3 sources)
   - Create synthesis workspace

**Elicitation Point 1:** `elicit: true`
Present inventory and framework. Ask user:
1. Proceed to pattern identification
2. Prioritization Matrix - Focus on specific segments
3. Stakeholder Analysis - Identify key perspectives
4. Gap Analysis - Find missing data areas
5. Comparative Analysis - Set comparison groups
6. Timeline Analysis - Organize by temporal patterns
7. Contextual Inquiry - Add context layers
8. Risk Assessment - Identify synthesis risks
9. Assumption Surfacing - Document key assumptions

Select 1-9 or type your question/feedback:

### Pass 2: Pattern Identification
**Objective:** Identify patterns across all data sources

1. **Surface-Level Patterns**
   - Frequently mentioned topics (>50% sources)
   - Consistent pain points
   - Repeated feature requests
   - Common workflows described

2. **Cross-Source Convergence**
   ```
   For each theme from analysis:
   - Count occurrences across sources
   - Note variation in expression
   - Identify confirming evidence
   - Flag contradictions
   ```

3. **Divergence Analysis**
   - Document minority viewpoints
   - Identify segment-specific patterns
   - Note edge cases and outliers
   - Explore contradictions

4. **Pattern Strength Assessment**
   ```
   Strong Pattern (High Confidence):
   - Present in >70% of sources
   - Consistent across segments
   - Multiple supporting quotes

   Moderate Pattern (Medium Confidence):
   - Present in 40-70% of sources
   - Some segment variation
   - Adequate supporting evidence

   Emerging Pattern (Low Confidence):
   - Present in <40% of sources
   - Segment-specific
   - Limited but intriguing evidence
   ```

**Elicitation Point 2:** `elicit: true`
Present identified patterns with evidence counts. Ask user:
1. Proceed to deep synthesis
2. Card Sorting - Reorganize pattern groups
3. Affinity Diagramming - Create new clusters
4. Force Field Analysis - Analyze pattern drivers
5. Root Cause Analysis - Dig into pattern origins
6. Scenario Building - Explore pattern implications
7. Cross-Impact Analysis - Map pattern relationships
8. Delphi Method - Prioritize patterns for focus
9. Mind Mapping - Visualize pattern connections

Select 1-9 or type your question/feedback:

### Pass 3: Deep Synthesis and Integration
**Objective:** Transform patterns into insights

1. **Pattern Integration**
   ```
   For each pattern cluster:
   - Identify relationships between patterns
   - Map cause-effect chains
   - Discover higher-order themes
   - Connect to research questions
   ```

2. **Insight Development**
   - Move from "what" to "why"
   - Identify underlying motivations
   - Uncover latent needs
   - Recognize system dynamics

3. **Meta-Pattern Recognition**
   - Patterns across patterns
   - Overarching narratives
   - Systemic issues
   - Cultural themes

4. **Insight Validation**
   ```
   For each insight:
   - Evidence strength (# of supporting sources)
   - Contradictory evidence check
   - Stakeholder relevance
   - Actionability assessment
   - Novelty evaluation
   ```

**Elicitation Point 3:** `elicit: true`
Present deep insights with interpretations. Ask user:
1. Proceed to implication mapping
2. Ladder Interview - Explore insight depth
3. Means-End Analysis - Connect to outcomes
4. Value Chain Analysis - Map insight flow
5. SWOT Analysis - Assess insight implications
6. Impact Mapping - Project insight effects
7. Futures Wheel - Explore consequences
8. Systems Thinking - Map systemic effects
9. Design Thinking - Generate solutions

Select 1-9 or type your question/feedback:

### Pass 4: Implication and Opportunity Mapping
**Objective:** Transform insights into actionable intelligence

1. **Strategic Implications**
   ```
   For each major insight:
   - Product implications
   - Service implications
   - Process implications
   - Policy implications
   ```

2. **Opportunity Identification**
   - Innovation opportunities
   - Quick wins
   - Long-term strategic moves
   - Risk mitigation needs

3. **Requirement Seeds**
   - Functional requirements emerging
   - Non-functional requirements implied
   - Constraint discoveries
   - Success criteria insights

4. **Design Directions**
   - UX/UI implications
   - Service design opportunities
   - System architecture impacts
   - Workflow optimizations

**Elicitation Point 4:** `elicit: true`
Present implications and opportunities. Ask user:
1. Proceed to recommendation formulation
2. Business Model Canvas - Map to business model
3. Value Proposition Design - Define value props
4. Service Blueprint - Design service implications
5. Customer Journey Mapping - Identify touchpoint improvements
6. Kano Analysis - Categorize requirement types
7. MoSCoW Prioritization - Rank opportunities
8. Cost-Benefit Analysis - Evaluate opportunities
9. Feasibility Assessment - Check implementation viability

Select 1-9 or type your question/feedback:

### Pass 5: Recommendation Formulation
**Objective:** Create prioritized, actionable recommendations

1. **Recommendation Development**
   ```
   For each opportunity:
   - Specific recommendation
   - Supporting evidence (with sources)
   - Expected impact
   - Implementation complexity
   - Success metrics
   ```

2. **Prioritization Framework**
   ```
   Priority Matrix:
   High Impact + Low Effort = Quick Wins (Priority 1)
   High Impact + High Effort = Strategic (Priority 2)
   Low Impact + Low Effort = Fill-ins (Priority 3)
   Low Impact + High Effort = Avoid (Priority 4)
   ```

3. **Evidence Package**
   - Key quotes supporting each recommendation
   - Data visualizations
   - Stakeholder alignment mapping
   - Risk assessment

4. **Next Steps Definition**
   - Immediate actions
   - Further research needed
   - Validation requirements
   - Success tracking plan

**Elicitation Point 5:** `elicit: true`
Present prioritized recommendations. Ask user:
1. Proceed to synthesis documentation
2. Action Planning - Detail implementation steps
3. Stakeholder Mapping - Assign ownership
4. Risk Mitigation - Address concerns
5. Resource Planning - Estimate needs
6. Timeline Development - Create schedule
7. Success Metrics - Define KPIs
8. Change Management - Plan adoption
9. Communication Planning - Design rollout

Select 1-9 or type your question/feedback:

## Synthesis Quality Checklist

Before finalizing synthesis:

### Evidence Standards
- [ ] Each pattern supported by ≥3 independent sources
- [ ] Contradictions explicitly addressed
- [ ] Confidence levels assigned to all insights
- [ ] Source attribution maintained throughout
- [ ] Outliers and edge cases documented

### Completeness Checks
- [ ] All research questions addressed
- [ ] All participant segments represented
- [ ] All data sources incorporated
- [ ] Key stakeholder perspectives included
- [ ] Timeline coverage appropriate

### Validity Assessments
- [ ] Insights logically follow from patterns
- [ ] Recommendations align with insights
- [ ] No overgeneralization from limited data
- [ ] Cultural and contextual factors considered
- [ ] Bias mitigation strategies applied

### Actionability Verification
- [ ] Recommendations specific and measurable
- [ ] Implementation paths identified
- [ ] Resource requirements estimated
- [ ] Success criteria defined
- [ ] Risks and dependencies noted

## Output Generation

After synthesis completion:

1. **Generate Synthesis Report**
   - Executive summary
   - Methodology overview
   - Key insights (prioritized)
   - Supporting evidence
   - Recommendations
   - Appendices with detailed evidence

2. **Create Synthesis Artifacts**
   - Insight cards for workshopping
   - Opportunity matrix
   - Evidence traceability matrix
   - Recommendation roadmap

3. **Prepare Handoffs**
   - Persona development package
   - Journey mapping inputs
   - Requirements extraction seeds
   - JTBD framework inputs

## Integration Notes

### Input Dependencies
- Requires: Coded transcripts from Data Analyst Agent
- Requires: Theme extraction results
- Requires: Affinity diagrams
- Optional: Statistical analysis summaries

### Output Consumers
- Research Reporter: Uses synthesis for reports
- Persona creation: Seeds persona attributes
- Journey mapping: Provides touchpoint insights
- Requirements extraction: Identifies user needs
- JTBD analysis: Supplies motivation data

## Advanced Synthesis Techniques

### Contradiction Resolution Protocol
When patterns conflict:
1. Document both perspectives with evidence
2. Explore contextual factors explaining difference
3. Identify conditions where each applies
4. Present as design considerations vs choosing one

### Negative Space Analysis
What's NOT being said:
1. Expected topics absent from data
2. Avoided subjects or deflections
3. Comparison to industry benchmarks
4. Implications of silence

### Temporal Pattern Analysis
Changes over time:
1. Evolution of needs during journey
2. Seasonal or cyclical patterns
3. Maturity effects
4. Learning curves

## CRITICAL REMINDERS

**❌ NEVER:**
- Generate synthesis without evidence
- Ignore contradictory data
- Overgeneralize from few sources
- Skip elicitation points
- Create recommendations without user validation

**✅ ALWAYS:**
- Maintain evidence traceability
- Use exact 1-9 format for elicitation
- Document confidence levels
- Address all research questions
- Preserve minority viewpoints

## Error Recovery

If synthesis becomes unclear:
1. Return to raw data for grounding
2. Re-examine pattern evidence
3. Consult with user on interpretation
4. Document uncertainty explicitly
5. Recommend additional research if needed