# Statistical Power & Sample Size Calculation Guide

## Overview

This guide provides comprehensive information on statistical power analysis and sample size calculations for user research. It covers both traditional hypothesis testing and practical applications for UX research, A/B testing, and survey design.

## Table of Contents

1. [Statistical Power Fundamentals](#statistical-power-fundamentals)
2. [Sample Size Formulas](#sample-size-formulas)
3. [Effect Size Guidelines](#effect-size-guidelines)
4. [Power Analysis Tools](#power-analysis-tools)
5. [A/B Testing Calculations](#ab-testing-calculations)
6. [Survey Sample Sizes](#survey-sample-sizes)
7. [Qualitative Saturation](#qualitative-saturation)
8. [Practical Applications](#practical-applications)

---

## Statistical Power Fundamentals

### Key Concepts

**Statistical Power:** Probability of detecting an effect if it truly exists
- Standard target: 80% (0.80)
- High-stakes research: 90% (0.90)
- Exploratory research: 70% (0.70) acceptable

**Type I Error (α):** False positive rate
- Standard: 5% (0.05)
- Conservative: 1% (0.01)
- Exploratory: 10% (0.10)

**Type II Error (β):** False negative rate
- Related to power: Power = 1 - β
- Standard: 20% (0.20) when power = 0.80

**Effect Size:** Magnitude of the difference
- Small: d = 0.2, r = 0.1, f² = 0.02
- Medium: d = 0.5, r = 0.3, f² = 0.15
- Large: d = 0.8, r = 0.5, f² = 0.35

### The Power Relationship

```
Sample Size ↑ → Power ↑
Effect Size ↑ → Power ↑
Alpha (α) ↑ → Power ↑
Variance ↓ → Power ↑
```

### When Power Analysis is Needed

**A Priori (Planning):**
- Determine sample size before study
- Most common and recommended
- Prevents underpowered studies

**Post Hoc (After Study):**
- Calculate achieved power
- Explain null findings
- Generally discouraged

**Sensitivity:**
- Minimum detectable effect given n
- Useful for fixed sample constraints

**Criterion:**
- Optimal alpha level given other parameters
- Rarely used in practice

---

## Sample Size Formulas

### Comparing Two Means (T-Test)

**Independent Samples:**
```
n = 2 × [(Zα + Zβ)² × σ²] / δ²

Where:
n = Sample size per group
Zα = Z-score for significance level (1.96 for α=0.05, two-tailed)
Zβ = Z-score for power (0.84 for power=0.80)
σ = Population standard deviation
δ = Minimum detectable difference
```

**Simplified with Effect Size:**
```
n = 2 × [(Zα + Zβ)² / d²]

Where:
d = Cohen's d (effect size)
```

**Quick Reference Table:**
```
Effect Size | α=0.05, Power=0.80 | α=0.05, Power=0.90
Small (0.2) | 393 per group      | 526 per group
Medium (0.5)| 64 per group       | 85 per group
Large (0.8) | 26 per group       | 35 per group
```

### Comparing Proportions

**Two Proportions:**
```
n = [(Zα√(2p̄q̄) + Zβ√(p₁q₁ + p₂q₂))²] / (p₁ - p₂)²

Where:
p̄ = (p₁ + p₂)/2
q̄ = 1 - p̄
q₁ = 1 - p₁
q₂ = 1 - p₂
```

**Conversion Rate Example:**
```
Current rate: 10% (p₁ = 0.10)
Target rate: 12% (p₂ = 0.12)
Absolute difference: 2%
Relative improvement: 20%

n = 3,842 per group (α=0.05, power=0.80)
```

### Correlation

**Sample Size for Correlation:**
```
n = [(Zα + Zβ) / C]² + 3

Where:
C = 0.5 × ln[(1+r)/(1-r)]  (Fisher's Z transformation)
```

**Quick Reference:**
```
Correlation | α=0.05, Power=0.80 | α=0.05, Power=0.90
r = 0.1     | 782                | 1046
r = 0.3     | 84                 | 112
r = 0.5     | 28                 | 37
```

### ANOVA (Multiple Groups)

**One-Way ANOVA:**
```
n = (σ² / f²) × (λ / k)

Where:
k = Number of groups
f = Effect size
λ = Non-centrality parameter (from tables)
```

**Effect Size for ANOVA:**
```
f = √[Σ(μᵢ - μ)² / kσ²]
```

---

## Effect Size Guidelines

### Cohen's d (Mean Differences)

**Calculation:**
```
d = (M₁ - M₂) / SDpooled
```

**Interpretation:**
```
Small:  d = 0.2  (shifts overlap by 85%)
Medium: d = 0.5  (shifts overlap by 67%)
Large:  d = 0.8  (shifts overlap by 53%)
```

**Practical Examples:**
- User satisfaction: 0.5 point on 7-point scale ≈ d = 0.3
- Task completion time: 20% reduction ≈ d = 0.5
- Error rate: 50% reduction ≈ d = 0.8

### Correlation Coefficient (r)

**Interpretation:**
```
Small:  r = 0.10  (1% variance explained)
Medium: r = 0.30  (9% variance explained)
Large:  r = 0.50  (25% variance explained)
```

**UX Research Context:**
- Usability-Satisfaction: r = 0.4-0.6 typical
- Time-Errors: r = 0.3-0.5 typical
- Experience-Retention: r = 0.2-0.4 typical

### Minimum Practical Effect

**Setting Meaningful Thresholds:**
```
Metric              | Minimum Practical Difference
Task Success Rate   | 10-15 percentage points
Task Time          | 20-30% reduction
Error Rate         | 30-50% reduction
SUS Score          | 5-10 points
NPS                | 10-15 points
Conversion Rate    | Relative 5-10%
```

---

## Power Analysis Tools

### Free Calculators

**G*Power (Recommended):**
- Download: [gpower.hhu.de](http://www.gpower.hhu.de)
- Supports: All major tests
- Features: Graphs, sensitivity analysis

**Online Calculators:**
1. **Evan's Awesome A/B Tools:** [evanmiller.org](https://www.evanmiller.org/ab-testing/)
2. **Optimizely Sample Size:** [optimizely.com](https://www.optimizely.com/sample-size-calculator/)
3. **SurveyMonkey Calculator:** [surveymonkey.com](https://www.surveymonkey.com/mp/sample-size-calculator/)

### R Packages

**pwr Package:**
```R
library(pwr)

# T-test
pwr.t.test(d=0.5, power=0.8, sig.level=0.05)

# Proportion test
pwr.2p.test(h=ES.h(0.12, 0.10), power=0.8)

# Correlation
pwr.r.test(r=0.3, power=0.8)

# ANOVA
pwr.anova.test(k=4, f=0.25, power=0.8)
```

### Python Libraries

**statsmodels:**
```python
from statsmodels.stats.power import TTestPower

# Calculate sample size
analysis = TTestPower()
n = analysis.solve_power(
    effect_size=0.5,
    power=0.8,
    alpha=0.05
)
```

**pingouin:**
```python
import pingouin as pg

# Sample size for t-test
n = pg.power_ttest(
    d=0.5,
    power=0.8,
    alpha=0.05
)
```

---

## A/B Testing Calculations

### Basic A/B Test

**Sample Size Formula:**
```
n = 16σ² / δ²  (for 80% power, 5% significance)
n = 21σ² / δ²  (for 90% power, 5% significance)
```

**Conversion Rate Testing:**
```
n = (p₁(1-p₁) + p₂(1-p₂)) × f(α,β) / (p₁-p₂)²

Where:
f(0.05, 0.20) = 7.85  (α=5%, power=80%)
f(0.05, 0.10) = 10.51 (α=5%, power=90%)
```

### Minimum Detectable Effect (MDE)

**Given Fixed Sample Size:**
```
MDE = √[(σ₁² + σ₂²)/n] × (Zα + Zβ)
```

**For Proportions:**
```
MDE = (Zα + Zβ) × √[p(1-p)(1/n₁ + 1/n₂)]
```

### Sequential Testing

**Optimizely's Stats Engine:**
- Always valid p-values
- No need to pre-specify sample size
- Automatically adjusts for peeking

**Evan Miller's Simple Sequential:**
```
Continue if: -4 < Z < 2.25
Stop for effect if: Z ≥ 2.25
Stop for null if: Z ≤ -4
```

### Multi-Armed Bandits

**Thompson Sampling:**
- Balances exploration and exploitation
- No fixed sample size
- Adaptive allocation

**Sample Size Multiplier:**
- 3 variants: 1.4× two-arm sample
- 4 variants: 1.7× two-arm sample
- 5 variants: 2.0× two-arm sample

---

## Survey Sample Sizes

### Population-Based Sampling

**Finite Population Correction:**
```
n = N × n₀ / (N + n₀ - 1)

Where:
n₀ = Initial sample size (infinite population)
N = Population size
```

**Quick Reference Table:**
```
Population | ±3% Margin | ±5% Margin | ±10% Margin
100        | 92         | 80         | 50
500        | 341        | 217        | 81
1,000      | 516        | 278        | 88
5,000      | 879        | 357        | 94
10,000     | 964        | 370        | 95
50,000     | 1,045      | 381        | 96
100,000+   | 1,067      | 384        | 96
```

### Subgroup Analysis

**Minimum Subgroup Sizes:**
```
Analysis Type          | Minimum n | Recommended n
Basic descriptives     | 10        | 30
Means comparison       | 30        | 50
Regression (per IV)    | 10        | 20
Factor analysis        | 100       | 200
```

**Stratified Sampling:**
```
Total n = Σ(Nₕ × sₕ)² / (N²D + Σ Nₕsₕ²)

Where:
Nₕ = Stratum population
sₕ = Stratum standard deviation
D = B²/4 (B = margin of error)
```

### Response Rate Adjustments

**Adjusted Sample Size:**
```
n_adjusted = n_target / expected_response_rate
```

**Typical Response Rates:**
```
Method              | Response Rate | Adjustment Factor
Email (cold)        | 10-20%       | 5-10×
Email (customer)    | 20-40%       | 2.5-5×
Phone              | 10-30%       | 3-10×
In-person intercept | 30-50%       | 2-3×
Panel              | 70-90%       | 1.1-1.4×
```

---

## Qualitative Saturation

### Saturation Guidelines

**By Method:**
```
Method          | Saturation Point | Recommended n
Interviews      | 12-15           | 20-30
Focus Groups    | 3-4 groups      | 4-6 groups
Ethnography     | 6-8 cases       | 10-15 cases
Diary Studies   | 10-12           | 15-20
Usability Tests | 5               | 8-12
```

### Saturation Monitoring

**New Information Curve:**
```
Interviews 1-6:   80% of themes
Interviews 7-12:  15% new themes
Interviews 13-18: 4% new themes
Interviews 19-24: <1% new themes
```

**Stopping Rules:**
- 3 consecutive interviews with no new themes
- <5% new codes in last 25% of sample
- Theoretical saturation achieved

### Mixed Methods Integration

**Sequential Design:**
```
Qual Phase: n = 20 (saturation)
    ↓
Quant Phase: n = 200 (validation)
```

**Concurrent Design:**
```
Qual: n = 20 (depth)
  +
Quant: n = 200 (breadth)
  =
Integrated: Comprehensive understanding
```

---

## Practical Applications

### UX Research Scenarios

**Usability Testing:**
```
Formative: n = 5-8 (finds 85% of issues)
Summative: n = 20+ (statistical comparison)
Comparative: n = 12-15 per design
```

**Card Sorting:**
```
Open sorting: n = 15-30
Closed sorting: n = 30-50
Tree testing: n = 50+
```

**Prototype Testing:**
```
Concept validation: n = 12-20
A/B preference: n = 30-50 per variant
Quantitative metrics: n = 50-100
```

### Business Metrics

**Conversion Rate Optimization:**
```
Current: 2%, Target: 2.5% (25% relative)
n = 6,300 per variant (80% power)
n = 8,400 per variant (90% power)
```

**NPS Studies:**
```
Detect 10-point change:
n = 400 (80% power)
n = 540 (90% power)
```

**Customer Satisfaction:**
```
Detect 0.5 point on 7-point scale:
n = 100 per group (d = 0.4)
```

### Time and Budget Constraints

**Fixed Budget Scenario:**
```
Budget: $10,000
Cost per participant: $100
Max n: 100

Power analysis:
Can detect d = 0.4 (medium) with 80% power
Can detect r = 0.28 with 80% power
```

**Fixed Timeline Scenario:**
```
Timeline: 2 weeks
Recruitment rate: 10/day
Max n: 100 (with weekends)

Achievable:
- Qualitative: Full saturation
- Quantitative: Medium effects detectable
```

---

## Quick Decision Tools

### Sample Size Decision Tree

```
Start: What type of research?
├── [Quantitative Comparison]
│   ├── Known variance? → Use exact formula
│   ├── Effect size known? → Use Cohen's d tables
│   └── Proportion data? → Use proportion calculator
│
├── [Survey Research]
│   ├── Population inference? → Use margin of error
│   ├── Subgroup analysis? → Multiply by groups
│   └── Just descriptive? → n = 100-200
│
├── [A/B Testing]
│   ├── Conversion rate? → Use Optimizely calculator
│   ├── Continuous metric? → Use t-test formula
│   └── Multiple variants? → Adjust for comparisons
│
└── [Qualitative]
    ├── Interviews? → 15-25 for saturation
    ├── Usability? → 5-8 for issues
    └── Mixed methods? → Both qual and quant needs
```

### Power Analysis Checklist

Before calculating:
- [ ] Define primary outcome measure
- [ ] Determine meaningful effect size
- [ ] Set significance level (usually 0.05)
- [ ] Choose power level (usually 0.80)
- [ ] Consider one vs. two-tailed test
- [ ] Account for attrition/dropout
- [ ] Plan for subgroup analyses
- [ ] Budget for pilot testing

### Common Mistakes to Avoid

1. **Post-hoc power analysis** - Circular reasoning
2. **Ignoring clustered data** - Underestimates sample size
3. **Multiple comparisons** - Increases Type I error
4. **Unrealistic effect sizes** - Underpowered studies
5. **No pilot data** - Poor variance estimates
6. **Ignoring dropout** - Final n too small
7. **Ceiling/floor effects** - Reduced power
8. **Unequal groups** - Reduces efficiency

---

## Formulas Reference Card

### Essential Formulas

**Mean Comparison:**
```
n = 2σ²(Zα + Zβ)² / δ²
```

**Proportion Comparison:**
```
n = [p₁(1-p₁) + p₂(1-p₂)](Zα + Zβ)² / (p₁-p₂)²
```

**Correlation:**
```
n = [(Zα + Zβ)/C]² + 3
C = 0.5 × ln[(1+r)/(1-r)]
```

**Survey Margin of Error:**
```
n = Z²p(1-p) / e²
```

### Quick Multipliers

**From Two-Group to Multi-Group:**
- 3 groups: ×1.2
- 4 groups: ×1.4
- 5 groups: ×1.6

**Adjusting for Dropout:**
- 10% dropout: ×1.11
- 20% dropout: ×1.25
- 30% dropout: ×1.43

**Unequal Group Sizes:**
- 2:1 ratio: ×1.125
- 3:1 ratio: ×1.33
- 4:1 ratio: ×1.56

---

## Resources & References

### Books
1. Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences
2. Lipsey, M. W. (1990). Design Sensitivity
3. Murphy, K. R., Myors, B., & Wolach, A. (2014). Statistical Power Analysis

### Online Tools
1. G*Power: www.gpower.hhu.de
2. PowerUpR: powerupr.shinyapps.io
3. Russ Lenth's Power: stat.uiowa.edu/~rlenth/Power

### Papers
1. Lakens, D. (2022). Sample Size Justification
2. Button, K. S. et al. (2013). Power failure: Why small sample size undermines reliability
3. Sauro, J. & Lewis, J. R. (2016). Quantifying the User Experience