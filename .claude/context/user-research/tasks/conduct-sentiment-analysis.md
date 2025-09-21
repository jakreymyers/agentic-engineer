# Conduct Sentiment Analysis

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **CONTEXT PRESERVATION REQUIRED** - Sentiment must be understood in context
2. **NUANCE DETECTION CRITICAL** - Beyond positive/negative classification
3. **CULTURAL SENSITIVITY** - Emotional expression varies by culture
4. **VALIDATION MANDATORY** - All findings require human verification

## Task Configuration
```yaml
task:
  id: conduct-sentiment-analysis
  name: Conduct Sentiment Analysis on Research Data
  agent: data-analyst
  elicit: true
  template: sentiment-analysis-tmpl.yaml
  output: docs/research/sentiment-analysis.md
  tools:
    - research-sentiment-analyzer
```

## Phase 1: Data Preparation

### Step 1.1: Assess Data Sources
**ELICIT: true**

Present available data sources for sentiment analysis:
```
Common Research Data Types:
1. Interview Transcripts
   - Speaker-separated text
   - Timestamps available
   - Context preserved

2. Survey Open-Ends
   - Short text responses
   - Question context
   - Respondent metadata

3. Observation Notes
   - Researcher interpretations
   - Behavioral descriptions
   - Environmental context

4. Social/Digital Data
   - User comments
   - Reviews/feedback
   - Support tickets
```

**Data Quality Assessment:**
- Volume of text data
- Language consistency
- Context availability
- Speaker identification
- Temporal markers

**Provide detailed rationale:**
- Why sentiment analysis adds value
- Expected insights from emotional patterns
- Limitations and considerations
- Integration with other analyses

**MANDATORY 1-9 OPTIONS:**
1. Proceed with data preparation
2. Select specific data sources
3. Clean and preprocess text
4. Validate data quality
5. Check language requirements
6. Segment by context
7. Prepare metadata
8. Handle missing data
9. Review ethical considerations

**WAIT FOR USER RESPONSE**

### Step 1.2: Preprocess Text Data
Prepare text for analysis:
- Remove identifiers
- Standardize formatting
- Handle multilingual content
- Preserve context markers
- Segment by speaker/source

## Phase 2: Sentiment Framework Selection

### Step 2.1: Choose Analysis Dimensions
**ELICIT: true**

**Sentiment Dimensions to Analyze:**

```
Basic Polarity:
- Positive
- Negative
- Neutral

Emotion Categories (Ekman):
- Joy/Happiness
- Sadness
- Anger
- Fear
- Surprise
- Disgust

Advanced Dimensions:
- Arousal (calm → excited)
- Valence (negative → positive)
- Dominance (submissive → dominant)

Research-Specific:
- Satisfaction/Dissatisfaction
- Frustration/Delight
- Trust/Distrust
- Confusion/Clarity
- Engagement/Disengagement
```

**Context Considerations:**
- Cultural emotion norms
- Domain-specific expressions
- Sarcasm and irony
- Mixed sentiments
- Intensity variations

**MANDATORY 1-9 OPTIONS:**
1. Use basic polarity only
2. Add emotion categories
3. Include arousal-valence model
4. Custom research dimensions
5. Combine multiple frameworks
6. Focus on specific emotions
7. Add intensity scoring
8. Include aspect-based sentiment
9. Design custom framework

**WAIT FOR USER RESPONSE**

### Step 2.2: Configure Analysis Parameters
Set analysis specifications:
- Granularity level (document/paragraph/sentence)
- Confidence thresholds
- Context window size
- Aggregation methods
- Temporal resolution

## Phase 3: Initial Automated Analysis

### Step 3.1: Run Baseline Analysis
**ELICIT: true**

**Execute Initial Analysis:**
```python
Analysis Configuration:
- Method: [Transformer-based / Lexicon / Hybrid]
- Model: [BERT / RoBERTa / Domain-specific]
- Confidence threshold: 0.7
- Context window: ±2 sentences
```

**Present Initial Results:**
```
Overall Sentiment Distribution:
- Positive: XX% (n=XXX)
- Negative: XX% (n=XXX)
- Neutral: XX% (n=XXX)
- Mixed: XX% (n=XXX)

Emotion Detection:
- Joy: XX occurrences
- Frustration: XX occurrences
- Confusion: XX occurrences
[Additional emotions...]

Confidence Metrics:
- High confidence: XX%
- Medium confidence: XX%
- Low confidence: XX%
```

**Quality Indicators:**
- Model performance metrics
- Ambiguous classifications
- Context challenges
- Domain adaptation needs

**MANDATORY 1-9 OPTIONS:**
1. Accept baseline results
2. Adjust confidence thresholds
3. Retrain with domain data
4. Apply different models
5. Segment by context
6. Focus on high-confidence only
7. Review edge cases
8. Validate with samples
9. Refine parameters

