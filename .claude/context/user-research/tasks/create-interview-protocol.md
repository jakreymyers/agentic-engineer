# Create Interview Protocol

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:

1. **DISABLE ALL EFFICIENCY OPTIMIZATIONS** - This workflow requires full user interaction
2. **MANDATORY STEP-BY-STEP EXECUTION** - Each section must be processed sequentially with user feedback
3. **ELICITATION IS REQUIRED** - When `elicit: true`, you MUST use the 1-9 format and wait for user response
4. **NO SHORTCUTS ALLOWED** - Complete protocols cannot be created without following this workflow

**VIOLATION INDICATOR:** If you create a complete interview protocol without user interaction, you have violated this workflow.

## Task Configuration

```yaml
task:
  id: create-interview-protocol
  name: Create Interview Execution Protocol
  type: interactive-protocol-development
  elicit: true
  template: interview-protocol-tmpl.yaml
  output: docs/research/interviews/interview-protocol-{{project}}.md
  estimated_time: 75-90 minutes
```

## CRITICAL: Mandatory Elicitation Format

**When `elicit: true`, this is a HARD STOP requiring user interaction:**

**YOU MUST:**

1. Present protocol section content
2. Provide detailed rationale (explain protocol necessity, risk mitigation, quality assurance)
3. **STOP and present numbered options 1-9:**
   - **Option 1:** Always "Proceed to next protocol section"
   - **Options 2-9:** Select 8 methods from protocol development techniques
   - End with: "Select 1-9 or just type your question/feedback:"
4. **WAIT FOR USER RESPONSE** - Do not proceed until user selects option or provides feedback

**WORKFLOW VIOLATION:** Creating content for elicit=true sections without user interaction violates this task.

## Workflow Steps

### Phase 1: Protocol Foundation & Standards
**MANDATORY ELICITATION**

1. **Protocol Scope & Objectives**
   - Define protocol coverage (pre-interview through post-analysis)
   - Establish quality standards for interview execution
   - Identify risk areas requiring standardized procedures
   - Set compliance requirements (IRB, legal, organizational)

   **Rationale:** Comprehensive protocols ensure consistent, high-quality data collection while protecting both participants and researchers from preventable risks.

   **Elicit:** "I've identified these critical protocol areas that need standardization..."

2. **Interviewer Competency Framework**
   - Required skills and knowledge for interview execution
   - Training completion requirements
   - Certification or approval process
   - Ongoing competency maintenance standards

   **Competency Areas:**
   - Technical interviewing skills (questioning, probing, listening)
   - Interpersonal skills (rapport, empathy, boundary management)
   - Ethical decision-making (consent, confidentiality, participant welfare)
   - Crisis management (distress, disclosure, emergency situations)

   **Elicit:** "This competency framework ensures interviewer readiness..."

### Phase 2: Pre-Interview Protocol
**MANDATORY ELICITATION FOR EACH STAGE**

3. **Participant Preparation Protocol**
   - Pre-interview communication sequence and timing
   - Information sharing (study overview, logistics, expectations)
   - Consent process and documentation requirements
   - Accessibility accommodation procedures

   **Timeline & Communications:**
   - Initial contact and screening (Day -7 to -14)
   - Confirmation and logistics (Day -3 to -5)
   - Reminder and final instructions (Day -1)
   - Day-of confirmation and tech check

   **Elicit:** "This preparation protocol ensures participant readiness and comfort..."

4. **Interviewer Preparation Protocol**
   - Research review and context preparation
   - Materials and technology setup checklist
   - Mental and emotional preparation procedures
   - Backup plan activation and testing

   **Preparation Elements:**
   - Participant background review (if available)
   - Discussion guide and probe bank review
   - Recording equipment and platform testing
   - Emergency contact information verification

   **Elicit:** "This interviewer preparation prevents technical and procedural issues..."

5. **Environment Setup Protocol**
   - Physical or virtual space configuration
   - Privacy and confidentiality measures
   - Technology testing and backup systems
   - Materials organization and accessibility

   **Setup Standards:**
   - Distraction-free environment for both parties
   - Reliable recording with backup systems
   - Comfortable temperature and lighting
   - Emergency contacts and procedures accessible

   **Elicit:** "This environment protocol creates optimal conditions for quality interviews..."

### Phase 3: Interview Execution Protocol
**MANDATORY ELICITATION FOR EACH PHASE**

