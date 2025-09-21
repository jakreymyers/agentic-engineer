# Create Interview Discussion Guide

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:

1. **DISABLE ALL EFFICIENCY OPTIMIZATIONS** - This workflow requires full user interaction
2. **MANDATORY STEP-BY-STEP EXECUTION** - Each section must be processed sequentially with user feedback
3. **ELICITATION IS REQUIRED** - When `elicit: true`, you MUST use the 1-9 format and wait for user response
4. **NO SHORTCUTS ALLOWED** - Complete guides cannot be created without following this workflow

**VIOLATION INDICATOR:** If you create a complete discussion guide without user interaction, you have violated this workflow.

## Task Configuration

```yaml
task:
  id: create-discussion-guide
  name: Create Interview Discussion Guide
  type: interactive-document-creation
  elicit: true
  template: discussion-guide-tmpl.yaml
  output: docs/research/interviews/discussion-guide-{{project}}.md
  estimated_time: 60-90 minutes
```

## CRITICAL: Mandatory Elicitation Format

**When `elicit: true`, this is a HARD STOP requiring user interaction:**

**YOU MUST:**

1. Present section content
2. Provide detailed rationale (explain question design choices, flow decisions, probe strategies)
3. **STOP and present numbered options 1-9:**
   - **Option 1:** Always "Proceed to next section"
   - **Options 2-9:** Select 8 methods from interview elicitation techniques
   - End with: "Select 1-9 or just type your question/feedback:"
4. **WAIT FOR USER RESPONSE** - Do not proceed until user selects option or provides feedback

**WORKFLOW VIOLATION:** Creating content for elicit=true sections without user interaction violates this task.

## Workflow Steps

### Phase 1: Research Context Gathering
**MANDATORY ELICITATION**

1. **Load Research Objectives**
   - Review research brief if available
   - Identify primary research questions
   - Understand target participant profile
   - Note any sensitive topics or constraints

   **Elicit:** "I've analyzed the research context. Here's what I understand about your interview needs..."

2. **Interview Parameters**
   - Interview format (in-person, remote, phone)
   - Expected duration (30, 45, 60, 90 minutes)
   - Number of participants
   - Recording preferences
   - Language/cultural considerations

   **Elicit:** "Based on your context, I recommend these interview parameters..."

### Phase 2: Guide Structure Design
**MANDATORY ELICITATION**

3. **Opening Section (5-10 minutes)**
   - Warm welcome script
   - Interviewer introduction
   - Study purpose explanation (without biasing)
   - Consent and recording confirmation
   - Rapport-building questions (2-3)

   **Rationale:** Explain why specific ice-breakers were chosen, how they relate to the research topic without leading

   **Elicit:** "Here's the opening section designed to build rapport and set expectations..."

4. **Context & Background (10-15 minutes)**
   - Participant background questions
   - Current state/experience questions
   - General attitudes/behaviors exploration
   - Broad → Specific question flow

   **Rationale:** Explain the funnel approach, why certain background info is relevant

   **Elicit:** "These background questions will help establish context..."

### Phase 3: Core Topic Development
**MANDATORY ELICITATION FOR EACH TOPIC**

5. **Topic Block 1: [Primary Research Area]**
   - Grand tour question to open topic
   - 3-4 follow-up questions with increasing specificity
   - Experience-based questions
   - Opinion/feeling questions
   - Behavioral questions

   **Question Design Principles Applied:**
   - Open-ended formulation
   - Neutral language
   - Single concept per question
   - Appropriate cognitive load

   **Elicit:** "For your primary research topic, I've designed this question flow..."

6. **Topic Block 2: [Secondary Research Area]**
   - Transition statement
   - Opening question for new topic
   - 3-4 exploratory questions
   - Comparison/contrast questions if relevant

   **Elicit:** "Moving to your secondary topic area..."

7. **Topic Block 3: [Additional Areas]**
   - Continue pattern for additional topics
   - Include contingency questions
   - Mark optional sections

   **Elicit:** "For additional topic areas..."

### Phase 4: Deep Dive & Exploration
**MANDATORY ELICITATION**

