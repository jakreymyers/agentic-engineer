# Simulate Interview Session

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:

1. **DISABLE ALL EFFICIENCY OPTIMIZATIONS** - This workflow requires full user interaction
2. **MANDATORY STEP-BY-STEP EXECUTION** - Each section must be processed sequentially with user feedback
3. **ELICITATION IS REQUIRED** - When `elicit: true`, you MUST use the 1-9 format and wait for user response
4. **NO SHORTCUTS ALLOWED** - Complete simulations cannot be created without following this workflow

**VIOLATION INDICATOR:** If you run a complete simulation without user interaction, you have violated this workflow.

## Task Configuration

```yaml
task:
  id: simulate-interview-session
  name: Interview Practice & Simulation
  type: interactive-simulation
  elicit: true
  template: interview-protocol-tmpl.yaml
  output: docs/research/interviews/simulation-report-{{project}}.md
  estimated_time: 90-120 minutes
```

## CRITICAL: Mandatory Elicitation Format

**When `elicit: true`, this is a HARD STOP requiring user interaction:**

**YOU MUST:**

1. Present simulation phase content
2. Provide detailed rationale (explain simulation value, learning objectives, skill development)
3. **STOP and present numbered options 1-9:**
   - **Option 1:** Always "Proceed to next simulation phase"
   - **Options 2-9:** Select 8 methods from simulation techniques
   - End with: "Select 1-9 or just type your question/feedback:"
4. **WAIT FOR USER RESPONSE** - Do not proceed until user selects option or provides feedback

**WORKFLOW VIOLATION:** Creating content for elicit=true sections without user interaction violates this task.

## Workflow Steps

### Phase 1: Simulation Setup & Preparation
**MANDATORY ELICITATION**

1. **Simulation Objectives Definition**
   - Primary skills to develop (rapport building, probing, time management)
   - Specific challenges to practice (difficult participants, sensitive topics)
   - Learning outcomes for each practice round
   - Success metrics for skill development

   **Rationale:** Clear objectives ensure focused practice and measurable improvement. Different interviewer skill levels require different simulation emphases.

   **Elicit:** "Based on your team's experience level, here are the simulation objectives I recommend..."

2. **Participant Persona Development**
   - Create 3-5 distinct participant personas
   - Include communication styles, backgrounds, potential challenges
   - Script typical responses and behavioral patterns
   - Define persona-specific triggers and sensitivities

   **Persona Categories:**
   - **Cooperative Sharer**: Provides rich detail, stays on topic
   - **Reluctant Participant**: Minimal responses, needs encouragement
   - **Tangential Speaker**: Goes off-topic frequently, needs redirection
   - **Emotional Responder**: Strong feelings about topics, needs sensitivity
   - **Expert Challenger**: Questions methodology, provides complex technical responses

   **Elicit:** "I've designed these participant personas to challenge different interviewing skills..."

### Phase 2: Core Simulation Modules
**MANDATORY ELICITATION FOR EACH MODULE**

3. **Opening & Rapport Building Simulation**
   - Practice introduction scripts
   - Experiment with different rapport-building approaches
   - Handle consent process naturally
   - Manage technology setup smoothly

   **Simulation Scenarios:**
   - Nervous first-time participant
   - Busy executive with limited time
   - Skeptical participant questioning study value
   - Participant with accessibility needs

   **Learning Focus:** Building immediate trust and comfort while establishing professional boundaries.

   **Elicit:** "This opening simulation will build confidence in those crucial first minutes..."

4. **Question Flow & Timing Simulation**
   - Practice transitioning between topics
   - Manage time allocation across sections
   - Handle when participants give unexpected responses
   - Maintain natural conversation flow

   **Simulation Challenges:**
   - Participant goes deep on early questions (time management)
   - Participant skips over important topics (gentle redirection)
   - Participant brings up topics out of sequence (flexible adaptation)
   - Running behind schedule (prioritization decisions)

   **Learning Focus:** Balancing structure with flexibility while maintaining research objectives.

   **Elicit:** "These flow simulations develop adaptive interviewing skills..."

5. **Probing & Deep Dive Simulation**
   - Practice probe selection and timing
   - Develop natural follow-up question skills
   - Learn to read when to push deeper vs. move on
   - Handle resistance to sensitive topics

   **Simulation Scenarios:**
   - Participant gives surface-level responses
   - Participant uses jargon or unclear language
   - Participant shares emotional or difficult experiences
   - Participant contradicts earlier statements

   **Learning Focus:** Extracting rich, meaningful data while respecting participant boundaries.

   **Elicit:** "These probing simulations develop critical depth-finding skills..."