6. **Opening Sequence Protocol**
   - Standardized welcome and introduction
   - Consent verification and recording initiation
   - Rapport building within time parameters
   - Transition to substantive content

   **Opening Script Elements:**
   - Professional but warm greeting
   - Study purpose without biasing (elevator pitch format)
   - Consent confirmation with opportunity for questions
   - Recording permission and backup consent
   - Timeline overview and break scheduling

   **Elicit:** "This opening protocol ensures consistent, professional starts..."

7. **Interview Flow Management Protocol**
   - Time allocation monitoring and adjustment procedures
   - Topic transition techniques and timing
   - Depth vs. breadth decision-making framework
   - Unexpected content handling procedures

   **Flow Management Rules:**
   - 25% time checkpoints for pacing assessment
   - Priority ranking system for time-constrained situations
   - Participant energy monitoring and response protocols
   - Natural transition identification and execution

   **Elicit:** "This flow protocol maintains quality while respecting time constraints..."

8. **Probing & Deep Dive Protocol**
   - Probe selection and timing decision tree
   - Depth escalation procedures and limits
   - Sensitive topic navigation protocols
   - Information saturation recognition

   **Probing Standards:**
   - Maximum 3 consecutive probes before topic shift
   - Participant comfort monitoring between probes
   - Emotional safety check protocols
   - Content richness vs. participant burden balance

   **Elicit:** "This probing protocol maximizes insight while protecting participants..."

### Phase 4: Crisis & Exception Management
**MANDATORY ELICITATION FOR EACH SCENARIO**

9. **Participant Distress Protocol**
   - Early distress recognition indicators
   - De-escalation and support procedures
   - Interview continuation vs. termination decisions
   - Follow-up care and resource provision

   **Distress Response Steps:**
   1. Immediate acknowledgment and validation
   2. Interview pause and check-in procedure
   3. Participant choice presentation (continue/pause/stop)
   4. Resource sharing and follow-up scheduling
   5. Documentation requirements for incident

   **Elicit:** "This distress protocol prioritizes participant welfare above research needs..."

10. **Disclosure & Mandatory Reporting Protocol**
    - Recognition of reportable disclosures
    - Legal and ethical obligations explanation
    - Reporting procedures and timelines
    - Participant support during process

    **Disclosure Categories:**
    - Imminent harm to self or others
    - Child or elder abuse
    - Legal violations requiring reporting
    - Professional misconduct in regulated fields

    **Elicit:** "This disclosure protocol balances legal obligations with participant trust..."

11. **Technical Failure Protocol**
    - Equipment malfunction recognition and response
    - Data recovery and backup procedures
    - Interview continuation vs. rescheduling decisions
    - Participant communication and expectation management

    **Technical Response Framework:**
    - Primary system failure (immediate backup activation)
    - Complete technology failure (manual notes and reschedule)
    - Partial data loss (participant consent for re-recording)
    - Platform issues (alternative communication methods)

    **Elicit:** "This technical protocol ensures data integrity despite equipment issues..."

### Phase 5: Closing & Post-Interview Protocol
**MANDATORY ELICITATION FOR EACH ELEMENT**

12. **Interview Conclusion Protocol**
    - Structured closing sequence and timing
    - Final opportunity for participant sharing
    - Next steps communication and expectations
    - Appreciation expression and relationship closure

    **Closing Elements:**
    - Summary check with participant
    - Final questions or additions invitation
    - Study timeline and results sharing
    - Contact information for follow-up questions
    - Compensation/incentive processing

    **Elicit:** "This closing protocol ensures participant satisfaction and clear expectations..."

13. **Immediate Post-Interview Protocol**
    - Data security and backup procedures
    - Initial reflection and note capture
    - Quality assessment and flags
    - Participant follow-up scheduling

    **Post-Interview Checklist:**
    - Recording file secure storage and backup
    - Interviewer reflection notes (within 30 minutes)
    - Technical issues documentation
    - Participant welfare assessment
    - Next session scheduling or study completion

    **Elicit:** "This post-interview protocol captures critical information while memory is fresh..."

14. **Data Processing Initiation Protocol**
    - File naming and organization standards
    - Transcription request and timeline
    - Initial analysis notes and observations
    - Quality control flag identification

    **Processing Standards:**
    - Standardized file naming convention
    - Metadata capture requirements
    - Transcription accuracy standards
    - Initial coding or categorization
    - Researcher bias acknowledgment notes

    **Elicit:** "This processing protocol ensures systematic, high-quality data management..."

### Phase 6: Quality Assurance & Compliance
**MANDATORY ELICITATION**

