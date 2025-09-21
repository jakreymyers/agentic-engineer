# Generate Interview Probes

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:

1. **DISABLE ALL EFFICIENCY OPTIMIZATIONS** - This workflow requires full user interaction
2. **MANDATORY STEP-BY-STEP EXECUTION** - Each section must be processed sequentially with user feedback
3. **ELICITATION IS REQUIRED** - When `elicit: true`, you MUST use the 1-9 format and wait for user response
4. **NO SHORTCUTS ALLOWED** - Complete probe banks cannot be created without following this workflow

**VIOLATION INDICATOR:** If you create a complete probe bank without user interaction, you have violated this workflow.

## Task Configuration

```yaml
task:
  id: generate-interview-probes
  name: Generate Interview Probes & Follow-up Questions
  type: interactive-probe-development
  elicit: true
  template: probe-bank-tmpl.yaml
  output: docs/research/interviews/probe-bank-{{project}}.md
  estimated_time: 45-60 minutes
```

## CRITICAL: Mandatory Elicitation Format

**When `elicit: true`, this is a HARD STOP requiring user interaction:**

**YOU MUST:**

1. Present probe category content
2. Provide detailed rationale (explain probe types, usage strategies, cognitive mechanisms)
3. **STOP and present numbered options 1-9:**
   - **Option 1:** Always "Proceed to next probe category"
   - **Options 2-9:** Select 8 methods from probe development techniques
   - End with: "Select 1-9 or just type your question/feedback:"
4. **WAIT FOR USER RESPONSE** - Do not proceed until user selects option or provides feedback

**WORKFLOW VIOLATION:** Creating content for elicit=true sections without user interaction violates this task.

## Workflow Steps

### Phase 1: Probe Strategy Foundation
**MANDATORY ELICITATION**

1. **Interview Context Analysis**
   - Review primary discussion guide
   - Identify key research objectives
   - Note sensitive or complex topics
   - Assess participant profile and communication style

   **Elicit:** "I've analyzed your interview context. Here's my understanding of the probing needs..."

2. **Probe Architecture Design**
   - Core probe categories needed
   - Depth vs. breadth strategy
   - Cultural and accessibility considerations
   - Integration with main discussion guide

   **Elicit:** "Based on your research goals, I recommend this probe architecture..."

### Phase 2: Core Probe Categories
**MANDATORY ELICITATION FOR EACH CATEGORY**

3. **Clarification Probes**
   - "What do you mean by [X]?"
   - "When you say [term], help me understand..."
   - "Can you define [concept] in your own words?"
   - "I want to make sure I understand - are you saying that..."
   - "Help me picture what [X] looks like..."

   **Cognitive Mechanism:** These probes address ambiguity and ensure shared understanding without leading the participant.

   **Usage Strategy:** Use when participants use jargon, vague terms, or concepts that could have multiple interpretations.

   **Elicit:** "These clarification probes ensure precision in understanding..."

4. **Elaboration Probes**
   - "Can you tell me more about that?"
   - "What else can you share about [topic]?"
   - "Help me understand the full picture of..."
   - "What other aspects of [X] are important?"
   - "Dive deeper into [specific aspect]..."

   **Cognitive Mechanism:** These probes encourage expansion while maintaining participant's frame of reference.

   **Usage Strategy:** Use when responses seem incomplete or when you sense there's more depth available.

   **Elicit:** "These elaboration probes encourage deeper sharing..."

5. **Example & Story Probes**
   - "Can you give me a specific example of that?"
   - "Tell me about a recent time when..."
   - "Walk me through a typical [process/experience]..."
   - "Paint me a picture of what that looked like..."
   - "What's a story that illustrates [concept]?"

   **Cognitive Mechanism:** These probes access episodic memory and concrete experiences rather than abstract generalizations.

   **Usage Strategy:** Use to ground abstract concepts in real experiences and reveal actual behavior patterns.

   **Elicit:** "These example probes ground concepts in real experiences..."

6. **Contrast & Comparison Probes**
   - "How does that compare to [alternative]?"
   - "What's different about [X] versus [Y]?"
   - "How has that changed over time?"
   - "What would the opposite of that look like?"
   - "How does your experience differ from others you know?"

   **Cognitive Mechanism:** These probes reveal boundaries, preferences, and relative importance through comparison.

   **Usage Strategy:** Use to understand decision criteria, preferences, and the participant's evaluative framework.

   **Elicit:** "These comparison probes reveal preferences and boundaries..."

