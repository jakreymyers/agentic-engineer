# Analysis Quality Validation Checklist

This checklist ensures rigorous quality standards for research data analysis, covering qualitative coding, quantitative analysis, synthesis, and insight generation. It adapts based on analysis type and methodology.

```
LLM: INITIALIZATION INSTRUCTIONS - ANALYSIS QUALITY CHECKLIST

ANALYSIS TYPE DETECTION:
Determine the analysis approach:

1. QUALITATIVE ANALYSIS:
   - Thematic analysis
   - Grounded theory
   - Content analysis
   - Narrative analysis
   - Framework analysis
   - Phenomenological analysis

2. QUANTITATIVE ANALYSIS:
   - Descriptive statistics
   - Inferential statistics
   - Predictive modeling
   - Segmentation analysis
   - Conjoint analysis
   - Time series analysis

3. MIXED ANALYSIS:
   - Sequential explanatory
   - Sequential exploratory
   - Convergent parallel
   - Embedded approaches

REQUIRED DOCUMENTS:
- analysis-plan.md - Analysis strategy and approach
- codebook.md - For qualitative analysis
- statistical-plan.md - For quantitative analysis
- data-dictionary.md - Variable definitions
- quality-criteria.md - Analysis quality standards

SKIP INSTRUCTIONS:
- Skip [[QUALITATIVE ONLY]] for pure quantitative
- Skip [[QUANTITATIVE ONLY]] for pure qualitative
- Skip [[THEMATIC ONLY]] for non-thematic approaches
- Skip [[GROUNDED THEORY ONLY]] for other methods
- Document skipped sections in summary

VALIDATION STANDARDS:
- Inter-rater reliability >0.70 for coding
- Statistical assumptions verified
- Saturation documented for qualitative
- Effect sizes reported for quantitative
- Audit trail maintained throughout

CRITICAL THRESHOLDS:
- Minimum 85% quality score for certification
- Any critical failure requires remediation
- Multiple reviewer validation required
```

## 1. DATA PREPARATION & ORGANIZATION

[[LLM: Quality analysis requires quality data. Garbage in, garbage out. Verify data integrity first.]]

### 1.1 Data Completeness

- [ ] **[CRITICAL]** All collected data accounted for
- [ ] Missing data documented and justified
- [ ] Data loss/corruption identified and addressed
- [ ] Incomplete responses handled systematically
- [ ] Dropout analysis conducted if applicable
- [ ] Data sufficiency for analysis confirmed
- [ ] Edge cases identified and decided

### 1.2 Data Cleaning & Transformation

- [ ] Data cleaning rules documented
- [ ] Outliers detected and decisions documented
- [ ] Duplicates identified and resolved
- [ ] Inconsistencies corrected systematically
- [ ] Transformations justified and reversible
- [ ] Original data preserved unchanged
- [ ] Cleaning audit trail maintained

### 1.3 Data Organization

- [ ] File structure logical and consistent
- [ ] Naming conventions standardized
- [ ] Version control implemented
- [ ] Metadata comprehensive
- [ ] Data dictionary complete
- [ ] Relationships mapped clearly
- [ ] Access permissions appropriate

### 1.4 Analysis Readiness

- [ ] **[CRITICAL]** Data format compatible with tools
- [ ] [[QUALITATIVE ONLY]] Transcripts formatted properly
- [ ] [[QUANTITATIVE ONLY]] Variables coded correctly
- [ ] Database/project file created
- [ ] Backup strategy implemented
- [ ] Team access configured
- [ ] Analysis environment tested

## 2. ANALYSIS FRAMEWORK DEVELOPMENT

[[LLM: Framework quality determines analysis consistency. Verify systematic approach.]]

### 2.1 Qualitative Coding Framework [[QUALITATIVE ONLY]]

- [ ] **[CRITICAL]** Coding approach justified (inductive/deductive)
- [ ] Initial codes developed systematically
- [ ] Code definitions clear and distinct
- [ ] Code hierarchy logical
- [ ] Code examples provided
- [ ] Exclusion criteria specified
- [ ] Codebook version controlled

### 2.2 Statistical Analysis Plan [[QUANTITATIVE ONLY]]

