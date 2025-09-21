# Create Affinity Diagram - Insight Organization Through Clustering

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **INTERACTIVE CLUSTERING REQUIRED** - User must validate groupings
2. **ITERATIVE REFINEMENT** - Multiple rounds of organization
3. **ELICITATION MANDATORY** - Cluster decisions need user input
4. **COLLABORATIVE PROCESS** - Not autonomous completion

**VIOLATION INDICATOR:** If you create final affinity diagram without user participation, you have violated this workflow.

## Task Configuration

```yaml
task: create-affinity-diagram
elicit: true
template: affinity-map-tmpl.yaml
output: analysis/affinity/{project}-affinity-map.md
method: Bottom-up clustering with hierarchical organization
prerequisites:
  - Coded data available
  - Individual insights extracted
  - Research questions defined
```

## Affinity Diagramming Process

### Phase 1: Data Preparation and Insight Extraction

**Objective:** Extract all individual insights for clustering

**Process:**

1. **Extract Individual Insights**
   ```
   Insight Card Format:
   ID: [I-001]
   Source: [Participant/Document ID]
   Insight: [Single observation or finding]
   Context: [Brief context if needed]
   Raw Quote: "[Supporting verbatim]"
   Tags: [Initial descriptive tags]
   ```

2. **Create Insight Inventory**
   - One insight per "card"
   - Keep insights atomic (single idea)
   - Preserve original language
   - Include source attribution
   - Maintain context notes

3. **Quality Check Each Insight**
   - Is it a single, complete thought?
   - Is the meaning clear standalone?
   - Is source documented?
   - Is it actually an insight (not just data)?

**Example Insights:**
```
I-001: Users check email first thing in morning before any other task
I-002: Notification sounds create anxiety even when not working
I-003: People create elaborate folder systems they rarely use
I-004: Friday afternoons used for "inbox zero" attempts
```

**Elicitation Point 1:** [elicit: true]
Present extracted insights count and sample. Offer options:
1. Proceed to Phase 2 (Initial Clustering)
2. Review insight extraction criteria
3. Add missing insights noticed
4. Split compound insights
5. Clarify ambiguous insights
6. Check insight completeness
7. Validate insight quality
8. Review source coverage
9. Examine insight distribution

### Phase 2: Initial Clustering - Natural Groupings

**Objective:** Allow natural groups to emerge from data

**Clustering Process:**

1. **Random Layout** (Mental Reset)
   - Present insights in random order
   - No preconceived categories
   - Fresh perspective on data

2. **Similarity Grouping**
   ```
   Look for insights that:
   - Address same topic
   - Share similar concepts
   - Describe related behaviors
   - Express comparable feelings
   - Involve same processes
   ```

3. **Create Initial Clusters**
   ```
   Cluster Formation:
   [Cluster A - Untitled]
   ├── I-001: Morning email checking
   ├── I-004: Friday inbox zero
   ├── I-017: Email as first task
   └── I-023: Daily email routines

   [Cluster B - Untitled]
   ├── I-002: Notification anxiety
   ├── I-011: Alert overwhelm
   └── I-019: Sound sensitivity
   ```

4. **Document Clustering Rationale**
   - Why these insights belong together
   - What unites them conceptually
   - Key similarities identified

**Clustering Rules:**
- Start with obvious connections
- Don't force insights into groups
- Okay to have singles initially
- Clusters can be different sizes
- Let patterns emerge naturally

**Elicitation Point 2:** [elicit: true]
Present initial clusters formed. Offer options:
1. Proceed to Phase 3 (Cluster Refinement)
2. Adjust cluster membership
3. Split large clusters
4. Merge similar clusters
5. Create new clusters for singles
6. Review clustering logic
7. Check cluster coherence
8. Explore edge cases
9. Validate grouping rationale

### Phase 3: Cluster Refinement and Labeling

**Objective:** Refine groups and create descriptive labels

**Refinement Process:**

1. **Review Each Cluster for Coherence**
   ```
   Coherence Check:
   - Do all insights truly belong?
   - Is there a clear unifying theme?
   - Are there outliers to move?
   - Should cluster be subdivided?
   ```

2. **Create Descriptive Labels**
   ```
   Labeling Progression:
   Initial: "Email stuff"
   ↓
   Refined: "Email management behaviors"
   ↓
   Final: "Ritualized Email Management Strategies"
   ```

   **Label Characteristics:**
   - Descriptive not prescriptive
   - Captures essence of group
   - Uses participant language when apt
   - Specific enough to differentiate
   - Broad enough to encompass insights

