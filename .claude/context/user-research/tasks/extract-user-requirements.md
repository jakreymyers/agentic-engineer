# Extract User Requirements from Research

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **MANDATORY STEP-BY-STEP EXECUTION** - Each extraction phase must be completed sequentially
2. **ELICITATION IS REQUIRED** - When `elicit: true`, you MUST use the 1-9 format
3. **TRACEABILITY IS CRITICAL** - Every requirement must link to source evidence
4. **NO ASSUMPTIONS** - Requirements must be evidence-based only

**VIOLATION INDICATOR:** If you create requirements without evidence traceability, you have violated this workflow.

## Task Configuration

```yaml
task:
  id: extract-user-requirements
  name: User Requirements Extraction
  template: requirements-matrix-tmpl.yaml
  output: docs/research/requirements-matrix.md
  elicitation_mode: mandatory
  traceability: strict
```

## Prerequisites

Before extracting requirements:
1. **Verify Synthesis Outputs**
   - Cross-interview synthesis complete
   - Patterns and insights documented
   - Pain points catalogued
   - Opportunities identified

2. **Gather Supporting Data**
   - Original transcripts for quotes
   - Affinity diagrams
   - Statistical validation data
   - Stakeholder priorities

3. **Understand Requirements Context**
   - Product/service scope
   - Technical constraints
   - Business constraints
   - Regulatory requirements

## Requirements Extraction Workflow

### Phase 1: Pain Point to Requirement Translation
**Objective:** Transform identified pain points into requirements

1. **Catalog All Pain Points**
   ```
   For each pain point from synthesis:
   - ID: [PP-001]
   - Description: [User's pain point]
   - Frequency: [% of users affected]
   - Severity: [High/Medium/Low]
   - Evidence: [Source references]
   ```

2. **Translate to Requirements**
   ```
   Translation Pattern:
   Pain Point → Requirement

   "Users struggle to find X" → "System shall provide intuitive X discovery"
   "Process takes too long" → "System shall complete process in <N seconds"
   "Can't do X on mobile" → "System shall support X on mobile devices"
   ```

3. **Requirement Formulation**
   - Use clear "shall" statements
   - Make measurable where possible
   - Avoid implementation details
   - Focus on user needs not solutions

**Elicitation Point 1:** `elicit: true`
Present pain point translations. Ask user:
1. Proceed to desire extraction
2. Priority Matrix - Rank pain points by impact
3. Root Cause Analysis - Deeper requirement understanding
4. Stakeholder Analysis - Validate pain point importance
5. Scenario Analysis - Context for requirements
6. Constraint Analysis - Identify limitations
7. Trade-off Analysis - Balance competing needs
8. Risk Assessment - Requirement risks
9. Validation Planning - How to verify requirements

Select 1-9 or type your question/feedback:

### Phase 2: Desire and Delight Extraction
**Objective:** Capture positive requirements and delighters

1. **Identify Expressed Desires**
   ```
   Categories:
   - Explicitly Requested Features
   - Wished-for Capabilities
   - Comparison to Ideal Solutions
   - Future Vision Statements
   ```

2. **Discover Latent Needs**
   - Implied requirements from behavior
   - Unstated expectations
   - Assumed capabilities
   - Environmental requirements

3. **Capture Delight Factors**
   - Unexpected positive reactions
   - Features that excited users
   - Memorable positive experiences
   - Competitive differentiators mentioned

**Elicitation Point 2:** `elicit: true`
Present desires and delighters. Ask user:
1. Proceed to requirement categorization
2. Kano Analysis - Classify requirement types
3. Value Proposition Canvas - Map to user value
4. Jobs-to-be-Done - Connect to user jobs
5. Emotional Journey - Map emotional requirements
6. Competitive Analysis - Benchmark requirements
7. Innovation Opportunities - Explore beyond stated
8. User Story Mapping - Create user stories
9. Feature Prioritization - Initial priority assessment

Select 1-9 or type your question/feedback:

### Phase 3: Requirements Categorization and Structure
**Objective:** Organize requirements into actionable categories

1. **Functional Requirements**
   ```
   Template: FR-[###]: [Actor] shall [capability] [condition] [measure]
   Example: FR-001: Users shall be able to search products by multiple criteria with results in <2 seconds

   Categories:
   - Core Functionality
   - Data Management
   - User Interaction
   - Integration Points
   - Reporting/Analytics
   ```

2. **Non-Functional Requirements**
   ```
   Template: NFR-[###]: System shall [quality attribute] [measure]
   Example: NFR-001: System shall maintain 99.9% uptime during business hours

   Categories:
   - Performance
   - Security
   - Usability
   - Reliability
   - Scalability
   - Accessibility
   - Compliance
   ```

3. **Constraints and Assumptions**
   - Technical constraints
   - Business constraints
   - Resource constraints
   - Timeline constraints
   - Assumptions about users
   - Environmental assumptions

**Elicitation Point 3:** `elicit: true`
Present categorized requirements. Ask user:
1. Proceed to priority and dependency mapping
2. Dependency Analysis - Map requirement relationships
3. Conflict Resolution - Address contradictions
4. Completeness Check - Identify gaps
5. Testability Review - Ensure measurability
6. Feasibility Assessment - Technical viability
7. Cost-Benefit Analysis - Requirement value
8. Regulatory Review - Compliance check
9. Architecture Impact - System implications