- [ ] **[CRITICAL]** Analysis plan pre-specified
- [ ] Hypotheses clearly stated
- [ ] Statistical tests appropriate for data
- [ ] Assumptions to be tested listed
- [ ] Power analysis conducted
- [ ] Multiple comparisons approach defined
- [ ] Sensitivity analyses planned

### 2.3 Mixed Methods Integration [[MIXED ONLY]]

- [ ] Integration points identified
- [ ] Joint displays planned
- [ ] Convergence/divergence approach defined
- [ ] Priority/weight of methods specified
- [ ] Meta-inference framework established
- [ ] Quality criteria for integration set
- [ ] Team roles clarified

## 3. CODING PROCESS [[QUALITATIVE ONLY]]

[[LLM: Systematic coding ensures reliability. Monitor consistency throughout.]]

### 3.1 Coder Training & Calibration

- [ ] **[CRITICAL]** Multiple coders trained (minimum 2)
- [ ] Practice coding completed
- [ ] Disagreements discussed and resolved
- [ ] Coding rules clarified
- [ ] Bias awareness addressed
- [ ] Consistency standards set
- [ ] Calibration documented

### 3.2 Coding Execution

- [ ] First-pass coding completed
- [ ] Coding density appropriate (not too sparse/dense)
- [ ] Code application consistent
- [ ] New codes documented when emerged
- [ ] Memos written during coding
- [ ] Difficult passages flagged
- [ ] Progress tracked systematically

### 3.3 Inter-Rater Reliability

