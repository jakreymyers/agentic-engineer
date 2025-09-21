<!-- Powered by User Research System -->

# Generate Research Report

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **DISABLE ALL EFFICIENCY OPTIMIZATIONS** - This workflow requires full user interaction
2. **MANDATORY STEP-BY-STEP EXECUTION** - Each phase must be processed sequentially with user feedback
3. **ELICITATION IS REQUIRED** - When `elicit: true`, you MUST use the 1-9 format and wait for user response
4. **NO SHORTCUTS ALLOWED** - Complete reports cannot be generated without following this workflow

**VIOLATION INDICATOR:** If you create a complete report without user interaction at elicitation points, you have violated this workflow.

## Task Configuration

```yaml
task:
  name: Generate Research Report
  id: generate-research-report
  description: Create comprehensive research report from synthesized findings
  version: 1.0
  dependencies:
    templates:
      - research-report-tmpl.yaml
    data:
      - reporting-standards.md
      - visualization-guidelines.md
    inputs:
      - Synthesized insights from insight-synthesizer
      - Analysis outputs from data-analyst
      - User personas and journey maps
      - Interview highlights and quotes
      - Statistical summaries
  outputs:
    - Complete research report (20-50 pages)
    - Executive summary integrated
    - Data visualizations embedded
    - Appendices with raw data
```

## Phase 1: Report Planning & Structure

### 1.1 Assess Research Scope
**elicit: true**

Review all available research artifacts:
- Interview transcripts analyzed: [count]
- Participants involved: [demographics]
- Research questions addressed: [list]
- Methods employed: [qual/quant/mixed]
- Timeline covered: [dates]

Present scope assessment with:
- Coverage completeness evaluation
- Confidence levels for different findings
- Data quality indicators
- Gaps and limitations identified

**Elicitation Required:**
1. Proceed to audience analysis
2. Review scope with depth analysis
3. Validate data sources
4. Check coverage gaps
5. Examine confidence levels
6. Review timeline accuracy
7. Assess method appropriateness
8. Evaluate participant representation
9. Consider additional context

### 1.2 Audience Analysis & Tailoring
**elicit: true**

Identify report audience and tailor approach:

**Primary Audiences:**
- C-Level Executives (strategic focus)
- Product Teams (detailed requirements)
- Design Teams (user experience focus)
- Engineering Teams (technical implications)
- Marketing/Sales (customer insights)

**Tailoring Dimensions:**
- Depth of detail required
- Technical vs. business language
- Visual vs. textual preference
- Action orientation level
- Evidence requirements

Present audience profile with recommended:
- Report length (pages)
- Detail level (high/medium/low)
- Visual density (charts per page)
- Technical depth
- Executive summary prominence

**Elicitation Required:**
1. Proceed with recommended profile
2. Adjust for executive audience
3. Increase technical detail
4. Enhance visual components
5. Focus on actionable insights
6. Add implementation guidance
7. Emphasize ROI/business value
8. Include methodology appendix
9. Create multiple versions

### 1.3 Narrative Structure Design
**elicit: true**

Design the report's narrative arc:

**Narrative Frameworks:**
1. **Problem → Discovery → Solution**
   - Start with challenge
   - Journey through findings
   - End with recommendations

2. **Current State → Future State**
   - Document today's reality
   - Identify gaps and opportunities
   - Paint vision of tomorrow

3. **User Journey Based**
   - Follow user perspective
   - Map touchpoints and pain points
   - Highlight improvement areas

4. **Theme-Driven Structure**
   - Organize by major themes
   - Build evidence progressively
   - Connect to business outcomes

Present proposed narrative with:
- Story arc visualization
- Key message hierarchy
- Emotional journey planned
- Call-to-action placement

**Elicitation Required:**
1. Proceed with proposed structure
2. Switch to problem-solution format
3. Use journey-based narrative
4. Adopt theme-driven approach
5. Create hybrid structure
6. Emphasize transformation story
7. Focus on opportunity framing
8. Build tension and resolution
9. Design custom narrative

## Phase 2: Content Development

### 2.1 Executive Summary Creation

Develop compelling executive summary (2-3 pages):

