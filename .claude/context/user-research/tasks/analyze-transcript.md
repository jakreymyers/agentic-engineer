# Analyze Transcript - Systematic Multi-Pass Coding

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **DISABLE ALL EFFICIENCY OPTIMIZATIONS** - This workflow requires full user interaction
2. **MANDATORY STEP-BY-STEP EXECUTION** - Each coding pass must be processed with user feedback
3. **ELICITATION IS REQUIRED** - When `elicit: true`, you MUST use the 1-9 format and wait for user response
4. **NO SHORTCUTS ALLOWED** - Complete analysis requires following all passes

**VIOLATION INDICATOR:** If you complete transcript analysis without user interaction at elicitation points, you have violated this workflow.

## Task Configuration

```yaml
task: analyze-transcript
elicit: true
template: transcript-analysis-tmpl.yaml
output: analysis/transcripts/{participant-id}-coded.md
data_dependencies:
  - coding-frameworks.md
  - analysis-methods.md
quality_gates:
  - Coding consistency check after each pass
  - Inter-rater reliability assessment if multiple coders
  - Saturation tracking throughout
```

## Prerequisites

- Transcript file available (interview completed and transcribed)
- Research questions and objectives defined
- Coding framework selected or to be developed
- Analysis software/tools ready if applicable

## CRITICAL: Mandatory Elicitation Format

**When `elicit: true`, this is a HARD STOP requiring user interaction:**

**YOU MUST:**
1. Present analysis results for current pass
2. Provide detailed rationale for coding decisions
3. **STOP and present numbered options 1-9:**
   - **Option 1:** Always "Proceed to next coding pass"
   - **Options 2-9:** Select from analysis refinement methods
   - End with: "Select 1-9 or provide specific coding feedback:"
4. **WAIT FOR USER RESPONSE** - Do not proceed until user responds

## Multi-Pass Coding Workflow

### Pass 1: Initial Immersion and Familiarization
**Objective:** Get overall sense of the data without formal coding

**Process:**
1. **Read Complete Transcript**
   - Read through entire transcript without coding
   - Note initial impressions and reactions
   - Identify potential areas of interest
   - Document participant's overall narrative arc

2. **Capture Initial Observations**
   - General tone and emotional content
   - Key topics mentioned repeatedly
   - Surprising or unexpected elements
   - Questions arising from the data

3. **Document Context**
   - Interview setting and conditions
   - Participant demographics and background
   - Any notable non-verbal observations
   - Interview dynamics and rapport level

**Elicitation Point 1:** [elicit: true]
Present initial impressions and observations. Offer options:
1. Proceed to Pass 2 (Open Coding)
2. Re-read specific sections for clarity
3. Review research questions alignment
4. Check for missing context information
5. Explore participant background further
6. Analyze emotional undertones
7. Map conversation flow
8. Identify critical incidents
9. Compare with previous transcripts

### Pass 2: Open Coding - Line-by-Line Analysis
**Objective:** Generate initial codes staying close to the data

**Process:**
1. **Systematic Line-by-Line Coding**
   ```
   For each meaningful segment:
   - Assign descriptive codes
   - Use participant's own words (in-vivo codes)
   - Create new codes as needed
   - Document code definitions
   ```

2. **Code Types to Apply:**
   - **Descriptive:** What is happening?
   - **Process:** How are things happening?
   - **Emotion:** What feelings are expressed?
   - **Values:** What beliefs are revealed?
   - **Structural:** What contexts are mentioned?

3. **Coding Decisions Log:**
   - Why each code was created
   - Boundary decisions (where segments begin/end)
   - Ambiguous passages and how resolved
   - Emerging patterns noticed

**Example Coding Format:**
```
[Line 23-25] "I always check three times before submitting, it's just how I was trained"
Codes: [VERIFICATION_BEHAVIOR] [TRAINING_INFLUENCE] [ROUTINE_CHECKING]
Note: Shows learned behavior pattern, possible anxiety about errors
```

