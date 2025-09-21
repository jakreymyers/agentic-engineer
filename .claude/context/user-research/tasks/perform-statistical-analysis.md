# Perform Statistical Analysis - Quantitative Research Data Processing

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **GUIDED ANALYSIS REQUIRED** - Statistical decisions need user input
2. **ASSUMPTION VALIDATION** - Each test requires prerequisite checks
3. **INTERPRETATION FOCUS** - Results must be explained in context
4. **COLLABORATIVE PROCESS** - Not automated number crunching

**VIOLATION INDICATOR:** If you run statistical tests without checking assumptions and user confirmation, you have violated this workflow.

## Task Configuration

```yaml
task: perform-statistical-analysis
elicit: true
template: statistical-summary-tmpl.yaml
output: analysis/statistics/{project}-statistical-report.md
prerequisites:
  - Quantitative data available
  - Research questions defined
  - Variables identified
  - Data cleaned and prepared
data_dependencies:
  - statistical-tests.md
  - analysis-methods.md
```

## Statistical Analysis Workflow

### Phase 1: Data Exploration and Preparation

**Objective:** Understand data characteristics and prepare for analysis

**Process:**

1. **Data Inventory**
   ```
   Dataset Overview:
   - Sample size (n): [Number]
   - Variables: [List with types]
   - Missing data: [Count and pattern]
   - Data collection method: [Survey/experiment/observation]
   - Time period: [When collected]
   ```

2. **Variable Classification**
   ```
   Variable Types:
   Continuous: Age, income, time spent, scores
   Ordinal: Satisfaction (1-5), education level
   Nominal: Gender, department, yes/no responses
   Count: Number of purchases, error frequency
   ```

3. **Descriptive Statistics**
   ```
   For Continuous Variables:
   - Mean (M)
   - Standard Deviation (SD)
   - Median (Mdn)
   - Range (Min-Max)
   - Skewness
   - Kurtosis

   For Categorical Variables:
   - Frequencies (n)
   - Percentages (%)
   - Mode
   ```

4. **Data Quality Checks**
   - Outlier detection (z-scores > 3.29)
   - Normality assessment (Shapiro-Wilk)
   - Missing data patterns (MCAR/MAR/MNAR)
   - Data entry errors
   - Logical inconsistencies

**Data Cleaning Decisions:**
```
Issue: [Outlier/Missing/Error]
Detection: [How identified]
Action: [Remove/Transform/Impute/Retain]
Justification: [Why this approach]
Impact: [Effect on sample size/power]
```

**Elicitation Point 1:** [elicit: true]
Present data exploration results. Offer options:
1. Proceed to Phase 2 (Analysis Selection)
2. Address missing data strategies
3. Handle outliers detected
4. Transform variables (log, square root)
5. Create composite variables
6. Check data assumptions
7. Examine distributions
8. Review variable relationships
9. Validate data quality

### Phase 2: Selecting Appropriate Analyses

**Objective:** Choose correct statistical tests based on research questions

**Decision Tree for Test Selection:**

1. **Research Question Type**
   ```
   Relationship Questions → Correlation/Regression
   Difference Questions → t-tests/ANOVA
   Association Questions → Chi-square
   Prediction Questions → Regression/Machine Learning
   ```

2. **Number of Variables**
   ```
   One Variable → Descriptive/One-sample tests
   Two Variables → Bivariate analyses
   Multiple Variables → Multivariate analyses
   ```

3. **Variable Types Determine Test**
   ```
   Continuous + Continuous → Pearson correlation
   Ordinal + Ordinal → Spearman correlation
   Continuous + Categorical(2) → Independent t-test
   Continuous + Categorical(3+) → ANOVA
   Categorical + Categorical → Chi-square
   ```

4. **Sample Characteristics**
   ```
   Independent samples → Between-subjects tests
   Paired samples → Within-subjects tests
   Small sample (n<30) → Non-parametric alternatives
   ```

**Test Selection Matrix:**
```
Research Question: [State the question]
Variables Involved: [List with types]
Recommended Test: [Primary choice]
Alternative Test: [If assumptions violated]
Power Analysis: [Sample size adequate?]
```