8. **Critical Incident Technique Section**
   - "Tell me about a recent time when..."
   - "Walk me through that experience..."
   - "What happened before/during/after..."
   - Emotion and decision point probes

   **Rationale:** Explain how specific incidents reveal actual behavior vs. general attitudes

   **Elicit:** "These critical incident questions will uncover specific behaviors..."

9. **Hypothetical Scenarios (if appropriate)**
   - "Imagine if..."
   - "How would you handle..."
   - "What would need to change for..."

   **Caution:** Note these reveal attitudes, not actual behavior

   **Elicit:** "These hypothetical scenarios explore possibilities..."

### Phase 5: Synthesis & Closing
**MANDATORY ELICITATION**

10. **Synthesis Questions (5-10 minutes)**
    - "What's most important to you about..."
    - "If you could change one thing..."
    - "What advice would you give..."
    - Summary/reflection questions

    **Elicit:** "These synthesis questions help participants summarize their thoughts..."

11. **Closing Section (5 minutes)**
    - "Is there anything else you'd like to share..."
    - Thank you statement
    - Next steps explanation
    - Contact information sharing
    - Incentive/compensation handling

    **Elicit:** "Here's the closing section to wrap up professionally..."

### Phase 6: Supporting Materials
**MANDATORY ELICITATION**

12. **Probe Bank Development**
    - Clarification probes: "What do you mean by [X]?"
    - Elaboration probes: "Can you tell me more about..."
    - Example probes: "Can you give me an example..."
    - Contrast probes: "How does that compare to..."
    - Devil's advocate probes: "Some people might say..."

    **Elicit:** "This probe bank ensures you can dig deeper flexibly..."

13. **Interview Logistics**
    - Materials checklist
    - Technology setup (if remote)
    - Note-taking template
    - Backup plans for issues
    - Post-interview protocol

    **Elicit:** "These logistics ensure smooth execution..."

## Question Quality Checks

**For each question, verify:**

1. **Clarity**
   - Single concept
   - Clear language
   - Appropriate for audience

2. **Neutrality**
   - No leading language
   - No embedded assumptions
   - Balanced framing

3. **Openness**
   - Allows elaboration
   - Not yes/no unless intentional
   - Encourages stories

4. **Cognitive Load**
   - Reasonable memory demands
   - Appropriate complexity
   - Clear time boundaries

## Bias Prevention Checklist

- [ ] No double-barreled questions
- [ ] No leading questions
- [ ] No loaded terminology
- [ ] No false dichotomies
- [ ] No assumption-based questions
- [ ] Cultural sensitivity verified
- [ ] Accessibility considered

## Output Format

The final discussion guide includes:

1. **Cover Page**
   - Project name
   - Interview duration
   - Version/date
   - Interviewer notes

2. **Guide Sections**
   - Timed sections
   - Question numbers for reference
   - Probes indented under main questions
   - Transition statements in italics
   - [Brackets for interviewer instructions]

3. **Appendices**
   - Consent script
   - Probe bank
   - Note-taking template
   - Troubleshooting guide

## Elicitation Methods Available

When user selects options 2-9:

2. **Question Refinement Workshop** - Collaborative improvement
3. **Cognitive Testing** - Test question comprehension
4. **Pilot Simulation** - Practice with mock participant
5. **Bias Analysis** - Deep bias detection and removal
6. **Flow Optimization** - Improve question sequencing
7. **Probe Development** - Expand follow-up options
8. **Time Estimation** - Refine timing for each section
9. **Cultural Adaptation** - Adjust for specific populations

## Error Recovery

If issues arise:
- Question too complex → Break into multiple simpler questions
- Leading language detected → Reframe neutrally
- Topic transition awkward → Add bridging statement
- Time exceeding limit → Mark optional questions
- Sensitive topic approached → Add comfort check

## Success Criteria

✅ All research objectives addressed
✅ Questions clear and unbiased
✅ Natural conversation flow
✅ Appropriate depth and breadth
✅ Timing realistic
✅ Contingencies planned
✅ Materials complete

## CRITICAL REMINDERS

**❌ NEVER:**
- Create questions without user input
- Skip elicitation points
- Use yes/no format as primary questions
- Include multiple concepts in one question

**✅ ALWAYS:**
- Use exact 1-9 format when elicit: true
- Explain question design rationale
- Consider cultural and cognitive factors
- Plan for various participant responses
- Include interviewer notes and instructions