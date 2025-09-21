<!-- Powered by User Research System -->

# Create Presentation

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **DISABLE ALL EFFICIENCY OPTIMIZATIONS** - This workflow requires full user interaction
2. **MANDATORY STEP-BY-STEP EXECUTION** - Each phase must be processed sequentially with user feedback
3. **ELICITATION IS REQUIRED** - When `elicit: true`, you MUST use the 1-9 format and wait for user response
4. **NO SHORTCUTS ALLOWED** - Presentations must be systematically crafted for maximum impact

**VIOLATION INDICATOR:** If you create a complete presentation without user interaction at elicitation points, you have violated this workflow.

## Task Configuration

```yaml
task:
  name: Create Presentation
  id: create-presentation
  description: Generate compelling presentation deck from research findings
  version: 1.0
  dependencies:
    templates:
      - presentation-deck-tmpl.yaml
      - insight-cards-tmpl.yaml
    data:
      - stakeholder-personas.md
      - narrative-frameworks.md
      - visualization-guidelines.md
    inputs:
      - Research findings and insights
      - Executive summary
      - Key recommendations
      - Data visualizations
      - Persona profiles and journey maps
      - Statistical analysis results
  outputs:
    - Presentation deck (15-30 slides)
    - Speaker notes and talking points
    - Handout materials
    - Interactive presentation version
    - Stakeholder-specific variants
```

## Phase 1: Presentation Strategy & Audience Analysis

### 1.1 Audience & Context Definition
**elicit: true**

Define presentation audience and context:

**Presentation Context Analysis:**
```markdown
## Audience Characteristics
- Primary: [C-level, Product Teams, Board, etc.]
- Secondary: [Supporting attendees]
- Decision makers: [Key influencers]
- Technical level: [High/Medium/Low]
- Research familiarity: [Expert/Informed/Novice]

## Presentation Setting
- Format: [In-person/Virtual/Hybrid]
- Duration: [15/30/45/60 minutes]
- Q&A time: [5/10/15 minutes]
- Room size: [Intimate/Medium/Large/Auditorium]
- Technology: [Projector/TV/Laptop/Mobile]

## Desired Outcomes
- Primary goal: [Inform/Persuade/Approve/Fund]
- Secondary goals: [Build awareness/Generate discussion]
- Success metrics: [Decisions made/Actions taken]
- Follow-up actions: [Next steps expected]
```

**Audience Persona Mapping:**
- **CEO/Executive:** Strategic focus, ROI emphasis, competitive implications
- **Product Leaders:** User insights, feature priorities, roadmap impact
- **Engineering Teams:** Technical feasibility, implementation complexity
- **Marketing:** Customer segments, messaging opportunities, positioning
- **Sales:** Customer objections, value propositions, competitive advantages

Present audience analysis and context definition.

**Elicitation Required:**
1. Proceed to content strategy
2. Adjust for executive audience
3. Focus on technical details
4. Emphasize business impact
5. Add competitive context
6. Include user stories
7. Highlight quick wins
8. Frame as transformation
9. Customize for specific group

### 1.2 Message Architecture
**elicit: true**

Design core message hierarchy:

**Primary Message Framework:**
```markdown
## Central Thesis (30 seconds)
"Based on research with [N] participants, we discovered [KEY INSIGHT]
that presents a [$X opportunity/critical risk] requiring [SPECIFIC ACTION]
to [ACHIEVE OUTCOME]."

## Supporting Pillars (3-5 key points)
1. **Discovery:** What we found that surprised us
2. **Implication:** What this means for our business
3. **Opportunity:** What's possible if we act
4. **Action:** What we need to do
5. **Timeline:** When we need to act

## Evidence Foundation
- Quantitative data: [Statistics, metrics, trends]
- Qualitative insights: [Quotes, stories, observations]
- Visual proof: [Charts, journey maps, personas]
- Comparative analysis: [Benchmarks, before/after]
```

**Message Testing:**
- Elevator pitch (30 seconds)
- Executive summary (2 minutes)
- Full presentation (target duration)
- Q&A preparation (likely questions)

Present message architecture with hierarchy visualization.