7. **Sequence & Process Probes**
   - "Walk me through that step by step..."
   - "What happens before/during/after [event]?"
   - "Take me through your typical [process]..."
   - "What's the first thing you do when..."
   - "How does that sequence usually unfold?"

   **Cognitive Mechanism:** These probes access procedural memory and reveal actual behavioral patterns.

   **Usage Strategy:** Use to understand workflows, decision processes, and temporal relationships.

   **Elicit:** "These sequence probes reveal actual behavioral patterns..."

### Phase 3: Advanced Probe Categories
**MANDATORY ELICITATION FOR EACH CATEGORY**

8. **Emotion & Feeling Probes**
   - "How did that make you feel?"
   - "What was going through your mind when..."
   - "What emotions come up around [topic]?"
   - "How do you feel about [situation] now versus then?"
   - "What's your gut reaction to [scenario]?"

   **Cognitive Mechanism:** These probes access affective responses and emotional associations.

   **Usage Strategy:** Use carefully after rapport is established. Essential for understanding motivation and satisfaction.

   **Cultural Sensitivity:** Some cultures are less comfortable with direct emotional expression.

   **Elicit:** "These emotion probes reveal motivational drivers..."

9. **Hypothetical & Scenario Probes**
   - "What would need to change for [X] to happen?"
   - "Imagine if [constraint] weren't an issue..."
   - "How would you handle [hypothetical situation]?"
   - "What's your ideal [experience/outcome]?"
   - "If you could wave a magic wand..."

   **Cognitive Mechanism:** These probes explore possibilities and reveal values/priorities.

   **Usage Strategy:** Use to understand aspirations and constraints. Note these reveal attitudes, not behavior.

   **Elicit:** "These hypothetical probes explore possibilities and values..."

10. **Devil's Advocate Probes**
    - "Some people might say [opposing view]... how would you respond?"
    - "What would someone who disagrees argue?"
    - "How would you convince a skeptic about [position]?"
    - "What are the downsides or challenges with [approach]?"
    - "Play devil's advocate with your own view for a moment..."

    **Cognitive Mechanism:** These probes reveal strength of conviction and counter-arguments.

    **Usage Strategy:** Use sparingly and only with confident participants. Can reveal underlying doubts or strengthen positions.

    **Elicit:** "These devil's advocate probes test conviction strength..."

### Phase 4: Specialized Probe Types
**MANDATORY ELICITATION FOR EACH TYPE**

11. **Contextual Probes**
    - "What else was happening in your life then?"
    - "How did the environment/setting affect [experience]?"
    - "Who else was involved in that situation?"
    - "What external factors influenced [decision]?"
    - "How did [context] shape your perspective?"

    **Cognitive Mechanism:** These probes reveal environmental and social influences on behavior.

    **Usage Strategy:** Use to understand broader context that shapes experiences and decisions.

    **Elicit:** "These contextual probes reveal environmental influences..."

12. **Meta-Cognitive Probes**
    - "How do you usually think about [topic]?"
    - "What goes through your decision-making process?"
    - "How do you know when you've made the right choice?"
    - "What helps you learn about [subject]?"
    - "How has your thinking about [X] evolved?"

    **Cognitive Mechanism:** These probes access metacognition - thinking about thinking.

    **Usage Strategy:** Use with thoughtful participants to understand decision-making processes and mental models.

    **Elicit:** "These meta-cognitive probes reveal thinking processes..."

13. **Social & Relational Probes**
    - "How do others in your life view [topic]?"
    - "What would your [family/friends/colleagues] say about this?"
    - "How does [topic] affect your relationships?"
    - "Who influences your thinking about [subject]?"
    - "How do you talk about [X] with others?"

    **Cognitive Mechanism:** These probes reveal social influences and relationship dynamics.

    **Usage Strategy:** Use to understand social context and peer influence on attitudes and behaviors.

    **Elicit:** "These social probes reveal relationship dynamics..."

### Phase 5: Probe Selection & Customization
**MANDATORY ELICITATION**

14. **Topic-Specific Probe Bank**
    - Customize probes for each major interview topic
    - Create topic-specific elaboration questions
    - Develop context-appropriate examples
    - Adapt language for target population

    **Customization Principles:**
    - Match vocabulary to participant education level
    - Consider cultural communication styles
    - Adapt complexity to cognitive load
    - Ensure sensitivity to potentially difficult topics

    **Elicit:** "Here's how I'll customize probes for your specific topics..."