3. **Identify Cluster Relationships**
   - Sequential relationships (A leads to B)
   - Hierarchical relationships (A contains B)
   - Oppositional relationships (A conflicts with B)
   - Causal relationships (A causes B)
   - Associative relationships (A relates to B)

4. **Create Sub-clusters if Needed**
   ```
   Main Cluster: "Digital Boundary Management"
   ├── Sub-cluster: "Temporal Boundaries"
   │   ├── I-031: No email after 6pm
   │   └── I-045: Weekend disconnection
   ├── Sub-cluster: "Spatial Boundaries"
   │   ├── I-052: Work laptop stays at office
   │   └── I-067: Separate work phone
   └── Sub-cluster: "Psychological Boundaries"
       ├── I-071: Mental compartmentalization
       └── I-089: Emotional detachment techniques
   ```

**Elicitation Point 3:** [elicit: true]
Present refined clusters with labels. Offer options:
1. Proceed to Phase 4 (Hierarchy Development)
2. Refine cluster labels
3. Adjust sub-cluster organization
4. Review cluster relationships
5. Validate cluster boundaries
6. Address remaining singles
7. Check label clarity
8. Test alternative organizations
9. Explore cluster meanings

### Phase 4: Developing Hierarchy and Themes

**Objective:** Organize clusters into meaningful hierarchy

**Hierarchy Development:**

1. **Identify Super-clusters (Themes)**
   ```
   Theme Level:
   "Digital Work Adaptation"
   ├── "Communication Management"
   │   ├── Email Strategies
   │   ├── Meeting Protocols
   │   └── Async Collaboration
   ├── "Boundary Setting"
   │   ├── Temporal Boundaries
   │   ├── Spatial Boundaries
   │   └── Psychological Boundaries
   └── "Productivity Systems"
       ├── Tool Adoption
       ├── Workflow Design
       └── Performance Tracking
   ```

2. **Create Connecting Narratives**
   - How clusters relate to tell a story
   - Progression or journey identified
   - Cause-effect relationships mapped
   - System dynamics revealed

3. **Identify Key Insights**
   ```
   Types of Key Insights:
   - Surprising findings
   - Strong patterns
   - Universal experiences
   - Unique perspectives
   - Actionable discoveries
   - Strategic implications
   ```

4. **Map to Research Questions**
   - Which clusters answer which questions
   - Gaps where questions aren't addressed
   - Unexpected findings beyond questions

**Elicitation Point 4:** [elicit: true]
Present hierarchical organization. Offer options:
1. Proceed to Phase 5 (Insight Synthesis)
2. Adjust hierarchy levels
3. Refine theme definitions
4. Explore narrative connections
5. Strengthen research alignment
6. Identify missing elements
7. Validate structural logic
8. Test alternative hierarchies
9. Review completeness

### Phase 5: Synthesizing Key Insights

**Objective:** Extract actionable insights from affinity structure

**Synthesis Process:**

1. **Identify Insight Categories**
   ```
   Category Types:
   - Behavioral Patterns: What people do
   - Mental Models: How people think
   - Emotional Responses: How people feel
   - Needs & Desires: What people want
   - Pain Points: What frustrates people
   - Workarounds: How people adapt
   - Opportunities: Where to improve
   ```

2. **Generate Insight Statements**
   ```
   Format: [Observation] + [Implication]

   Example:
   "Users create elaborate filing systems they never use,
   suggesting that the act of organizing provides more
   value than the organization itself—possibly offering
   a sense of control in overwhelming situations."
   ```

3. **Prioritize Insights**
   ```
   Priority Matrix:
   High Impact + High Frequency = Critical Insight
   High Impact + Low Frequency = Important Edge Case
   Low Impact + High Frequency = Hygiene Factor
   Low Impact + Low Frequency = Interesting Anomaly
   ```

4. **Create Opportunity Statements**
   Transform insights into opportunities:
   - "How might we..." statements
   - "What if..." explorations
   - "We could..." possibilities

**Elicitation Point 5:** [elicit: true]
Present synthesized insights. Offer options:
1. Proceed to Phase 6 (Documentation)
2. Refine insight statements
3. Adjust prioritization
4. Generate more opportunities
5. Validate with raw data
6. Check actionability
7. Explore implications
8. Test with stakeholders
9. Strengthen evidence

### Phase 6: Documentation and Visualization

**Objective:** Create comprehensive affinity diagram documentation

**Documentation Components:**