**Elicitation Required:**
1. Proceed to narrative structure
2. Simplify the message
3. Add urgency factors
4. Strengthen evidence base
5. Include risk framing
6. Add competitive angle
7. Emphasize transformation
8. Include customer voice
9. Create multiple variants

### 1.3 Narrative Framework Selection
**elicit: true**

Choose optimal storytelling approach:

**Narrative Framework Options:**

**1. Problem-Solution Arc**
```markdown
- Current State: Pain points and challenges
- Discovery: What research revealed
- Solution: Recommended actions
- Future State: Vision of success
```

**2. Hero's Journey**
```markdown
- Call to Adventure: Business challenge
- Trials: Research discoveries
- Revelation: Key insights
- Return: Transformed recommendations
```

**3. Three-Act Structure**
```markdown
- Act 1: Setup (context and questions)
- Act 2: Conflict (findings and tensions)
- Act 3: Resolution (recommendations and vision)
```

**4. Data-Driven Discovery**
```markdown
- Hypothesis: What we thought we'd find
- Method: How we investigated
- Discovery: What we actually found
- Implications: What this changes
```

**5. Transformation Story**
```markdown
- Before: Current user experience
- Journey: Research process and insights
- After: Improved user experience
- Impact: Business value created
```

Present narrative framework options with audience fit analysis.

**Elicitation Required:**
1. Proceed with selected framework
2. Combine multiple approaches
3. Create custom narrative
4. Add emotional elements
5. Include user journey perspective
6. Emphasize business transformation
7. Focus on competitive advantage
8. Build tension and resolution
9. Design interactive storytelling

## Phase 2: Slide Architecture & Content Planning

### 2.1 Slide Flow Design
**elicit: true**

Design optimal slide sequence and flow:

**Presentation Structure (Example: 20-slide deck):**
```markdown
## Opening (Slides 1-3)
1. Title slide with compelling hook
2. Agenda and expected outcomes
3. Research overview and credibility

## Context Setting (Slides 4-6)
4. Business context and challenge
5. Research questions and approach
6. Participant overview and methodology

## Core Findings (Slides 7-14)
7. Key finding #1 + evidence
8. Key finding #2 + evidence
9. Key finding #3 + evidence
10. Cross-cutting insights synthesis
11. User personas revealed
12. Customer journey insights
13. Opportunity quantification
14. Risk assessment if no action

## Recommendations (Slides 15-18)
15. Strategic recommendations overview
16. Quick wins (immediate actions)
17. Implementation roadmap
18. Expected ROI and success metrics

## Closing (Slides 19-20)
19. Call to action and next steps
20. Questions and discussion
```

**Flow Optimization:**
- Information density per slide
- Visual-to-text ratio
- Transition logic between slides
- Pause points for discussion
- Interactive elements placement

Present slide architecture with flow visualization.

**Elicitation Required:**
1. Proceed to content development
2. Adjust slide count
3. Reorder for impact
4. Add more context slides
5. Emphasize findings section
6. Expand recommendations
7. Include appendix slides
8. Add interactive breaks
9. Create modular structure

### 2.2 Visual Hierarchy & Design Principles
**elicit: true**

Establish visual design framework:

**Design Principles:**
```markdown
## Visual Hierarchy
- Slide titles: 44pt, bold, primary color
- Section headers: 36pt, medium weight
- Body text: 24pt minimum, high contrast
- Captions: 18pt, secondary color
- Maximum 6 lines of text per slide

## Color Strategy
- Primary palette: Brand colors
- Data visualization: Accessible colors
- Emphasis: High contrast accents
- Background: Professional neutrals
- Consistent color meaning

## Typography
- Headings: [Brand font/Professional sans-serif]
- Body text: [Readable sans-serif]
- Data labels: [Clean, technical font]
- Consistent font hierarchy

## Layout Principles
- One key message per slide
- Visual breathing room (30% white space)
- Left-to-right reading flow
- Consistent element placement
- Progressive disclosure of information
```

**Slide Templates:**
- Title slide template
- Section divider template
- Content slide template
- Data visualization template
- Quote/testimonial template
- Call-to-action template

Present design framework and template specifications.

**Elicitation Required:**
1. Proceed to content creation
2. Adjust visual hierarchy
3. Modify color strategy
4. Change typography choices
5. Add brand elements
6. Include animation guidelines
7. Create custom templates
8. Add accessibility features
9. Design interactive elements

