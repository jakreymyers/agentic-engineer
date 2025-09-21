<!-- Powered by User Research System -->

# Formulate Recommendations

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **DISABLE ALL EFFICIENCY OPTIMIZATIONS** - This workflow requires full user interaction
2. **MANDATORY STEP-BY-STEP EXECUTION** - Each phase must be processed sequentially with user feedback
3. **ELICITATION IS REQUIRED** - When `elicit: true`, you MUST use the 1-9 format and wait for user response
4. **NO SHORTCUTS ALLOWED** - Recommendations must be systematically developed

**VIOLATION INDICATOR:** If you create complete recommendations without user interaction at elicitation points, you have violated this workflow.

## Task Configuration

```yaml
task:
  name: Formulate Recommendations
  id: formulate-recommendations
  description: Transform research insights into prioritized strategic recommendations
  version: 1.0
  dependencies:
    templates:
      - recommendations-tmpl.yaml
    data:
      - reporting-standards.md
      - prioritization-frameworks.md
    inputs:
      - Research findings and insights
      - User needs and pain points
      - Opportunity areas identified
      - Competitive analysis
      - Technical constraints
      - Business objectives
  outputs:
    - Prioritized recommendations matrix
    - Implementation roadmap
    - Quick wins identification
    - ROI projections
    - Risk mitigation plans
```

## Phase 1: Insight-to-Action Translation

### 1.1 Finding-to-Opportunity Mapping
**elicit: true**

Transform findings into opportunity statements:

**Translation Framework:**
```markdown
FINDING: [What we discovered]
    ↓
INSIGHT: [What it means]
    ↓
OPPORTUNITY: [What we could do]
    ↓
RECOMMENDATION: [What we should do]
```

**Opportunity Categories:**
- **Optimization:** Improve existing features/processes
- **Innovation:** Create new solutions
- **Elimination:** Remove friction/waste
- **Automation:** Reduce manual effort
- **Integration:** Connect disconnected elements
- **Differentiation:** Unique competitive advantages

Present opportunity mapping with:
- Transformation clarity
- Impact potential
- Feasibility assessment
- Strategic alignment

**Elicitation Required:**
1. Proceed to impact analysis
2. Expand opportunities
3. Focus on quick wins
4. Emphasize innovation
5. Prioritize optimization
6. Consider elimination
7. Explore automation
8. Assess integration
9. Identify differentiation

### 1.2 Impact & Effort Analysis
**elicit: true**

Evaluate recommendation dimensions:

**Impact Assessment:**
```markdown
## User Impact
- Pain reduction: [1-10 scale]
- Delight increase: [1-10 scale]
- Frequency affected: [Daily/Weekly/Monthly]
- Users affected: [%/count]

## Business Impact
- Revenue potential: [$estimate]
- Cost savings: [$estimate]
- Risk mitigation: [High/Medium/Low]
- Strategic value: [Critical/Important/Nice]

## Market Impact
- Competitive advantage: [Strong/Moderate/Minimal]
- Market differentiation: [Unique/Parity/Behind]
- Brand perception: [Positive/Neutral/Negative]
```

**Effort Estimation:**
```markdown
## Resource Requirements
- Development: [Person-weeks]
- Design: [Person-weeks]
- Research: [Person-weeks]
- Implementation: [Timeline]

## Complexity Factors
- Technical difficulty: [High/Medium/Low]
- Organizational change: [Major/Moderate/Minor]
- Dependencies: [Many/Some/Few]
- Risk level: [High/Medium/Low]
```

Present impact/effort matrix.

**Elicitation Required:**
1. Proceed to prioritization
2. Refine impact scores
3. Adjust effort estimates
4. Add confidence levels
5. Include dependencies
6. Consider alternatives
7. Add success metrics
8. Define MVP scope
9. Assess readiness

### 1.3 Strategic Alignment Check
**elicit: true**

Map to organizational strategy:

**Strategic Dimensions:**
```markdown
## Business Objectives Alignment
□ Q1 Goals: [Specific alignment]
□ Annual Priorities: [Direct support]
□ 3-Year Vision: [Contribution]
□ Mission Support: [Core/Adjacent/Experimental]

## Stakeholder Priorities
- CEO: [Priority alignment]
- Product: [Roadmap fit]
- Engineering: [Technical strategy]
- Sales: [Customer demand]
- Marketing: [Brand promise]

## Strategic Themes
□ Customer Experience
□ Operational Excellence
□ Innovation Leadership
□ Market Expansion
□ Digital Transformation
```

