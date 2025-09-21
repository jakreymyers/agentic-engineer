# Identify Jobs-to-be-Done

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **EVIDENCE-BASED JTBD** - Every job must come from actual user data
2. **OUTCOME FOCUS** - Focus on what users want to achieve, not features
3. **ELICITATION REQUIRED** - User input needed at job definition points
4. **CONTEXT MATTERS** - Situational factors are critical to JTBD

**VIOLATION INDICATOR:** If you create jobs without user evidence, you have violated this workflow.

## Task Configuration

```yaml
task:
  id: identify-jobs-to-be-done
  name: Jobs-to-be-Done Analysis
  template: jtbd-framework-tmpl.yaml
  output: docs/research/jobs-to-be-done.md
  elicitation_mode: mandatory
  framework: clayton-christensen
```

## Prerequisites

Before JTBD analysis:
1. **Verify Research Outputs**
   - Interview transcripts with context
   - Synthesis insights available
   - Pain points documented
   - User goals identified
   - Behavioral patterns analyzed

2. **Understand JTBD Framework**
   - Jobs vs solutions distinction
   - Functional/emotional/social dimensions
   - Progress-making forces
   - Job statement structure
   - Outcome expectations

## JTBD Discovery Workflow

### Phase 1: Context and Trigger Identification
**Objective:** Understand when and why users "hire" solutions

1. **Situation Mining**
   ```
   From research data, identify:

   Triggering Events:
   - What prompts action?
   - What changed in their situation?
   - What became intolerable?
   - What opportunity arose?

   Contextual Factors:
   - Where are they?
   - Who else is involved?
   - What constraints exist?
   - What time pressures?
   - What resources available?
   ```

2. **First Thought Analysis**
   ```
   Document initial responses:
   - What do they first consider?
   - What comes to mind immediately?
   - What past experiences influence?
   - What assumptions do they make?

   Evidence Required:
   - Direct quotes about situations
   - Stories of specific instances
   - Timeline of events
   - Context descriptions
   ```

3. **Struggling Moment Identification**
   ```
   Find the struggle that creates demand:

   Types of Struggles:
   - Functional: Can't accomplish task
   - Emotional: Feeling frustrated/anxious
   - Social: Looking bad to others
   - Financial: Wasting money/time

   Document:
   - Specific struggle descriptions
   - Intensity of struggle
   - Duration of struggle
   - Previous attempts to resolve
   ```

**Elicitation Point 1:** `elicit: true`
Present contexts and triggers identified. Ask user:
1. Proceed to job extraction
2. Timeline Analysis - Map temporal patterns
3. Struggle Deep Dive - Explore pain intensity
4. Context Mapping - Environmental factors
5. Trigger Clustering - Group similar situations
6. Alternative Analysis - What else they consider
7. Non-consumption - When they do nothing
8. Workaround Documentation - Current solutions
9. Expectation Setting - Desired outcomes

Select 1-9 or type your question/feedback:

### Phase 2: Job Extraction and Definition
**Objective:** Articulate the jobs users are trying to get done

1. **Raw Job Identification**
   ```
   From user language, extract:

   Functional Jobs (Main):
   - Core task to accomplish
   - Problem to solve
   - Objective to achieve
   - Goal to reach

   Format: [Verb] + [Object] + [Contextual Clarifier]
   Examples:
   - "Stay informed about industry changes when traveling"
   - "Minimize errors when under time pressure"
   - "Learn new skills while maintaining work pace"
   ```

2. **Emotional Job Components**
   ```
   Identify emotional dimensions:

   Personal Feelings:
   - How they want to feel
   - What emotions to avoid
   - Confidence desires
   - Security needs

   Examples:
   - "Feel confident about decisions"
   - "Avoid anxiety about missing information"
   - "Feel in control of the process"
   ```

3. **Social Job Aspects**
   ```
   Uncover social dimensions:

   How Others Perceive:
   - Image to project
   - Reputation to maintain
   - Status to achieve
   - Relationships to preserve

   Examples:
   - "Look competent to colleagues"
   - "Demonstrate innovation to boss"
   - "Maintain expert reputation"
   ```

