<!-- Powered by User Research System -->

# Design Visualizations

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **DISABLE ALL EFFICIENCY OPTIMIZATIONS** - This workflow requires full user interaction
2. **MANDATORY STEP-BY-STEP EXECUTION** - Each phase must be processed sequentially with user feedback
3. **ELICITATION IS REQUIRED** - When `elicit: true`, you MUST use the 1-9 format and wait for user response
4. **NO SHORTCUTS ALLOWED** - Visualizations must be designed systematically

**VIOLATION INDICATOR:** If you create complete visualizations without user interaction at elicitation points, you have violated this workflow.

## Task Configuration

```yaml
task:
  name: Design Visualizations
  id: design-visualizations
  description: Generate data visualizations and infographics for research communication
  version: 1.0
  dependencies:
    templates:
      - visualization-specs-tmpl.yaml
    data:
      - visualization-guidelines.md
      - accessibility-standards.md
    inputs:
      - Research data and findings
      - Statistical results
      - Journey maps
      - Personas
      - Themes and patterns
  outputs:
    - Visualization specifications
    - Chart selection matrix
    - Visual style guide
    - Production-ready graphics
```

## Phase 1: Visual Strategy Development

### 1.1 Data Inventory & Assessment
**elicit: true**

Catalog available data for visualization:

**Data Categories:**
```markdown
## Quantitative Data
- Statistical findings (means, frequencies, correlations)
- Demographic distributions
- Likert scale responses
- Performance metrics
- Temporal patterns
- Comparative data

## Qualitative Data
- Theme hierarchies
- Quote collections
- Journey stages
- Persona attributes
- Pain point clusters
- Opportunity areas

## Relational Data
- Cause-effect relationships
- Process flows
- System interactions
- Stakeholder networks
- Dependency chains
```

Present data inventory with:
- Visualization potential per dataset
- Complexity assessment
- Story value rating
- Technical requirements

**Elicitation Required:**
1. Proceed to audience analysis
2. Review quantitative options
3. Explore qualitative visuals
4. Focus on relationships
5. Assess data quality
6. Check completeness
7. Identify gaps
8. Prioritize datasets
9. Gather additional data

### 1.2 Audience Visual Literacy
**elicit: true**

Assess audience visualization preferences:

**Audience Profiles:**
- **Executives:** Simple, high-impact, business-focused
- **Product Teams:** Detailed, interactive, explorable
- **Designers:** Aesthetic, emotional, user-centered
- **Engineers:** Precise, technical, data-rich
- **Marketing:** Story-driven, customer-focused, shareable

**Complexity Levels:**
```markdown
Level 1: Basic (Bar, Pie, Line)
Level 2: Standard (Scatter, Heat Map, Stacked)
Level 3: Advanced (Sankey, Treemap, Network)
Level 4: Specialized (Parallel Coordinates, Violin)
```

Present audience assessment with:
- Recommended complexity level
- Preferred chart types
- Interaction requirements
- Distribution channels

**Elicitation Required:**
1. Proceed with assessment
2. Simplify for executives
3. Add interactivity
4. Increase sophistication
5. Focus on storytelling
6. Emphasize aesthetics
7. Prioritize accuracy
8. Enable exploration
9. Mix complexity levels

### 1.3 Visual Narrative Planning
**elicit: true**

Design the visual storytelling approach:

**Narrative Structures:**
1. **Sequential Story** - Charts build on each other
2. **Comparison Focus** - Side-by-side contrasts
3. **Zoom Approach** - Overview to detail
4. **Thematic Grouping** - Organized by topics
5. **Journey-Based** - Following user path

**Visual Hierarchy:**
```markdown
Primary Visual: The "Money Chart"
- Most important finding
- Largest size/prominence
- Best position

Secondary Visuals: Supporting Evidence
- Reinforce main message
- Medium prominence
- Grouped logically

Tertiary Visuals: Context & Detail
- Background information
- Smaller size
- Appendix placement
```