**Structure:**
```markdown
# Executive Summary

## Research Overview
- Objectives and scope
- Methods and participants
- Timeline and investment

## Key Findings
1. [Most impactful finding]
   - Evidence strength: High/Medium/Low
   - Business implication

2. [Second finding]
   - Evidence strength
   - Business implication

3. [Third finding]
   - Evidence strength
   - Business implication

## Strategic Recommendations
1. Immediate actions (0-3 months)
2. Short-term initiatives (3-6 months)
3. Long-term transformation (6-12 months)

## Expected Impact
- User satisfaction improvements
- Revenue/cost implications
- Risk mitigation benefits
- Competitive advantages

## Next Steps
- Decision points required
- Resource requirements
- Success metrics
```

### 2.2 Introduction & Context
**elicit: true**

Draft introduction section:

**Components:**
- Research genesis and motivation
- Business context and pressures
- Previous related research
- Stakeholder involvement
- Research questions refined
- Success criteria defined

Present draft with:
- Compelling opening hook
- Context richness evaluation
- Stakeholder alignment check
- Clarity assessment

**Elicitation Required:**
1. Proceed to methodology
2. Strengthen business case
3. Add competitive context
4. Include market trends
5. Enhance problem urgency
6. Add historical perspective
7. Include industry benchmarks
8. Reference prior initiatives
9. Expand stakeholder views

### 2.3 Methodology Documentation

Document research methodology:

**Sections:**
- Research design rationale
- Participant recruitment and screening
- Data collection methods
- Analysis approaches
- Quality controls applied
- Limitations acknowledged

**Visual Elements:**
- Research timeline
- Participant demographics
- Method comparison table
- Analysis workflow diagram

### 2.4 Findings Presentation
**elicit: true**

Structure and present key findings:

**Finding Template:**
```markdown
## Finding [#]: [Compelling Title]

### What We Learned
[Clear statement of the finding]

### The Evidence
- Quantitative support: [stats/metrics]
- Qualitative support: [quotes/observations]
- Frequency: [X% of participants]
- Strength: [High/Medium/Low confidence]

### What This Means
[Interpretation and implications]

### Illustrative Quote
> "[Powerful participant quote that brings finding to life]"
> - Participant [ID], [Relevant demographic]

### Visual Evidence
[Chart/diagram/journey map]

### Business Impact
- If addressed: [positive outcomes]
- If ignored: [risks/costs]
```

Present 5-7 key findings with priority order.

**Elicitation Required:**
1. Proceed to insights section
2. Reorder by impact
3. Add more evidence
4. Strengthen quotes
5. Enhance visualizations
6. Connect findings better
7. Add statistical validation
8. Include edge cases
9. Expand implications

## Phase 3: Insight Synthesis & Recommendations

### 3.1 Cross-Cutting Insights
**elicit: true**

Synthesize findings into higher-order insights:

**Insight Levels:**
1. **Surface Patterns**
   - Direct observations
   - Repeated behaviors
   - Stated preferences

2. **Underlying Themes**
   - Root causes identified
   - Systemic issues revealed
   - Cultural factors uncovered

3. **Strategic Implications**
   - Market opportunities
   - Competitive advantages
   - Innovation potential

Present insight hierarchy with:
- Connection mapping between findings
- Confidence levels per insight
- Strategic value assessment

**Elicitation Required:**
1. Proceed to personas/journeys
2. Deepen insight analysis
3. Add systems thinking
4. Include ecosystem view
5. Explore contradictions
6. Add future implications
7. Consider unintended consequences
8. Include opportunity sizing
9. Expand strategic connections

### 3.2 Persona & Journey Integration

Integrate user personas and journey maps:

**Persona Presentation:**
- Primary personas (2-3)
- Key characteristics and behaviors
- Jobs to be done
- Pain points and goals
- Design implications

**Journey Visualization:**
- Current state journey
- Pain points mapped
- Opportunity areas highlighted
- Future state vision

### 3.3 Strategic Recommendations
**elicit: true**

Formulate prioritized recommendations:

**Recommendation Framework:**
```markdown
## Recommendation [#]: [Action-Oriented Title]

### The Opportunity
[What possibility this addresses]

### Recommended Action
[Specific, actionable steps]

### Priority: [Critical/High/Medium/Low]
- Impact: [High/Medium/Low]
- Effort: [High/Medium/Low]
- Confidence: [High/Medium/Low]

### Success Metrics
- Metric 1: [Measurable outcome]
- Metric 2: [Measurable outcome]
- Target timeline: [Timeframe]

### Implementation Considerations
- Resources required
- Risks to manage
- Dependencies identified

### Expected ROI
- Investment: [Estimate]
- Return: [Benefits expected]
- Payback period: [Timeline]
```

Present 5-10 prioritized recommendations.