**Elicitation Point 2:** [elicit: true]
Present test selection rationale. Offer options:
1. Proceed to Phase 3 (Assumption Testing)
2. Clarify research questions
3. Consider alternative tests
4. Review variable types
5. Check sample size requirements
6. Plan multiple comparisons
7. Consider effect size importance
8. Review literature precedents
9. Validate analytical approach

### Phase 3: Testing Statistical Assumptions

**Objective:** Verify prerequisites for chosen analyses

**Common Assumptions to Test:**

1. **Normality Testing**
   ```
   Methods:
   - Visual: Q-Q plots, histograms
   - Statistical: Shapiro-Wilk (n<50), Kolmogorov-Smirnov (n≥50)

   Interpretation:
   p > .05 → Normally distributed
   p ≤ .05 → Non-normal (consider transformation/non-parametric)
   ```

2. **Homogeneity of Variance**
   ```
   Levene's Test:
   p > .05 → Equal variances assumed
   p ≤ .05 → Unequal variances (use Welch's correction)
   ```

3. **Independence of Observations**
   ```
   Check for:
   - Repeated measures from same participants
   - Clustered data (teams, schools)
   - Time series dependencies
   - Spatial autocorrelation
   ```

4. **Linearity (for correlation/regression)**
   ```
   Assessment:
   - Scatterplots of relationships
   - Residual plots
   - Curve estimation
   ```

5. **Sample Size and Power**
   ```
   Power Analysis:
   - Desired power: 0.80 (80%)
   - Alpha level: 0.05 (5%)
   - Effect size: Small (d=0.2), Medium (d=0.5), Large (d=0.8)
   - Required n: [Calculate based on test]
   ```

**Assumption Violation Decisions:**
```
Assumption: [Which one]
Test Result: [Pass/Fail]
If Failed:
- Option 1: Transform data
- Option 2: Use robust alternative
- Option 3: Use non-parametric test
- Option 4: Report with caveats
Decision: [Which option chosen]
Justification: [Why appropriate]
```

**Elicitation Point 3:** [elicit: true]
Present assumption testing results. Offer options:
1. Proceed to Phase 4 (Analysis Execution)
2. Apply data transformations
3. Switch to non-parametric tests
4. Use robust statistics
5. Bootstrap confidence intervals
6. Adjust for violations
7. Collect more data
8. Revise analysis plan
9. Document limitations

### Phase 4: Executing Statistical Analyses

**Objective:** Run selected tests and calculate results

**Analysis Execution Framework:**

1. **Descriptive Statistics First**
   ```
   Group Statistics:
   Group 1: M = X.XX, SD = X.XX, n = XX
   Group 2: M = X.XX, SD = X.XX, n = XX

   Visual Representation:
   - Bar charts with error bars
   - Box plots for distributions
   - Scatter plots for relationships
   ```

2. **Primary Analysis**
   ```
   Test: [Name of test]
   Hypotheses:
   H₀: [Null hypothesis]
   H₁: [Alternative hypothesis]

   Results:
   Test statistic: [t/F/χ²/r] = X.XX
   Degrees of freedom: df = XX
   p-value: p = .XXX
   Effect size: [d/η²/φ/r²] = X.XX
   95% CI: [Lower, Upper]
   ```

3. **Effect Size Interpretation**
   ```
   Cohen's d (mean differences):
   0.2 = small, 0.5 = medium, 0.8 = large

   Correlation r:
   0.1 = small, 0.3 = medium, 0.5 = large

   Eta-squared η² (ANOVA):
   0.01 = small, 0.06 = medium, 0.14 = large
   ```

4. **Post-hoc Analyses** (if applicable)
   ```
   Multiple Comparisons:
   Correction method: [Bonferroni/Tukey/Scheffé]
   Adjusted α: [.05/number of comparisons]

   Pairwise comparisons:
   Group A vs B: p = .XXX, d = X.XX
   Group A vs C: p = .XXX, d = X.XX
   Group B vs C: p = .XXX, d = X.XX
   ```