15. **Probe Timing & Usage Strategy**
    - Early interview probes (rapport-building)
    - Mid-interview probes (depth exploration)
    - Late interview probes (synthesis and reflection)
    - Emergency probes (when interviews stall)

    **Strategic Considerations:**
    - Participant energy and engagement levels
    - Cognitive load management
    - Emotional safety maintenance
    - Time management within sessions

    **Elicit:** "This timing strategy ensures optimal probe deployment..."

### Phase 6: Integration & Training
**MANDATORY ELICITATION**

16. **Interviewer Training Materials**
    - Probe usage guidelines
    - Practice scenarios
    - Common mistakes to avoid
    - Probe selection decision tree

    **Training Components:**
    - When to use each probe type
    - How to chain probes effectively
    - Reading participant readiness for probes
    - Balancing structure with flexibility

    **Elicit:** "These training materials will prepare interviewers..."

17. **Probe Bank Organization**
    - Quick reference cards for interviews
    - Digital probe bank with search functionality
    - Integration with note-taking templates
    - Real-time access during sessions

    **Organization Principles:**
    - Easy scanning during live interviews
    - Logical grouping by purpose
    - Quick access to topic-specific probes
    - Mobile-friendly format for remote interviews

    **Elicit:** "This organization system enables smooth interview flow..."

## Probe Quality Standards

**For each probe, verify:**

1. **Open-Ended Design**
   - Cannot be answered with yes/no
   - Encourages elaboration
   - Allows for unexpected responses

2. **Neutral Language**
   - No leading or loaded terms
   - No embedded assumptions
   - Culturally appropriate phrasing

3. **Clear Intent**
   - Single purpose per probe
   - Understandable to target audience
   - Appropriate cognitive demand

4. **Natural Flow**
   - Connects logically to main questions
   - Feels conversational, not interrogational
   - Maintains interview momentum

## Cultural Adaptation Guidelines

**Consider these factors:**

- **Direct vs. Indirect Communication**: Some cultures prefer indirect probing approaches
- **Authority Relationships**: Probes may need to account for power dynamics
- **Emotional Expression**: Comfort levels with sharing feelings vary culturally
- **Storytelling Traditions**: Some cultures respond better to narrative probes
- **Time Orientation**: Linear vs. circular time concepts affect sequence probes

## Technology Integration

**Digital probe management:**

- **Real-time Access**: Searchable probe bank during interviews
- **Usage Tracking**: Log which probes work best for different topics
- **Dynamic Suggestions**: AI-powered probe recommendations based on context
- **Collaboration Tools**: Share effective probes across research team
- **Integration**: Connect with transcription and analysis tools

## Common Probe Mistakes to Avoid

**❌ NEVER:**
- Use multiple concepts in one probe
- Ask leading or suggestive probes
- Overwhelm participants with too many probes
- Use probes as primary questions (they're follow-ups)
- Interrupt natural storytelling with probes

**✅ ALWAYS:**
- Listen for natural pause points
- Match probe intensity to participant energy
- Use silence effectively before probing
- Acknowledge responses before probing further
- Maintain empathy and curiosity in probes

## Elicitation Methods Available

When user selects options 2-9:

2. **Probe Effectiveness Testing** - Test probes with mock participants
3. **Cultural Adaptation Workshop** - Adapt probes for specific populations
4. **Probe Chain Development** - Create sequences of related probes
5. **Digital Integration Design** - Build technology-enabled probe systems
6. **Interviewer Training Design** - Create comprehensive training materials
7. **Real-time Optimization** - Develop in-interview probe selection strategies
8. **Bias Detection Analysis** - Review probes for hidden bias or leading language
9. **Accessibility Enhancement** - Ensure probes work for diverse abilities and needs

## Error Recovery

If issues arise during probe development:
- Probe too complex → Break into simpler components
- Leading language detected → Reframe neutrally with user input
- Cultural insensitivity identified → Workshop alternative approaches
- Scope too broad → Focus on highest-priority probe categories
- Integration challenges → Develop phased implementation plan

## Success Criteria

✅ Comprehensive probe bank covering all interview topics
✅ Probes tested for clarity and neutrality
✅ Integration strategy with main discussion guide
✅ Interviewer training materials complete
✅ Cultural adaptations considered
✅ Technology integration planned
✅ Usage guidelines documented

## CRITICAL REMINDERS

**❌ NEVER:**
- Create probe banks without user interaction
- Skip elicitation points
- Use closed-ended probes as primary tools
- Overwhelm interviews with excessive probing
- Ignore cultural communication differences

**✅ ALWAYS:**
- Use exact 1-9 format when elicit: true
- Explain probe design rationale and cognitive mechanisms
- Consider participant comfort and energy
- Plan for various participant response styles
- Test probes before full implementation