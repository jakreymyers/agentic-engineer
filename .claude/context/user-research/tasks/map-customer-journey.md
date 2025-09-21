# Map Customer Journey

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **EVIDENCE-BASED MAPPING** - Every touchpoint must come from research data
2. **EMOTIONAL ACCURACY** - Emotions must reflect actual user sentiments
3. **ELICITATION REQUIRED** - User input needed at journey definition points
4. **OPPORTUNITY FOCUS** - Identify improvement opportunities at each stage

**VIOLATION INDICATOR:** If you create journey stages without evidence, you have violated this workflow.

## Task Configuration

```yaml
task:
  id: map-customer-journey
  name: Customer Journey Mapping
  template: journey-map-tmpl.yaml
  output: docs/research/customer-journey-map.md
  elicitation_mode: mandatory
  visualization: required
```

## Prerequisites

Before journey mapping:
1. **Verify Data Sources**
   - Personas created and validated
   - Interview transcripts with process descriptions
   - Touchpoint inventory from synthesis
   - Emotional data from analysis
   - Pain points and delights catalogued

2. **Define Journey Scope**
   - Start and end points
   - Primary persona focus
   - Level of detail required
   - Time horizon covered
   - Channels included

## Journey Mapping Workflow

### Phase 1: Journey Framework Definition
**Objective:** Establish the journey structure and boundaries

1. **Scenario Selection**
   ```
   Define primary journey scenarios:
   - Most common path (from data)
   - Critical business path
   - Problem scenario
   - Ideal/happy path

   For each scenario:
   - Starting trigger/context
   - Success criteria/end state
   - Persona involved
   - Evidence sources
   ```

2. **Stage Identification**
   ```
   From research data, identify:
   - Major phases users go through
   - Natural breakpoints in process
   - Decision points
   - Milestone moments

   Common Stages (adapt based on data):
   - Awareness/Discovery
   - Consideration/Research
   - Decision/Purchase
   - Onboarding/Setup
   - Usage/Value Realization
   - Growth/Expansion
   - Renewal/Advocacy
   ```

3. **Timeline Mapping**
   ```
   For each stage:
   - Typical duration (from data)
   - Range of timeframes observed
   - Factors affecting duration
   - Urgency indicators
   ```

**Elicitation Point 1:** `elicit: true`
Present journey framework with stages. Ask user:
1. Proceed to touchpoint mapping
2. Scenario Analysis - Explore alternative paths
3. Stage Refinement - Adjust stage boundaries
4. Persona Variation - Compare different personas
5. Channel Strategy - Define channel focus
6. Timeline Analysis - Deep dive on duration
7. Entry Point Mapping - Multiple start points
8. Success Definition - Clarify end states
9. Scope Adjustment - Modify journey boundaries

Select 1-9 or type your question/feedback:

### Phase 2: Touchpoint and Action Mapping
**Objective:** Document all interactions and user actions

1. **Touchpoint Inventory**
   ```
   For each stage, from research data:

   Digital Touchpoints:
   - Website interactions
   - App usage
   - Email communications
   - Social media contacts
   - Digital documents

   Human Touchpoints:
   - Sales conversations
   - Support interactions
   - Peer discussions
   - Internal communications

   Physical Touchpoints:
   - Product interactions
   - Environmental factors
   - Documentation/materials
   ```

2. **User Actions**
   ```
   Document what users actually do:
   - Primary actions taken
   - Alternative paths observed
   - Workarounds employed
   - Information seeking behavior
   - Decision-making activities

   Include:
   - Action frequency
   - Action duration
   - Success rates
   - Abandonment points
   ```

3. **Channel Transitions**
   ```
   Map channel switching:
   - Where users change channels
   - Why they switch (from data)
   - Friction in transitions
   - Preferred channels by stage
   - Forced channel changes
   ```

