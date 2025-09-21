# Calculate Sample Size

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:

1. **MATHEMATICAL PRECISION REQUIRED** - All calculations must be statistically valid
2. **RESEARCH TYPE SENSITIVITY** - Different methods need different approaches
3. **ELICITATION IS MANDATORY** - User must validate assumptions and constraints
4. **NO STATISTICAL SHORTCUTS** - Proper power analysis cannot be skipped

**VIOLATION INDICATOR:** If you provide sample sizes without systematic calculation, you have violated this workflow.

## Task Configuration

```yaml
elicit: true
template: study-design-tmpl.yaml
output: research-outputs/sample-size-calculation.md
requires:
  - research-brief.md
  - methodology-selection.md
data_dependencies:
  - statistical-power.md
  - sampling-methods.md
```

## Prerequisites

Before starting:
- Research methodology must be selected
- Research questions must be defined
- Population characteristics must be known
- Resource constraints must be identified
- Power requirements must be established

## Workflow Steps

### Phase 1: Research Type Classification
**ELICIT: true**

Determine the appropriate sample size approach based on research design:

**Research Type Analysis:**
- **Exploratory Qualitative**: Saturation-based approach
- **Descriptive Quantitative**: Population inference approach
- **Comparative Quantitative**: Power analysis approach
- **Mixed Methods**: Combined requirements approach
- **Specialized Methods**: Method-specific calculations

**Primary Research Questions:**
- What type of insight is needed?
- What level of precision is required?
- What is the target population?
- Are comparisons planned?
- What are the practical constraints?

**Statistical Inference Goals:**
```
Population Inference → Representative sampling needed
Pattern Detection → Saturation-based sampling
Hypothesis Testing → Power-based calculations
Effect Estimation → Precision-based calculations
Exploration → Purposive sampling adequate
```

Present research classification with sample size implications, then provide 1-9 elicitation options.

### Phase 2: Qualitative Sample Size Determination
**ELICIT: true**

For qualitative research methods, calculate sample requirements:

**Saturation-Based Calculation:**

**Method-Specific Guidelines:**
```
Interview Studies:
- Exploratory: 12-20 participants
- Phenomenological: 15-25 participants
- Grounded Theory: 20-30 participants
- Case Study: 4-10 cases

Focus Groups:
- Exploratory: 3-4 groups
- Segmented: 2-3 groups per segment
- Total participants: 24-36

Ethnographic Studies:
- Cultural analysis: 8-15 participants
- Organizational: 10-20 participants
- Digital ethnography: 15-30 participants

Diary Studies:
- Short-term (1 week): 15-25 participants
- Long-term (1 month): 10-20 participants
```

**Saturation Monitoring Framework:**
```
Theoretical Saturation Indicators:
- No new themes emerge (3 consecutive sessions)
- Categories are well-developed
- Relationships between concepts are clear
- Theory explains variations in data

Information Power Calculation:
High Power (smaller n needed):
✓ Narrow study aim
✓ Rich data quality
✓ Strong theory base
✓ Homogeneous sample

Low Power (larger n needed):
✓ Broad study aim
✓ Sparse data quality
✓ Weak theory base
✓ Heterogeneous sample
```

**Practical Minimum Calculations:**
```
Minimum Viable Sample (MVS):
Interviews: n = 6-8 (identifies 80% of themes)
Focus Groups: n = 2 groups (captures major themes)
Diary Studies: n = 5-7 (reveals primary patterns)

Confidence Buffer:
Add 30-50% to MVS for:
- First-time researchers
- Complex phenomena
- Diverse populations
- High stakes decisions
```

Present qualitative calculation with saturation plan, then provide 1-9 elicitation options.

### Phase 3: Quantitative Power Analysis
**ELICIT: true**

For quantitative research, perform statistical power calculations:

**Power Analysis Parameters:**
```
Standard Settings:
- Statistical Power (1-β): 0.80 (80%)
- Significance Level (α): 0.05 (5%)
- Effect Size: To be determined
- Test Type: One-tailed vs Two-tailed
```

**Effect Size Determination:**