- [ ] **[CRITICAL]** IRR calculated (Cohen's kappa >0.70)
- [ ] IRR sample size adequate (>10-20%)
- [ ] Disagreements analyzed systematically
- [ ] Reconciliation process documented
- [ ] Final agreement achieved
- [ ] Reliability by code type assessed
- [ ] Drift monitored over time

### 3.4 Coding Refinement

- [ ] Code merging/splitting justified
- [ ] Code hierarchy refined
- [ ] Redundant codes eliminated
- [ ] Code saturation assessed
- [ ] Negative cases coded
- [ ] Final codebook comprehensive
- [ ] Examples updated

## 4. STATISTICAL ANALYSIS [[QUANTITATIVE ONLY]]

[[LLM: Statistical rigor ensures valid conclusions. Verify assumptions and interpretations.]]

### 4.1 Assumption Testing

- [ ] **[CRITICAL]** Normality assessed
- [ ] Homogeneity of variance tested
- [ ] Independence verified
- [ ] Linearity checked (if applicable)
- [ ] Multicollinearity assessed
- [ ] Sample size adequacy confirmed
- [ ] Violations addressed appropriately

### 4.2 Descriptive Analysis

- [ ] Central tendency reported appropriately
- [ ] Dispersion measures included
- [ ] Distributions examined
- [ ] Missing data patterns analyzed
- [ ] Demographics summarized
- [ ] Key variables profiled
- [ ] Visualizations accurate

### 4.3 Inferential Analysis

- [ ] **[CRITICAL]** Appropriate tests selected
- [ ] Significance levels pre-specified
- [ ] Confidence intervals reported
- [ ] Effect sizes calculated
- [ ] Power achieved documented
- [ ] Multiple comparisons corrected
- [ ] Assumptions met or robust methods used

### 4.4 Advanced Analysis

- [ ] Model fit assessed
- [ ] Diagnostics performed
- [ ] Cross-validation conducted
- [ ] Sensitivity analysis completed
- [ ] Robustness checks performed
- [ ] Limitations acknowledged
- [ ] Alternative models considered

## 5. THEME DEVELOPMENT & PATTERN IDENTIFICATION

[[LLM: Patterns must emerge from data, not imagination. Verify evidence-based development.]]

### 5.1 Theme Construction [[QUALITATIVE ONLY]]

- [ ] **[CRITICAL]** Themes grounded in data
- [ ] Theme boundaries clear
- [ ] Internal homogeneity achieved
- [ ] External heterogeneity maintained
- [ ] Theme names capture essence
- [ ] Hierarchy/relationships mapped
- [ ] Prevalence documented

### 5.2 Pattern Recognition

- [ ] Patterns identified systematically
- [ ] Frequency/intensity considered
- [ ] Context preserved
- [ ] Variations explained
- [ ] Exceptions noted
- [ ] Temporal patterns examined
- [ ] Relationships explored

### 5.3 Saturation Assessment

- [ ] Saturation criteria defined
- [ ] Saturation point identified
- [ ] New information tracked
- [ ] Code saturation achieved
- [ ] Meaning saturation reached
- [ ] Theoretical saturation considered [[GROUNDED THEORY ONLY]]
- [ ] Documentation complete

## 6. SYNTHESIS & INTEGRATION

[[LLM: Synthesis creates insights from findings. Ensure systematic integration.]]

### 6.1 Cross-Case/Variable Analysis

- [ ] Comparisons systematic
- [ ] Similarities identified
- [ ] Differences explained
- [ ] Patterns across cases/variables
- [ ] Typologies developed if appropriate
- [ ] Contradictions addressed
- [ ] Context considered

### 6.2 Theoretical Integration

- [ ] Existing theory considered
- [ ] Theoretical framework applied appropriately
- [ ] New theoretical insights identified
- [ ] Conceptual model developed
- [ ] Mechanisms explored
- [ ] Boundary conditions specified
- [ ] Contribution to theory articulated

### 6.3 Mixed Methods Synthesis [[MIXED ONLY]]

- [ ] **[CRITICAL]** Integration strategy executed
- [ ] Convergent findings identified
- [ ] Divergent findings explained
- [ ] Complementary insights combined
- [ ] Meta-inferences developed
- [ ] Integration quality assessed
- [ ] Joint displays created

## 7. VALIDITY & RELIABILITY

[[LLM: Trustworthiness determines credibility. Verify all quality dimensions.]]

### 7.1 Qualitative Trustworthiness [[QUALITATIVE ONLY]]

- [ ] **[CRITICAL]** Credibility established
- [ ] Transferability addressed
- [ ] Dependability demonstrated
- [ ] Confirmability maintained
- [ ] Reflexivity practiced
- [ ] Member checking conducted (if appropriate)
- [ ] Peer debriefing completed

### 7.2 Quantitative Validity [[QUANTITATIVE ONLY]]

- [ ] **[CRITICAL]** Internal validity assessed
- [ ] External validity considered
- [ ] Construct validity evaluated
- [ ] Statistical conclusion validity checked
- [ ] Measurement validity confirmed
- [ ] Ecological validity addressed
- [ ] Face validity reasonable

### 7.3 Triangulation

- [ ] Data triangulation applied
- [ ] Method triangulation used
- [ ] Investigator triangulation implemented
- [ ] Theoretical triangulation considered
- [ ] Convergence assessed
- [ ] Divergence explained
- [ ] Confidence increased

## 8. INSIGHT GENERATION & VALIDATION

[[LLM: Insights must be actionable and valid. Quality over quantity.]]

### 8.1 Insight Development

- [ ] **[CRITICAL]** Insights emerge from analysis
- [ ] Evidence clearly linked
- [ ] Confidence levels assigned
- [ ] Practical implications identified
- [ ] Novelty assessed
- [ ] Relevance confirmed
- [ ] Actionability evaluated

### 8.2 Insight Quality

- [ ] Specific rather than generic
- [ ] Depth beyond surface observations
- [ ] Context preserved
- [ ] Nuance captured
- [ ] Contradictions acknowledged
- [ ] Limitations specified
- [ ] Generalizability assessed

### 8.3 Validation Process

- [ ] Negative case analysis performed
- [ ] Alternative explanations considered
- [ ] Peer review conducted
- [ ] Expert validation sought
- [ ] Stakeholder feedback incorporated
- [ ] Practical feasibility assessed
- [ ] Implementation barriers identified

## 9. DOCUMENTATION & AUDIT TRAIL

[[LLM: Transparency enables replication and trust. Document everything.]]

### 9.1 Analysis Documentation

- [ ] **[CRITICAL]** Analysis decisions documented
- [ ] Process steps recorded chronologically
- [ ] Tools and versions specified
- [ ] Team contributions tracked
- [ ] Iterations documented
- [ ] Dead ends acknowledged
- [ ] Pivots explained

### 9.2 Audit Trail Components

- [ ] Raw data preserved
- [ ] Analysis files versioned
- [ ] Memos and notes saved
- [ ] Decision log maintained
- [ ] Code evolution tracked
- [ ] Query history preserved
- [ ] Output files organized

### 9.3 Reproducibility

- [ ] Analysis scripts/syntax saved
- [ ] Random seeds documented
- [ ] Software environments specified
- [ ] Data processing reproducible
- [ ] Analysis steps replicable
- [ ] Results verifiable
- [ ] Archive complete

## 10. BIAS & ERROR MITIGATION

[[LLM: Bias destroys validity. Actively identify and mitigate.]]

### 10.1 Analyst Bias

- [ ] **[CRITICAL]** Confirmation bias checked
- [ ] Selection bias assessed
- [ ] Interpretation bias monitored
- [ ] Anchoring bias avoided
- [ ] Availability heuristic considered
- [ ] Reflexivity practiced
- [ ] Blind analysis used where possible

### 10.2 Systematic Error

- [ ] Measurement error assessed
- [ ] Sampling error evaluated
- [ ] Processing errors identified
- [ ] Coding errors corrected
- [ ] Calculation errors checked
- [ ] Transcription errors fixed
- [ ] Software bugs identified

### 10.3 Quality Controls

- [ ] Independent verification performed
- [ ] Spot checks conducted
- [ ] Outlier investigation completed
- [ ] Consistency checks passed
- [ ] Logic checks applied
- [ ] Range checks performed
- [ ] Cross-validation successful

## ANALYSIS QUALITY VALIDATION SUMMARY

[[LLM: FINAL ANALYSIS QUALITY REPORT

Generate comprehensive assessment:

1. Overall Analysis Quality Score
   - Data Preparation: /100
   - Framework Development: /100
   - Analysis Execution: /100
   - Synthesis Quality: /100
   - Validity/Reliability: /100
   - Documentation: /100
   - TOTAL SCORE: /100

2. Critical Checkpoints
   - All critical items passed: YES/NO
   - Failed items requiring remediation: [List]
   - Risk level: Low/Medium/High

3. Methodological Rigor Assessment

   FOR QUALITATIVE:
   - Coding consistency: Excellent/Good/Fair/Poor
   - Theme development: Systematic/Adequate/Weak
   - Saturation achievement: Full/Partial/Insufficient
   - Trustworthiness: High/Medium/Low

   FOR QUANTITATIVE:
   - Statistical appropriateness: Optimal/Acceptable/Questionable
   - Assumption compliance: Met/Violated with correction/Violated
   - Effect interpretation: Appropriate/Overreaching/Understated
   - Power adequacy: Excellent/Sufficient/Insufficient

4. Insight Quality Evaluation
   - Evidence strength: Strong/Moderate/Weak
   - Actionability: High/Medium/Low
   - Novelty: Breakthrough/Incremental/Confirmatory
   - Confidence level: High/Medium/Low

5. Risk Assessment
   - Bias risks: [List with severity]
   - Error risks: [List with mitigation]
   - Validity threats: [List with impact]

6. Required Improvements
   Priority 1 - Must complete:
   Priority 2 - Should address:
   Priority 3 - Could enhance:

7. Certification Decision
   - CERTIFIED: Exceeds quality standards
   - APPROVED: Meets quality standards
   - CONDITIONAL: Minor issues to address
   - REVISION REQUIRED: Significant gaps
   - REJECTED: Fundamental flaws

Request if user needs:
- Specific technique guidance
- Statistical consultation
- Coding improvement strategies
- Validity enhancement methods]]

### Analysis Quality Dashboard

| Dimension | Score | Status | Critical Issues |
|-----------|-------|--------|-----------------|
| Data Preparation | /15 | _TBD_ | |
| Framework Quality | /15 | _TBD_ | |
| Execution Rigor | /25 | _TBD_ | |
| Synthesis Quality | /15 | _TBD_ | |
| Validity/Reliability | /20 | _TBD_ | |
| Documentation | /10 | _TBD_ | |
| **TOTAL QUALITY** | **/100** | | |

### Critical Failures Identified
(List any critical checkpoint failures)

### Methodological Strengths
(Notable areas of excellence)

### Improvement Requirements
(Prioritized list of necessary enhancements)

### Certification Recommendation
**Decision:** _TBD_
**Justification:** _TBD_
**Conditions:** _TBD_