**Results Interpretation Template:**
```
Statistical Finding:
"There was a [significant/non-significant] [relationship/difference]
between [Variable A] and [Variable B], [test details], p = .XXX,
[effect size]. This suggests that [practical interpretation]."
```

**Elicitation Point 4:** [elicit: true]
Present statistical results. Offer options:
1. Proceed to Phase 5 (Advanced Analyses)
2. Run additional post-hoc tests
3. Calculate different effect sizes
4. Examine subgroup analyses
5. Check for moderators
6. Test for mediators
7. Explore interactions
8. Validate with bootstrap
9. Sensitivity analysis

### Phase 5: Advanced and Supplementary Analyses

**Objective:** Conduct deeper analyses for comprehensive understanding

**Advanced Analysis Options:**

1. **Regression Analysis**
   ```
   Multiple Regression Model:
   Predictors: [List of IVs]
   Outcome: [DV]

   Model Summary:
   R² = .XXX (XX% variance explained)
   Adjusted R² = .XXX
   F(df1, df2) = XX.X, p < .001

   Coefficients:
   Predictor 1: β = .XXX, t = X.XX, p = .XXX
   Predictor 2: β = .XXX, t = X.XX, p = .XXX

   Assumptions checked:
   - Multicollinearity (VIF < 10)
   - Independence (Durbin-Watson ~2)
   - Homoscedasticity (residual plots)
   - Normality of residuals
   ```

2. **Moderation Analysis**
   ```
   Testing if relationship varies by third variable:
   Main effect A: β = .XXX, p = .XXX
   Main effect Moderator: β = .XXX, p = .XXX
   Interaction A×Moderator: β = .XXX, p = .XXX

   Simple slopes analysis at:
   - Low moderator (-1 SD): β = .XXX, p = .XXX
   - High moderator (+1 SD): β = .XXX, p = .XXX
   ```

3. **Mediation Analysis**
   ```
   Testing if relationship is explained by mediator:
   Path a (IV→Mediator): β = .XXX, p = .XXX
   Path b (Mediator→DV): β = .XXX, p = .XXX
   Direct effect c': β = .XXX, p = .XXX
   Indirect effect: β = .XXX, 95% CI [.XX, .XX]
   ```

4. **Cluster Analysis**
   ```
   Identifying natural groups in data:
   Method: [Hierarchical/K-means]
   Number of clusters: [Determined by dendrogram/elbow]

   Cluster profiles:
   Cluster 1 (n=XX): High on A, Low on B
   Cluster 2 (n=XX): Low on A, High on B
   ```

**Elicitation Point 5:** [elicit: true]
Present advanced analyses results. Offer options:
1. Proceed to Phase 6 (Synthesis and Reporting)
2. Explore alternative models
3. Test model assumptions
4. Cross-validate findings
5. Examine residuals
6. Check influential cases
7. Compare nested models
8. Robustness checks
9. Theoretical implications

### Phase 6: Results Synthesis and Reporting

**Objective:** Integrate findings into coherent narrative

**Synthesis Framework:**

1. **Key Findings Summary**
   ```
   Primary Findings:
   1. [Main result with effect size and significance]
   2. [Second key finding]
   3. [Third key finding]

   Unexpected Findings:
   - [Surprising result and potential explanation]

   Null Findings:
   - [Non-significant results that matter]
   ```

2. **Practical Significance**
   ```
   Beyond Statistical Significance:
   - Effect size magnitude
   - Real-world impact
   - Cost-benefit implications
   - Clinical/practical importance
   ```

3. **Limitations and Caveats**
   ```
   Methodological Limitations:
   - Sample size constraints
   - Assumption violations addressed
   - Generalizability limits
   - Measurement issues

   Statistical Limitations:
   - Power limitations
   - Multiple testing concerns
   - Missing data impact
   ```

4. **Visual Summary Creation**
   ```
   Essential Visualizations:
   - Main effects plot
   - Interaction graphs
   - Confidence interval plots
   - Effect size forest plot
   ```

