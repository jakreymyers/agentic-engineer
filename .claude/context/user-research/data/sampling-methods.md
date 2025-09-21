# Sampling Methods Reference Guide

## Overview

This guide provides comprehensive information on sampling methods for user research, including when to use each method, how to implement them, and sample size calculations.

## Table of Contents

1. [Sampling Fundamentals](#sampling-fundamentals)
2. [Probability Sampling Methods](#probability-sampling-methods)
3. [Non-Probability Sampling Methods](#non-probability-sampling-methods)
4. [Sample Size Determination](#sample-size-determination)
5. [Recruitment Strategies](#recruitment-strategies)
6. [Quota Management](#quota-management)
7. [Common Challenges](#common-challenges)

---

## Sampling Fundamentals

### Key Concepts

**Population:** The entire group you want to study
**Sample:** The subset of the population you actually study
**Sampling Frame:** The list from which you draw your sample
**Sampling Unit:** Individual elements in the population
**Sampling Error:** Difference between sample and population characteristics

### Representativeness vs. Depth

```
Representativeness ←→ Depth Trade-off
├── Large samples → Statistical generalization
├── Random selection → Population inference
└── Quantitative focus → Measurable patterns

vs.

├── Small samples → Rich insights
├── Purposeful selection → Theoretical insights
└── Qualitative focus → Deep understanding
```

### Sampling Decision Framework

1. **Research Questions**
   - Exploratory → Purposive/Convenience sampling
   - Descriptive → Stratified/Quota sampling
   - Explanatory → Random/Systematic sampling

2. **Resources Available**
   - Limited budget → Convenience/Snowball
   - Limited time → Convenience/Purposive
   - Limited access → Snowball/Respondent-driven

3. **Required Precision**
   - High precision → Probability sampling
   - Directional insights → Non-probability acceptable

---

## Probability Sampling Methods

### Simple Random Sampling

**Definition:** Every member has equal chance of selection

**When to Use:**
- Population is homogeneous
- Complete sampling frame available
- Statistical inference required
- No subgroup analysis needed

**Implementation:**
```
1. Define population precisely
2. Create complete sampling frame
3. Assign unique numbers to each unit
4. Use random number generator
5. Select n units
```

**Sample Size Formula:**
```
n = (Z²p(1-p))/e²

Where:
Z = Z-score (1.96 for 95% confidence)
p = Expected proportion (use 0.5 if unknown)
e = Margin of error (typically 0.05)
```

**Example Calculation:**
- 95% confidence, 5% margin of error, unknown proportion
- n = (1.96²×0.5×0.5)/0.05² = 384

---

### Systematic Random Sampling

**Definition:** Select every kth element after random start

**When to Use:**
- Large populations
- Ordered sampling frame exists
- No periodic patterns in frame
- Simpler than simple random

**Implementation:**
```
1. Determine sampling interval: k = N/n
2. Random start between 1 and k
3. Select every kth element
4. Continue through entire frame
```

**Advantages:**
- Easier to implement than simple random
- Ensures spread across frame
- Can be done without full frame upfront

**Watch Out For:**
- Periodicity in sampling frame
- Hidden patterns that align with interval

---

### Stratified Random Sampling

**Definition:** Divide population into strata, random sample from each

**When to Use:**
- Distinct subgroups exist
- Subgroup comparisons needed
- Improve precision over simple random
- Ensure minority representation

**Types:**
1. **Proportionate:** Sample size proportional to stratum size
2. **Disproportionate:** Equal samples per stratum
3. **Optimal:** Sample size based on stratum variability

**Implementation:**
```
1. Identify stratification variables
2. Define mutually exclusive strata
3. Determine sample size per stratum
4. Random sample within each stratum
5. Weight if disproportionate
```

**Sample Size per Stratum:**
```
Proportionate: n_h = (N_h/N) × n
Disproportionate: n_h = n/H
Optimal: n_h = n × (N_h×S_h)/(ΣN_h×S_h)

Where:
N_h = Stratum population
S_h = Stratum standard deviation
H = Number of strata
```

---

### Cluster Sampling

**Definition:** Divide population into clusters, randomly select clusters

**When to Use:**
- Geographic dispersion
- No complete sampling frame
- Cost constraints
- Natural groupings exist

**Types:**
1. **Single-stage:** Sample all units in selected clusters
2. **Two-stage:** Sample clusters, then sample within clusters
3. **Multi-stage:** Multiple levels of clustering

**Implementation:**
```
1. Define clusters (schools, neighborhoods, etc.)
2. Create cluster frame
3. Randomly select clusters
4. Sample within clusters (if multi-stage)
5. Adjust for design effect
```

**Design Effect:**
```
DEFF = 1 + (m-1)×ρ

Where:
m = Average cluster size
ρ = Intraclass correlation
```

---

## Non-Probability Sampling Methods

### Convenience Sampling

**Definition:** Sample whoever is easily accessible

**When to Use:**
- Pilot studies
- Exploratory research
- Resource constraints severe
- Quick directional insights

**Implementation:**
```
1. Define inclusion criteria
2. Identify accessible locations/channels
3. Recruit until target reached
4. Document sample characteristics
```

**Limitations:**
- No statistical generalization
- High bias risk
- Limited external validity

**Quality Improvements:**
- Multiple recruitment sites
- Varied times of data collection
- Clear inclusion/exclusion criteria
- Document sample limitations

---

### Purposive (Judgment) Sampling

**Definition:** Deliberately select information-rich cases

**When to Use:**
- Qualitative research
- Expert opinions needed
- Specific characteristics required
- Theory development

**Types:**
1. **Maximum Variation:** Diverse cases
2. **Homogeneous:** Similar cases for focus
3. **Typical Case:** Representative examples
4. **Extreme Case:** Outliers and exceptions
5. **Critical Case:** If true here, true everywhere
6. **Expert Sampling:** Domain expertise required

**Implementation:**
```
1. Define selection criteria clearly
2. Identify information-rich cases
3. Select purposefully
4. Document selection rationale
5. Continue until saturation
```

**Saturation Guidelines:**
- Interviews: 12-15 typically sufficient
- Focus groups: 3-5 groups
- Ethnography: 8-12 cases
- Monitor for new themes

---

### Snowball Sampling

**Definition:** Participants recruit other participants

**When to Use:**
- Hard-to-reach populations
- Hidden populations
- Sensitive topics
- Trust required for participation
- No sampling frame exists

**Implementation:**
```
1. Identify initial seeds (2-3)
2. Interview/survey seeds
3. Ask for referrals
4. Screen referrals
5. Continue chains
6. Monitor diversity
```

**Chain Management:**
- Track referral chains
- Limit chain length (3-4 waves)
- Multiple seeds for diversity
- Incentivize referrals carefully

**Respondent-Driven Sampling (RDS):**
- Advanced snowball variant
- Weighted for network properties
- Can approximate probability sample
- Requires special analysis

---

### Quota Sampling

**Definition:** Non-random sampling to fill predetermined quotas

**When to Use:**
- Ensure demographic representation
- Market research standard
- Quick and cost-effective
- Approximate representativeness

**Implementation:**
```
1. Define quota variables (age, gender, etc.)
2. Set quota targets (match population)
3. Recruit convenience until quotas filled
4. Monitor quota progress
5. Close filled quotas
```

**Quota Matrix Example:**
```
| Age    | Male | Female | Total |
|--------|------|--------|-------|
| 18-34  | 25   | 25     | 50    |
| 35-54  | 30   | 30     | 60    |
| 55+    | 20   | 20     | 40    |
| Total  | 75   | 75     | 150   |
```

---

### Theoretical Sampling

**Definition:** Sampling to develop theory (grounded theory)

**When to Use:**
- Theory development
- Concept refinement
- Category saturation
- Grounded theory studies

**Process:**
```
1. Initial sampling (open)
2. Analyze data
3. Identify emerging concepts
4. Sample to develop concepts
5. Continue until theoretical saturation
```

**Saturation Indicators:**
- No new concepts emerging
- Categories well-developed
- Relationships established
- Theory explains data well

---

## Sample Size Determination

### Quantitative Sample Sizes

**Survey Research:**
```
Confidence Level | Margin of Error | Population Size → Sample Size
95%             | ±5%             | 1,000 → 278
95%             | ±5%             | 10,000 → 370
95%             | ±5%             | 100,000 → 383
95%             | ±5%             | 1,000,000+ → 384

95%             | ±3%             | 1,000 → 516
95%             | ±3%             | 10,000 → 965
95%             | ±3%             | 100,000 → 1,056
95%             | ±3%             | 1,000,000+ → 1,067
```

**Subgroup Analysis:**
- Minimum 30 per subgroup for statistics
- Preferably 100+ per subgroup
- Consider smallest important subgroup

**Effect Size Detection:**
```
Effect Size | Power = 0.80 | Power = 0.90
Small (0.2) | 393/group    | 526/group
Medium (0.5)| 64/group     | 85/group
Large (0.8) | 26/group     | 35/group
```

### Qualitative Sample Sizes

**By Method:**
```
Method              | Typical Range | Saturation Point
Interviews          | 15-30         | 12-15
Focus Groups        | 3-5 groups    | 3-4 groups
Ethnography         | 8-15 cases    | 6-12
Case Studies        | 3-10 cases    | 4-6
Diary Studies       | 12-20         | 10-15
Usability Testing   | 5-8           | 5
```

**Saturation Monitoring:**
```
Interviews 1-6:    New themes = 80%
Interviews 7-12:   New themes = 15%
Interviews 13-18:  New themes = 5%
Interviews 19+:    New themes = <1%
```

---

## Recruitment Strategies

### Recruitment Channels

**Direct Recruitment:**
- Customer databases
- Email lists
- In-app/website intercepts
- Social media ads
- Professional panels
- University subject pools

**Indirect Recruitment:**
- Recruitment agencies
- Market research panels
- Craigslist/classifieds
- Professional associations
- Community organizations
- Snowball referrals

### Screening Best Practices

**Screening Funnel:**
```
1. Broad Outreach (1000s)
   ↓
2. Initial Interest (100s)
   ↓
3. Screening Survey (10s)
   ↓
4. Qualified Pool (2X target)
   ↓
5. Scheduled Participants (1.25X target)
   ↓
6. Completed Sessions (target)
```

**Over-recruitment Guidelines:**
- Interviews: Recruit 125% of target
- Focus Groups: Recruit 150% per group
- Surveys: Recruit 110% for online
- Diary Studies: Recruit 130% for completion

### Incentive Guidelines

**By Participant Type:**
```
Consumers:          $50-100/hour
Professionals:      $100-200/hour
Executives:         $200-500/hour
Specialized/Rare:   $150-300/hour
Students:           $25-50/hour
General Public:     $25-75/hour
```

**By Method:**
```
5-min survey:       $1-5
20-min survey:      $5-20
60-min interview:   $75-150
2-hr focus group:   $100-200
Week diary study:   $100-200
Usability test:     $50-100
```

---

## Quota Management

### Setting Quotas

**Demographic Quotas:**
- Match population census
- Or match target market
- Consider intersectionality
- Minimum cell sizes (n≥5)

**Behavioral Quotas:**
- Usage frequency
- Experience level
- Role/responsibility
- Customer segment

### Monitoring Systems

**Real-time Tracking:**
```
Dashboard Elements:
- Overall progress bar
- Quota cell status (open/closing/closed)
- Screener completion rate
- Qualification rate by source
- Time to quota completion estimate
```

**Quota Prioritization:**
1. Hard-to-reach segments first
2. Slow-filling quotas prioritized
3. Nested quotas (age within gender)
4. Soft quotas flexible

### Quota Challenges

**Common Issues:**
- One quota fills too fast
- Hard-to-reach quotas lag
- Intersectional quotas difficult
- Quality vs. quota pressure

**Solutions:**
- Adjust screener routing
- Increase incentives selectively
- Expand recruitment channels
- Relax non-critical quotas
- Use quota weighting in analysis

---

## Common Challenges

### Response Bias

**Types:**
- Selection bias: Who participates
- Non-response bias: Who doesn't
- Volunteer bias: Self-selection
- Survivorship bias: Dropouts

**Mitigation:**
- Multiple recruitment channels
- Incentives for participation
- Follow-up with non-responders
- Weight for non-response
- Document limitations

### Recruitment Difficulties

**Hard-to-Reach Populations:**
- Build trust through partners
- Use respondent-driven sampling
- Increase incentives
- Allow more time
- Consider remote methods

**Low Response Rates:**
- Personalize invitations
- Multiple reminders
- Simplify screening
- Test different messages
- Various channels

### Quality Control

**Participant Quality:**
- Attention checks in surveys
- Verification questions
- Behavioral consistency
- Professional respondent detection
- Post-session validation

**Sample Quality:**
- Monitor demographics
- Check against population
- Verify inclusion criteria
- Audit recruitment sources
- Statistical tests for bias

---

## Decision Trees

### Sampling Method Selection

```
Start: What is your research goal?
├── [Generalize to population]
│   ├── Have complete frame? → Simple Random
│   ├── Natural groups exist? → Cluster
│   └── Subgroups important? → Stratified
│
├── [Explore phenomenon]
│   ├── Specific expertise needed? → Expert
│   ├── Extreme cases valuable? → Extreme Case
│   └── Maximum diversity wanted? → Maximum Variation
│
└── [Access challenges]
    ├── Hidden population? → Snowball/RDS
    ├── Geographic dispersion? → Cluster
    └── Time/cost constraints? → Convenience/Quota
```

### Sample Size Decision

```
Start: Qualitative or Quantitative?
├── [Quantitative]
│   ├── Population inference? → Power analysis
│   ├── Subgroup analysis? → Min 30-100 per group
│   └── Description only? → 100-200 total
│
└── [Qualitative]
    ├── Interviews? → 12-30 (saturation)
    ├── Focus groups? → 3-5 groups
    └── Ethnography? → 8-15 cases
```

---

## Quick Reference Tables

### Sample Size Quick Guide

| Research Type | Method | Minimum | Typical | Robust |
|--------------|--------|---------|---------|---------|
| Exploratory | Interviews | 8 | 15 | 25 |
| Descriptive | Survey | 100 | 300 | 500 |
| Evaluative | Usability | 5 | 8 | 12 |
| Comparative | A/B Test | 100/group | 500/group | 1000/group |
| Ethnographic | Observation | 5 | 10 | 15 |

### Recruitment Timeline Guide

| Method | Recruitment Time | Buffer Needed |
|--------|-----------------|---------------|
| Survey (online) | 1-2 weeks | 25% |
| Interviews | 2-3 weeks | 50% |
| Focus Groups | 2-4 weeks | 75% |
| Diary Study | 3-4 weeks | 50% |
| B2B/Enterprise | 4-6 weeks | 100% |

### Cost Estimation Guide

| Component | Low | Medium | High |
|-----------|-----|--------|------|
| Recruitment | $20/participant | $50/participant | $150/participant |
| Incentives | $25/session | $75/session | $200/session |
| Panel Costs | $5/complete | $15/complete | $50/complete |
| Screening | $2/complete | $5/complete | $10/complete |

---

## References & Further Reading

1. **Probability Sampling:**
   - Cochran, W. G. (1977). Sampling Techniques
   - Lohr, S. (2019). Sampling: Design and Analysis

2. **Qualitative Sampling:**
   - Patton, M. Q. (2015). Qualitative Research Methods
   - Guest, G. et al. (2006). How Many Interviews Are Enough?

3. **Mixed Methods:**
   - Teddlie & Yu (2007). Mixed Methods Sampling
   - Onwuegbuzie & Collins (2007). Sampling Designs

4. **Online Research:**
   - Callegaro et al. (2015). Web Survey Methodology
   - Tourangeau et al. (2013). Hard-to-Survey Populations