**Cohen's d (Mean Differences):**
```
Small Effect: d = 0.2
- 10% improvement in satisfaction
- 0.5 point change on 7-point scale
- 15% reduction in task time

Medium Effect: d = 0.5
- 25% improvement in metrics
- 1.0 point change on 7-point scale
- 30% reduction in errors

Large Effect: d = 0.8
- 40% improvement in performance
- 1.5+ point change on scales
- 50% reduction in failure rates
```

**Sample Size Formulas:**

**Two-Group Comparison (t-test):**
```
n = 2σ²(Zα + Zβ)² / δ²

Where:
n = Sample size per group
σ = Population standard deviation
Zα = 1.96 (for α = 0.05, two-tailed)
Zβ = 0.84 (for power = 0.80)
δ = Minimum detectable difference

Quick Reference:
Small effect (d=0.2): n = 393 per group
Medium effect (d=0.5): n = 64 per group
Large effect (d=0.8): n = 26 per group
```

**Proportion Comparison:**
```
n = [p₁(1-p₁) + p₂(1-p₂)] × f(α,β) / (p₁-p₂)²

Where:
p₁, p₂ = Proportions to compare
f(0.05, 0.20) = 7.85 (standard values)

Example: 10% vs 15% conversion
n = [0.10×0.90 + 0.15×0.85] × 7.85 / (0.05)²
n = 858 per group
```

**Correlation Studies:**
```
n = [(Zα + Zβ) / C]² + 3

Where:
C = 0.5 × ln[(1+r)/(1-r)]

Quick Reference:
Small correlation (r=0.1): n = 782
Medium correlation (r=0.3): n = 84
Large correlation (r=0.5): n = 28
```

**ANOVA (Multiple Groups):**
```
One-Way ANOVA:
n = σ²(λ/k) / f²σ²

Where:
k = Number of groups
f = Effect size (0.1=small, 0.25=medium, 0.4=large)
λ = Non-centrality parameter

3 Groups, Medium Effect: n = 52 per group
4 Groups, Medium Effect: n = 45 per group
5 Groups, Medium Effect: n = 39 per group
```

Present power analysis with calculations, then provide 1-9 elicitation options.

### Phase 4: Survey Sample Size Planning
**ELICIT: true**

For survey research, calculate population-representative samples:

**Margin of Error Approach:**
```
n = Z²p(1-p) / e²

Where:
Z = 1.96 (95% confidence)
p = Expected proportion (0.5 if unknown)
e = Margin of error (typically 0.03 to 0.05)

Standard Calculations:
±3% margin: n = 1,067
±5% margin: n = 384
±10% margin: n = 96
```

**Finite Population Correction:**
```
n_adjusted = n × N / (n + N - 1)

Where:
n = Initial sample size
N = Population size

Population Effects:
N = 500: Reduces sample by ~30%
N = 1,000: Reduces sample by ~20%
N = 5,000: Reduces sample by ~5%
N = 50,000+: No meaningful reduction
```

**Subgroup Analysis Requirements:**
```
Minimum Subgroup Sizes:
Basic Analysis: n ≥ 30 per subgroup
Statistical Comparison: n ≥ 50 per subgroup
Regression Analysis: n ≥ 20 per predictor
Factor Analysis: n ≥ 100 total (5-10 per item)

Example Calculation:
4 demographic segments × 50 each = 200 base
Add 25% for dropout = 250 total needed
```

**Response Rate Adjustments:**
```
Adjusted Sample = Target Sample / Expected Response Rate

Typical Response Rates:
Email to customers: 25-40%
Email to prospects: 5-15%
Phone surveys: 10-30%
Panel surveys: 70-90%
In-person intercept: 30-60%

Example: Need n=400, expect 20% response
Recruit: 400 / 0.20 = 2,000 contacts
```

Present survey calculations with response planning, then provide 1-9 elicitation options.

### Phase 5: Mixed Methods Integration
**ELICIT: true**

For mixed methods research, integrate qualitative and quantitative requirements:

**Sequential Designs:**