**WAIT FOR USER RESPONSE**

### Step 3.2: Handle Edge Cases
Address analysis challenges:
- Sarcasm detection
- Mixed sentiments
- Cultural expressions
- Technical jargon
- Implicit emotions

## Phase 4: Contextual Deep Analysis

### Step 4.1: Analyze Sentiment Patterns
**ELICIT: true**

**Temporal Patterns:**
```
Sentiment Over Time:
- Interview progression
- Survey completion
- Research phases
- Day/time patterns

Sentiment Trajectories:
- Starting sentiment → Ending sentiment
- Inflection points
- Emotional arcs
- Stability measures
```

**Contextual Patterns:**
```
By Topic/Theme:
Topic A: Predominantly positive (75%)
Topic B: Mixed sentiment (45% pos, 40% neg)
Topic C: Strongly negative (70%)

By Speaker/Segment:
Participant Type 1: Generally satisfied
Participant Type 2: Frustrated with specific aspects
Participant Type 3: Highly variable

By Question/Prompt:
Q1: Elicits positive responses
Q2: Triggers frustration
Q3: Causes confusion
```

**Intensity Analysis:**
- Mild expressions
- Moderate sentiment
- Strong emotions
- Extreme reactions

**MANDATORY 1-9 OPTIONS:**
1. Accept pattern analysis
2. Drill into specific patterns
3. Segment differently
4. Analyze transitions
5. Identify triggers
6. Compare groups
7. Extract exemplars
8. Visualize patterns
9. Statistical testing

**WAIT FOR USER RESPONSE**

### Step 4.2: Identify Sentiment Drivers
Uncover factors influencing sentiment:
- Specific features/aspects
- Events or incidents
- Comparison points
- Expectation gaps
- Social influences

## Phase 5: Qualitative Validation

### Step 5.1: Human Review & Validation
**ELICIT: true**

**Validation Sample Selection:**
```
Stratified Sample:
- 10% of high-confidence classifications
- 25% of medium-confidence
- 50% of low-confidence
- All edge cases
- Representative mix
```

**Present for Review:**
```
Example Classification:
Text: "The interface is okay I guess, not terrible but
       I've definitely seen better"
Auto-Classification: Neutral (conf: 0.65)
Context: Discussing product usability
Your Assessment: [Slightly Negative/Neutral/Mixed?]

[Present 10-20 examples for validation]
```

**Validation Metrics:**
- Agreement rate
- Systematic biases
- Context importance
- Cultural factors
- Refinement needs

**MANDATORY 1-9 OPTIONS:**
1. Validate classifications
2. Correct misclassifications
3. Add context rules
4. Adjust model weights
5. Create custom dictionary
6. Review more samples
7. Involve multiple coders
8. Document disagreements
9. Retrain model

**WAIT FOR USER RESPONSE**

### Step 5.2: Incorporate Corrections
Apply validation insights:
- Update classifications
- Add domain rules
- Adjust algorithms
- Document decisions
- Calculate final metrics

## Phase 6: Aspect-Based Analysis

### Step 6.1: Extract Aspect Sentiments
**ELICIT: true**

**Identify Key Aspects:**
```
For Product Research:
- Usability: [sentiment distribution]
- Features: [sentiment distribution]
- Performance: [sentiment distribution]
- Value: [sentiment distribution]
- Support: [sentiment distribution]

For Service Research:
- Staff interaction: [sentiment]
- Process efficiency: [sentiment]
- Communication: [sentiment]
- Problem resolution: [sentiment]
- Overall experience: [sentiment]
```

**Aspect Extraction Methods:**
- Rule-based extraction
- Topic modeling integration
- Dependency parsing
- Named entity recognition

**Present Aspect Matrix:**
| Aspect | Positive | Negative | Neutral | Key Themes |
|--------|----------|----------|---------|------------|
| Aspect1 | XX% | XX% | XX% | Theme list |
| Aspect2 | XX% | XX% | XX% | Theme list |

**MANDATORY 1-9 OPTIONS:**
1. Accept aspect analysis
2. Refine aspect definitions
3. Merge similar aspects
4. Add missing aspects
5. Drill into specific aspects
6. Compare aspect importance
7. Link to requirements
8. Extract verbatims
9. Prioritize improvements

**WAIT FOR USER RESPONSE**

### Step 6.2: Create Sentiment Maps
Visualize relationships:
- Aspect correlation matrix
- Sentiment flow diagrams
- Emotional journey maps
- Heat maps by segment

## Phase 7: Integration with Other Analyses

### Step 7.1: Cross-Reference with Themes
**ELICIT: true**