### 2.3 Data Visualization Strategy
**elicit: true**

Plan impactful data presentations:

**Visualization Portfolio:**
```markdown
## The Money Chart
- Single most impactful finding
- Clear business value demonstration
- Memorable and quotable
- Executive-friendly complexity

## Comparison Visuals
- Before/after scenarios
- Us vs. competitors
- Current vs. future state
- Expected vs. actual results

## Process Flows
- User journey maps
- Research methodology
- Implementation timeline
- Decision-making process

## Evidence Charts
- Statistical summaries
- Sentiment analysis
- Demographic breakdowns
- Behavioral patterns

## Opportunity Mapping
- Market size visualizations
- Priority matrices
- Risk/reward quadrants
- Investment scenarios
```

**Chart Design Standards:**
- Maximum 5 data series per chart
- Clear, descriptive titles
- Annotated key insights
- Consistent color coding
- Source attribution
- Accessibility compliance

Present visualization strategy with chart inventory.

**Elicitation Required:**
1. Proceed to slide development
2. Add more chart types
3. Simplify visualizations
4. Enhance story flow
5. Include interactive charts
6. Add animation effects
7. Create infographic elements
8. Include photo documentation
9. Design custom graphics

## Phase 3: Slide Content Development

### 3.1 Opening Slides Creation
**elicit: true**

Craft compelling presentation opening:

**Title Slide Components:**
```markdown
## Title Slide Design
- Compelling presentation title
- Subtitle with key value proposition
- Research timeframe and scope
- Presenter name and title
- Date and confidentiality level
- Company branding elements

Title Options:
1. "[Topic] Research: Unlocking $X Opportunity"
2. "Customer Insights That Will Transform [Product/Service]"
3. "What [N] Customers Told Us About [Challenge]"
4. "Research-Driven Path to [Desired Outcome]"
```

**Agenda Slide:**
```markdown
## Presentation Flow
1. Research Overview (5 min)
2. Key Discoveries (15 min)
3. Strategic Implications (10 min)
4. Recommended Actions (8 min)
5. Q&A Discussion (7 min)

Expected Outcome: [Clear decision/next steps]
```

**Research Credibility Slide:**
```markdown
## Research Foundation
- Methodology: [Qualitative/Quantitative/Mixed]
- Participants: [N] customers across [segments]
- Timeline: [Duration] over [period]
- Coverage: [Geographic/demographic scope]
- Confidence: [Statistical/evidence level]
```

Present opening slides with impact assessment.

**Elicitation Required:**
1. Proceed to context slides
2. Strengthen the hook
3. Adjust agenda timing
4. Add credibility elements
5. Include preview of insights
6. Add urgency framing
7. Include stakeholder benefits
8. Add interactive opening
9. Create multiple title options

### 3.2 Findings Presentation Slides
**elicit: true**

Develop core findings presentation:

**Finding Slide Template:**
```markdown
## Finding [#]: [Compelling Headline]

### What We Discovered
[One clear sentence describing the finding]

### The Evidence
- Quantitative: [X% of participants, statistical significance]
- Qualitative: "[Powerful representative quote]"
- Frequency: [How often this occurred]
- Confidence: [High/Medium/Low with reasoning]

### What This Means
[Business implication in concrete terms]

### Visual Evidence
[Chart, diagram, or photo supporting the finding]
```

**Story Flow Between Findings:**
- Logical progression from surface to deep insights
- Building tension toward key revelations
- Connecting individual findings to larger patterns
- Transitional slides that synthesize themes

**Evidence Presentation:**
- Balance of quantitative and qualitative data
- Memorable quotes that bring findings to life
- Visual proof that supports claims
- Clear confidence indicators

Present findings slide structure and evidence strategy.

**Elicitation Required:**
1. Proceed to insights synthesis
2. Reorder findings by impact
3. Add more visual evidence
4. Strengthen story connections
5. Include user voice more
6. Add statistical validation
7. Include comparative data
8. Add emotional elements
9. Create interactive findings

### 3.3 Recommendations & Action Slides
**elicit: true**

Design compelling recommendations presentation:

