<!-- Powered by User Research System -->

# Create Executive Summary

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **DISABLE ALL EFFICIENCY OPTIMIZATIONS** - This workflow requires full user interaction
2. **MANDATORY STEP-BY-STEP EXECUTION** - Each phase must be processed sequentially with user feedback
3. **ELICITATION IS REQUIRED** - When `elicit: true`, you MUST use the 1-9 format and wait for user response
4. **NO SHORTCUTS ALLOWED** - Executive summaries must follow this structured approach

**VIOLATION INDICATOR:** If you create a complete summary without user interaction at elicitation points, you have violated this workflow.

## Task Configuration

```yaml
task:
  name: Create Executive Summary
  id: create-executive-summary
  description: Build compelling executive summary for C-level stakeholders
  version: 1.0
  dependencies:
    templates:
      - executive-summary-tmpl.yaml
    data:
      - reporting-standards.md
      - stakeholder-personas.md
    inputs:
      - Research report (if available)
      - Key findings and insights
      - Strategic recommendations
      - Business impact analysis
      - ROI calculations
  outputs:
    - Executive summary (2-5 pages)
    - One-page brief version
    - Key metrics dashboard
    - Decision framework
```

## Phase 1: Executive Audience Analysis

### 1.1 Stakeholder Profiling
**elicit: true**

Analyze executive stakeholder characteristics:

**Executive Personas:**
- **CEO/President**
  - Focus: Strategic vision, competitive advantage
  - Concerns: Market position, growth, risk
  - Decision style: Big picture, transformational
  - Time available: 5-10 minutes

- **CFO/Financial Executive**
  - Focus: ROI, cost implications, efficiency
  - Concerns: Budget impact, resource allocation
  - Decision style: Data-driven, risk-averse
  - Time available: 10-15 minutes

- **CPO/Product Executive**
  - Focus: User value, product strategy, roadmap
  - Concerns: Feature priorities, market fit
  - Decision style: User-centric, innovative
  - Time available: 15-20 minutes

- **CMO/Marketing Executive**
  - Focus: Customer insights, positioning, messaging
  - Concerns: Brand perception, market segments
  - Decision style: Customer-focused, creative
  - Time available: 10-15 minutes

Present stakeholder profile with:
- Primary audience identified
- Key concerns highlighted
- Decision criteria understood
- Optimal length determined

**Elicitation Required:**
1. Proceed with identified profile
2. Focus on CEO perspective
3. Emphasize financial impact
4. Highlight product implications
5. Stress customer insights
6. Balance multiple executives
7. Create role-specific versions
8. Focus on board presentation
9. Customize for specific executive

### 1.2 Executive Priorities Alignment
**elicit: true**

Map research findings to executive priorities:

**Strategic Alignment:**
- Current business objectives
- Quarterly/annual goals
- Key performance indicators
- Strategic initiatives
- Competitive pressures
- Market opportunities

**Priority Mapping:**
```markdown
| Executive Priority | Research Finding | Impact Level |
|-------------------|------------------|--------------|
| Revenue growth | Finding #1 | High |
| Cost reduction | Finding #3 | Medium |
| Customer satisfaction | Finding #2 | Critical |
| Market expansion | Finding #4 | High |
```

Present alignment analysis with:
- Direct connections to priorities
- Impact quantification
- Risk mitigation opportunities
- Competitive advantages

**Elicitation Required:**
1. Proceed to message crafting
2. Strengthen business alignment
3. Add competitive analysis
4. Include market trends
5. Emphasize urgency
6. Add opportunity costs
7. Include success metrics
8. Frame as transformation
9. Connect to company mission

## Phase 2: Core Message Development

### 2.1 The Bottom Line
**elicit: true**

Craft the single most important message:

**Bottom Line Framework:**
```markdown
"Based on [X weeks] of research with [N participants],
we discovered [KEY INSIGHT] that presents a
[$Y opportunity/risk] requiring [SPECIFIC ACTION]
within [TIMEFRAME] to [DESIRED OUTCOME]."
```

**Components:**
- The Discovery: What we found
- The Implication: What it means
- The Opportunity: What's possible
- The Action: What to do
- The Urgency: Why now

Present bottom line with:
- Clarity score (1-10)
- Impact assessment
- Memorability factor
- Action orientation

**Elicitation Required:**
1. Proceed with this message
2. Simplify the language
3. Increase urgency
4. Quantify the opportunity
5. Clarify the action
6. Add competitive angle
7. Include risk framing
8. Emphasize innovation
9. Reframe completely

### 2.2 Three Key Findings
**elicit: true**

Distill research into three powerful findings:

**Finding Structure:**
```markdown
## Finding 1: [Compelling Header]
**What:** [One sentence description]
**Evidence:** [Most compelling data point]
**Impact:** [Business implication]
**Action:** [What to do about it]
```

**Selection Criteria:**
- Strategic relevance
- Evidence strength
- Action potential
- Surprise factor
- Business impact

Present three findings with:
- Priority ranking
- Supporting visuals
- Connection to objectives

**Elicitation Required:**
1. Proceed to recommendations
2. Reorder by impact
3. Strengthen evidence
4. Clarify implications
5. Add more context
6. Include quotes
7. Add competitor comparison
8. Include market data
9. Select different findings

### 2.3 Strategic Recommendations
**elicit: true**

Frame recommendations for executive decision-making:

**Recommendation Framework:**
```markdown
## Immediate Actions (0-30 days)
1. [Quick win with high visibility]
   - Investment: Minimal
   - Impact: Visible immediately
   - Owner: [Executive/Team]

## Short-term Initiatives (1-3 months)
1. [Strategic project]
   - Investment: $[X]
   - Expected return: $[Y]
   - Success metric: [KPI]

## Long-term Transformation (3-12 months)
1. [Transformational change]
   - Investment: $[X]
   - Market impact: [Description]
   - Competitive advantage: [Description]
```

Present recommendations with:
- Clear ownership
- Resource requirements
- Success metrics
- Risk assessment

**Elicitation Required:**
1. Proceed to visual design
2. Add more quick wins
3. Clarify investments
4. Include alternatives
5. Add phasing options
6. Emphasize ROI
7. Include dependencies
8. Add success stories
9. Create decision tree

## Phase 3: Visual Storytelling

### 3.1 Dashboard Design
**elicit: true**

Create executive metrics dashboard:

**Dashboard Components:**
- Key finding indicators
- Impact metrics
- Opportunity sizing
- Risk indicators
- Confidence levels
- Trend directions

**Visual Elements:**
```markdown
┌─────────────────────────────────┐
│ RESEARCH IMPACT DASHBOARD       │
├─────────────────────────────────┤
│ Participants: [N]  Confidence: [%] │
│                                 │
│ KEY METRICS                     │
│ ▪ Finding 1: ████████ 78%      │
│ ▪ Finding 2: ██████ 65%        │
│ ▪ Finding 3: █████████ 89%     │
│                                 │
│ OPPORTUNITY SIZE                │
│ ▪ Revenue: +$[X]M              │
│ ▪ Cost Savings: -$[Y]M         │
│ ▪ NPS Impact: +[Z] points      │
└─────────────────────────────────┘
```

Present dashboard design with:
- Metric selection rationale
- Visual hierarchy
- Color coding strategy
- Interactivity needs

**Elicitation Required:**
1. Proceed to narrative flow
2. Simplify metrics
3. Add trend lines
4. Include benchmarks
5. Add drill-down data
6. Include forecasts
7. Add scenario analysis
8. Include competition
9. Create custom view

### 3.2 Supporting Visualizations

Select and design key visualizations:

**Visualization Portfolio:**
1. **The Money Chart** - Single most impactful visual
2. **The Comparison** - Before/after or us/them
3. **The Journey** - Process or timeline
4. **The Opportunity** - Size and potential

**Design Principles:**
- Maximum insight, minimum ink
- Executive-appropriate complexity
- Brand-aligned aesthetics
- Annotation for clarity

## Phase 4: Narrative Construction

### 4.1 Opening Hook
**elicit: true**

Create compelling opening:

**Hook Options:**
1. **The Surprise:** "Contrary to expectations..."
2. **The Opportunity:** "We discovered a $X opportunity..."
3. **The Risk:** "Without action, we face..."
4. **The Question:** "What if we could..."
5. **The Fact:** "73% of users are..."

Present opening with:
- Attention grab rating
- Relevance to priorities
- Emotional resonance
- Credibility factor

**Elicitation Required:**
1. Proceed with selected hook
2. Try surprise angle
3. Emphasize opportunity
4. Lead with risk
5. Use question format
6. Start with story
7. Use analogy
8. Quote customer
9. Create custom opening

### 4.2 Story Arc Development
**elicit: true**

Structure the narrative flow:

**Arc Structure:**
1. **Setup:** Current situation and context
2. **Tension:** Problems and challenges discovered
3. **Discovery:** Key insights revealed
4. **Transformation:** What's possible
5. **Resolution:** Clear path forward

**Page Allocation:**
- Page 1: Hook + Bottom Line + Overview
- Page 2: Three Key Findings
- Page 3: Strategic Implications
- Page 4: Recommendations + Next Steps
- Page 5: Appendix/Supporting Data