1. **Visual Affinity Map**
   ```
   [Digital Format Representation]

   THEME A: Digital Communication Evolution
   ├──┬── Cluster 1: Email Management (12 insights)
   │  ├── Sub 1.1: Timing Strategies (5)
   │  └── Sub 1.2: Organization Systems (7)
   ├──┬── Cluster 2: Meeting Transformation (8 insights)
   │  ├── Sub 2.1: Virtual Etiquette (3)
   │  └── Sub 2.2: Engagement Tactics (5)
   └──┬── Cluster 3: Async Collaboration (10 insights)
      ├── Sub 3.1: Tool Selection (4)
      └── Sub 3.2: Response Expectations (6)
   ```

2. **Detailed Cluster Documentation**
   For each cluster include:
   - Label and description
   - All constituent insights
   - Supporting quotes
   - Frequency/strength indicators
   - Relationships to other clusters
   - Implications identified

3. **Insight Traceability Matrix**
   - Insight ID → Cluster → Theme
   - Source attribution maintained
   - Easy lookup and validation

**Elicitation Point 6:** [elicit: true]
Review complete affinity diagram. Offer options:
1. Finalize affinity diagram
2. Adjust visual representation
3. Enhance documentation
4. Add interpretive notes
5. Include methodological notes
6. Validate completeness
7. Prepare presentation version
8. Export for other tools
9. Plan next steps

## Affinity Diagram Outputs

### 1. Complete Affinity Map Document
```markdown
# Affinity Diagram - [Project Name]
## Creation Date: [Date]
## Analyst: Alex (Data Analyst)
## Participants/Sources: [Number]

### Executive Summary
- Total Insights: [Number]
- Clusters Formed: [Number]
- Major Themes: [Number]
- Key Findings: [Bullet list]

### Affinity Map Structure
[Visual hierarchy representation]

### Theme Details

#### Theme 1: [Name]
Description: [What this theme represents]

##### Cluster 1.1: [Name] ([X] insights)
Description: [Cluster meaning]
Key Insights:
- [Notable insight 1]
- [Notable insight 2]
Supporting Quotes:
- "[Representative quote]" - Source

[Continue for all themes/clusters]

### Cross-Cutting Insights
[Insights that span multiple themes]

### Outliers and Unique Perspectives
[Important singles or unusual findings]

### Implications and Opportunities
- For Product: [List]
- For Service: [List]
- For Strategy: [List]

### Methodological Notes
- Clustering approach used
- Decision points documented
- Team members involved
- Validation steps taken
```

### 2. Insight Database
Spreadsheet/database with:
- Insight ID
- Text
- Source
- Cluster assignment
- Theme alignment
- Tags/codes
- Priority rating

### 3. Opportunity Canvas
Transform top insights into:
- Problem statements
- Opportunity areas
- "How might we" questions
- Solution hypotheses

## Quality Assurance

**Affinity Diagram Checklist:**
- [ ] All relevant insights included
- [ ] Natural groupings emerged
- [ ] Clear cluster labels
- [ ] Logical hierarchy
- [ ] Relationships mapped
- [ ] Research questions addressed
- [ ] Actionable insights identified
- [ ] Clear documentation
- [ ] Stakeholder-ready outputs

## Common Pitfalls

1. **Forced Clustering:** Making insights fit predetermined categories
2. **Over-Categorization:** Too many small clusters
3. **Under-Categorization:** Too few large clusters
4. **Label Ambiguity:** Vague or overlapping labels
5. **Lost Context:** Insights removed from source meaning
6. **Analysis Paralysis:** Over-thinking natural groupings

## Advanced Techniques

**For Large Datasets (500+ insights):**
1. **Digital Tools:** Use Miro, Mural, or specialized software
2. **Team Sessions:** Multiple analysts for reliability
3. **Progressive Clustering:** Work in waves
4. **Meta-Affinity:** Affinity diagram of affinity diagrams

**For Remote Teams:**
1. **Virtual Sticky Notes:** Digital collaboration tools
2. **Async Clustering:** Time-shifted participation
3. **Video Sessions:** Screen-shared clustering
4. **Documentation:** Extra detail for alignment

## Integration Points

**From Previous Analysis:**
- Coded transcripts
- Extracted themes
- Individual insights
- Pattern identification

**To Insight Synthesizer:**
- Organized insight clusters
- Theme hierarchy
- Relationship maps
- Priority insights

**To Research Reporter:**
- Visual affinity maps
- Key insight statements
- Opportunity areas
- Strategic implications

## CRITICAL REMINDERS

**❌ NEVER:**
- Force insights into predetermined groups
- Create clusters without clear rationale
- Ignore insights that don't fit
- Rush the emergence process
- Complete without user validation

**✅ ALWAYS:**
- Let patterns emerge naturally
- Document clustering decisions
- Maintain insight traceability
- Consider multiple organizations
- Validate with user at each phase
- Keep original context accessible
- Look for surprising connections