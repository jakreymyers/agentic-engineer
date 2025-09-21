# Establish Research Project

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:

1. **DISABLE ALL EFFICIENCY OPTIMIZATIONS** - This workflow requires full user interaction
2. **MANDATORY STEP-BY-STEP EXECUTION** - Each section must be processed sequentially with user feedback
3. **ELICITATION IS REQUIRED** - When `elicit: true`, you MUST use the 1-9 format and wait for user response
4. **NO SHORTCUTS ALLOWED** - Research projects cannot be established without following this workflow

**VIOLATION INDICATOR:** If you create a complete research brief without user interaction, you have violated this workflow.

## Task Configuration

```yaml
elicit: true
template: research-brief-tmpl.yaml
output: research-outputs/project-brief.md
```

## Critical: Template Discovery

If research-brief-tmpl.yaml has not been provided, load it from context/user-research/templates/ or ask the user to provide research objectives directly.

## CRITICAL: Mandatory Elicitation Format

**When `elicit: true`, this is a HARD STOP requiring user interaction:**

**YOU MUST:**

1. Present section content
2. Provide detailed rationale (explain trade-offs, assumptions, decisions made)
3. **STOP and present numbered options 1-9:**
   - **Option 1:** Always "Proceed to next section"
   - **Options 2-9:** Select 8 methods from elicitation techniques
   - End with: "Select 1-9 or just type your question/feedback:"
4. **WAIT FOR USER RESPONSE** - Do not proceed until user selects option or provides feedback

**WORKFLOW VIOLATION:** Creating content for elicit=true sections without user interaction violates this task.

## Workflow Steps

### 1. Define Research Objectives
**ELICIT: true**

Draft the research objectives covering:
- **Business Goals Alignment**: How does this research support organizational objectives?
- **Research Questions**: What specific questions need answering?
- **Success Criteria**: How will we measure research success?
- **Expected Outcomes**: What decisions will this research inform?

Present draft and rationale, then provide 1-9 elicitation options.

### 2. Stakeholder Mapping
**ELICIT: true**

Identify and map stakeholders:
- **Primary Stakeholders**: Decision makers who will act on findings
- **Secondary Stakeholders**: Teams affected by research outcomes
- **Research Consumers**: Who needs access to findings?
- **Communication Plan**: How/when to update stakeholders
- **Review Gates**: Key approval points and reviewers

Present stakeholder map with rationale, then provide 1-9 elicitation options.

### 3. Resource Planning
**ELICIT: true**

Plan research resources:
- **Timeline**: Key milestones and deadlines
- **Budget**: Participant incentives, tools, team time
- **Team Assignment**: Roles and responsibilities
- **Tools & Infrastructure**: Required research tools
- **Risk Mitigation**: Potential blockers and contingencies

Present resource plan with rationale, then provide 1-9 elicitation options.

### 4. Scope Definition
**ELICIT: true**

Define research scope:
- **In Scope**: What will be investigated
- **Out of Scope**: What won't be covered
- **Constraints**: Limitations and boundaries
- **Dependencies**: What's needed from other teams
- **Assumptions**: Key assumptions being made

Present scope definition with rationale, then provide 1-9 elicitation options.

## Elicitation Points Summary

After each section:
1. Review and refine content based on user feedback
2. Validate alignment with overall objectives
3. Confirm feasibility and resources
4. Document any changes or concerns

## Decision Framework

For each decision point:
- **Strategic Impact**: High priority if directly impacts product strategy
- **User Impact**: High priority if affects core user experience
- **Business Value**: Consider ROI and resource investment
- **Feasibility**: Balance ideal with practical constraints
- **Timeline**: Urgent vs. important considerations

## Quality Checkpoints

Before finalizing:
- ✓ Research questions are specific and answerable
- ✓ Stakeholders have been consulted
- ✓ Resources are confirmed available
- ✓ Timeline is realistic
- ✓ Success metrics are measurable
- ✓ Ethical considerations addressed

## Output Format

The final research brief should include:
```markdown
# Research Project Brief: [Project Name]

## Executive Summary
[1-2 paragraphs summarizing the research initiative]

## Research Objectives
### Business Goals
- [Goal 1]
- [Goal 2]

### Research Questions
1. [Primary question]
2. [Secondary question]

### Success Criteria
- [Criterion 1]
- [Criterion 2]

## Stakeholder Map
[Table of stakeholders, roles, and involvement]

## Resource Plan
### Timeline
[Gantt chart or milestone list]

### Budget
[Budget breakdown]

### Team
[RACI matrix]

## Scope
### In Scope
- [Item 1]

### Out of Scope
- [Item 1]

## Next Steps
1. [Immediate action]
2. [Follow-up action]
```

## YOLO Mode

User can type `#yolo` to toggle to YOLO mode (process all sections at once) - NOT RECOMMENDED for research projects.

## CRITICAL REMINDERS

**❌ NEVER:**
- Skip stakeholder consultation
- Proceed without clear research questions
- Ignore resource constraints
- Bypass ethical considerations

**✅ ALWAYS:**
- Use exact 1-9 format when elicit: true
- Validate objectives with stakeholders
- Consider participant welfare
- Document all decisions and rationale
- End with "Select 1-9 or just type your question/feedback:"