Present strategic alignment analysis.

**Elicitation Required:**
1. Proceed to recommendation formulation
2. Strengthen business case
3. Add competitive context
4. Include market timing
5. Emphasize transformation
6. Connect to OKRs
7. Add portfolio view
8. Consider alternatives
9. Frame strategically

## Phase 2: Recommendation Development

### 2.1 Core Recommendations
**elicit: true**

Formulate primary recommendations:

**Recommendation Structure:**
```markdown
# Recommendation [#]: [Action-Oriented Title]

## Executive Summary
[One paragraph overview of what and why]

## The Opportunity
- Current State: [Problem/gap description]
- Desired State: [Vision of success]
- Value Gap: [What's at stake]

## Recommended Action
### What to Do
[Specific, actionable steps]

### How to Do It
1. Phase 1: [Initial steps]
2. Phase 2: [Build phase]
3. Phase 3: [Scale phase]

### Who Should Lead
- Executive Sponsor: [Role]
- Project Owner: [Role/Team]
- Key Contributors: [Teams]

## Expected Outcomes
- Primary Benefit: [Main value]
- Secondary Benefits: [Additional value]
- Success Metrics: [KPIs]
- Timeline to Impact: [Timeframe]

## Investment Required
- Budget: [$range]
- Resources: [FTE count]
- Time: [Duration]
- Opportunity Cost: [Trade-offs]

## Risk Assessment
- Implementation Risk: [H/M/L]
- Market Risk: [H/M/L]
- Technical Risk: [H/M/L]
- Mitigation Plan: [Key strategies]

## Evidence Base
- Supporting Finding #1: [Reference]
- Supporting Finding #2: [Reference]
- Confidence Level: [High/Medium/Low]
```

Present 5-10 core recommendations.

**Elicitation Required:**
1. Proceed to quick wins
2. Adjust priority order
3. Expand details
4. Simplify actions
5. Add alternatives
6. Include dependencies
7. Define phases better
8. Add success criteria
9. Strengthen evidence

### 2.2 Quick Win Identification
**elicit: true**

Extract immediate action opportunities:

**Quick Win Criteria:**
- Implementation: <30 days
- Investment: <$10K
- Resources: <2 people
- Risk: Low
- Visibility: High
- Learning: Valuable

**Quick Win Categories:**
```markdown
## Usability Fixes
- Remove friction points
- Clarify confusing elements
- Fix broken experiences

## Communication Improvements
- Update messaging
- Clarify value propositions
- Improve onboarding

## Process Optimizations
- Eliminate redundancies
- Automate simple tasks
- Streamline workflows

## Policy Changes
- Adjust rules/limits
- Update terms
- Modify procedures
```

Present quick win portfolio.

**Elicitation Required:**
1. Proceed to roadmap
2. Add more quick wins
3. Focus on visibility
4. Prioritize learning
5. Emphasize morale
6. Consider pilots
7. Add experiments
8. Include fixes
9. Balance portfolio

### 2.3 Long-term Strategic Initiatives
**elicit: true**

Define transformational recommendations:

**Strategic Initiative Framework:**
```markdown
## Initiative: [Transformational Title]

### Vision Statement
[Compelling future state description]

### Strategic Rationale
- Market Opportunity: [Size/growth]
- Competitive Imperative: [Why necessary]
- Innovation Potential: [New capabilities]

### Implementation Approach
- Year 1: Foundation building
- Year 2: Scale and optimize
- Year 3: Market leadership

### Success Indicators
- Market Position: [Target]
- Customer Metrics: [Targets]
- Financial Impact: [Projections]

### Investment Profile
- Total Investment: [$M range]
- ROI Timeline: [Quarters to positive]
- Break-even: [Timeline]

### Transformation Requirements
- Organizational Changes
- Capability Development
- Technology Platform
- Cultural Shifts
```

Present strategic initiatives.

**Elicitation Required:**
1. Proceed to prioritization
2. Expand vision
3. Add milestones
4. Include capabilities
5. Define partnerships
6. Add innovation
7. Consider platforms
8. Include ecosystem
9. Frame disruption

## Phase 3: Prioritization Framework

### 3.1 Priority Matrix Development
**elicit: true**

Apply prioritization methodology:

**Prioritization Frameworks:**