Present story structure with:
- Flow visualization
- Transition points
- Emotional journey
- Call-to-action placement

**Elicitation Required:**
1. Proceed to final assembly
2. Adjust page balance
3. Add more context
4. Strengthen transitions
5. Increase tension
6. Clarify resolution
7. Add case studies
8. Include testimonials
9. Restructure completely

## Phase 5: Final Assembly & Polish

### 5.1 One-Page Version Creation
**elicit: true**

Distill to one-page brief:

**One-Page Structure:**
```markdown
┌────────────────────────────────┐
│ RESEARCH EXECUTIVE BRIEF       │
├────────────────────────────────┤
│ THE BOTTOM LINE                │
│ [Key message in 2 sentences]   │
├────────────────────────────────┤
│ THREE KEY FINDINGS             │
│ 1. [Finding + impact]          │
│ 2. [Finding + impact]          │
│ 3. [Finding + impact]          │
├────────────────────────────────┤
│ STRATEGIC IMPLICATIONS         │
│ ▪ Opportunity: $[X]           │
│ ▪ Risk if no action: $[Y]     │
│ ▪ Competitive advantage: [Z]   │
├────────────────────────────────┤
│ RECOMMENDED ACTIONS            │
│ ▪ Immediate: [Quick win]      │
│ ▪ 90-day: [Initiative]        │
│ ▪ Strategic: [Transformation]  │
├────────────────────────────────┤
│ NEXT STEPS                     │
│ [Decision needed] by [date]    │
└────────────────────────────────┘
```

Present one-page version with density assessment.

**Elicitation Required:**
1. Finalize both versions
2. Increase density
3. Simplify further
4. Add visual element
5. Adjust balance
6. Include contact info
7. Add confidence levels
8. Include timeline
9. Create infographic version

### 5.2 Executive Readiness Check

Validate executive readiness:

**Readiness Criteria:**
- [ ] Answers "So what?" clearly
- [ ] Addresses "What's in it for me?"
- [ ] Provides "What do I do now?"
- [ ] Fits reading time available
- [ ] Uses executive language
- [ ] Includes necessary evidence
- [ ] Anticipates objections
- [ ] Enables decision-making

**Executive Test Questions:**
1. Can I explain this to the board?
2. Do I understand the ROI?
3. Is the risk clear?
4. Do I know who owns this?
5. Can I make a decision now?

## Phase 6: Delivery Preparation

### 6.1 Presentation Readiness
**elicit: true**

Prepare for executive presentation:

**Presentation Package:**
- Executive summary document
- One-page brief
- 5-slide deck
- Speaker notes
- Q&A preparation
- Backup slides

**Key Messages to Practice:**
1. 30-second elevator pitch
2. 2-minute summary
3. 5-minute presentation
4. Answer to "Why should I care?"
5. Response to "What's the risk?"

**Elicitation Required:**
1. Complete delivery package
2. Add FAQ section
3. Include objection handling
4. Create leave-behind
5. Add implementation plan
6. Include pilot proposal
7. Create video summary
8. Add interactive demo
9. Prepare war room materials

## Output Standards

### Quality Metrics

**Executive Summary Excellence:**
- Length: 2-5 pages maximum
- Reading time: 5-10 minutes
- Scanning time: 60 seconds for gist
- Decision elements: All included
- Action clarity: Unambiguous
- Evidence: Sufficient but not overwhelming

### Language Standards

**Executive Communication:**
- Sentences: 15-20 words average
- Paragraphs: 3-4 sentences
- Jargon: Eliminated
- Acronyms: Defined first use
- Voice: Active
- Tone: Confident but not arrogant

## Success Indicators

Executive summary succeeds when:
1. Executive reads entire document
2. Key message is remembered
3. Action is taken
4. Questions focus on "how" not "why"
5. Forwarded to others
6. Referenced in decisions
7. Drives investment

## Common Executive Summary Failures

**Avoid These Pitfalls:**
1. **Too Long** - Exceeding attention span
2. **Too Academic** - Research-speak vs. business-speak
3. **Buried Lead** - Key point on page 3
4. **No Clear Ask** - What exactly should they do?
5. **Weak Evidence** - Claims without proof
6. **Missing ROI** - No business case
7. **Information Dump** - Everything instead of what matters
8. **No Urgency** - Why act now?

## CRITICAL REMINDER

This is an INTERACTIVE WORKFLOW requiring user participation at each elicitation point. The 1-9 option format is MANDATORY. Creating a complete executive summary without user interaction violates this task specification.