**Elicitation Point 2:** `elicit: true`
Present extracted jobs with evidence. Ask user:
1. Proceed to outcome expectations
2. Job Refinement - Clarify job statements
3. Priority Assessment - Rank job importance
4. Substitution Analysis - Alternative hire options
5. Job Sizing - Market opportunity
6. Stability Check - How enduring is job?
7. Universality Test - Who else has this job?
8. Competition Mapping - Current solutions
9. Innovation Potential - Unmet aspects

Select 1-9 or type your question/feedback:

### Phase 3: Desired Outcomes and Success Metrics
**Objective:** Define what success looks like for each job

1. **Outcome Statements**
   ```
   For each job, identify desired outcomes:

   Structure: [Direction] + [Metric] + [Object] + [Context]

   Examples:
   - "Minimize time to find relevant information"
   - "Maximize accuracy of data entry"
   - "Increase confidence in decisions"
   - "Reduce stress during peak periods"

   Categories:
   - Speed outcomes
   - Quality outcomes
   - Cost outcomes
   - Convenience outcomes
   - Reliability outcomes
   ```

2. **Success Criteria**
   ```
   Define how users measure success:

   Objective Measures:
   - Time saved
   - Errors reduced
   - Steps eliminated
   - Cost decreased

   Subjective Measures:
   - Confidence level
   - Satisfaction degree
   - Stress reduction
   - Control feeling
   ```

3. **Importance vs Satisfaction**
   ```
   Map current state:

   For each outcome:
   - Importance: How critical (1-10)
   - Satisfaction: Current solutions (1-10)
   - Opportunity: Importance - Satisfaction

   High opportunity = High importance + Low satisfaction
   ```

**Elicitation Point 3:** `elicit: true`
Present outcomes and metrics. Ask user:
1. Proceed to forces analysis
2. Outcome Prioritization - Rank by opportunity
3. Metric Refinement - Clarify measurements
4. Benchmark Analysis - Industry comparisons
5. Threshold Definition - Minimum acceptable
6. Trade-off Analysis - Outcome conflicts
7. Segment Variation - Different user groups
8. Evolution Tracking - Changing expectations
9. Solution Mapping - Feature implications

Select 1-9 or type your question/feedback:

### Phase 4: Forces Analysis
**Objective:** Understand what drives and blocks progress

1. **Push Forces** (Away from current)
   ```
   What pushes from current state:

   Functional Push:
   - Current solution failures
   - Increasing inefficiency
   - Growing complexity

   Emotional Push:
   - Mounting frustration
   - Increasing anxiety
   - Lost confidence

   Social Push:
   - Peer pressure
   - Status concerns
   - Reputation risks

   Evidence: Quotes expressing dissatisfaction
   ```

2. **Pull Forces** (Toward new)
   ```
   What attracts to new solution:

   Functional Pull:
   - Better performance promise
   - Easier process
   - More capabilities

   Emotional Pull:
   - Peace of mind
   - Excitement about possibilities
   - Confidence boost

   Social Pull:
   - Social proof
   - Status enhancement
   - Community belonging

   Evidence: Quotes about desires
   ```

3. **Anxiety Forces** (New solution concerns)
   ```
   What creates hesitation:

   Functional Anxiety:
   - Learning curve fears
   - Integration concerns
   - Performance doubts

   Emotional Anxiety:
   - Fear of failure
   - Change resistance
   - Overwhelm concerns

   Social Anxiety:
   - Looking foolish
   - Peer judgment
   - Authority pushback
   ```

4. **Habit Forces** (Current solution attachment)
   ```
   What maintains status quo:

   Functional Habits:
   - Familiar workflows
   - Muscle memory
   - Known workarounds

   Emotional Habits:
   - Comfort with known
   - Sunk cost feeling
   - Loss aversion

   Social Habits:
   - Team processes
   - Organizational inertia
   - Cultural norms
   ```