**Theme-Sentiment Alignment:**
```
Major Themes with Sentiment:
Theme 1: "Ease of use"
- Overall: 70% positive
- Key emotion: Satisfaction
- Outliers: Frustration with learning curve

Theme 2: "Cost concerns"
- Overall: 65% negative
- Key emotion: Anxiety
- Context: Budget constraints

Theme 3: "Innovation excitement"
- Overall: 85% positive
- Key emotion: Anticipation
- Driver: Future possibilities
```

**Behavioral Correlations:**
- High satisfaction → Continued use
- Frustration → Support requests
- Confusion → Abandonment
- Delight → Advocacy

**MANDATORY 1-9 OPTIONS:**
1. Accept integration analysis
2. Deepen theme connections
3. Analyze outliers
4. Compare segments
5. Link to behaviors
6. Predict outcomes
7. Identify interventions
8. Test correlations
9. Validate findings

**WAIT FOR USER RESPONSE**

### Step 7.2: Connect to User Outcomes
Link sentiment to outcomes:
- Satisfaction scores
- Recommendation likelihood
- Retention probability
- Feature adoption
- Support needs

## Phase 8: Insight Development

### Step 8.1: Synthesize Sentiment Insights
**ELICIT: true**

**Key Sentiment Insights:**
```
1. Emotional Journey Patterns
   - Initial enthusiasm
   - Reality adjustment
   - Stabilization point

2. Sentiment Triggers
   - Positive: [list]
   - Negative: [list]
   - Transition points

3. Segment Differences
   - Power users: Generally positive
   - New users: Mixed, confusion
   - Churned users: Frustration peaks

4. Unmet Emotional Needs
   - Desire for recognition
   - Need for control
   - Seeking simplicity
```

**Strategic Implications:**
- Experience improvements
- Communication adjustments
- Feature priorities
- Support interventions
- Expectation management

**MANDATORY 1-9 OPTIONS:**
1. Finalize insights
2. Add supporting evidence
3. Prioritize by impact
4. Create action items
5. Design interventions
6. Plan follow-up research
7. Validate with stakeholders
8. Develop metrics
9. Create monitoring plan

**WAIT FOR USER RESPONSE**

### Step 8.2: Generate Recommendations
Transform insights into actions:
- Quick wins for sentiment
- Systematic improvements
- Communication strategies
- Experience design changes
- Support enhancements

## Phase 9: Visualization & Reporting

### Step 9.1: Create Sentiment Visualizations
Design compelling visuals:
- Sentiment distribution charts
- Emotion wheel diagrams
- Temporal progression graphs
- Aspect-sentiment matrices
- Journey emotion maps
- Word clouds by sentiment
- Comparative heat maps

### Step 9.2: Prepare Narrative Report
Structure findings story:
- Overall emotional landscape
- Key sentiment patterns
- Critical triggers and drivers
- Segment variations
- Strategic implications
- Recommended actions

## Quality Assurance Checklist

**Data Quality:**
- [ ] Sufficient volume for analysis
- [ ] Context preserved
- [ ] Language handled appropriately
- [ ] Bias checked and addressed

**Analysis Quality:**
- [ ] Multiple methods triangulated
- [ ] Human validation completed
- [ ] Context incorporated
- [ ] Cultural factors considered

**Insight Quality:**
- [ ] Patterns are robust
- [ ] Findings actionable
- [ ] Links to outcomes clear
- [ ] Recommendations specific

## Common Pitfalls & Solutions

**Over-relying on Automation:**
- Always validate with humans
- Check cultural context
- Review edge cases
- Understand limitations

**Ignoring Context:**
- Preserve surrounding text
- Consider question prompts
- Understand situation
- Note temporal factors

**Missing Nuance:**
- Look for mixed sentiments
- Detect subtle expressions
- Identify sarcasm/irony
- Capture intensity variations

**Aggregation Errors:**
- Weight appropriately
- Segment meaningfully
- Consider outliers
- Preserve variation

## Deliverables

1. **Sentiment Analysis Report**
   - Overall sentiment landscape
   - Temporal patterns
   - Aspect-based analysis
   - Segment comparisons

2. **Visualization Package**
   - Interactive dashboards
   - Static infographics
   - Journey emotion maps
   - Comparison matrices

3. **Strategic Recommendations**
   - Priority improvements
   - Communication adjustments
   - Experience interventions
   - Monitoring metrics

4. **Technical Appendix**
   - Methodology details
   - Validation results
   - Confidence metrics
   - Limitations noted

## Tools & Technologies

**NLP Libraries:**
- NLTK, spaCy, TextBlob
- Transformers (Hugging Face)
- Google Cloud Natural Language
- AWS Comprehend
- Azure Text Analytics

**Visualization:**
- Plotly (interactive)
- Matplotlib/Seaborn
- D3.js (web-based)
- Tableau (dashboards)

## Success Metrics

- Classification accuracy: >80%
- Human validation agreement: >85%
- Actionable insights generated: >5
- Stakeholder value confirmed: Yes
- Decisions influenced: Documented