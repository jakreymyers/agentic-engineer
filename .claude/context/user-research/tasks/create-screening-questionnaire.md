# Create Screening Questionnaire

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:

1. **BIAS-FREE DESIGN REQUIRED** - Questions must not lead or exclude unfairly
2. **LOGICAL FLOW MANDATORY** - Questions must follow screening logic
3. **ELICITATION IS REQUIRED** - User must validate screening criteria
4. **NO ASSUMPTIONS** - Do not assume participant criteria without confirmation

**VIOLATION INDICATOR:** If you create screening questions without systematic design, you have violated this workflow.

## Task Configuration

```yaml
elicit: true
template: screening-criteria-tmpl.yaml
output: research-outputs/screening-questionnaire.md
requires:
  - study-design.md
```

## Prerequisites

Before starting:
- Target participant profile must be defined
- Inclusion/exclusion criteria must be established
- Sample quotas must be determined
- Recruitment channels must be identified

## Workflow Steps

### 1. Define Screening Objectives
**ELICIT: true**

Establish clear screening goals:

**Screening Purpose:**
- Identify qualified participants
- Ensure sample diversity
- Exclude confounding factors
- Meet quota requirements
- Manage recruitment costs

**Target Profile Summary:**
- **Must Have**: Critical characteristics for inclusion
- **Should Have**: Preferred characteristics for diversity
- **Must Not Have**: Disqualifying characteristics
- **Quotas**: Specific distribution requirements

**Quality Targets:**
- False positive rate: <5% (unqualified passing)
- False negative rate: <10% (qualified failing)
- Completion rate: >90% (avoiding abandonment)
- Time to complete: 3-5 minutes maximum

Present objectives with rationale, then provide 1-9 elicitation options.

### 2. Design Screening Logic
**ELICIT: true**

Create logical flow for efficient screening:

**Screening Funnel Structure:**
```
Level 1: Immediate Disqualifiers (Save time/cost)
├── Geographic location
├── Age range
└── Basic demographic requirements

Level 2: Behavioral Qualifiers (Identify target users)
├── Product/service usage
├── Frequency of behavior
└── Recency of experience

Level 3: Psychographic Qualifiers (Ensure fit)
├── Attitudes and preferences
├── Decision-making role
└── Willingness to participate

Level 4: Quota Management (Ensure diversity)
├── Demographic distribution
├── Experience levels
└── User segments
```

**Branching Logic:**
- If fails Level 1 → Polite termination
- If passes all levels → Collect contact info
- If quota full → Waitlist option
- If edge case → Flag for manual review

Present screening logic with flow diagram, then provide 1-9 elicitation options.

### 3. Craft Screening Questions
**ELICIT: true**

Develop specific questions for each level:

**Level 1: Immediate Disqualifiers**
```markdown
Q1. In which country do you currently reside?
    ○ United States
    ○ Canada
    ○ Other [TERMINATE]

Q2. What is your age?
    ○ Under 18 [TERMINATE]
    ○ 18-24
    ○ 25-34
    ○ 35-44
    ○ 45-54
    ○ 55-64
    ○ 65+

Q3. Are you currently employed in any of the following industries?
    [Multi-select]
    □ Market research [TERMINATE]
    □ Advertising [TERMINATE]
    □ Journalism [TERMINATE]
    □ [Competitor company] [TERMINATE]
    □ None of the above
```

**Level 2: Behavioral Qualifiers**
```markdown
Q4. How often do you [target behavior]?
    ○ Daily [QUALIFY]
    ○ 2-3 times per week [QUALIFY]
    ○ Weekly [QUALIFY]
    ○ Monthly [REVIEW]
    ○ Rarely [TERMINATE]
    ○ Never [TERMINATE]

Q5. When did you last [specific action]?
    ○ Within the last week [QUALIFY]
    ○ Within the last month [QUALIFY]
    ○ Within the last 3 months [REVIEW]
    ○ More than 3 months ago [TERMINATE]
    ○ Never [TERMINATE]

Q6. Which of the following best describes your role in [decision/process]?
    ○ Primary decision maker [QUALIFY]
    ○ Key influencer [QUALIFY]
    ○ Provide input [REVIEW]
    ○ Not involved [TERMINATE]
```

**Level 3: Psychographic Qualifiers**
```markdown
Q7. How comfortable are you with [technology/process]?
    [5-point scale]
    Very uncomfortable [1] [TERMINATE]
    Somewhat uncomfortable [2] [REVIEW]
    Neutral [3] [QUALIFY]
    Somewhat comfortable [4] [QUALIFY]
    Very comfortable [5] [QUALIFY]

Q8. How would you describe your attitude toward [topic]?
    ○ Very negative [REVIEW]
    ○ Somewhat negative [QUALIFY]
    ○ Neutral [QUALIFY]
    ○ Somewhat positive [QUALIFY]
    ○ Very positive [REVIEW - check for bias]
```

**Level 4: Quota Management**
```markdown
Q9. Which of the following best describes your [segment criteria]?
    ○ Segment A [Check quota]
    ○ Segment B [Check quota]
    ○ Segment C [Check quota]
    ○ Other [REVIEW]

Q10. What is your highest level of education completed?
    ○ High school or less [Check quota]
    ○ Some college [Check quota]
    ○ Bachelor's degree [Check quota]
    ○ Graduate degree [Check quota]
```