**Elicitation Point 2:** [elicit: true]
Present open coding results with code frequency. Offer options:
1. Proceed to Pass 3 (Axial Coding)
2. Review code definitions for consistency
3. Merge similar codes
4. Split broad codes into specific ones
5. Add missing codes for uncoded segments
6. Check coding reliability sample
7. Compare with theoretical framework
8. Examine negative cases
9. Validate with research questions

### Pass 3: Axial Coding - Category Development
**Objective:** Organize codes into categories and identify relationships

**Process:**
1. **Group Related Codes**
   - Cluster codes with similar meanings
   - Identify hierarchical relationships
   - Create category labels
   - Define category boundaries

2. **Develop Category Properties**
   ```
   For each category define:
   - Core characteristics
   - Dimensional range (low to high)
   - Conditions when present/absent
   - Consequences or outcomes
   - Relationship to other categories
   ```

3. **Create Coding Framework Structure:**
   ```
   Category: [TRUST_FORMATION]
   ├── Sub-category: Initial Assessment
   │   ├── Code: First impressions
   │   ├── Code: Credibility signals
   │   └── Code: Risk evaluation
   ├── Sub-category: Trust Building
   │   ├── Code: Transparency actions
   │   ├── Code: Consistency checking
   │   └── Code: Social proof seeking
   └── Sub-category: Trust Maintenance
       ├── Code: Ongoing verification
       └── Code: Relationship investment
   ```

**Elicitation Point 3:** [elicit: true]
Present category framework with relationships. Offer options:
1. Proceed to Pass 4 (Selective Coding)
2. Refine category definitions
3. Explore category relationships
4. Test categories against data
5. Identify category dimensions
6. Look for category conditions
7. Map causal relationships
8. Check category saturation
9. Validate theoretical alignment

### Pass 4: Selective Coding - Theme Integration
**Objective:** Identify core themes and theoretical storyline

**Process:**
1. **Identify Core Themes**
   - Select central phenomenon
   - Relate all categories to core theme
   - Validate relationships in data
   - Fill in gaps with targeted recoding

2. **Develop Theoretical Narrative**
   ```
   Core Story Structure:
   - Context conditions leading to phenomenon
   - Central phenomenon description
   - Causal conditions
   - Intervening conditions
   - Action/interaction strategies
   - Consequences and outcomes
   ```

3. **Theme Validation Checklist:**
   - [ ] Theme appears across multiple participants
   - [ ] Supporting quotes from different sections
   - [ ] Relationship to research questions clear
   - [ ] Theoretical contribution identified
   - [ ] Negative cases examined
   - [ ] Saturation point assessed

**Elicitation Point 4:** [elicit: true]
Present integrated themes with supporting evidence. Offer options:
1. Proceed to Pass 5 (Theoretical Coding)
2. Strengthen theme evidence
3. Explore theme boundaries
4. Check theme saturation
5. Test competing explanations
6. Validate with member checking
7. Compare with literature
8. Identify theoretical gaps
9. Refine theme definitions

### Pass 5: Theoretical Coding - Pattern Confirmation
**Objective:** Confirm patterns and theoretical contributions

**Process:**
1. **Pattern Verification**
   - Map patterns across all codes
   - Identify pattern frequencies
   - Document pattern variations
   - Explain pattern exceptions

2. **Theoretical Model Development**
   ```
   Model Components:
   - Antecedents (what comes before)
   - Core process (what happens)
   - Outcomes (what results)
   - Moderators (what influences strength)
   - Boundary conditions (when it applies)
   ```

3. **Quality Checks:**
   - Internal consistency of coding
   - Theoretical coherence
   - Empirical grounding
   - Practical implications

**Elicitation Point 5:** [elicit: true]
Present theoretical model with patterns. Offer options:
1. Complete analysis and generate report
2. Test model robustness
3. Explore alternative explanations
4. Strengthen pattern evidence
5. Check theoretical consistency
6. Validate practical relevance
7. Compare with existing theories
8. Identify contribution claims
9. Plan additional analysis