Present narrative plan with storyboard.

**Elicitation Required:**
1. Proceed to chart selection
2. Adjust story flow
3. Change primary visual
4. Add more context
5. Simplify narrative
6. Increase drama
7. Focus on transformation
8. Add emotional arc
9. Create multiple paths

## Phase 2: Chart Type Selection

### 2.1 Statistical Visualizations
**elicit: true**

Select appropriate statistical charts:

**Chart Selection Matrix:**
```markdown
| Data Type | Relationship | Best Chart | Alternative |
|-----------|-------------|------------|-------------|
| Distribution | 1 variable | Histogram | Box Plot |
| Comparison | Categories | Bar Chart | Dot Plot |
| Trend | Over time | Line Chart | Area Chart |
| Correlation | 2 variables | Scatter | Bubble |
| Part-to-whole | Proportions | Pie/Donut | Treemap |
| Multiple variables | Patterns | Radar | Parallel |
```

**Statistical Graphics:**
1. **Confidence Intervals** - Show uncertainty
2. **Effect Sizes** - Visualize impact magnitude
3. **Significance Markers** - Indicate statistical relevance
4. **Distribution Overlays** - Compare populations

Present statistical visualization plan.

**Elicitation Required:**
1. Proceed to qualitative visuals
2. Simplify statistics
3. Add error bars
4. Show distributions
5. Include benchmarks
6. Add annotations
7. Use small multiples
8. Create dashboard
9. Design custom chart

### 2.2 Qualitative Visualizations
**elicit: true**

Design qualitative data visualizations:

**Qualitative Visual Types:**
```markdown
## Theme Visualization
- Word Clouds (frequency-based sizing)
- Tree Maps (hierarchical themes)
- Network Diagrams (theme relationships)
- Affinity Maps (cluster visualization)

## Quote Visualization
- Quote Cards (designed testimonials)
- Quote Walls (collection displays)
- Sentiment Rivers (emotion over time)
- Speech Bubbles (persona quotes)

## Journey Visualization
- Linear Journey Maps
- Circular Journey Cycles
- Service Blueprints
- Experience Maps

## Persona Visualization
- Persona Cards
- Comparison Matrices
- Empathy Maps
- Behavioral Spectrums
```

Present qualitative visualization designs.

**Elicitation Required:**
1. Proceed to journey maps
2. Focus on themes
3. Emphasize quotes
4. Visualize patterns
5. Show relationships
6. Add emotional data
7. Include behaviors
8. Map ecosystems
9. Create hybrids

### 2.3 Journey & Flow Visualizations
**elicit: true**

Design journey and process visualizations:

**Journey Map Components:**
```markdown
## Horizontal Layers
1. Stages/Phases
2. Actions/Tasks
3. Touchpoints
4. Thoughts
5. Emotions
6. Pain Points
7. Opportunities

## Visual Elements
- Timeline backbone
- Emotional curve
- Touchpoint icons
- Pain point markers
- Opportunity flags
- Persona indicators
```

**Flow Visualizations:**
- Process flows
- Decision trees
- System diagrams
- Workflow maps
- State diagrams

Present journey visualization approach.

**Elicitation Required:**
1. Proceed to infographics
2. Simplify journey
3. Add emotional curve
4. Include touchpoints
5. Show parallel journeys
6. Add backstage processes
7. Include metrics layer
8. Create service blueprint
9. Design custom format

## Phase 3: Visual Design System

### 3.1 Color Strategy
**elicit: true**

Develop color palette and usage:

**Color Framework:**
```markdown
## Semantic Colors
- Positive/Success: Green (#00C853)
- Negative/Problem: Red (#D32F2F)
- Neutral/Info: Blue (#1976D2)
- Warning/Caution: Amber (#FFA000)

## Data Categories
- Category A: Primary Blue
- Category B: Secondary Teal
- Category C: Tertiary Purple
- Category D: Quaternary Orange

## Emotional Mapping
- Joy/Delight: Warm yellows
- Frustration: Deep reds
- Confusion: Muted grays
- Satisfaction: Soft greens

## Accessibility
- Contrast ratio: 4.5:1 minimum
- Colorblind safe palettes
- Pattern alternatives
```

Present color system with swatches.

**Elicitation Required:**
1. Proceed to typography
2. Adjust for brand
3. Increase contrast
4. Simplify palette
5. Add gradients
6. Use monochrome
7. Apply color theory
8. Consider culture
9. Create custom palette

### 3.2 Typography & Labeling

Define typography system:

**Type Hierarchy:**
- Chart Titles: Bold, 16-18pt
- Axis Labels: Medium, 12-14pt
- Data Labels: Regular, 10-11pt
- Annotations: Light, 9-10pt

**Labeling Strategy:**
- Direct labeling when possible
- Legend minimization
- Smart label placement
- Abbreviation standards

### 3.3 Visual Style Guide
**elicit: true**

Create comprehensive style guide:

**Style Components:**
```markdown
## Chart Styling
- Grid: Subtle gray lines
- Axes: 2pt weight, dark gray
- Data marks: Consistent sizing
- Borders: None or minimal

## Iconography
- Style: Outline/Filled
- Weight: Consistent stroke
- Size: Proportional scaling
- Meaning: Intuitive mapping

## Spacing
- Margins: 10% of chart area
- Padding: Consistent internal
- Grouping: Visual proximity
- Alignment: Grid-based

## Interactions
- Hover: Highlight + tooltip
- Click: Drill-down action
- Filter: Visual feedback
- Zoom: Progressive detail
```

Present complete style guide.

**Elicitation Required:**
1. Proceed to production
2. Align with brand
3. Increase minimalism
4. Add decorative elements
5. Improve clarity
6. Enhance aesthetics
7. Prioritize function
8. Balance both
9. Create variations

## Phase 4: Infographic Development

### 4.1 Infographic Strategy
**elicit: true**

Design comprehensive infographics:

**Infographic Types:**
1. **Statistical** - Data-driven story
2. **Timeline** - Historical progression
3. **Process** - How it works
4. **Comparison** - Side-by-side analysis
5. **Hierarchical** - Levels and relationships

**Layout Patterns:**
```markdown
┌─────────────────────┐
│     HEADLINE        │
├─────────────────────┤
│   KEY STATISTIC     │
│      [BIG #]        │
├──────┬──────┬───────┤
│ FACT │ FACT │ FACT  │
│  1   │  2   │  3    │
├──────┴──────┴───────┤
│   VISUALIZATION     │
│    [MAIN CHART]     │
├─────────────────────┤
│   SUPPORTING DATA   │
└─────────────────────┘
```

Present infographic concepts.

**Elicitation Required:**
1. Proceed to annotation
2. Add more statistics
3. Simplify layout
4. Increase visual interest
5. Tell stronger story
6. Add icons
7. Include illustrations
8. Create series
9. Design custom layout

### 4.2 Annotation & Insights
**elicit: true**

Add interpretive elements:

**Annotation Strategy:**
```markdown
## Insight Callouts
"Key Finding" → [Arrow to data point]

## Trend Indicators
↑ 23% increase (highlight positive)
↓ 15% decrease (highlight negative)

## Benchmark Lines
Industry average: - - - - -
Target goal: ═══════

## Statistical Markers
* = p < 0.05 (significant)
** = p < 0.01 (highly significant)

## Context Boxes
[What this means: explanation text]
```

Present annotation approach.

**Elicitation Required:**
1. Proceed to accessibility
2. Add more context
3. Reduce annotations
4. Highlight insights
5. Include definitions
6. Add calculations
7. Show confidence
8. Include sources
9. Create legend

## Phase 5: Accessibility & Production