**Recommendation Slide Structure:**
```markdown
## Recommendation [#]: [Action-Oriented Title]

### The Opportunity
[What this addresses and potential value]

### Recommended Action
[Specific, concrete steps to take]

### Implementation Approach
- Phase 1: [Immediate actions - 0-30 days]
- Phase 2: [Short-term initiatives - 1-3 months]
- Phase 3: [Long-term transformation - 3-12 months]

### Expected Impact
- User experience: [Improvement description]
- Business metrics: [Specific KPI improvements]
- Competitive advantage: [Differentiation gained]

### Investment Required
- Resources: [People, time, budget]
- Timeline: [Duration to full implementation]
- ROI: [Expected return and payback period]
```

**Prioritization Visualization:**
```markdown
┌─────────────────────────────────┐
│         IMPACT vs EFFORT         │
├─────────────────────────────────┤
│ High Impact │                   │
│            │  DO FIRST  │  DO NEXT │
│            │     🚀     │    📈    │
│ ─────────────────────────────── │
│            │  DO LATER  │ DON'T DO │
│            │     ⏰     │    🚫    │
│ Low Impact │                   │
│           Low Effort   High Effort│
└─────────────────────────────────┘
```

Present recommendations structure with prioritization framework.

**Elicitation Required:**
1. Proceed to closing slides
2. Add more detail to actions
3. Strengthen business case
4. Include quick wins emphasis
5. Add risk mitigation
6. Include success metrics
7. Add implementation support
8. Include pilot options
9. Create decision framework

## Phase 4: Speaker Support & Delivery Preparation

### 4.1 Speaker Notes Development
**elicit: true**

Create comprehensive speaker notes:

**Speaker Notes Template:**
```markdown
## Slide [#]: [Title]

### Key Message (30 seconds)
[Core point to communicate]

### Talking Points (2-3 minutes)
- Opening hook: [Attention-grabbing statement]
- Main content: [2-3 bullet points with details]
- Evidence: [Data points and quotes to mention]
- Transition: [Bridge to next slide]

### Anticipated Questions
Q: [Likely question]
A: [Prepared response with supporting data]

### Time Check
- Target time: [X minutes]
- Critical points: [Must-mention items]
- Optional details: [If time permits]

### Backup Information
- Additional data: [Extra evidence if needed]
- Alternative explanations: [Different ways to explain]
- Related insights: [Connected findings]
```

**Presentation Flow Notes:**
- Slide timing guidelines
- Pause points for questions
- Interactive elements cues
- Technology checkpoints
- Backup slide references

Present speaker notes framework and content strategy.

**Elicitation Required:**
1. Proceed to handout creation
2. Add more detail
3. Include storytelling cues
4. Add interaction prompts
5. Include body language notes
6. Add energy management
7. Include contingency plans
8. Add audience engagement
9. Create custom coaching

### 4.2 Handout Materials Creation
**elicit: true**

Design supporting handout materials:

**Handout Package:**
```markdown
## Executive Summary Handout (1-2 pages)
- Key findings at-a-glance
- Strategic recommendations
- Implementation timeline
- Contact information

## Detailed Findings Reference (3-4 pages)
- Complete finding summaries
- Supporting evidence
- Statistical data
- Key quotes

## Implementation Toolkit (2-3 pages)
- Quick wins checklist
- Success metrics tracker
- Resource requirements
- Timeline template

## FAQ Document (1-2 pages)
- Anticipated questions and answers
- Additional resources
- Follow-up contacts
- Next steps guidance
```

**Design Considerations:**
- Consistent with presentation visual design
- Standalone readability
- Print-friendly formatting
- Easy reference structure
- Professional binding/packaging

Present handout strategy and content overview.

**Elicitation Required:**
1. Proceed to practice preparation
2. Expand handout content
3. Add interactive worksheets
4. Include assessment tools
5. Add implementation guides
6. Include resource lists
7. Add contact directories
8. Create digital versions
9. Design custom materials

### 4.3 Practice & Rehearsal Preparation
**elicit: true**

Plan presentation practice and refinement:

**Practice Schedule:**
```markdown
## Rehearsal Plan
- Solo practice: [X sessions, Y hours]
- Peer review: [Feedback from colleagues]
- Stakeholder preview: [Key audience members]
- Technical rehearsal: [Equipment and setup]
- Final run-through: [Complete presentation]

## Practice Focus Areas
- Opening impact and confidence
- Key message clarity
- Transition smoothness
- Data presentation clarity
- Closing call-to-action strength
- Q&A preparation

## Feedback Collection
- Content clarity and accuracy
- Visual design effectiveness
- Flow and pacing
- Engagement and energy
- Persuasiveness of recommendations
```

**Presentation Skills Checklist:**
- Voice projection and pacing
- Body language and gestures
- Eye contact and engagement
- Technology comfort
- Confidence and authority
- Question handling skills

Present practice plan and skill development focus.

**Elicitation Required:**
1. Proceed to final production
2. Add more practice sessions
3. Include specific skill coaching
4. Add audience simulation
5. Include video review
6. Add expert feedback
7. Include stress testing
8. Add backup preparations
9. Create custom coaching plan

## Phase 5: Production & Final Assembly

### 5.1 Slide Design Implementation
**elicit: true**

Execute final slide design and production:

**Production Checklist:**
```markdown
## Visual Design Implementation
- [ ] Brand compliance verification
- [ ] Typography consistency check
- [ ] Color accessibility validation
- [ ] Image quality optimization
- [ ] Chart clarity and accuracy
- [ ] Animation timing (if used)
- [ ] Slide transitions

## Content Finalization
- [ ] Spelling and grammar check
- [ ] Data accuracy verification
- [ ] Citation and source validation
- [ ] Legal and compliance review
- [ ] Confidentiality marking
- [ ] Version control implementation
```

**Technical Specifications:**
- File format optimization (PPTX, PDF, HTML)
- Resolution for different display types
- Font embedding for portability
- Image compression for file size
- Backup format creation

Present production timeline and quality standards.

**Elicitation Required:**
1. Proceed to stakeholder versions
2. Add more quality checks
3. Include accessibility testing
4. Add technical optimization
5. Include brand review
6. Add legal compliance
7. Include backup formats
8. Add version control
9. Create custom specifications

### 5.2 Stakeholder-Specific Versions
**elicit: true**

Create tailored presentation variants:

**Audience Variations:**
```markdown
## Executive Version (15 slides, 20 minutes)
- Focus: Strategic implications and ROI
- Depth: High-level with key details
- Evidence: Business metrics emphasis
- Recommendations: Investment decisions

## Product Team Version (25 slides, 45 minutes)
- Focus: User insights and implications
- Depth: Detailed findings and evidence
- Evidence: User quotes and journey maps
- Recommendations: Feature and design priorities

## Technical Team Version (20 slides, 30 minutes)
- Focus: Implementation requirements
- Depth: Technical specifications
- Evidence: Usage data and performance
- Recommendations: Architecture and development
```

**Customization Elements:**
- Slide order adjustment
- Content depth modification
- Visual emphasis changes
- Timing and pacing variants
- Q&A preparation differences

Present stakeholder variant strategy.

**Elicitation Required:**
1. Proceed to delivery formats
2. Add more audience types
3. Include modular sections
4. Add interactive elements
5. Include role-specific insights
6. Add custom visualizations
7. Include specialized content
8. Add presentation alternatives
9. Create adaptive presentations

### 5.3 Multi-Format Delivery Preparation
**elicit: true**

Prepare presentation for various delivery contexts:

**Delivery Format Options:**
```markdown
## Live Presentation
- Full interactive deck
- Speaker notes loaded
- Backup slides prepared
- Technology tested
- Handouts printed

## Virtual Presentation
- Screen-sharing optimized
- Larger fonts for readability
- Simplified animations
- Chat interaction planned
- Recording preparation

## Self-Guided Presentation
- Detailed slide notes
- Voice-over audio (optional)
- Interactive navigation
- Progress indicators
- Contact information

## Print Version
- High-resolution images
- Print-friendly colors
- Page optimization
- Binding considerations
- Handout integration
```

**Technology Contingencies:**
- Offline presentation backup
- Multiple file format options
- Equipment compatibility testing
- Internet connectivity alternatives
- Mobile device preparation

Present delivery preparation strategy.

**Elicitation Required:**
1. Complete presentation creation
2. Add more delivery options
3. Include accessibility features
4. Add technology backups
5. Include remote capabilities
6. Add interactive features
7. Include multilingual options
8. Add streaming capabilities
9. Create custom delivery solutions