**Results Narrative Template:**
```
"Analysis of [sample description] revealed [primary finding].
Specifically, [detailed statistics with effect sizes].
This finding suggests [practical interpretation].
Additionally, [secondary findings]. These results should
be interpreted considering [key limitations].
Implications include [practical applications]."
```

**Elicitation Point 6:** [elicit: true]
Review synthesized results. Offer options:
1. Finalize statistical report
2. Enhance visualizations
3. Strengthen interpretations
4. Add sensitivity analyses
5. Include additional context
6. Clarify limitations
7. Expand implications
8. Technical appendix
9. Stakeholder summary

## Statistical Analysis Outputs

### 1. Comprehensive Statistical Report
```markdown
# Statistical Analysis Report - [Project Name]
## Analysis Date: [Date]
## Analyst: Alex (Data Analyst)
## Sample Size: n = [Number]

### Executive Summary
- Key findings in plain language
- Effect sizes and practical significance
- Main recommendations

### Method
#### Participants
- Sample characteristics
- Recruitment method
- Demographics table

#### Measures
- Variables assessed
- Reliability statistics
- Validity evidence

#### Analysis Plan
- Statistical tests used
- Assumption checks performed
- Corrections applied

### Results

#### Descriptive Statistics
[Table with means, SDs, correlations]

#### Primary Analyses
[Test results with interpretations]

#### Supplementary Analyses
[Additional tests and explorations]

### Discussion
- Key findings interpreted
- Theoretical implications
- Practical applications
- Limitations acknowledged
- Future research suggested

### Technical Appendix
- Assumption testing details
- Alternative analyses
- Sensitivity analyses
- Full statistical output
```

### 2. Statistical Summary Table
Create publication-ready table:
- Variables with descriptive stats
- Test statistics and p-values
- Effect sizes with confidence intervals
- Sample sizes per analysis

### 3. Visualization Package
Generate appropriate graphs:
- Distribution plots
- Relationship visualizations
- Group comparison charts
- Interaction plots
- Effect size displays

## Quality Assurance

**Statistical Rigor Checklist:**
- [ ] Appropriate test selected
- [ ] Assumptions tested and addressed
- [ ] Effect sizes calculated
- [ ] Confidence intervals reported
- [ ] Multiple comparisons corrected
- [ ] Power analysis conducted
- [ ] Outliers addressed appropriately
- [ ] Missing data handled correctly
- [ ] Results reproducible

## Common Statistical Pitfalls

1. **p-hacking:** Running many tests until significant
2. **Assumption Ignorance:** Not checking prerequisites
3. **Effect Size Neglect:** Focusing only on p-values
4. **Over-interpretation:** Claims beyond data support
5. **Sample Size Issues:** Underpowered analyses
6. **Multiple Testing:** Not correcting for many tests
7. **Outlier Mishandling:** Removing without justification

## Statistical Software Commands Reference

**For transparency, document analysis code:**

```r
# R Example
t.test(outcome ~ group, data = df, var.equal = TRUE)
cohen.d(outcome ~ group, data = df)
```

```python
# Python Example
from scipy import stats
stats.ttest_ind(group1, group2)
```

```spss
# SPSS Syntax
T-TEST GROUPS=group(1 2)
  /VARIABLES=outcome
  /CRITERIA=CI(.95).
```

## Integration Points

**From Data Collection:**
- Raw quantitative data
- Survey responses
- Experimental results
- Behavioral metrics

**To Insight Synthesizer:**
- Statistical findings
- Effect size summaries
- Significant predictors
- Group differences

**To Research Reporter:**
- Results narratives
- Statistical tables
- Key visualizations
- Technical appendix

## CRITICAL REMINDERS

**❌ NEVER:**
- Run tests without checking assumptions
- Report only p-values without effect sizes
- Make causal claims from correlational data
- Remove data without documentation
- Ignore non-significant but meaningful results
- Complete without user validation at each phase

**✅ ALWAYS:**
- Check and report assumptions
- Calculate and interpret effect sizes
- Consider practical significance
- Document all analytical decisions
- Report confidence intervals
- Acknowledge limitations
- Wait for user input at elicitation points