**Exploratory Sequential (QUAL → quant):**
```
Phase 1 (Qualitative):
- Purpose: Develop constructs/hypotheses
- Sample: 15-25 interviews
- Outcome: Survey instrument

Phase 2 (Quantitative):
- Purpose: Test/validate findings
- Sample: Power analysis based
- Minimum: 200+ for validation

Integration Point:
Phase 1 findings inform Phase 2 sample size via:
- Effect size estimates from qualitative
- Subgroup identification
- Hypothesis specificity
```

**Explanatory Sequential (QUANT → qual):**
```
Phase 1 (Quantitative):
- Purpose: Identify patterns/relationships
- Sample: Full power analysis
- Minimum: 300+ for segmentation

Phase 2 (Qualitative):
- Purpose: Explain quantitative findings
- Sample: Purposive from Phase 1
- Size: 12-20 explaining outliers/patterns

Integration Point:
Phase 1 results determine Phase 2 sampling via:
- Extreme case selection
- Maximum variation sampling
- Typical case illustration
```

**Concurrent Designs:**

**Convergent Parallel (QUAL + QUANT):**
```
Simultaneous Data Collection:
Qualitative Component: 15-25 participants
Quantitative Component: 200+ participants

Integration Requirements:
- Same population sampled
- Comparable demographics
- Overlapping timeframe
- Joint analysis protocols

Sample Size Logic:
Qual: Saturation for depth
Quant: Power for breadth
Total: Larger of requirements
```

**Transformative Framework:**
```
Community-Based Participatory:
Community representatives: 8-12 co-researchers
Survey participants: 500+ community members
Interview participants: 25-40 diverse voices

Social Justice Focus:
Marginalized voices: Purposive 15-20
Dominant perspective: Random 200+
Integration: Equal weight in analysis
```

Present mixed methods plan with integration points, then provide 1-9 elicitation options.

### Phase 6: Special Population Considerations
**ELICIT: true**

Adjust calculations for challenging recruitment scenarios:

**Hard-to-Reach Populations:**

**Rare Populations (<5% prevalence):**
```
Screening Ratio Calculation:
Target n = 30 qualified participants
Population prevalence = 2%
Screening needed = 30 / 0.02 = 1,500 contacts

Cost Implications:
Screening cost: $5 × 1,500 = $7,500
Participant cost: $100 × 30 = $3,000
Total recruitment: $10,500

Efficiency Strategies:
- Referral bonuses: $25 per successful referral
- Community partnerships
- Snowball sampling adjustments
```

**Expert Panels (Delphi Method):**
```
Round 1 (Brainstorming): 15-25 experts
Round 2 (Rating): 80% retention (12-20)
Round 3 (Consensus): 70% retention (8-14)

Expert Definition:
- Minimum 5 years experience
- Recognized expertise in field
- Willingness for multiple rounds
- Geographic/organizational diversity

Consensus Criteria:
- 70% agreement threshold
- Interquartile range ≤ 1
- Stability across rounds
```

**Vulnerable Populations:**

**Ethical Sample Size Limits:**
```
Children (under 18):
- Maximum burden: 30 minutes
- Parental consent required
- Sample: Minimum needed only
- Typical: 15-20 for qualitative

Elderly (cognitive concerns):
- Shorter sessions: 20-30 minutes
- Higher dropout rates: 40%
- Over-recruit: 175% of target
- Frequent breaks needed

Medical Populations:
- IRB approval required
- Medical clearance needed
- Higher no-show rates: 50%
- Recruit: 200% of target
```

**B2B/Professional Sampling:**
```
Executive Interviews:
- C-level: 8-12 (access constraints)
- Director level: 12-18
- Manager level: 15-25
- Individual contributor: 20-30

Professional Survey:
- Industry specialists: 100-200
- General professionals: 300-500
- Response rates: 5-15%
- Recruit: 3,000-10,000 contacts

Recruitment Timeline:
- Initial outreach: 6-8 weeks
- Follow-up: 2-3 rounds
- Buffer time: 100% of estimate
```

Present special population adjustments with feasibility assessment, then provide 1-9 elicitation options.

### Phase 7: Resource and Feasibility Constraints
**ELICIT: true**

Integrate practical limitations with statistical ideals:

**Budget Constraint Analysis:**