**Elicitation Point 2:** `elicit: true`
Present touchpoints and actions. Ask user:
1. Proceed to thoughts and emotions
2. Touchpoint Deep Dive - Detailed interaction analysis
3. Channel Optimization - Identify best channels
4. Action Streamlining - Simplify user actions
5. Automation Opportunities - What could be automated
6. Self-Service Analysis - Where users want control
7. Support Needs - Where help is needed
8. Integration Points - System connections needed
9. Failure Analysis - Where things break down

Select 1-9 or type your question/feedback:

### Phase 3: Thoughts, Feelings, and Emotions
**Objective:** Capture the emotional journey from research

1. **Thinking Documentation**
   ```
   From quotes and observations:

   User Questions:
   - What users ask at each stage
   - Information they seek
   - Decisions they contemplate
   - Comparisons they make
   - Doubts and concerns

   Mental Models:
   - How users conceptualize process
   - Expectations at each stage
   - Assumptions they make
   - Knowledge gaps identified
   ```

2. **Emotional Mapping**
   ```
   Plot emotional curve from data:

   Emotional States by Stage:
   - Excitement/Anticipation
   - Frustration/Anger
   - Confusion/Uncertainty
   - Satisfaction/Delight
   - Anxiety/Fear
   - Confidence/Empowerment

   Evidence:
   - Direct quotes expressing emotion
   - Observed behaviors indicating feelings
   - Intensity indicators
   - Emotional triggers
   ```

3. **Motivation Tracking**
   ```
   Document driving forces:
   - What motivates progression
   - What causes hesitation
   - What triggers abandonment
   - What creates advocacy

   Include confidence levels:
   - High confidence (multiple sources)
   - Medium confidence (some evidence)
   - Low confidence (limited data)
   ```

**Elicitation Point 3:** `elicit: true`
Present thoughts and emotions. Ask user:
1. Proceed to pain points and opportunities
2. Empathy Deep Dive - Explore emotional nuances
3. Cognitive Load Analysis - Mental effort required
4. Motivation Mapping - Understand drivers
5. Anxiety Triggers - Identify stress points
6. Delight Moments - Find positive peaks
7. Trust Building - Where trust is gained/lost
8. Expectation Setting - Alignment opportunities
9. Emotional Design - Design for feelings

Select 1-9 or type your question/feedback:

### Phase 4: Pain Points and Opportunities
**Objective:** Identify problems and improvement areas

1. **Pain Point Mapping**
   ```
   For each stage, document:

   Pain Points:
   - Specific frustrations observed
   - Frequency of occurrence
   - Severity/impact
   - Current workarounds
   - Quotes expressing pain

   Root Causes:
   - System limitations
   - Process gaps
   - Information gaps
   - Expectation mismatches
   - Technical barriers
   ```

2. **Opportunity Identification**
   ```
   Transform pain points to opportunities:

   Quick Wins:
   - Simple fixes
   - High impact, low effort
   - Clear user benefit

   Strategic Improvements:
   - System enhancements
   - Process redesigns
   - New capabilities

   Innovation Areas:
   - Breakthrough experiences
   - Competitive differentiation
   - Delighter features
   ```

3. **Moment of Truth Analysis**
   ```
   Identify critical moments:
   - Make-or-break decisions
   - Trust-building moments
   - Value realization points
   - Advocacy triggers
   - Abandonment risks
   ```

**Elicitation Point 4:** `elicit: true`
Present pain points and opportunities. Ask user:
1. Proceed to metrics and measurement
2. Solution Ideation - Generate solutions
3. Priority Matrix - Rank opportunities
4. Feasibility Assessment - Technical viability
5. Impact Analysis - Quantify improvements
6. Resource Planning - Estimate effort
7. Risk Assessment - Implementation risks
8. Competitive Benchmarking - Industry comparison
9. Innovation Workshop - Creative solutions

Select 1-9 or type your question/feedback:

### Phase 5: Metrics and Success Indicators
**Objective:** Define measurable journey improvements

1. **Current State Metrics**
   ```
   From research data:

   Stage Progression:
   - Completion rates
   - Time in stage
   - Drop-off points
   - Retry attempts

   Satisfaction Indicators:
   - NPS/CSAT by stage
   - Support tickets
   - Complaints/compliments
   - Behavioral indicators
   ```