15. **Quality Monitoring Protocol**
    - Session quality assessment criteria
    - Peer review and feedback procedures
    - Continuous improvement identification
    - Performance tracking and development

    **Quality Indicators:**
    - Research objective coverage completeness
    - Participant engagement and comfort levels
    - Data richness and depth assessment
    - Protocol adherence evaluation
    - Ethical standard maintenance

    **Elicit:** "This monitoring protocol ensures consistent quality improvement..."

16. **Compliance Documentation Protocol**
    - Required documentation creation and storage
    - Audit trail maintenance procedures
    - Regulatory compliance verification
    - Stakeholder reporting requirements

    **Documentation Requirements:**
    - Consent forms and participant communications
    - Session notes and quality assessments
    - Incident reports and resolution actions
    - Protocol deviation logs and justifications
    - Training completion and competency records

    **Elicit:** "This documentation protocol ensures full compliance and accountability..."

## Protocol Risk Assessment

**High-Risk Scenarios Requiring Specific Protocols:**

1. **Vulnerable Populations**
   - Children, elderly, individuals with cognitive impairments
   - Enhanced consent procedures and capacity assessment
   - Additional safeguards and monitoring

2. **Sensitive Topics**
   - Trauma, illegal activities, personal failures
   - Specialized training requirements
   - Enhanced participant support resources

3. **High-Stakes Research**
   - Medical, legal, or financial decision-making research
   - Additional quality controls and verification
   - Expert review and oversight requirements

4. **Remote/Virtual Interviews**
   - Technology dependency and failure risks
   - Reduced environmental control
   - Privacy and confidentiality challenges

## Protocol Customization Guidelines

**Adapting Protocols for Specific Contexts:**

- **Research Type**: Adjust depth and formality based on exploratory vs. confirmatory research
- **Participant Population**: Modify language, pace, and cultural sensitivity
- **Topic Sensitivity**: Enhance support and safety measures for difficult topics
- **Interview Format**: Adapt for in-person, remote, phone, or group interviews
- **Organizational Requirements**: Incorporate institutional policies and procedures

## Training & Implementation

**Protocol Training Components:**

1. **Initial Training** (8-12 hours)
   - Protocol overview and rationale
   - Hands-on practice with scenarios
   - Role-playing and simulation
   - Competency assessment and certification

2. **Ongoing Development** (2-4 hours quarterly)
   - Protocol updates and improvements
   - Case study review and learning
   - Advanced technique development
   - Quality performance feedback

3. **Peer Support** (Ongoing)
   - Pre-interview consultation availability
   - Real-time support for challenging situations
   - Post-interview debriefing and learning
   - Community of practice participation

## Elicitation Methods Available

When user selects options 2-9:

2. **Risk Scenario Planning** - Comprehensive risk identification and mitigation
3. **Legal Compliance Review** - Detailed regulatory requirement analysis
4. **Cultural Adaptation Workshop** - Protocol modification for diverse populations
5. **Technology Integration Design** - Digital workflow and backup system development
6. **Crisis Simulation Training** - Practice with emergency and difficult situations
7. **Quality Metric Development** - Measurable standards and assessment criteria
8. **Stakeholder Alignment Session** - Protocol approval and buy-in process
9. **Implementation Pilot Testing** - Small-scale protocol testing and refinement

## Error Recovery

If issues arise during protocol development:
- Scope too broad → Focus on highest-risk areas first
- Compliance requirements unclear → Consult legal and IRB experts
- Protocol too rigid → Build in flexibility points and decision frameworks
- Training requirements excessive → Prioritize critical competencies
- Technology too complex → Simplify with robust backup options

## Success Criteria

✅ Comprehensive protocol covering all interview phases
✅ Clear procedures for high-risk and exception scenarios
✅ Quality assurance and compliance measures integrated
✅ Training materials and competency standards defined
✅ Risk mitigation strategies for identified vulnerabilities
✅ Stakeholder approval and implementation readiness
✅ Continuous improvement mechanisms established

## CRITICAL REMINDERS

**❌ NEVER:**
- Create protocols without considering actual implementation challenges
- Skip elicitation points for efficiency
- Develop overly rigid procedures that prevent good judgment
- Ignore legal, ethical, or organizational requirements
- Assume protocols will work without testing and refinement

**✅ ALWAYS:**
- Use exact 1-9 format when elicit: true
- Explain protocol rationale and risk mitigation value
- Balance standardization with necessary flexibility
- Consider diverse scenarios and edge cases
- Test protocols before full implementation