**Cost-Per-Participant Calculation:**
```
Recruitment Costs:
Advertising/outreach: $10-50 per qualified
Screening: $5-15 per qualified
Scheduling: $10-25 per scheduled

Data Collection Costs:
Incentives: $50-200 per participant
Interviewer time: $50-150 per session
Technology/space: $10-30 per session
Analysis time: $100-300 per participant

Total Per-Participant: $235-770

Budget-Sample Trade-off:
$10,000 budget ÷ $400 per participant = 25 participants
$25,000 budget ÷ $400 per participant = 62 participants
$50,000 budget ÷ $400 per participant = 125 participants
```

**Timeline Constraint Analysis:**
```
Recruitment Timeline:
Consumer panels: 1-2 weeks
General population: 3-4 weeks
Professional/B2B: 6-8 weeks
Specialized populations: 8-12 weeks

Data Collection Timeline:
Surveys: 1-2 weeks
Interviews (20 participants): 3-4 weeks
Focus groups: 2-3 weeks
Diary studies: 4-6 weeks (including study period)

Analysis Timeline:
Quantitative: 1-2 weeks
Qualitative: 3-4 weeks
Mixed methods: 4-6 weeks

Total Project Timeline:
Minimum viable: 8-10 weeks
Standard thorough: 12-16 weeks
Comprehensive: 20-24 weeks
```

**Sample Size Compromise Strategies:**

**When Sample Size Must Be Reduced:**
```
Statistical Compromises:
Increase α to 0.10 (reduces n by ~20%)
Reduce power to 0.70 (reduces n by ~25%)
Focus on larger effects only
Use one-tailed tests (reduces n by ~20%)

Methodological Adaptations:
Within-subjects design (halves n needed)
Matching participants (reduces n by 20-30%)
Covariates in analysis (increases power)
Bayesian approaches (smaller n adequate)

Quality Enhancements:
More careful recruitment (reduce noise)
Better measurement instruments (reduce error)
Pilot testing to refine approach
Multiple smaller studies vs one large
```

**Minimum Viable Study Calculations:**
```
Qualitative Minimum:
6-8 interviews (captures 80% of themes)
Risk: May miss important themes
Mitigation: Follow-up study if needed

Quantitative Minimum:
n = 30 per group (CLT applies)
Risk: Low power for small effects
Mitigation: Focus on medium+ effects only

Survey Minimum:
n = 100 (basic descriptives reliable)
Risk: Large confidence intervals
Mitigation: Report uncertainty clearly
```

Present resource-constrained options with risk assessment, then provide 1-9 elicitation options.

## Statistical Calculation Tools

### Manual Calculation Formulas

**Two-Sample t-test:**
```
n = 2σ²(t_α + t_β)² / (μ₁ - μ₂)²

Simplified with Cohen's d:
n = 2(t_α + t_β)² / d²

For α=0.05, power=0.80:
n = 15.68 / d²

Examples:
d = 0.2: n = 392 per group
d = 0.5: n = 63 per group
d = 0.8: n = 25 per group
```

**One-Sample t-test:**
```
n = σ²(t_α + t_β)² / (μ - μ₀)²

For α=0.05, power=0.80:
n = 7.84 / d²

Examples:
d = 0.3: n = 87
d = 0.6: n = 22
d = 0.9: n = 10
```

**Chi-Square Test:**
```
n = (Z_α + Z_β)² / φ²

Where φ = effect size

Small effect (φ=0.1): n = 785
Medium effect (φ=0.3): n = 87
Large effect (φ=0.5): n = 31
```

### Recommended Software Tools

**Free Options:**
- G*Power: Comprehensive power analysis
- R pwr package: Scriptable calculations
- Online calculators: Quick estimates

**Professional Options:**
- PASS: Specialized power software
- SAS/SPSS: Built-in procedures
- Stata: Power and sample size commands

**Calculation Validation:**
Always verify calculations with:
1. Second software tool
2. Hand calculation check
3. Literature comparison
4. Expert consultation for complex designs

## Decision Framework Matrix

### Sample Size Decision Tree