Select 1-9 or type your question/feedback:

### Phase 4: Priority and Dependency Mapping
**Objective:** Establish requirement priorities and relationships

1. **Priority Assignment**
   ```
   MoSCoW Method:
   - Must Have: Critical for launch
   - Should Have: Important but not critical
   - Could Have: Desirable if resources allow
   - Won't Have: Out of scope for this phase

   Evidence for Priority:
   - User impact (% affected)
   - Business value
   - Technical dependency
   - Risk mitigation
   ```

2. **Dependency Mapping**
   ```
   For each requirement:
   - Prerequisites: [Required before this]
   - Enables: [Unlocked by this]
   - Conflicts: [Contradicts with]
   - Related: [Works together with]
   ```

3. **Requirement Grouping**
   - Epic level groupings
   - Feature sets
   - User journey alignment
   - Release planning groups

**Elicitation Point 4:** `elicit: true`
Present priorities and dependencies. Ask user:
1. Proceed to traceability matrix completion
2. Release Planning - Map to releases
3. Resource Planning - Estimate effort
4. Risk Mitigation - Address high-risk items
5. MVP Definition - Minimum viable set
6. Roadmap Development - Long-term view
7. Stakeholder Alignment - Validate priorities
8. Trade-off Decisions - Balance constraints
9. Success Metrics - Define acceptance criteria

Select 1-9 or type your question/feedback:

### Phase 5: Traceability Matrix Completion
**Objective:** Ensure complete evidence chain for all requirements

1. **Evidence Linking**
   ```
   For EVERY requirement:
   Requirement ID: [REQ-###]
   Type: [Functional/Non-functional]
   Priority: [Must/Should/Could/Won't]

   Evidence Sources:
   - Interview quotes: [Participant ID, Quote]
   - Survey data: [Question, Results]
   - Observation notes: [Context, Behavior]
   - Analytics: [Metric, Value]
   - Synthesis insight: [Insight ID]

   Confidence Level: [High/Medium/Low]
   ```

2. **Validation Criteria**
   ```
   For each requirement:
   - Acceptance Criteria: [How to verify]
   - Test Approach: [How to validate]
   - Success Metrics: [How to measure]
   - User Scenarios: [Usage contexts]
   ```

3. **Stakeholder Mapping**
   - Primary beneficiaries
   - Secondary stakeholders
   - Approval required from
   - Communication needed to

## Requirements Quality Checklist

### Clarity and Completeness
- [ ] Each requirement has unique ID
- [ ] Written in clear "shall" statements
- [ ] Avoids technical jargon
- [ ] Complete and self-contained
- [ ] Unambiguous interpretation

### Measurability
- [ ] Quantifiable where possible
- [ ] Clear acceptance criteria
- [ ] Testable conditions
- [ ] Defined success metrics
- [ ] Verification approach identified

### Traceability
- [ ] Links to source evidence (minimum 2 sources preferred)
- [ ] Participant quotes included
- [ ] Confidence level assigned
- [ ] Contradictions documented
- [ ] Assumptions explicit

### Feasibility
- [ ] Technical feasibility assessed
- [ ] Resource requirements considered
- [ ] Timeline impacts evaluated
- [ ] Risk factors identified
- [ ] Dependencies mapped

## Output Artifacts

1. **Requirements Matrix Document**
   - Executive summary
   - Requirements inventory
   - Priority rankings
   - Dependency map
   - Traceability matrix
   - Validation approach

2. **Supporting Deliverables**
   - Requirements cards for planning
   - User story seeds
   - Acceptance criteria library
   - Test case foundations

3. **Handoff Packages**
   - Product team requirements
   - Development team specs
   - QA team test plans
   - Stakeholder summaries

## Integration Notes

### Input Sources
- Cross-interview synthesis
- Pain point analysis
- Opportunity identification
- Stakeholder priorities
- Technical constraints

### Output Consumers
- Product managers for roadmapping
- Development teams for implementation
- QA teams for test planning
- Business analysts for specifications
- UX designers for design requirements

## Advanced Extraction Techniques

### Negative Requirements
What users DON'T want:
- Explicit rejections
- Avoided features
- Discontinued behaviors
- Frustration triggers

### Comparative Requirements
From competitive mentions:
- "Like X but better"
- "Without the problems of Y"
- "Combining best of A and B"
- Industry standard expectations

### Contextual Requirements
Environmental needs:
- Location-based requirements
- Time-based requirements
- Role-based requirements
- Situation-specific needs

## CRITICAL REMINDERS

**❌ NEVER:**
- Create requirements without evidence
- Make assumptions about user needs
- Ignore minority requirements
- Skip traceability documentation
- Overlook non-functional requirements

**✅ ALWAYS:**
- Link every requirement to evidence
- Use standard requirement formats
- Maintain priority justification
- Document confidence levels
- Consider edge cases

## Error Recovery

If requirements become unclear:
1. Return to original quotes
2. Re-examine synthesis insights
3. Validate with stakeholders
4. Mark as "needs clarification"
5. Schedule follow-up research