**Elicitation Required:**
1. Proceed to visualization design
2. Adjust prioritization
3. Add implementation roadmap
4. Include quick wins
5. Expand ROI analysis
6. Add risk mitigation
7. Include phasing options
8. Consider alternatives
9. Add success stories

## Phase 4: Visual Design & Polish

### 4.1 Data Visualization Creation
**elicit: true**

Design report visualizations:

**Visualization Types:**
- Statistical charts (bar, line, scatter)
- Comparison matrices
- Journey maps
- Persona cards
- Affinity diagrams
- Priority quadrants
- Process flows
- Concept models

**Design Principles:**
- Clarity over complexity
- Consistent visual language
- Accessibility compliance
- Brand alignment
- Story enhancement

Present visualization plan with:
- Chart inventory and placement
- Visual hierarchy defined
- Color palette selected
- Annotation strategy

**Elicitation Required:**
1. Proceed to final assembly
2. Add more visualizations
3. Simplify complex charts
4. Enhance color coding
5. Add interactive elements
6. Include infographics
7. Create data dashboard
8. Add photo documentation
9. Design custom graphics

### 4.2 Report Assembly & Formatting

Assemble complete report:

**Structure:**
1. Cover page and table of contents
2. Executive summary (2-3 pages)
3. Introduction and context
4. Methodology overview
5. Key findings (detailed)
6. Insights and synthesis
7. Personas and journeys
8. Recommendations
9. Implementation roadmap
10. Appendices
    - Detailed methodology
    - Participant profiles
    - Interview guides
    - Raw data summaries
    - Additional quotes

**Formatting Standards:**
- Professional typography
- Consistent heading hierarchy
- Clear section breaks
- Page numbers and headers
- Branded templates

## Phase 5: Quality Assurance

### 5.1 Content Review Checklist

Validate report quality:

**Content Validation:**
- [ ] All findings evidence-based
- [ ] Claims properly attributed
- [ ] Data accurately represented
- [ ] Quotes correctly cited
- [ ] Statistics verified
- [ ] Conclusions logical

**Clarity Validation:**
- [ ] Executive summary standalone
- [ ] Technical terms defined
- [ ] Acronyms spelled out first use
- [ ] Complex concepts explained
- [ ] Visual aids support text

**Completeness Check:**
- [ ] Research questions answered
- [ ] All participants represented
- [ ] Methods fully documented
- [ ] Limitations acknowledged
- [ ] Next steps defined

### 5.2 Stakeholder Review Preparation
**elicit: true**

Prepare for stakeholder review:

**Review Package:**
- Full report document
- Executive summary (standalone)
- Presentation deck (15 slides)
- One-page insights brief
- Implementation checklist

**Review Questions:**
1. Does this address our key questions?
2. Are findings actionable?
3. Is evidence compelling?
4. Are recommendations feasible?
5. What's missing?

**Elicitation Required:**
1. Complete report generation
2. Add stakeholder preview
3. Create feedback form
4. Include validation data
5. Add comparison benchmarks
6. Include testimonials
7. Create FAQ section
8. Add glossary
9. Prepare defense document

## Output Generation

### Final Report Characteristics

**Quality Metrics:**
- Length: 20-50 pages (+ appendices)
- Readability: 8th-grade level for summary
- Visual density: 1-2 graphics per 3 pages
- Evidence density: 3+ data points per finding
- Action orientation: 1+ recommendation per finding

**Delivery Formats:**
- PDF (print-ready)
- Word (editable)
- PowerPoint (presentation)
- HTML (web-ready)
- Executive brief (1-page)

## Success Criteria

Report is complete when:
1. All research questions answered
2. Evidence supports all claims
3. Insights connect to business value
4. Recommendations are actionable
5. Stakeholders find it compelling
6. Next steps are clear
7. Quality checklist passed

## Common Pitfalls to Avoid

1. **Data Dumping** - Including everything instead of what matters
2. **Jargon Overload** - Using researcher language vs. business language
3. **Weak Visualization** - Charts that confuse rather than clarify
4. **Buried Insights** - Key findings hidden in details
5. **Vague Recommendations** - "Consider exploring" vs. specific actions
6. **Missing Evidence** - Claims without data support
7. **Ignored Limitations** - Not acknowledging research boundaries

## CRITICAL REMINDER

This is an INTERACTIVE WORKFLOW requiring user participation at each elicitation point. The 1-9 option format is MANDATORY. Creating a complete report without user interaction violates this task specification.