### 5.1 Accessibility Compliance
**elicit: true**

Ensure inclusive design:

**Accessibility Requirements:**
```markdown
## Visual Accessibility
- Color contrast: WCAG AA (4.5:1)
- Color independence: Patterns/shapes
- Font size: Minimum 10pt
- Alt text: Descriptive summaries

## Cognitive Accessibility
- Clear titles and labels
- Logical reading order
- Consistent conventions
- Progressive complexity

## Technical Accessibility
- Screen reader compatible
- Keyboard navigable
- Table data alternatives
- Text descriptions
```

Present accessibility validation.

**Elicitation Required:**
1. Proceed to export specs
2. Increase contrast
3. Add patterns
4. Improve labels
5. Include alt text
6. Simplify design
7. Add data tables
8. Create text version
9. Test with tools

### 5.2 Export Specifications
**elicit: true**

Define production requirements:

**Export Formats:**
```markdown
## Print Specifications
- Resolution: 300 DPI
- Color: CMYK
- Format: PDF/EPS
- Bleed: 3mm

## Digital Specifications
- Resolution: 144 DPI
- Color: RGB
- Format: PNG/SVG
- Size: Optimized for web

## Interactive Specifications
- Framework: D3.js/Plotly
- Responsiveness: Mobile-first
- Performance: <3s load
- Fallbacks: Static images
```

**Production Checklist:**
- [ ] All data verified
- [ ] Labels spell-checked
- [ ] Sources cited
- [ ] Brand compliant
- [ ] Accessibility tested
- [ ] Multiple formats exported
- [ ] Version controlled
- [ ] Documentation complete

**Elicitation Required:**
1. Complete specifications
2. Add print versions
3. Create web versions
4. Enable interactivity
5. Optimize performance
6. Include raw data
7. Add documentation
8. Create templates
9. Package deliverables

## Phase 6: Visualization Gallery

### 6.1 Core Visualizations

Define essential visualizations:

**The Big Five:**
1. **The Money Chart** - Single most impactful finding
2. **The Comparison** - Key before/after or A/B
3. **The Journey** - User experience flow
4. **The Distribution** - Data spread and patterns
5. **The Relationship** - Correlation or causation

### 6.2 Supporting Graphics

Additional visualization needs:
- Demographic breakdowns
- Geographic distributions
- Temporal patterns
- Sentiment analysis
- Priority matrices
- Gap analyses

## Output Specifications

### Visualization Quality Standards

**Excellence Criteria:**
- Data-ink ratio: Maximized
- Lie factor: 1.0 (no distortion)
- Clarity: Instant understanding
- Accuracy: 100% data fidelity
- Beauty: Aesthetically pleasing
- Memorability: Sticky insights

### Deliverable Package

**Complete Package Includes:**
1. Visualization specifications document
2. Style guide with examples
3. Production-ready files (multiple formats)
4. Source files (editable)
5. Data files (structured)
6. Implementation guide
7. Accessibility report

## Common Visualization Mistakes

**Avoid These Pitfalls:**
1. **Chart Junk** - Unnecessary decoration
2. **3D Effects** - Distorting data
3. **Poor Color Choice** - Confusing or inaccessible
4. **Truncated Axes** - Misleading scales
5. **Pie Chart Overuse** - When bars work better
6. **Missing Context** - No baseline or comparison
7. **Information Overload** - Too much in one visual
8. **Inconsistent Styling** - Mixed conventions

## Success Metrics

Visualizations succeed when:
1. Message understood in <3 seconds
2. Insights are memorable
3. Actions become clear
4. Stakeholders share them
5. Decisions reference them
6. No misinterpretation occurs
7. Accessibility validated

## CRITICAL REMINDER

This is an INTERACTIVE WORKFLOW requiring user participation at each elicitation point. The 1-9 option format is MANDATORY. Creating complete visualization designs without user interaction violates this task specification.