2. **Target Metrics**
   ```
   Define success measures:

   Efficiency Metrics:
   - Reduced time to value
   - Fewer steps required
   - Lower effort score
   - Decreased support needs

   Experience Metrics:
   - Improved satisfaction
   - Higher completion rates
   - Increased advocacy
   - Reduced frustration events
   ```

3. **Leading Indicators**
   ```
   Early warning signals:
   - Engagement patterns
   - Feature adoption
   - Support contact reasons
   - Search queries
   - FAQ visits
   ```

## Journey Map Visualization

### Visual Components

1. **Horizontal Layers**
   ```
   Standard Journey Map Structure:

   Stage:        [Awareness] [Research] [Decision] [Setup] [Usage]
   Actions:      [••••••••] [••••••••] [•••••••] [•••••] [•••••]
   Touchpoints:  [🌐📧💬]   [🌐📱💻]   [📞💳]    [📱⚙️]  [📱💻]
   Thoughts:     ["..."]    ["..."]    ["..."]   ["..."] ["..."]
   Emotions:     [😊😐😟]   [😟😊😐]   [😰😊]    [😟😊]  [😊😊]
   Opportunities:[💡]       [💡💡]     [💡]      [💡💡💡] [💡]
   ```

2. **Emotional Curve**
   ```
   Plot emotion over time:
   😊 ----╱╲------╱╲--------
   😐 ---╱--╲----╱--╲-------
   😟 --╱----╲--╱----╲------
   😰 -╱------╲╱------╲-----
   ```

3. **Opportunity Heat Map**
   - Red: Critical pain points
   - Yellow: Moderate issues
   - Green: Working well

## Quality Checklist

### Evidence Standards
- [ ] Every stage backed by research
- [ ] Touchpoints verified in data
- [ ] Emotions traced to quotes
- [ ] Pain points documented
- [ ] Opportunities justified

### Completeness
- [ ] Full journey covered
- [ ] All channels included
- [ ] Multiple personas considered
- [ ] Edge cases documented
- [ ] Metrics defined

### Actionability
- [ ] Opportunities prioritized
- [ ] Owners identified
- [ ] Success metrics clear
- [ ] Next steps defined
- [ ] Quick wins highlighted

## Output Deliverables

1. **Journey Map Document**
   - Visual journey map
   - Detailed stage descriptions
   - Evidence documentation
   - Opportunity register
   - Metrics dashboard

2. **Supporting Artifacts**
   - Persona-specific variations
   - Scenario comparisons
   - Opportunity cards
   - Implementation roadmap

3. **Action Plans**
   - Quick win initiatives
   - Strategic improvements
   - Innovation projects
   - Measurement plans

## Integration Notes

### Input Dependencies
- Persona profiles
- Synthesis insights
- Interview transcripts
- Touchpoint data
- Emotional analysis

### Output Consumers
- UX designers for experience design
- Product managers for roadmapping
- Service designers for blueprints
- Marketing for campaign planning
- Operations for process improvement

## Advanced Journey Techniques

### Multi-Persona Journeys
Show journey variations:
- Primary vs secondary personas
- Expert vs novice paths
- Success vs struggle patterns

### Future State Journeys
Based on opportunities:
- Ideal journey design
- Phased improvements
- Vision alignment

### Service Blueprint Integration
Connect to backstage:
- Internal processes
- System interactions
- Support structures

## CRITICAL REMINDERS

**❌ NEVER:**
- Assume journey stages without evidence
- Create fictional touchpoints
- Invent emotions not in data
- Skip pain point documentation
- Ignore minority experiences

**✅ ALWAYS:**
- Base everything on research
- Include emotional evidence
- Document confidence levels
- Identify opportunities
- Consider all personas

## Error Recovery

If journey seems incomplete:
1. Return to interview data
2. Look for process descriptions
3. Check temporal sequences
4. Validate with stakeholders
5. Mark gaps for research