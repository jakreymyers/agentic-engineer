# Statistical Tests Reference Guide

## Overview

This guide provides a comprehensive reference for selecting and interpreting statistical tests commonly used in user research. Each test includes assumptions, use cases, and interpretation guidelines.

## Test Selection Framework

### Key Questions for Test Selection

1. **What type of research question?**
   - Difference between groups
   - Relationship between variables
   - Prediction of outcomes
   - Change over time

2. **What type of variables?**
   - Independent: Continuous, Ordinal, Nominal
   - Dependent: Continuous, Ordinal, Nominal

3. **How many groups/variables?**
   - Two groups vs. multiple groups
   - One variable vs. multiple variables

4. **What's the data structure?**
   - Independent samples
   - Paired/repeated measures
   - Nested/hierarchical

## Parametric Tests

### T-Tests

#### Independent Samples T-Test

**Purpose:** Compare means between two independent groups

**Assumptions:**
- Continuous dependent variable
- Independent observations
- Normal distribution (or n>30)
- Equal variances (use Welch's if violated)

**When to Use:**
- Comparing two user groups
- A/B testing
- Pre/post with different participants

**Formula:**
```
t = (M₁ - M₂) / SE
differenced
```

**Effect Size:** Cohen's d = (M₁ - M₂) / SD
pooled
- Small: 0.2
- Medium: 0.5
- Large: 0.8

#### Paired Samples T-Test

**Purpose:** Compare means for same participants at two times/conditions

**Assumptions:**
- Continuous dependent variable
- Paired observations
- Differences normally distributed

**When to Use:**
- Before/after measurements
- Comparing two conditions for same users
- Matched pairs design

**Effect Size:** Cohen's d = M
diff / SD
diff

### ANOVA (Analysis of Variance)

#### One-Way ANOVA

**Purpose:** Compare means across 3+ independent groups

**Assumptions:**
- Continuous dependent variable
- Independent observations
- Normal distribution in each group
- Equal variances (homogeneity)

**When to Use:**
- Comparing multiple user segments
- Testing multiple design versions
- Comparing across categories

**Test Statistic:**
```
F = MS
between / MS
within
```

**Effect Size:** Eta-squared (η²)
- Small: 0.01
- Medium: 0.06
- Large: 0.14

**Post-hoc Tests:**
- Tukey HSD: All pairwise comparisons
- Bonferroni: Conservative correction
- Scheffé: Most conservative
- Dunnett: Compare to control

#### Two-Way ANOVA

**Purpose:** Test main effects and interaction of two factors

**Additional Considerations:**
- Main effect A
- Main effect B
- Interaction A×B

**When to Use:**
- Two independent variables
- Testing interaction effects
- Factorial designs

#### Repeated Measures ANOVA

**Purpose:** Compare means across 3+ conditions for same participants

**Assumptions:**
- Sphericity (equal variances of differences)
- If violated: Use Greenhouse-Geisser correction

**When to Use:**
- Multiple time points
- Within-subjects designs
- Longitudinal studies

### Correlation

#### Pearson Correlation

**Purpose:** Measure linear relationship between two continuous variables

**Assumptions:**
- Both variables continuous
- Linear relationship
- Bivariate normal distribution
- No significant outliers

**Interpretation:**
- r = 0: No linear relationship
- r = ±1: Perfect linear relationship
- Small: ±0.1
- Medium: ±0.3
- Large: ±0.5

**Coefficient of Determination:** r² = variance explained

### Regression

#### Simple Linear Regression

**Purpose:** Predict outcome from one predictor

**Equation:** Y = β₀ + β₁X + ε

**Assumptions:**
- Linear relationship
- Independence
- Homoscedasticity
- Normality of residuals

**Key Statistics:**
- R²: Variance explained
- F-test: Overall model significance
- t-tests: Individual predictors
- RMSE: Prediction error

#### Multiple Linear Regression

**Purpose:** Predict outcome from multiple predictors

**Additional Considerations:**
- Multicollinearity (VIF < 10)
- Adjusted R² for model comparison
- Partial correlations
- Standardized coefficients (β)

## Non-Parametric Tests

### Mann-Whitney U Test

**Purpose:** Compare distributions between two independent groups

**Alternative to:** Independent samples t-test

**When to Use:**
- Ordinal dependent variable
- Non-normal distributions
- Small samples
- Outliers present

**Effect Size:** r = Z / √N
- Small: 0.1
- Medium: 0.3
- Large: 0.5

### Wilcoxon Signed-Rank Test

**Purpose:** Compare paired observations

**Alternative to:** Paired samples t-test

**When to Use:**
- Ordinal data
- Non-normal differences
- Small samples

### Kruskal-Wallis Test

**Purpose:** Compare distributions across 3+ groups

**Alternative to:** One-way ANOVA

**Post-hoc:** Dunn's test with Bonferroni correction

### Friedman Test

**Purpose:** Compare 3+ related samples

**Alternative to:** Repeated measures ANOVA

### Spearman Correlation

**Purpose:** Measure monotonic relationship

**When to Use:**
- Ordinal variables
- Non-linear monotonic relationships
- Presence of outliers

## Categorical Data Tests

### Chi-Square Tests

#### Chi-Square Test of Independence

**Purpose:** Test association between two categorical variables

**Assumptions:**
- Independent observations
- Expected frequency ≥5 per cell
- If violated: Use Fisher's exact test

**Effect Sizes:**
- Phi (φ): 2×2 tables
- Cramér's V: Larger tables
  - Small: 0.1
  - Medium: 0.3
  - Large: 0.5

#### Chi-Square Goodness of Fit

**Purpose:** Test if distribution matches expected

**When to Use:**
- Testing against theoretical distribution
- Checking proportions

### Fisher's Exact Test

**Purpose:** Test association for small samples

**When to Use:**
- 2×2 tables
- Expected frequencies <5
- Small samples

### McNemar's Test

**Purpose:** Test change in paired categorical data

**When to Use:**
- Before/after binary outcomes
- Paired binary data

## Advanced Tests

### MANOVA (Multivariate ANOVA)

**Purpose:** Compare multiple dependent variables across groups

**Test Statistics:**
- Wilks' Lambda
- Pillai's Trace
- Hotelling's T²
- Roy's Largest Root

### ANCOVA (Analysis of Covariance)

**Purpose:** Compare groups while controlling for covariates

**When to Use:**
- Need to control for confounds
- Increase statistical power
- Adjust for baseline differences

### Mixed Effects Models

**Purpose:** Handle nested/hierarchical data

**Components:**
- Fixed effects: Consistent across units
- Random effects: Vary across units

**When to Use:**
- Repeated measures
- Nested data (users in teams)
- Longitudinal data

### Logistic Regression

**Purpose:** Predict binary outcomes

**Interpretation:**
- Odds ratios
- Probability predictions
- ROC curves
- AUC values

## Effect Size Guidelines

### Why Effect Sizes Matter

- Independent of sample size
- Indicate practical significance
- Enable meta-analysis
- Compare across studies

### Common Effect Sizes

| Test | Effect Size | Small | Medium | Large |
|------|------------|-------|--------|-------|
| T-test | Cohen's d | 0.2 | 0.5 | 0.8 |
| ANOVA | Eta-squared | 0.01 | 0.06 | 0.14 |
| Correlation | Pearson's r | 0.1 | 0.3 | 0.5 |
| Chi-square | Cramér's V | 0.1 | 0.3 | 0.5 |
| Regression | f² | 0.02 | 0.15 | 0.35 |

## Power Analysis

### Components of Power

1. **Effect size:** Expected magnitude
2. **Alpha (α):** Type I error rate (usually 0.05)
3. **Power (1-β):** Probability of finding effect (usually 0.80)
4. **Sample size:** Number of observations

### Sample Size Estimation

**For t-test (two-tailed, α=0.05, power=0.80):**
- Small effect (d=0.2): n=394 per group
- Medium effect (d=0.5): n=64 per group
- Large effect (d=0.8): n=26 per group

### Post-hoc Power

- Calculate achieved power
- Interpret non-significant results
- Plan follow-up studies

## Multiple Comparisons

### The Problem

- Increased Type I error with multiple tests
- Family-wise error rate (FWER)
- False discovery rate (FDR)

### Correction Methods

**Bonferroni Correction:**
- Adjusted α = 0.05 / number of tests
- Very conservative
- Use for small number of tests

**Holm-Bonferroni:**
- Sequential Bonferroni
- Less conservative
- More power

**Benjamini-Hochberg (FDR):**
- Controls false discovery rate
- Less conservative
- Good for many tests

**Tukey HSD:**
- For all pairwise comparisons
- After significant ANOVA

## Assumption Testing

### Normality Tests

**Shapiro-Wilk Test:**
- Best for small samples (n<50)
- Null: Data is normal

**Kolmogorov-Smirnov Test:**
- For larger samples
- Less powerful than Shapiro-Wilk

**Visual Inspection:**
- Q-Q plots
- Histograms
- Box plots

### Homogeneity of Variance

**Levene's Test:**
- Robust to non-normality
- Use median-based for skewed data

**Bartlett's Test:**
- Sensitive to non-normality
- Use only for normal data

**F-test:**
- For two groups only
- Sensitive to non-normality

## Reporting Guidelines

### APA Style Reporting

**T-test Example:**
"There was a significant difference in satisfaction scores between Group A (M = 4.2, SD = 0.8) and Group B (M = 3.5, SD = 0.9); t(98) = 4.12, p < .001, d = 0.82."

**ANOVA Example:**
"The main effect of design version was significant, F(2, 147) = 8.34, p < .001, η² = .10."

**Correlation Example:**
"Task time was negatively correlated with experience, r(48) = -.45, p = .001."

### Essential Elements

1. Test statistic value
2. Degrees of freedom
3. P-value
4. Effect size
5. Confidence intervals (when appropriate)
6. Descriptive statistics

## Quick Reference Decision Tree

```
Dependent Variable?
├── Continuous
│   ├── Groups to Compare?
│   │   ├── 2 Groups
│   │   │   ├── Independent → Independent t-test
│   │   │   └── Paired → Paired t-test
│   │   └── 3+ Groups
│   │       ├── Independent → One-way ANOVA
│   │       └── Repeated → RM-ANOVA
│   └── Relationships?
│       ├── Two variables → Correlation
│       └── Prediction → Regression
│
├── Ordinal
│   ├── 2 Groups
│   │   ├── Independent → Mann-Whitney U
│   │   └── Paired → Wilcoxon
│   └── 3+ Groups
│       ├── Independent → Kruskal-Wallis
│       └── Repeated → Friedman
│
└── Categorical
    ├── Association → Chi-square
    ├── Small sample → Fisher's exact
    └── Paired → McNemar
```

## Common Mistakes to Avoid

1. **P-hacking:** Running multiple tests until significant
2. **Ignoring assumptions:** Not checking prerequisites
3. **Overreliance on p-values:** Ignoring effect sizes
4. **Wrong test selection:** Parametric for ordinal data
5. **Multiple comparisons:** Not correcting for multiple tests
6. **Sample size neglect:** Underpowered studies
7. **Outlier mishandling:** Arbitrary removal
8. **Causation claims:** From correlational data

## Conclusion

Successful statistical analysis requires:
- Appropriate test selection
- Assumption verification
- Effect size calculation
- Proper interpretation
- Clear reporting

Always consider both statistical and practical significance when interpreting results.