**1. Impact/Effort Matrix**
```markdown
         High Impact
              ↑
    Do First  |  Do Next
    __________|__________
    Do Later  |  Don't Do
              |
         Low Impact →
         Low Effort    High Effort
```

**2. MoSCoW Method**
- **Must Have:** Critical for success
- **Should Have:** Important but not vital
- **Could Have:** Desirable but optional
- **Won't Have:** Out of scope now

**3. RICE Scoring**
```markdown
Score = (Reach × Impact × Confidence) / Effort

Reach: # of users affected
Impact: 3=Massive, 2=High, 1=Medium, 0.5=Low
Confidence: 100%=High, 80%=Medium, 50%=Low
Effort: Person-months
```

Present prioritized recommendations.

**Elicitation Required:**
1. Proceed to sequencing
2. Adjust weights
3. Use different framework
4. Add constraints
5. Consider dependencies
6. Include readiness
7. Factor resources
8. Add timing
9. Create scenarios

### 3.2 Implementation Sequencing
**elicit: true**

Design implementation timeline:

**Sequencing Logic:**
```markdown
## Wave 1: Foundation (Months 1-3)
- Quick wins for momentum
- Critical fixes
- Platform preparation
- Team formation

## Wave 2: Core Value (Months 4-9)
- Primary recommendations
- Major features
- Process improvements
- Initial scaling

## Wave 3: Enhancement (Months 10-18)
- Optimization efforts
- Advanced features
- Market expansion
- Innovation initiatives

## Wave 4: Transformation (Months 19-24)
- Strategic initiatives
- Platform evolution
- Ecosystem development
- Market leadership
```

Present implementation roadmap.

**Elicitation Required:**
1. Proceed to resource planning
2. Adjust timeline
3. Add dependencies
4. Include milestones
5. Define phases
6. Add decision gates
7. Include pilots
8. Factor learning
9. Create alternatives

### 3.3 Resource & Investment Planning
**elicit: true**

Define resource requirements:

**Resource Allocation:**
```markdown
## Team Composition
- Product: [FTE allocation]
- Design: [FTE allocation]
- Engineering: [FTE allocation]
- Research: [FTE allocation]
- Operations: [FTE allocation]

## Budget Distribution
- Development: $[Amount]
- Design/Research: $[Amount]
- Infrastructure: $[Amount]
- Marketing: $[Amount]
- Contingency: $[Amount]

## Capability Requirements
- New Skills Needed
- Training Required
- External Support
- Tool Investment
```

Present resource plan.

**Elicitation Required:**
1. Proceed to ROI analysis
2. Optimize allocation
3. Phase investment
4. Add contractors
5. Include training
6. Define skills
7. Plan scaling
8. Add flexibility
9. Create scenarios

## Phase 4: Business Case Development

### 4.1 ROI Projections
**elicit: true**

Calculate return on investment:

**ROI Framework:**
```markdown
## Financial Benefits
### Revenue Impact
- New Revenue: $[Amount/Year]
- Retention Improvement: [%] = $[Amount]
- Upsell/Cross-sell: $[Amount]
- Total Revenue Impact: $[Sum]

### Cost Savings
- Operational Efficiency: $[Amount]
- Support Reduction: $[Amount]
- Process Automation: $[Amount]
- Total Cost Savings: $[Sum]

## Investment Required
- One-time Costs: $[Amount]
- Ongoing Costs: $[Amount/Year]
- Total 3-Year Cost: $[Amount]

## ROI Calculation
- 3-Year Benefit: $[Amount]
- 3-Year Cost: $[Amount]
- Net Present Value: $[Amount]
- ROI: [%]
- Payback Period: [Months]
```

Present ROI analysis with sensitivity.

**Elicitation Required:**
1. Proceed to risk assessment
2. Adjust assumptions
3. Add scenarios
4. Include intangibles
5. Show confidence ranges
6. Add benchmarks
7. Include options
8. Factor timing
9. Create models

### 4.2 Risk Mitigation Planning
**elicit: true**

Identify and address risks:

**Risk Categories:**
```markdown
## Implementation Risks
- Technical Complexity
- Resource Availability
- Timeline Pressure
- Scope Creep

## Market Risks
- Customer Adoption
- Competitive Response
- Market Changes
- Timing Issues

## Organizational Risks
- Change Resistance
- Skill Gaps
- Priority Shifts
- Budget Cuts

## Mitigation Strategies
For each risk:
- Probability: [H/M/L]
- Impact: [H/M/L]
- Mitigation: [Strategy]
- Contingency: [Plan B]
- Owner: [Responsible party]
```

