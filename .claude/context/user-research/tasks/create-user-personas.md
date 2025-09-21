# Create Evidence-Based User Personas

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **EVIDENCE-BASED ONLY** - Every persona attribute must trace to real data
2. **NO STEREOTYPES** - Avoid demographic assumptions and clichés
3. **ELICITATION REQUIRED** - User input needed at key decision points
4. **BEHAVIORAL FOCUS** - Prioritize behaviors over demographics

**VIOLATION INDICATOR:** If you create fictional attributes without evidence, you have violated this workflow.

## Task Configuration

```yaml
task:
  id: create-user-personas
  name: Evidence-Based Persona Development
  template: persona-profile-tmpl.yaml
  output: docs/research/user-personas.md
  elicitation_mode: mandatory
  evidence_requirement: strict
  persona_count: 3-5 (optimal)
```

## Prerequisites

Before creating personas:
1. **Verify Data Availability**
   - Synthesis patterns identified
   - Behavioral segments discovered
   - Demographics documented
   - Quotes and stories collected
   - Journey data available

2. **Understand Persona Purpose**
   - Design decision support
   - Empathy building
   - Requirement prioritization
   - Communication tool
   - NOT marketing segments

## Persona Development Workflow

### Phase 1: Behavioral Segmentation
**Objective:** Identify distinct user segments based on behavior patterns

1. **Behavioral Variable Identification**
   ```
   Key Behavioral Dimensions:
   - Frequency of use patterns
   - Depth of feature usage
   - Problem-solving approaches
   - Technology comfort levels
   - Collaboration patterns
   - Decision-making styles
   - Information seeking behavior
   - Goal achievement strategies
   ```

2. **Cluster Analysis**
   ```
   For each behavioral dimension:
   - Map participants along continuum
   - Identify natural clusters
   - Note cluster boundaries
   - Document cluster characteristics

   Example:
   Dimension: Technology Adoption
   Cluster 1: Early adopters (P1, P4, P7)
   Cluster 2: Pragmatists (P2, P5, P8, P9)
   Cluster 3: Cautious users (P3, P6, P10)
   ```

3. **Segment Definition**
   - Combine related behavioral clusters
   - Identify 3-5 distinct segments
   - Ensure segments are mutually exclusive
   - Verify comprehensive coverage

**Elicitation Point 1:** `elicit: true`
Present behavioral segments with evidence. Ask user:
1. Proceed to persona skeleton creation
2. Card Sorting - Reorganize segments
3. Statistical Validation - Verify segment significance
4. Gap Analysis - Identify missing segments
5. Stakeholder Mapping - Align with business segments
6. Competitive Analysis - Compare to market segments
7. Journey Mapping - Map segments to journeys
8. Priority Setting - Rank segment importance
9. Validation Planning - How to verify segments

Select 1-9 or type your question/feedback:

### Phase 2: Persona Skeleton Development
**Objective:** Create evidence-based framework for each persona

1. **Core Attributes Assembly**
   ```
   For each persona segment:

   Foundation (from synthesis):
   - Primary goals (3-5 from data)
   - Key frustrations (3-5 from data)
   - Success criteria (what matters most)
   - Mental models (how they think)

   Evidence Required:
   - Minimum 3 participants per attribute
   - Direct quotes supporting each
   - Behavioral observations
   - Frequency/intensity data
   ```

2. **Behavioral Patterns**
   ```
   Document observed behaviors:
   - Typical workflows
   - Tool preferences
   - Communication styles
   - Learning approaches
   - Problem-solving methods
   - Help-seeking behavior

   Include:
   - Frequency data (daily/weekly/monthly)
   - Context of use
   - Triggers and motivations
   ```

3. **Environmental Context**
   ```
   From research data only:
   - Work environment characteristics
   - Technical environment
   - Social/collaborative context
   - Constraints they operate under
   - External pressures
   ```

**Elicitation Point 2:** `elicit: true`
Present persona skeletons with evidence. Ask user:
1. Proceed to persona enrichment
2. Empathy Mapping - Add emotional dimensions
3. Day-in-Life - Build typical scenarios
4. Pain Point Deep Dive - Expand frustrations
5. Motivation Analysis - Understand drivers
6. Relationship Mapping - Social connections
7. Technology Ecosystem - Tool landscape
8. Cultural Factors - Context influences
9. Edge Case Exploration - Boundary conditions

Select 1-9 or type your question/feedback:

### Phase 3: Persona Enrichment and Validation
**Objective:** Add depth while maintaining evidence base

1. **Narrative Development**
   ```
   Create persona story from evidence:

   Background (inferred from data):
   - Relevant experience indicators
   - Skill level evidence
   - Domain expertise signs

   Current Situation:
   - Actual problems they're solving
   - Real challenges faced
   - Observed workarounds

   Future Aspirations:
   - Expressed desires
   - Implied goals
   - Success visions shared
   ```

2. **Quote Integration**
   ```
   For each persona, select:
   - Defining quote (captures essence)
   - Goal quotes (what they want)
   - Frustration quotes (pain points)
   - Success quotes (what works)
   - Aspiration quotes (future vision)

   Format:
   "Actual quote from participant" - [P##]
   ```

3. **Scenario Validation**
   ```
   Test persona against real scenarios:
   - Use cases from research
   - Edge cases encountered
   - Failure scenarios observed
   - Success stories documented

   Persona should explain/predict:
   - Behavioral choices made
   - Preferences expressed
   - Reactions observed
   - Decisions documented
   ```