## Phase 6: Quality Assurance & Testing

### 6.1 Content Validation
**elicit: true**

Validate presentation accuracy and effectiveness:

**Content Review Checklist:**
```markdown
## Accuracy Validation
- [ ] Data points verified against source
- [ ] Statistical calculations confirmed
- [ ] Quotes attributed correctly
- [ ] Citations complete and accurate
- [ ] Methodology description precise
- [ ] Conclusions supported by evidence

## Message Clarity
- [ ] Key messages easily understood
- [ ] Technical terms defined
- [ ] Acronyms spelled out first use
- [ ] Complex concepts explained clearly
- [ ] Visual aids support understanding
- [ ] Call-to-action specific and clear

## Flow and Logic
- [ ] Logical progression of ideas
- [ ] Smooth transitions between slides
- [ ] Appropriate pacing and timing
- [ ] Compelling narrative arc
- [ ] Strong opening and closing
- [ ] Balanced content distribution
```

Present validation results and issue resolution plan.

**Elicitation Required:**
1. Proceed to stakeholder preview
2. Add more validation steps
3. Include external review
4. Add fact-checking process
5. Include expert validation
6. Add statistical review
7. Include legal compliance
8. Add accessibility audit
9. Create custom validation

### 6.2 Stakeholder Preview & Feedback
**elicit: true**

Conduct stakeholder preview and incorporate feedback:

**Preview Process:**
```markdown
## Stakeholder Review Sessions
- Key decision makers preview
- Subject matter expert review
- End-user representative feedback
- Technical accuracy validation
- Business alignment confirmation

## Feedback Collection
- Structured feedback forms
- Content accuracy assessment
- Message clarity evaluation
- Visual design effectiveness
- Recommendation feasibility
- Implementation readiness

## Iteration Process
- Feedback prioritization
- Critical issue resolution
- Enhancement implementation
- Second review cycle (if needed)
- Final approval process
```

**Feedback Integration Strategy:**
- Must-fix issues (accuracy, compliance)
- Should-fix issues (clarity, flow)
- Nice-to-fix issues (enhancement, polish)
- Won't-fix issues (scope, resource constraints)

Present preview process and feedback integration plan.

**Elicitation Required:**
1. Finalize presentation
2. Add more reviewers
3. Include customer preview
4. Add board-level review
5. Include competitive review
6. Add market validation
7. Include regulatory review
8. Add partner feedback
9. Create comprehensive review

## Output Standards

### Presentation Quality Criteria

**Excellence Standards:**
- Clarity: Messages easily understood by target audience
- Impact: Compelling evidence and persuasive recommendations
- Professional: Publication-ready visual design and content
- Actionable: Clear next steps and implementation guidance
- Memorable: Key insights stick with audience
- Engaging: Maintains attention throughout delivery

### Deliverable Package Components

**Complete Package:**
1. Main presentation deck (15-30 slides)
2. Executive summary version (5-10 slides)
3. Detailed appendix slides (10-20 slides)
4. Speaker notes and talking points
5. Handout materials
6. Practice guide and tips
7. Q&A preparation document
8. Multiple format versions (PPTX, PDF, HTML)

## Common Presentation Failures

**Avoid These Pitfalls:**
1. **Information Overload** - Too much content per slide
2. **Weak Opening** - Fails to grab attention immediately
3. **Buried Insights** - Key findings hidden in details
4. **Poor Visuals** - Charts confuse rather than clarify
5. **Weak Call-to-Action** - Unclear what audience should do
6. **No Story Arc** - Random collection of facts
7. **Technical Issues** - Untested technology problems
8. **Poor Timing** - Rushing through or running long

## Success Indicators

Presentation succeeds when:
1. Audience engages throughout delivery
2. Key messages are remembered and repeated
3. Questions focus on "how" not "why"
4. Decisions are made or next steps agreed
5. Stakeholders take ownership of recommendations
6. Follow-up meetings are scheduled
7. Implementation begins promptly

## CRITICAL REMINDER

This is an INTERACTIVE WORKFLOW requiring user participation at each elicitation point. The 1-9 option format is MANDATORY. Creating complete presentations without user interaction violates this task specification.