```
Start: What is your research goal?
├── [Explore phenomenon]
│   ├── Rich understanding needed? → 20-25 interviews
│   ├── Basic themes sufficient? → 12-15 interviews
│   └── Quick insights only? → 6-8 interviews
│
├── [Describe population]
│   ├── High precision needed? → ±3% margin (n=1,067)
│   ├── Moderate precision OK? → ±5% margin (n=384)
│   └── Rough estimates sufficient? → ±10% margin (n=96)
│
├── [Compare groups]
│   ├── Small differences important? → High power calculation
│   ├── Medium differences expected? → Standard power
│   └── Large differences only? → Lower power acceptable
│
└── [Predict outcomes]
    ├── Many predictors? → n ≥ 20 per predictor
    ├── Few predictors? → n ≥ 100 minimum
    └── Single predictor? → Correlation power analysis
```

### Quality vs. Quantity Trade-offs

**When to Prioritize Sample Size:**
- Population inference required
- Small effects are important
- Regulatory/publication standards
- High-stakes decisions
- Subgroup analyses planned

**When to Prioritize Sample Quality:**
- Exploratory research
- Hard-to-reach populations
- Complex phenomena
- Rich contextual understanding
- Resource constraints severe

## Output Specifications

### Sample Size Calculation Report

```yaml
sample_size_report:
  study_overview:
    research_type: [qualitative/quantitative/mixed]
    methodology: [interviews/survey/experiment/etc]
    population: [description]
    constraints: [budget/time/access]

  calculations:
    primary_analysis:
      method: [specific statistical test]
      assumptions:
        effect_size: [value and justification]
        power: [typically 0.80]
        alpha: [typically 0.05]
        test_type: [one/two-tailed]
      result:
        sample_size: [n per group]
        total_sample: [overall n]
        confidence: [95% CI for estimate]

    secondary_analyses:
      subgroup_analysis:
        minimum_per_group: [number]
        total_additional: [number]
      exploratory_analysis:
        anticipated_tests: [number]
        alpha_adjustment: [method]

  practical_considerations:
    recruitment:
      target_sample: [final n needed]
      over_recruitment: [percentage buffer]
      recruitment_goal: [total to contact]
      expected_response_rate: [percentage]

    timeline:
      recruitment_weeks: [estimate]
      data_collection_weeks: [estimate]
      buffer_weeks: [contingency]

    budget:
      cost_per_participant: [amount]
      recruitment_costs: [amount]
      total_budget_needed: [amount]

  quality_assurance:
    power_sensitivity:
      minimum_detectable_effect: [if n reduced]
      power_if_reduced: [actual power with constraints]
    assumptions_tested:
      normality_plan: [how to check]
      outlier_plan: [how to handle]
      missing_data_plan: [how to address]

  recommendations:
    final_sample_size: [recommended n]
    rationale: [justification]
    risks: [what could go wrong]
    mitigations: [how to address risks]
    alternatives: [if constraints change]
```

## Integration with Study Design

**Data Flow to Study Design:**
- Confirmed sample size feeds participant recruitment plan
- Power analysis informs data collection timeline
- Resource calculations guide budget allocation
- Quality requirements inform screening criteria

**Validation Checkpoints:**
- Sample size meets research objectives
- Budget supports calculated sample
- Timeline accommodates recruitment needs
- Analysis plan matches sample size

## Quality Checkpoints

Before finalizing sample size:
- ✓ Calculations verified with second method
- ✓ Effect sizes are realistic and justified
- ✓ Power requirements meet study goals
- ✓ Sample size is feasible given constraints
- ✓ Recruitment plan supports target n
- ✓ Budget accommodates actual costs
- ✓ Timeline includes adequate buffers
- ✓ Ethical considerations addressed
- ✓ Alternative plans for if recruitment fails

## CRITICAL REMINDERS

**❌ NEVER:**
- Use rule-of-thumb without calculation
- Ignore practical constraints in planning
- Proceed without effect size justification
- Skip pilot testing for recruitment estimates
- Assume 100% participation rates
- Use sample sizes from other studies without validation
- Forget to account for dropout/attrition

**✅ ALWAYS:**
- Calculate based on specific research needs
- Include recruitment buffer (25-50%)
- Document all assumptions and rationale
- Plan for multiple scenarios (best/worst case)
- Consider ethical minimums for vulnerable populations
- Validate with pilot data when possible
- Prepare alternative plans if recruitment lags