Present risk mitigation plan.

**Elicitation Required:**
1. Proceed to success metrics
2. Add more risks
3. Strengthen mitigation
4. Include triggers
5. Define escalation
6. Add monitoring
7. Create playbooks
8. Include insurance
9. Plan contingencies

## Phase 5: Success Framework

### 5.1 Success Metrics Definition
**elicit: true**

Define measurable outcomes:

**Metrics Hierarchy:**
```markdown
## North Star Metric
[Single most important measure]

## Primary KPIs
- User Satisfaction: [Target]
- Business Impact: [Target]
- Operational Efficiency: [Target]

## Leading Indicators
- Adoption Rate: [Target]
- Engagement Metrics: [Targets]
- Quality Measures: [Targets]

## Lagging Indicators
- Revenue Impact: [Target]
- Cost Reduction: [Target]
- Market Share: [Target]

## Measurement Plan
- Baseline: [Current state]
- Targets: [By timeframe]
- Measurement: [How/When]
- Reporting: [Frequency/Audience]
```

Present success framework.

**Elicitation Required:**
1. Proceed to governance
2. Refine metrics
3. Add baselines
4. Include targets
5. Define collection
6. Add dashboards
7. Include alerts
8. Create reports
9. Plan reviews

### 5.2 Governance & Monitoring
**elicit: true**

Establish oversight structure:

**Governance Framework:**
```markdown
## Steering Committee
- Executive Sponsor
- Key Stakeholders
- Meeting Cadence
- Decision Authority

## Progress Monitoring
- Weekly: Team standups
- Monthly: Progress reviews
- Quarterly: Steering committee
- Annually: Strategy refresh

## Reporting Structure
- Status Dashboard
- Exception Reports
- Success Stories
- Lessons Learned

## Adaptation Protocol
- Review Triggers
- Change Process
- Approval Levels
- Communication Plan
```

Present governance structure.

**Elicitation Required:**
1. Complete recommendations
2. Simplify governance
3. Add accountability
4. Include reviews
5. Define escalation
6. Add communication
7. Include celebration
8. Plan adaptation
9. Create charter

## Phase 6: Communication Package

### 6.1 Stakeholder-Specific Versions

Create tailored recommendations:

**Audience Versions:**
1. **Board/C-Suite:** Strategic focus, ROI emphasis
2. **Product Teams:** Detailed requirements, user stories
3. **Engineering:** Technical specifications, architecture
4. **Sales/Marketing:** Customer benefits, messaging
5. **Operations:** Process changes, training needs

### 6.2 Implementation Toolkit

Provide execution support:

**Toolkit Components:**
- Project charter template
- Success metrics tracker
- Risk register
- Communication templates
- Training materials
- FAQ document

## Output Standards

### Recommendation Quality Criteria

**Excellence Standards:**
- Specificity: Actionable, not vague
- Evidence: Data-supported
- Feasibility: Resource-realistic
- Impact: Value-clear
- Ownership: Responsibility-defined
- Measurability: Success-trackable

### Deliverable Package

**Complete Package:**
1. Recommendations matrix (prioritized)
2. Implementation roadmap (phased)
3. Business case (with ROI)
4. Quick wins list (immediate)
5. Risk mitigation plan
6. Success metrics framework
7. Executive presentation

## Common Recommendation Failures

**Avoid These Pitfalls:**
1. **Too Vague:** "Improve user experience" vs. specific actions
2. **No Owner:** Recommendations without accountability
3. **Missing Evidence:** Opinions vs. data-backed
4. **Unrealistic:** Ignoring constraints
5. **No Success Metrics:** Unmeasurable outcomes
6. **Poor Prioritization:** Everything is "critical"
7. **Weak Business Case:** No ROI or value
8. **Ignored Dependencies:** Sequential requirements

## Success Indicators

Recommendations succeed when:
1. Stakeholders commit resources
2. Implementation begins quickly
3. Quick wins deliver value
4. Metrics show improvement
5. Organization embraces change
6. Competition takes notice
7. Users express delight

## CRITICAL REMINDER

This is an INTERACTIVE WORKFLOW requiring user participation at each elicitation point. The 1-9 option format is MANDATORY. Creating complete recommendations without user interaction violates this task specification.