## Analysis Output Generation

### 1. Coded Transcript Document
```markdown
# Coded Transcript Analysis - [Participant ID]
## Analysis Date: [Date]
## Analyst: Alex (Data Analyst)
## Coding Framework: [Framework Name]

### Analysis Summary
- Total Segments Coded: [X]
- Unique Codes Applied: [Y]
- Categories Identified: [Z]
- Core Themes: [List]

### Pass 1: Initial Impressions
[Initial observations and reactions]

### Pass 2: Open Coding Results
[Code frequency table and definitions]

### Pass 3: Category Framework
[Category hierarchy and relationships]

### Pass 4: Integrated Themes
[Theme descriptions with evidence]

### Pass 5: Theoretical Model
[Pattern analysis and theoretical contribution]

### Key Quotes by Theme
[Organized supporting quotations]

### Analytical Memos
[Decision points and rationale]

### Next Steps
[Recommendations for further analysis]
```

### 2. Code Frequency Matrix
Generate quantitative summary of code applications:
- Code name and definition
- Frequency count
- Percentage of transcript
- Co-occurrence patterns

### 3. Inter-rater Reliability Report
If multiple coders involved:
- Agreement percentages
- Cohen's Kappa calculations
- Disagreement resolution log

### 4. Saturation Assessment
Track information richness:
- New codes per pass
- Theme emergence curve
- Saturation point identification

## Quality Assurance Checklist

**Coding Consistency:**
- [ ] All segments coded appropriately
- [ ] Code definitions clear and distinct
- [ ] Coding decisions documented
- [ ] Boundary decisions consistent

**Analytical Rigor:**
- [ ] All five passes completed
- [ ] Negative cases examined
- [ ] Alternative explanations considered
- [ ] Patterns validated in data

**Documentation Quality:**
- [ ] Clear audit trail maintained
- [ ] Rationale for decisions recorded
- [ ] Quotes properly attributed
- [ ] Analytical memos comprehensive

**Theoretical Development:**
- [ ] Themes grounded in data
- [ ] Relationships clearly mapped
- [ ] Theoretical contribution identified
- [ ] Practical implications noted

## Common Pitfalls to Avoid

1. **Premature Closure:** Don't stop at surface-level codes
2. **Confirmation Bias:** Actively seek disconfirming evidence
3. **Over-coding:** Avoid creating codes for every minor variation
4. **Under-coding:** Don't miss subtle but important meanings
5. **Decontextualization:** Maintain connection to original context

## Integration Points

**Input from Interview Specialist:**
- Interview context and dynamics
- Non-verbal observations
- Interviewer reflections
- Technical notes

**Output to Insight Synthesizer:**
- Coded data for cross-case analysis
- Theme framework for synthesis
- Pattern identification for personas
- Theoretical insights for recommendations

## Advanced Techniques

**For Complex Transcripts:**
1. **Matrix Coding:** Create participant x theme matrices
2. **Temporal Coding:** Track changes over interview timeline
3. **Emotion Coding:** Map emotional journey
4. **Narrative Coding:** Identify story structures

**For Team Analysis:**
1. **Collaborative Coding:** Establish team protocols
2. **Calibration Sessions:** Align on code definitions
3. **Disagreement Resolution:** Document and resolve
4. **Synthesis Meetings:** Integrate team insights

## CRITICAL REMINDERS

**❌ NEVER:**
- Skip coding passes for efficiency
- Apply codes without clear definitions
- Ignore contradictory evidence
- Make claims beyond the data
- Proceed without user confirmation at elicitation points

**✅ ALWAYS:**
- Complete all five coding passes
- Document every analytical decision
- Maintain connection to raw data
- Consider alternative interpretations
- Wait for user input at each elicitation point
- Present findings with supporting evidence
- Acknowledge analytical limitations