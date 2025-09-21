# Setup Conjoint Analysis Study

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **MANDATORY ELICITATION** - User must be involved in attribute and level selection
2. **STEP-BY-STEP EXECUTION** - Each phase requires user validation
3. **TECHNICAL VALIDATION** - Design efficiency must be verified
4. **NO SHORTCUTS** - All design decisions must be justified

## Task Configuration
```yaml
task:
  id: setup-conjoint-analysis
  name: Setup Conjoint Analysis Study
  agent: research-strategist
  elicit: true
  template: conjoint-setup-tmpl.yaml
  output: docs/research/conjoint-design.md
```

## Phase 1: Objective Definition

### Step 1.1: Define Decision Context
**ELICIT: true**

Present to user:
- What product/service decisions need to be made?
- What trade-offs are stakeholders facing?
- What market scenarios need testing?

**Provide detailed rationale:**
- Why conjoint is appropriate for these decisions
- Expected insights and applications
- Alternative methods considered

**MANDATORY 1-9 OPTIONS:**
1. Proceed with conjoint setup
2. Clarify objectives through examples
3. Map stakeholder decisions
4. Explore alternative methods
5. Define success metrics
6. Review similar studies
7. Assess resource requirements
8. Validate with stakeholders
9. Refine research questions

**WAIT FOR USER RESPONSE**

### Step 1.2: Select Conjoint Type
Based on objectives, recommend appropriate conjoint methodology:

**Choice-Based Conjoint (CBC)**
- Most common and realistic
- Mimics actual purchase decisions
- Best for: Product configuration, pricing

**Adaptive Conjoint Analysis (ACA)**
- Adapts to respondent preferences
- Handles many attributes (up to 30)
- Best for: Complex products, B2B

**Menu-Based Choice (MBC)**
- Multiple items selected
- Bundle configuration
- Best for: Service packages, subscriptions

**MaxDiff Scaling**
- Best-worst scaling
- Preference prioritization
- Best for: Feature prioritization

## Phase 2: Attribute Identification

### Step 2.1: Generate Attribute List
**ELICIT: true**

**Process:**
1. Review product/service documentation
2. Analyze competitor offerings
3. Consider user research insights
4. Map to decision criteria

**Present Initial Attributes (aim for 4-7):**
```
Example for Software Product:
1. Price ($X - $Y per month)
2. Features (Basic/Pro/Enterprise)
3. Support (Email/Chat/Phone/Dedicated)
4. Integration (None/Limited/Full)
5. Security (Standard/Advanced/Enterprise)
```

**Attribute Criteria:**
- Meaningful to decision makers
- Actionable by organization
- Independent (not overlapping)
- Measurable and communicable

**MANDATORY 1-9 OPTIONS:**
1. Accept attribute list
2. Add attributes from user research
3. Remove redundant attributes
4. Combine related attributes
5. Split complex attributes
6. Test attribute independence
7. Validate with stakeholders
8. Review competitor attributes
9. Prioritize must-have attributes

**WAIT FOR USER RESPONSE**

### Step 2.2: Check Attribute Independence
Verify attributes are truly independent:
- No logical dependencies
- No impossible combinations
- Clear differentiation

Create correlation matrix to identify issues.

## Phase 3: Level Definition

### Step 3.1: Define Attribute Levels
**ELICIT: true**

For each attribute, define 2-5 levels that:
- Cover realistic range
- Are clearly differentiated
- Include current offering
- Test stretches believably

**Example Level Definition:**
```
Attribute: Price
Levels:
- Level 1: $29/month (current)
- Level 2: $49/month
- Level 3: $79/month
- Level 4: $99/month

Rationale:
- Covers price sensitivity range
- Tests willingness to pay
- Includes competitive benchmarks
```

**Level Selection Criteria:**
- Balanced (similar gaps)
- Realistic (market feasible)
- Actionable (can implement)
- Testable (distinguishable)

**MANDATORY 1-9 OPTIONS:**
1. Proceed with level definitions
2. Adjust level ranges
3. Add intermediate levels
4. Test extreme levels
5. Include competitive levels
6. Validate feasibility
7. Check level balance
8. Create level descriptions
9. Test comprehension

**WAIT FOR USER RESPONSE**

### Step 3.2: Create Level Descriptions
Write clear, concise descriptions for each level:
- Unambiguous language
- Consistent format
- Visual aids if helpful
- Avoid loaded terms

## Phase 4: Experimental Design

### Step 4.1: Generate Design
**ELICIT: true**

**Design Parameters:**
```
Total Profiles = ∏(levels per attribute)
Example: 4×3×3×2×3 = 216 possible combinations

Fractional Factorial Design:
- Main effects: Always included
- Two-way interactions: Selected
- Efficiency target: >0.85
```

**Design Generation:**
1. Use orthogonal arrays
2. Apply D-efficiency criteria
3. Balance level appearance
4. Minimize correlation

**Present Design Summary:**
- Number of choice sets: 12-20
- Profiles per set: 2-4 + none option
- Design efficiency: X.XX
- Level balance: Show frequency

**MANDATORY 1-9 OPTIONS:**
1. Accept experimental design
2. Adjust number of tasks
3. Add holdout tasks
4. Include none option
5. Test design efficiency
6. Create blocks for rotation
7. Add prohibition pairs
8. Review cognitive load
9. Generate alternative design