**Elicitation Point 3:** `elicit: true`
Present enriched personas. Ask user:
1. Proceed to differentiation and naming
2. Scenario Testing - Validate with use cases
3. Team Review - Stakeholder feedback
4. Completeness Check - Missing elements
5. Accuracy Review - Evidence alignment
6. Usefulness Assessment - Decision support
7. Memorability Check - Stickiness factors
8. Diversity Audit - Representation check
9. Evolution Planning - Update mechanisms

Select 1-9 or type your question/feedback:

### Phase 4: Differentiation and Naming
**Objective:** Make personas distinct and memorable

1. **Differentiation Matrix**
   ```
   Create comparison table:

   Dimension     | Persona 1 | Persona 2 | Persona 3
   --------------|-----------|-----------|----------
   Primary Goal  | Speed     | Accuracy  | Learning
   Approach      | Intuitive | Methodical| Exploratory
   Tech Comfort  | High      | Medium    | Low
   Support Need  | Minimal   | Moderate  | High
   ```

2. **Naming Strategy**
   ```
   Avoid stereotypes, use functional names:

   Good Examples:
   - "The Efficiency Expert"
   - "The Careful Validator"
   - "The Collaborative Explorer"

   Include:
   - Memorable identifier
   - Role/approach indicator
   - Avoid demographic identifiers
   ```

3. **Visual Identity** (if applicable)
   ```
   Evidence-based visual cues:
   - Environment indicators
   - Tool/device preferences
   - Work style elements
   - Avoid stock photos
   - Consider illustrations
   ```

### Phase 5: Documentation and Delivery
**Objective:** Create actionable persona artifacts

1. **Persona Profile Creation**
   ```
   Standard Format per Persona:

   HEADER
   - Name/Title
   - Defining Quote
   - Segment Size (% of users)

   GOALS & NEEDS
   - Primary objectives (3-5)
   - Success metrics
   - Core needs

   BEHAVIORS & PREFERENCES
   - Key behaviors observed
   - Tool preferences
   - Workflow patterns

   FRUSTRATIONS & BARRIERS
   - Major pain points
   - Blockers encountered
   - Workarounds used

   CONTEXT & ENVIRONMENT
   - Technical environment
   - Social context
   - Constraints

   EVIDENCE BASE
   - Participant IDs represented
   - Key supporting quotes
   - Confidence level
   ```

2. **Usage Guidelines**
   ```
   Document how to use personas:

   For Design Decisions:
   "Would [Persona] find this intuitive?"

   For Prioritization:
   "Which persona benefits most?"

   For Communication:
   "How would we explain to [Persona]?"

   For Validation:
   "Does this solve [Persona]'s problem?"
   ```

## Quality Checklist

### Evidence Standards
- [ ] Every attribute traceable to data
- [ ] Minimum 3 participants per persona
- [ ] Direct quotes included
- [ ] Behavioral evidence documented
- [ ] Contradictions addressed

### Differentiation
- [ ] Personas clearly distinct
- [ ] No overlap in core attributes
- [ ] Different goals and needs
- [ ] Unique value propositions
- [ ] Clear use case alignment

### Usefulness
- [ ] Actionable for design decisions
- [ ] Memorable and distinct
- [ ] Scenario coverage complete
- [ ] Stakeholder validated
- [ ] Update mechanism defined

### Bias Prevention
- [ ] No unfounded demographics
- [ ] No stereotypes present
- [ ] Diverse representation
- [ ] Behavioral focus maintained
- [ ] Evidence-based throughout

## Output Deliverables

1. **Persona Profiles** (3-5 personas)
   - One-page summaries
   - Detailed profiles
   - Comparison matrix
   - Evidence documentation

2. **Supporting Materials**
   - Persona cards for workshops
   - Scenario validation results
   - Usage guidelines
   - Update protocols

3. **Integration Artifacts**
   - Journey mapping inputs
   - Requirement prioritization matrix
   - Design decision framework
   - Communication templates

## Integration Notes

### Input Requirements
- Synthesis patterns and insights
- Behavioral clustering data
- Interview quotes and stories
- Journey and workflow data
- Demographic data (where relevant)

### Output Consumers
- UX/UI designers for interface design
- Product managers for prioritization
- Development teams for user stories
- Marketing for messaging (with caveats)
- Customer success for support design

## Advanced Persona Techniques

### Anti-Personas
Document who we're NOT designing for:
- Edge cases we won't support
- Users outside our scope
- Behaviors we won't enable

### Persona Evolution
Plan for updates:
- Validation checkpoints
- Update triggers
- Evolution tracking
- Retirement criteria

### Accessibility Personas
Special considerations:
- Assistive technology users
- Cognitive differences
- Physical limitations
- Environmental constraints

## CRITICAL REMINDERS

**❌ NEVER:**
- Invent attributes without evidence
- Use demographic stereotypes
- Create more than 7 personas
- Mix marketing segments with design personas
- Ignore minority user types

**✅ ALWAYS:**
- Trace every attribute to data
- Focus on behaviors over demographics
- Maintain evidence documentation
- Validate with real scenarios
- Plan for persona evolution

## Error Recovery

If personas feel fictional:
1. Return to behavioral data
2. Increase evidence requirements
3. Remove unsupported attributes
4. Add more participant quotes
5. Validate with team