Present questions with bias check notes, then provide 1-9 elicitation options.

### 4. Add Validation Questions
**ELICIT: true**

Include questions to ensure data quality:

**Attention Checks:**
```markdown
Hidden Q: Please select "Somewhat agree" to show you're paying attention
    ○ Strongly disagree
    ○ Disagree
    ○ Somewhat agree [CORRECT]
    ○ Agree
    ○ Strongly agree
```

**Consistency Checks:**
- Ask about same concept in different ways
- Compare answers for logical consistency
- Flag contradictory responses for review

**Open-End Validation:**
```markdown
Q11. In 1-2 sentences, please describe your biggest challenge with [topic]:
    [Text field - manual review for relevance and articulation]
```

**Red Herrings** (to catch professionals):
```markdown
Q12. Which of these have you used? [Multi-select]
    □ Real Option A
    □ Real Option B
    □ Fake Option [TERMINATE if selected]
    □ Real Option C
    □ None of these
```

Present validation questions with quality rationale, then provide 1-9 elicitation options.

### 5. Create Screener Flow
**ELICIT: true**

Design the complete screener experience:

**Introduction Script:**
```
Thank you for your interest in participating in our research study.
This brief questionnaire will take 3-5 minutes and help us determine
if you qualify for our upcoming research. Your responses are confidential
and will only be used for qualification purposes.
```

**Termination Messages:**
- **Quota Full**: "Thank you for your interest. We've already filled positions for participants with your background, but we'd like to keep you on our waitlist."
- **Not Qualified**: "Thank you for completing our questionnaire. Unfortunately, you don't meet the specific requirements for this particular study."
- **Industry Conflict**: "Thank you for your time. Due to the nature of this research, we're unable to include participants from your industry."

**Qualification Message:**
```
Congratulations! You qualify for our research study.
- Compensation: $[amount] for [duration]
- Format: [Interview/Survey/etc.]
- Next Steps: We'll contact you within 48 hours to schedule
```

**Contact Collection:**
```markdown
First Name: [________]
Last Name: [________]
Email: [________]
Phone: [________]
Preferred contact method: ○ Email ○ Phone ○ Text
Best time to reach you: [________]
```

Present complete flow with user experience notes, then provide 1-9 elicitation options.

### 6. Testing & Optimization
**ELICIT: true**

Plan screener validation:

**Pilot Testing Plan:**
- Test with 5-10 known qualified participants
- Test with 5-10 known unqualified participants
- Measure: completion time, drop-off points, confusion
- Refine based on results

**Metrics to Track:**
- Completion rate (target >90%)
- Qualification rate (expect 10-30%)
- Time to complete (target <5 minutes)
- Drop-off points (identify problem questions)
- False positives (post-screening validation)

**Optimization Strategies:**
- Reorder questions for better flow
- Simplify complex wording
- Adjust quota logic
- Add progressive disclosure
- Mobile optimization

Present testing plan with success metrics, then provide 1-9 elicitation options.

## Bias Prevention Guidelines

### Question Design Principles

**Avoid Leading Questions:**
- ❌ "Don't you think [product] is difficult to use?"
- ✅ "How would you describe your experience with [product]?"

**Avoid Loaded Terms:**
- ❌ "innovative solution"
- ✅ "this approach"

**Provide Balanced Options:**
- Include full range of responses
- Avoid forcing positive responses
- Include "Other" and "None" where appropriate

**Cultural Sensitivity:**
- Use inclusive language
- Avoid assumptions about lifestyle
- Respect privacy boundaries
- Consider international variations

## Quality Checkpoints

Before finalizing:
- ✓ All inclusion criteria are covered
- ✓ All exclusion criteria are addressed
- ✓ Questions flow logically
- ✓ No leading or biased language
- ✓ Completion time is under 5 minutes
- ✓ Quota logic is implemented
- ✓ Termination messages are respectful
- ✓ Contact collection is complete

## Output Format

```markdown
# Participant Screening Questionnaire

## Screening Overview
- **Target Qualification Rate**: [X]%
- **Estimated Completion Time**: [X] minutes
- **Total Questions**: [X]

## Screening Logic Flow
[Visual flow diagram]

## Introduction
[Opening script]

## Screening Questions

### Section 1: Basic Qualification
[Questions with logic]

### Section 2: Behavioral Screening
[Questions with logic]

### Section 3: Psychographic Screening
[Questions with logic]

### Section 4: Quota Management
[Questions with logic]

### Section 5: Validation
[Quality check questions]

## Contact Collection
[Fields for qualified participants]

## Termination Scripts
### Quota Full
[Message]

### Not Qualified
[Message]

### Industry Conflict
[Message]

## Implementation Notes
- Platform requirements
- Integration needs
- Testing plan
- Launch timeline
```

## CRITICAL REMINDERS

**❌ NEVER:**
- Use jargon participants won't understand
- Ask for sensitive information unnecessarily
- Create questions longer than 2 sentences
- Use double negatives
- Make participation seem mandatory

**✅ ALWAYS:**
- Test with real users before launch
- Provide clear instructions
- Respect participant time
- Use neutral language
- Include progress indicators
- Allow participants to skip sensitive questions
- Thank participants regardless of outcome