**WAIT FOR USER RESPONSE**

### Step 4.2: Create Holdout Tasks
Generate 2-3 holdout tasks for validation:
- Not used in utility estimation
- Tests prediction accuracy
- Validates model

## Phase 5: Choice Task Construction

### Step 5.1: Build Choice Cards
**ELICIT: true**

**Card Format Example:**
```
Which option would you choose?

Option A          Option B          Option C
---------         ---------         ---------
Price: $49        Price: $79        Price: $29
Features: Pro     Features: Basic   Features: Enterprise
Support: Chat     Support: Phone    Support: Email
Integration: Full Integration: None Integration: Limited
Security: Advanced Security: Standard Security: Enterprise

[Select A]        [Select B]        [Select C]        [None]
```

**Visual Design Considerations:**
- Consistent layout
- Clear differentiation
- Mobile responsive
- Accessibility compliant

**MANDATORY 1-9 OPTIONS:**
1. Approve card design
2. Adjust visual layout
3. Add visual elements
4. Simplify presentation
5. Test on devices
6. Include descriptions
7. Add hover details
8. Create card templates
9. Test with users

**WAIT FOR USER RESPONSE**

### Step 5.2: Create Instructions
Write clear participant instructions:
- Task explanation
- Decision context
- Time expectations
- Example walkthrough

## Phase 6: Implementation Planning

### Step 6.1: Sample Size Calculation
**ELICIT: true**

**Minimum Sample Requirements:**
```
Base Calculation:
n = 500 / (levels × tasks)

Recommended:
- Main effects only: 200-300
- With interactions: 300-500
- Segmentation planned: 500+
- Individual modeling: 750+
```

**Present Sample Plan:**
- Target sample size: XXX
- Per segment: XXX
- Power analysis results
- Margin of error

**MANDATORY 1-9 OPTIONS:**
1. Accept sample size
2. Increase for segmentation
3. Adjust for budget
4. Calculate power
5. Plan recruitment
6. Define quotas
7. Set quality criteria
8. Plan incentives
9. Review feasibility

**WAIT FOR USER RESPONSE**

### Step 6.2: Analysis Planning
Define analysis approach:
- Aggregate logit
- Hierarchical Bayes
- Latent class
- Individual utilities

## Phase 7: Validation & Testing

### Step 7.1: Design Validation
Run technical validation checks:
- Orthogonality test
- Efficiency metrics
- Balance verification
- Correlation matrix

### Step 7.2: Pilot Testing
**ELICIT: true**

**Pilot Test Protocol:**
1. Test with 10-20 respondents
2. Measure completion time
3. Check comprehension
4. Gather feedback
5. Assess choice patterns

**Present Pilot Results:**
- Completion rate
- Average time
- Comprehension issues
- Feedback themes
- Recommended changes

**MANDATORY 1-9 OPTIONS:**
1. Proceed to full study
2. Refine based on feedback
3. Adjust task difficulty
4. Improve instructions
5. Modify attributes/levels
6. Reduce cognitive load
7. Add practice tasks
8. Test alternative format
9. Conduct additional pilot

**WAIT FOR USER RESPONSE**

## Phase 8: Documentation & Handoff

### Step 8.1: Create Design Document
Compile comprehensive design specification:
- Objectives and hypotheses
- Attributes and levels
- Experimental design details
- Choice task examples
- Sample requirements
- Analysis plan
- Timeline and budget

### Step 8.2: Prepare Implementation Materials
Package for field execution:
- Survey programming specs
- Visual assets
- Screening criteria
- Quality check protocols
- Analysis scripts

## Quality Checkpoints

**Design Quality:**
- [ ] Efficiency >0.85
- [ ] Orthogonality maintained
- [ ] Balance achieved
- [ ] Prohibitions handled

**Content Quality:**
- [ ] Attributes meaningful
- [ ] Levels realistic
- [ ] Descriptions clear
- [ ] Instructions tested

**Technical Quality:**
- [ ] Sample size adequate
- [ ] Power sufficient
- [ ] Analysis planned
- [ ] Validation included

## Common Issues & Solutions

**Too Many Attributes:**
- Use partial profile designs
- Consider ACA instead of CBC
- Create attribute blocks

**Complex Interactions:**
- Include specific scenarios
- Use conditional pricing
- Add prohibition rules

**Respondent Fatigue:**
- Reduce number of tasks
- Simplify presentation
- Add progress indicators

## Deliverables

1. **Conjoint Design Specification**
   - Complete methodology documentation
   - Experimental design details
   - Implementation requirements

2. **Choice Task Materials**
   - Card layouts and designs
   - Survey programming specifications
   - Visual assets

3. **Analysis Plan**
   - Statistical approach
   - Output specifications
   - Simulation scenarios

## References

**Design Efficiency Formulas:**
- D-efficiency: |X'X|^(1/p) / N
- A-efficiency: p / trace((X'X)^-1)

**Sample Size Guidelines:**
- Johnson & Orme (2003): 20*k/n rule
- Orme (2010): Market simulators need 200+

**Software Recommendations:**
- Sawtooth Software (CBC/HB)
- R packages: choiceModelR, bayesm
- Python: pylogit, choix

## Success Metrics

- Design efficiency achieved: >0.85
- Pilot test success rate: >90%
- Predicted vs actual holdout: >70%
- Stakeholder approval: Yes
- Implementation ready: Complete