### Phase 3: Challenging Situation Simulations
**MANDATORY ELICITATION FOR EACH SITUATION**

6. **Difficult Participant Simulation**
   - Hostile or defensive participants
   - Participants who dominate conversation
   - Participants who provide minimal responses
   - Participants who challenge research methodology

   **Advanced Scenarios:**
   - Participant becomes emotional or distressed
   - Participant asks to end interview early
   - Participant provides information that seems untruthful
   - Participant makes inappropriate comments

   **Skill Development:**
   - De-escalation techniques
   - Professional boundary maintenance
   - Empathetic but firm guidance
   - Ethical decision-making under pressure

   **Elicit:** "These challenging scenarios build resilience and professional skill..."

7. **Technical Problem Simulation**
   - Recording failures during interview
   - Internet connectivity issues (remote interviews)
   - Participant technology difficulties
   - Platform or tool malfunctions

   **Simulation Elements:**
   - Graceful problem acknowledgment
   - Quick backup plan implementation
   - Maintaining participant engagement during delays
   - Decision-making about continuing vs. rescheduling

   **Learning Focus:** Maintaining professionalism and participant experience despite technical challenges.

   **Elicit:** "These technical simulations prepare for real-world disruptions..."

8. **Cultural & Accessibility Simulation**
   - Participants from different cultural backgrounds
   - Language barriers or communication styles
   - Participants with hearing, vision, or cognitive accessibility needs
   - Age-related communication preferences

   **Scenario Considerations:**
   - Different comfort levels with directness
   - Varying storytelling and response patterns
   - Time orientation differences (linear vs. circular)
   - Authority relationship expectations

   **Learning Focus:** Inclusive interviewing practices that respect diverse communication styles.

   **Elicit:** "These diversity simulations build inclusive interviewing capabilities..."

### Phase 4: Advanced Simulation Techniques
**MANDATORY ELICITATION FOR EACH TECHNIQUE**

9. **Real-Time Coaching Simulation**
   - Observer provides live feedback during simulation
   - Practice receiving and implementing coaching mid-interview
   - Develop skills for supporting less experienced interviewers
   - Create feedback protocols for live sessions

   **Coaching Elements:**
   - Silent hand signals for common guidance
   - Note-passing for complex feedback
   - Post-simulation debriefing protocols
   - Skill development planning

   **Elicit:** "This coaching simulation develops both interviewing and mentoring skills..."

10. **Multi-Modal Simulation**
    - Practice with different interview formats
    - Handle interviews with screen sharing or document review
    - Manage group or paired interviews
    - Integrate observational data collection

    **Format Variations:**
    - In-person in participant's environment
    - Remote video with screen sharing
    - Phone-only interviews
    - Walking interviews or mobile sessions

    **Elicit:** "These multi-modal simulations prepare for diverse interview contexts..."

11. **Cognitive Load Management Simulation**
    - Practice managing complex information in real-time
    - Handle note-taking while maintaining engagement
    - Manage multiple research objectives simultaneously
    - Balance deep listening with strategic thinking

    **Simulation Elements:**
    - Information-dense participant responses
    - Multiple competing research priorities
    - Unexpected valuable information outside main topics
    - Time pressure with rich content

    **Elicit:** "These cognitive load simulations develop mental agility under pressure..."

### Phase 5: Simulation Analysis & Improvement
**MANDATORY ELICITATION**

12. **Performance Analysis Framework**
    - Video/audio review of simulation sessions
    - Structured feedback collection and analysis
    - Skill progression tracking over multiple sessions
    - Peer observation and learning from others

    **Analysis Dimensions:**
    - Question quality and neutrality
    - Probe effectiveness and timing
    - Rapport building and maintenance
    - Professional boundary management
    - Time and flow management

    **Elicit:** "This analysis framework ensures continuous improvement through practice..."

13. **Personalized Improvement Planning**
    - Individual skill development priorities
    - Targeted practice recommendations
    - Advanced challenge selection
    - Real-world application strategies

    **Development Areas:**
    - Technical skills (questioning, probing, listening)
    - Interpersonal skills (rapport, empathy, boundaries)
    - Cognitive skills (synthesis, pattern recognition, decision-making)
    - Professional skills (ethics, time management, stakeholder communication)

    **Elicit:** "Based on simulation results, here's your personalized development plan..."