**Elicitation Point 4:** `elicit: true`
Present forces analysis. Ask user:
1. Proceed to job architecture
2. Force Quantification - Measure strength
3. Intervention Points - Where to influence
4. Barrier Removal - Address anxieties
5. Catalyst Design - Amplify pulls
6. Habit Breaking - Disruption strategies
7. Social Proof - Evidence gathering
8. Risk Mitigation - Reduce anxieties
9. Migration Path - Transition planning

Select 1-9 or type your question/feedback:

### Phase 5: Job Architecture and Hierarchy
**Objective:** Structure jobs into actionable framework

1. **Job Hierarchy**
   ```
   Organize jobs by level:

   Big Job (Main objective):
   "Manage my professional development"

   Related Jobs (Supporting):
   - "Stay current with industry trends"
   - "Build relevant skills"
   - "Demonstrate expertise"
   - "Network effectively"

   Little Jobs (Micro-tasks):
   - "Find relevant content quickly"
   - "Track learning progress"
   - "Share accomplishments"
   ```

2. **Job Chains**
   ```
   Map sequential relationships:

   Job Flow:
   Trigger → Job 1 → Job 2 → Job 3 → Success

   Example:
   Need arises → Research options → Make decision →
   Implement → Monitor results → Optimize

   Document:
   - Prerequisite jobs
   - Subsequent jobs
   - Parallel jobs
   - Optional jobs
   ```

3. **Solution Criteria**
   ```
   Define hiring criteria:

   For each job:
   - Must-have capabilities
   - Nice-to-have features
   - Deal breakers
   - Trade-off willing to make

   Evaluation Framework:
   - How well does it do the job?
   - How much effort required?
   - How reliable is it?
   - How does it fit context?
   ```

## Quality Checklist

### Evidence Standards
- [ ] Every job traced to user quotes
- [ ] Context clearly documented
- [ ] Struggles explicitly identified
- [ ] Outcomes measurable
- [ ] Forces balanced and realistic

### Completeness
- [ ] Functional jobs defined
- [ ] Emotional dimensions included
- [ ] Social aspects considered
- [ ] Full job chain mapped
- [ ] Success metrics clear

### Actionability
- [ ] Jobs clearly articulated
- [ ] Opportunities prioritized
- [ ] Innovation spaces identified
- [ ] Solution criteria defined
- [ ] Implementation implications clear

## Output Deliverables

1. **JTBD Framework Document**
   - Job statements catalog
   - Outcome expectations
   - Forces analysis
   - Opportunity scores
   - Solution criteria

2. **Supporting Artifacts**
   - Job cards for ideation
   - Forces diagrams
   - Opportunity matrix
   - Innovation spaces map

3. **Design Implications**
   - Feature prioritization
   - Messaging framework
   - Onboarding focus
   - Value proposition

## Integration Notes

### Input Dependencies
- Interview transcripts
- Synthesis insights
- Persona profiles
- Journey maps
- Pain point analysis

### Output Consumers
- Product managers for roadmapping
- Designers for solution design
- Marketing for messaging
- Innovation teams for opportunities
- Strategy for positioning

## Advanced JTBD Techniques

### Job Evolution Tracking
How jobs change over time:
- Maturity effects
- Technology shifts
- Context changes
- Expectation inflation

### Competing Jobs Analysis
What else competes for priority:
- Other jobs in same context
- Resource allocation
- Attention competition
- Time constraints

### Non-Consumption Analysis
When users choose nothing:
- Barriers too high
- No good enough solution
- Not worth the effort
- Living with problem

### Job Bundling Opportunities
Jobs that cluster together:
- Complementary jobs
- Sequential dependencies
- Same context jobs
- Efficiency bundles

## CRITICAL REMINDERS

**❌ NEVER:**
- Confuse solutions with jobs
- Create jobs from assumptions
- Focus only on functional dimension
- Ignore context and situation
- Skip forces analysis

**✅ ALWAYS:**
- Start with user struggles
- Include all three dimensions
- Document evidence trail
- Consider forces balance
- Focus on progress desired

## Error Recovery

If jobs seem unclear:
1. Return to struggle moments
2. Re-examine user language
3. Check for solution bias
4. Validate with scenarios
5. Test with outcome statements