### Phase 6: Implementation & Transfer
**MANDATORY ELICITATION**

14. **Real-World Preparation**
    - Final preparation checklist
    - Confidence assessment and building
    - Backup plan development
    - Support system activation

    **Preparation Elements:**
    - Interview kit assembly and testing
    - Emergency contact and escalation procedures
    - Self-care and stress management planning
    - Quality assurance protocol review

    **Elicit:** "This preparation ensures smooth transition from simulation to real interviews..."

15. **Ongoing Support System**
    - Peer consultation protocols
    - Expert mentorship access
    - Real-time support during actual interviews
    - Continuous learning community

    **Support Mechanisms:**
    - Pre-interview preparation sessions
    - Post-interview debriefing and learning
    - Skill refresher training
    - Advanced technique workshops

    **Elicit:** "This support system maintains skill development beyond initial training..."

## Simulation Quality Standards

**For each simulation, ensure:**

1. **Realistic Scenarios**
   - Based on actual interview challenges
   - Appropriate complexity for skill level
   - Multiple pathways and outcomes possible

2. **Safe Learning Environment**
   - Psychological safety for making mistakes
   - Constructive feedback focus
   - Growth mindset emphasis

3. **Skill Transfer Focus**
   - Clear connection to real-world application
   - Practice with actual tools and materials
   - Progressive complexity building

4. **Measurable Learning**
   - Observable skill improvements
   - Specific feedback on performance
   - Clear next steps for development

## Persona Development Guidelines

**Creating Effective Practice Personas:**

- **Background Authenticity**: Base on real participant types from target population
- **Response Patterns**: Consistent with personality and background
- **Challenge Gradation**: Progressive difficulty for skill building
- **Cultural Sensitivity**: Respectful representation of diverse populations
- **Scenario Flexibility**: Adaptable to different research topics and contexts

## Technology Requirements

**Simulation Infrastructure:**

- **Recording Capability**: Video/audio capture for review and analysis
- **Role-Play Platforms**: Video conferencing with screen sharing and breakout rooms
- **Feedback Tools**: Real-time annotation and scoring systems
- **Progress Tracking**: Skill development dashboards and analytics
- **Resource Library**: Persona scripts, scenario descriptions, and coaching guides

## Assessment & Certification

**Skill Validation Approach:**

- **Competency Checklists**: Observable behaviors and skills
- **Scenario-Based Testing**: Performance in challenging situations
- **Peer Evaluation**: 360-degree feedback from simulation partners
- **Self-Reflection**: Critical analysis of own performance and growth areas
- **Expert Review**: Final assessment by experienced interview professionals

## Elicitation Methods Available

When user selects options 2-9:

2. **Immersive Role-Play Deep Dive** - Extended character-based simulation
3. **Video Analysis Workshop** - Detailed review of recorded simulations
4. **Peer Learning Circles** - Group-based skill development sessions
5. **Expert Mentorship Session** - One-on-one coaching with interview masters
6. **Real-Time Challenge Injection** - Dynamic scenario adaptation during simulation
7. **Cross-Cultural Competency Building** - Specialized diversity and inclusion practice
8. **Advanced Technique Masterclass** - Expert-level interviewing skill development
9. **Simulation Design Workshop** - Create custom scenarios for specific research contexts

## Error Recovery

If issues arise during simulation:
- Simulation too overwhelming → Reduce complexity and add more support
- Participant personas unrealistic → Revise based on actual target population
- Skills not transferring → Increase real-world practice integration
- Feedback too harsh → Emphasize growth mindset and psychological safety
- Technology barriers → Simplify tools and provide additional training

## Success Criteria

✅ Multiple simulation scenarios completed successfully
✅ Observable skill improvement across practice sessions
✅ Confidence in handling challenging interview situations
✅ Smooth technology and logistics management
✅ Professional and ethical interviewing practices demonstrated
✅ Ready for real-world interview implementation
✅ Support systems activated for ongoing development

## CRITICAL REMINDERS

**❌ NEVER:**
- Run simulations without clear learning objectives
- Skip elicitation points in favor of efficiency
- Use unrealistic or stereotypical participant personas
- Provide harsh or discouraging feedback
- Simulate without considering psychological safety

**✅ ALWAYS:**
- Use exact 1-9 format when elicit: true
- Explain simulation value and learning rationale
- Create safe environments for making mistakes
- Focus on specific, actionable skill development
- Connect simulation learning to real-world application