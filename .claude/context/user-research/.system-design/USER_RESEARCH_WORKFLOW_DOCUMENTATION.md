# User Research Multi-Agent System - Workflow Documentation

## Overview

This document provides comprehensive workflow documentation for the User Research Multi-Agent System, featuring 5 specialized research workflows that coordinate 6 research agents to deliver high-quality user insights.

### Agent Team Structure

```mermaid
graph TB
    RO[Research Orchestrator<br/>🎯 Project Management & Coordination]
    RS[Research Strategist<br/>📋 Study Design & Planning]
    IS[Interview Specialist<br/>🎤 Data Collection & Interviews]
    DA[Data Analyst<br/>📊 Analysis & Coding]
    ISY[Insight Synthesizer<br/>💡 Synthesis & Sensemaking]
    RR[Research Reporter<br/>📄 Reporting & Communication]

    RO --> RS
    RS --> IS
    IS --> DA
    DA --> ISY
    ISY --> RR
    RR --> RO

    style RO fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style RS fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    style IS fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    style DA fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style ISY fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    style RR fill:#f1f8e9,stroke:#33691e,stroke-width:2px
```

## Workflow Overview Matrix

| Workflow | Duration | Team Size | Primary Use Case | Key Outputs |
|----------|----------|-----------|------------------|-------------|
| **User Interview Research** | 3-6 weeks | 2-4 researchers | Comprehensive user insights | Personas, Journey Maps, Requirements |
| **Rapid Discovery** | 5 days | 2-3 researchers | Quick insights for urgent decisions | Top insights, Quick wins |
| **Conjoint Analysis** | 2-3 weeks | 2-3 researchers + analyst | Preference & trade-off analysis | Utility scores, Market simulations |
| **Ethnographic Research** | 4-8 weeks | 2-3 researchers | Deep cultural & behavioral insights | Thick descriptions, Cultural patterns |
| **Mixed Methods Research** | 4-6 weeks | 3-4 researchers | Holistic understanding (qual + quant) | Validated findings, Integrated model |

---

# 1. User Interview Research Workflow

## High-Level Flow

```mermaid
flowchart TD
    Start([Start Project]) --> Setup[Project Setup<br/>2-3 days]
    Setup --> Design[Study Design<br/>3-4 days]
    Design --> Prep[Interview Prep<br/>2-3 days]
    Prep --> Collect[Data Collection<br/>5-10 days]
    Collect --> Analyze[Data Analysis<br/>4-5 days]
    Analyze --> Synth[Synthesis<br/>3-4 days]
    Synth --> Report[Reporting<br/>3-4 days]
    Report --> Deliver[Delivery<br/>1-2 days]
    Deliver --> End([Project Complete])

    %% Quality Gates
    Setup -.->|QG1: Stakeholder Approval| QG1{Quality Gate 1}
    Design -.->|QG2: IRB/Ethics Approval| QG2{Quality Gate 2}
    Prep -.->|QG3: Pilot Success| QG3{Quality Gate 3}
    Collect -.->|QG4: Sample Target| QG4{Quality Gate 4}
    Analyze -.->|QG5: Coding Reliability| QG5{Quality Gate 5}
    Synth -.->|QG6: Insights Validated| QG6{Quality Gate 6}
    Report -.->|QG7: Quality Review| QG7{Quality Gate 7}
    Deliver -.->|QG8: Stakeholder Acceptance| QG8{Quality Gate 8}

    QG1 -->|Pass| Design
    QG1 -->|Fail| Setup
    QG2 -->|Pass| Prep
    QG2 -->|Fail| Design
    QG3 -->|Pass| Collect
    QG3 -->|Fail| Prep
    QG4 -->|Pass| Analyze
    QG4 -->|Fail| Collect
    QG5 -->|Pass| Synth
    QG5 -->|Fail| Analyze
    QG6 -->|Pass| Report
    QG6 -->|Fail| Synth
    QG7 -->|Pass| Deliver
    QG7 -->|Fail| Report
    QG8 -->|Pass| End
    QG8 -->|Fail| Deliver

    style Start fill:#a5d6a7,stroke:#388e3c,stroke-width:2px
    style End fill:#ffcdd2,stroke:#d32f2f,stroke-width:2px
    style QG1 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style QG2 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style QG3 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style QG4 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style QG5 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style QG6 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style QG7 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style QG8 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
```

## Detailed Phase Breakdown

```mermaid
gantt
    title User Interview Research Timeline
    dateFormat  X
    axisFormat %d

    section Setup (2-3d)
    Establish Project    :setup1, 0, 1d
    Select Methodology   :setup2, after setup1, 1d

    section Design (3-4d)
    Design Study         :design1, after setup2, 2d
    Create Screener      :design2, after design1, 1d

    section Preparation (2-3d)
    Discussion Guide     :prep1, after design2, 1d
    Generate Probes      :prep2, after prep1, 1d
    Create Protocol      :prep3, after prep2, 1d

    section Collection (5-10d)
    Conduct Interviews   :collect1, after prep3, 7d
    Manage Transcripts   :collect2, after collect1, 2d

    section Analysis (4-5d)
    Analyze Transcripts  :analyze1, after collect2, 2d
    Extract Themes       :analyze2, after analyze1, 1d
    Create Affinity      :analyze3, after analyze2, 1d
    Sentiment Analysis   :analyze4, after analyze3, 1d

    section Synthesis (3-4d)
    Synthesize Findings  :synth1, after analyze4, 1d
    Create Personas      :synth2, after synth1, 1d
    Map Journey          :synth3, after synth2, 1d
    Extract Requirements :synth4, after synth3, 1d

    section Reporting (3-4d)
    Generate Report      :report1, after synth4, 2d
    Create Visuals       :report2, after report1, 1d
    Executive Summary    :report3, after report2, 1d

    section Delivery (1-2d)
    Prepare Presentation :deliver1, after report3, 1d
    Deliver Findings     :deliver2, after deliver1, 1d
```

## Agent Handoffs & Data Flow

```mermaid
sequenceDiagram
    participant RO as Research<br/>Orchestrator
    participant RS as Research<br/>Strategist
    participant IS as Interview<br/>Specialist
    participant DA as Data<br/>Analyst
    participant ISY as Insight<br/>Synthesizer
    participant RR as Research<br/>Reporter

    Note over RO,RR: Project Setup Phase
    RO->>RO: Establish project objectives
    RO->>RO: Select methodology
    RO->>RS: Handoff: Research brief, methodology, timeline

    Note over RO,RR: Study Design Phase
    RS->>RS: Design research study
    RS->>RS: Create screening questionnaire
    RS->>IS: Handoff: Study design, screening criteria, requirements

    Note over RO,RR: Interview Preparation Phase
    IS->>IS: Create discussion guide
    IS->>IS: Generate interview probes
    IS->>IS: Create interview protocol
    IS->>DA: Handoff: Discussion guide, protocol, (future recordings)

    Note over RO,RR: Data Collection Phase
    IS->>IS: Conduct interviews (12-20)
    IS->>IS: Manage transcripts
    IS->>DA: Handoff: Interview transcripts, session notes, metadata

    Note over RO,RR: Data Analysis Phase
    DA->>DA: Analyze transcripts
    DA->>DA: Extract themes
    DA->>DA: Create affinity diagram
    DA->>DA: Conduct sentiment analysis
    DA->>ISY: Handoff: Coded data, themes, affinity map, sentiment

    Note over RO,RR: Synthesis Phase
    ISY->>ISY: Synthesize findings
    ISY->>ISY: Create personas
    ISY->>ISY: Map customer journey
    ISY->>ISY: Extract requirements
    ISY->>RR: Handoff: Synthesis, personas, journey maps, requirements

    Note over RO,RR: Reporting Phase
    RR->>RR: Generate research report
    RR->>RR: Create executive summary
    RR->>RR: Design visualizations
    RR->>RR: Formulate recommendations
    RR->>RO: Handoff: Report, presentation, visuals, recommendations

    Note over RO,RR: Delivery Phase
    RO->>RO: Prepare stakeholder presentation
    RO->>RO: Deliver findings
    RO->>RO: Project closeout
```

## Error Handling & Recovery

```mermaid
flowchart TD
    subgraph "Error Types"
        E1[Stakeholder Misalignment]
        E2[Resource Shortage]
        E3[Insufficient Participants]
        E4[Transcription Failure]
        E5[Coding Reliability Failure]
        E6[Format Conversion Error]
    end

    subgraph "Detection Mechanisms"
        D1[Approval Score < 75%]
        D2[Available Resources < 80%]
        D3[Recruited < 80% of Target]
        D4[Service Unavailable or Accuracy < 85%]
        D5[Cohen's Kappa < 0.7]
        D6[Markdown to JSON Conversion Fails]
    end

    subgraph "Handlers"
        H1[Escalate to Sponsor]
        H2[Negotiate Scope Reduction]
        H3[Extend Recruitment Period]
        H4[Retry with Exponential Backoff]
        H5[Recalibrate Coding Framework]
        H6[Invoke Data Format Converter]
    end

    subgraph "Fallbacks"
        F1[Defer Project Start]
        F2[Extend Timeline]
        F3[Adjust Sample Size with Justification]
        F4[Manual Transcription Service]
        F5[Single Coder with Expert Review]
        F6[Manual JSON Creation]
    end

    E1 --> D1 --> H1 --> F1
    E2 --> D2 --> H2 --> F2
    E3 --> D3 --> H3 --> F3
    E4 --> D4 --> H4 --> F4
    E5 --> D5 --> H5 --> F5
    E6 --> D6 --> H6 --> F6

    style E1 fill:#ffebee,stroke:#c62828,stroke-width:2px
    style E2 fill:#ffebee,stroke:#c62828,stroke-width:2px
    style E3 fill:#ffebee,stroke:#c62828,stroke-width:2px
    style E4 fill:#ffebee,stroke:#c62828,stroke-width:2px
    style E5 fill:#ffebee,stroke:#c62828,stroke-width:2px
    style E6 fill:#ffebee,stroke:#c62828,stroke-width:2px
```

---

# 2. Rapid Discovery Sprint Workflow

## Sprint Overview

```mermaid
gantt
    title 5-Day Rapid Discovery Sprint
    dateFormat  YYYY-MM-DD
    axisFormat %a

    section Day 1: Plan
    Define Focus         :day1a, 2024-01-01, 4h
    Select Approach      :day1b, after day1a, 4h

    section Day 2: Interviews
    Interview Block 1    :day2a, 2024-01-02, 8h

    section Day 3: Interviews
    Interview Block 2    :day3a, 2024-01-03, 8h

    section Day 4: Analysis
    Rapid Coding         :day4a, 2024-01-04, 4h
    Synthesis            :day4b, after day4a, 4h

    section Day 5: Report
    Create Presentation  :day5a, 2024-01-05, 4h
    Stakeholder Workshop :day5b, after day5a, 4h
```

## Sprint Flow with Decision Points

```mermaid
flowchart TD
    Start([Start Sprint]) --> D1{Day 1 Complete?}
    D1 -->|Yes| D2[Day 2: Interviews]
    D1 -->|No - Behind| Emergency1[Emergency Replan]

    D2 --> Check1{4+ Interviews Done?}
    Check1 -->|Yes| D3[Day 3: More Interviews]
    Check1 -->|No| Recruit[Emergency Recruitment]

    D3 --> Check2{8+ Total Interviews?}
    Check2 -->|Yes| D4[Day 4: Analysis]
    Check2 -->|No| Extend[Extend Collection]

    D4 --> Check3{Analysis Quality OK?}
    Check3 -->|Yes| D5[Day 5: Reporting]
    Check3 -->|No| Simplify[Simplify Analysis]

    D5 --> Check4{Presentation Ready?}
    Check4 -->|Yes| Deliver[Stakeholder Workshop]
    Check4 -->|No| Bullets[Bullets Over Slides]

    Deliver --> Success([Sprint Complete])

    %% Emergency paths
    Emergency1 --> Abort1{Abort or Continue?}
    Abort1 -->|Abort| Fail([Sprint Failed])
    Abort1 -->|Continue| Compress[Compress Activities]
    Compress --> D2

    Recruit --> Emergency2{Success?}
    Emergency2 -->|Yes| D3
    Emergency2 -->|No| Reduce[Reduce Sample Size]
    Reduce --> D4

    Extend --> D4
    Simplify --> D5
    Bullets --> Deliver

    style Start fill:#a5d6a7,stroke:#388e3c,stroke-width:2px
    style Success fill:#c8e6c9,stroke:#4caf50,stroke-width:2px
    style Fail fill:#ffcdd2,stroke:#f44336,stroke-width:2px
    style Emergency1 fill:#fff3e0,stroke:#ff9800,stroke-width:2px
    style Emergency2 fill:#fff3e0,stroke:#ff9800,stroke-width:2px
```

## Rapid Techniques & Quality Trade-offs

```mermaid
graph LR
    subgraph "Speed Optimizations"
        SO1[30-45 min interviews]
        SO2[Top-line analysis only]
        SO3[Single-pass coding]
        SO4[Team consensus validation]
        SO5[Presentation format]
    end

    subgraph "Quality Maintained"
        QM1[Participant consent]
        QM2[Data security]
        QM3[Research ethics]
        QM4[Evidence for insights]
        QM5[Actionable findings]
    end

    subgraph "Quality Compromised"
        QC1[Inter-rater reliability]
        QC2[Full transcription]
        QC3[Deep thematic coding]
        QC4[Comprehensive report]
        QC5[Extensive validation]
    end

    SO1 --> QM4
    SO2 --> QM5
    SO3 --> QC1
    SO4 --> QC5
    SO5 --> QC4

    style QM1 fill:#c8e6c9,stroke:#4caf50,stroke-width:2px
    style QM2 fill:#c8e6c9,stroke:#4caf50,stroke-width:2px
    style QM3 fill:#c8e6c9,stroke:#4caf50,stroke-width:2px
    style QM4 fill:#c8e6c9,stroke:#4caf50,stroke-width:2px
    style QM5 fill:#c8e6c9,stroke:#4caf50,stroke-width:2px
    style QC1 fill:#ffcdd2,stroke:#f44336,stroke-width:2px
    style QC2 fill:#ffcdd2,stroke:#f44336,stroke-width:2px
    style QC3 fill:#ffcdd2,stroke:#f44336,stroke-width:2px
    style QC4 fill:#ffcdd2,stroke:#f44336,stroke-width:2px
    style QC5 fill:#ffcdd2,stroke:#f44336,stroke-width:2px
```

---

# 3. Conjoint Analysis Workflow

## Research Design Process

```mermaid
flowchart TD
    Start([Start Conjoint Study]) --> Plan[Study Planning<br/>2-3 days]
    Plan --> Attr[Attribute Design<br/>3-4 days]
    Attr --> Instr[Instrument Development<br/>2-3 days]
    Instr --> Collect[Data Collection<br/>5-7 days]
    Collect --> Quant[Quantitative Analysis<br/>3-4 days]
    Quant --> Insight[Insight Integration<br/>2-3 days]
    Insight --> Report[Reporting & Delivery<br/>2-3 days]
    Report --> Impl[Implementation<br/>1-2 days]
    Impl --> End([Study Complete])

    %% Decision branches
    Attr --> Validate1{Attributes Valid?}
    Validate1 -->|Yes| Instr
    Validate1 -->|No| Refine1[Refine Attributes]
    Refine1 --> Attr

    Instr --> Pilot{Pilot Test OK?}
    Pilot -->|Yes| Collect
    Pilot -->|No| Refine2[Refine Instrument]
    Refine2 --> Instr

    Collect --> SampleOK{Sample Size OK?}
    SampleOK -->|Yes| Quant
    SampleOK -->|No| ExtendCollection[Extend Collection]
    ExtendCollection --> Collect

    Quant --> ModelOK{Model Converged?}
    ModelOK -->|Yes| Insight
    ModelOK -->|No| AdjustModel[Adjust Parameters]
    AdjustModel --> Quant

    style Start fill:#a5d6a7,stroke:#388e3c,stroke-width:2px
    style End fill:#ffcdd2,stroke:#d32f2f,stroke-width:2px
    style Validate1 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style Pilot fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style SampleOK fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style ModelOK fill:#fff3e0,stroke:#f57c00,stroke-width:2px
```

## Attribute & Level Design

```mermaid
graph TD
    subgraph "Attribute Requirements"
        AR1[4-7 Attributes Total]
        AR2[Independent Attributes]
        AR3[Clear Definitions]
        AR4[Measurable]
    end

    subgraph "Level Requirements"
        LR1[2-5 Levels per Attribute]
        LR2[Realistic Levels]
        LR3[Appropriate Range]
        LR4[Clearly Differentiated]
    end

    subgraph "Design Quality"
        DQ1[Design Efficiency > 0.8]
        DQ2[Orthogonality Maintained]
        DQ3[Balance Achieved]
        DQ4[12-20 Choice Tasks]
    end

    AR1 --> DQ1
    AR2 --> DQ2
    LR1 --> DQ1
    LR2 --> DQ3
    LR3 --> DQ4
    LR4 --> DQ4

    style AR1 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style AR2 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style AR3 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style AR4 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style DQ1 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style DQ2 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style DQ3 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style DQ4 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
```

## Statistical Analysis Flow

```mermaid
flowchart LR
    RawData[Raw Choice Data<br/>n>200] --> Clean[Data Validation<br/>& Cleaning]
    Clean --> HB[Hierarchical Bayes<br/>Analysis]
    HB --> Utilities[Individual Utilities<br/>& Part-worths]
    Utilities --> Importance[Attribute Importance<br/>Calculation]
    Importance --> Segments[Preference Segments<br/>3-5 segments]
    Segments --> Simulation[Market Simulation<br/>& Optimization]

    %% Quality checks
    Clean -.-> QC1{Quality OK?}
    QC1 -->|Yes| HB
    QC1 -->|No| Exclude[Exclude Bad Responses]
    Exclude --> Clean

    HB -.-> QC2{Converged?}
    QC2 -->|Yes| Utilities
    QC2 -->|No| Adjust[Adjust Parameters]
    Adjust --> HB

    Simulation --> Validate{Realistic?}
    Validate -->|Yes| Results[Final Results]
    Validate -->|No| Review[Review Model]
    Review --> Segments

    style RawData fill:#e1f5fe,stroke:#0277bd,stroke-width:2px
    style Results fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style QC1 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style QC2 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style Validate fill:#fff3e0,stroke:#f57c00,stroke-width:2px
```

---

# 4. Ethnographic Research Workflow

## Field Work Process

```mermaid
flowchart TD
    Start([Start Ethnographic Study]) --> Design[Study Design<br/>3-4 days]
    Design --> Protocol[Protocol Development<br/>2-3 days]
    Protocol --> Immersion[Field Immersion<br/>2-4 weeks]
    Immersion --> Coding[Coding & Analysis<br/>1 week]
    Coding --> Interpret[Interpretation<br/>3-4 days]
    Interpret --> Document[Documentation<br/>3-4 days]
    Document --> Transfer[Knowledge Transfer<br/>2-3 days]
    Transfer --> End([Study Complete])

    %% Immersion sub-phases
    Immersion --> Initial[Initial Immersion<br/>Week 1]
    Initial --> Deep[Deep Observation<br/>Weeks 2-3]
    Deep --> Participate[Participant Activities]
    Participate --> Contextual[Contextual Interviews]
    Contextual --> Analysis[Rolling Analysis]
    Analysis --> Immersion

    style Start fill:#a5d6a7,stroke:#388e3c,stroke-width:2px
    style End fill:#ffcdd2,stroke:#d32f2f,stroke-width:2px
    style Initial fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    style Deep fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    style Participate fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    style Contextual fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
```

## Ethnographic Data Types & Analysis

```mermaid
graph LR
    subgraph "Data Collection"
        DC1[Field Notes<br/>Descriptive, Reflective, Analytic]
        DC2[Audio/Video<br/>Recordings]
        DC3[Photography<br/>Environmental & Social]
        DC4[Artifacts<br/>Cultural Objects]
        DC5[Interviews<br/>Contextual & Walking]
    end

    subgraph "Analysis Methods"
        AM1[Open Coding<br/>Initial Categories]
        AM2[Axial Coding<br/>Relationships]
        AM3[Selective Coding<br/>Core Themes]
        AM4[Constant Comparison<br/>Pattern Validation]
        AM5[Thick Description<br/>Rich Narratives]
    end

    subgraph "Outputs"
        O1[Cultural Patterns]
        O2[Behavioral Models]
        O3[Environmental Influences]
        O4[Design Principles]
        O5[Thick Descriptions]
    end

    DC1 --> AM1
    DC2 --> AM2
    DC3 --> AM3
    DC4 --> AM4
    DC5 --> AM5

    AM1 --> O1
    AM2 --> O2
    AM3 --> O3
    AM4 --> O4
    AM5 --> O5

    style DC1 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style DC2 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style DC3 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style DC4 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style DC5 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style O1 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style O2 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style O3 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style O4 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style O5 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
```

## Quality Criteria (Lincoln & Guba)

```mermaid
quadrantChart
    title Ethnographic Quality Framework
    x-axis Low --> High
    y-axis Internal --> External

    Credibility: [0.8, 0.8]
    Transferability: [0.8, 0.2]
    Dependability: [0.2, 0.8]
    Confirmability: [0.2, 0.2]
```

---

# 5. Mixed Methods Research Workflow

## Integration Strategy

```mermaid
flowchart TD
    Start([Start Mixed Methods Study]) --> DesignInt[Design Integration<br/>2-3 days]
    DesignInt --> ParPlan[Parallel Planning<br/>3-4 days]

    %% Parallel execution
    ParPlan --> QualCol[Qualitative Collection<br/>1-2 weeks]
    ParPlan --> QuantCol[Quantitative Collection<br/>1-2 weeks]

    %% Convergence
    QualCol --> Sync1{Sync Point 1}
    QuantCol --> Sync1
    Sync1 --> IntAnalysis[Integrated Analysis<br/>1 week]

    IntAnalysis --> SynthVal[Synthesis & Validation<br/>3-4 days]
    SynthVal --> MixedReport[Mixed Reporting<br/>3-4 days]
    MixedReport --> ImplPlan[Implementation Planning<br/>2-3 days]
    ImplPlan --> End([Study Complete])

    %% Quality validation
    IntAnalysis -.-> QC1{Convergence OK?}
    QC1 -->|Yes| SynthVal
    QC1 -->|No| Investigate[Investigate Divergence]
    Investigate --> IntAnalysis

    SynthVal -.-> QC2{Triangulation Valid?}
    QC2 -->|Yes| MixedReport
    QC2 -->|No| MemberCheck[Member Checking]
    MemberCheck --> SynthVal

    style Start fill:#a5d6a7,stroke:#388e3c,stroke-width:2px
    style End fill:#ffcdd2,stroke:#d32f2f,stroke-width:2px
    style Sync1 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style QC1 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style QC2 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
```

## Integration Techniques

```mermaid
graph TB
    subgraph "Data Transformation"
        DT1[Qualitizing<br/>Quant → Qual]
        DT2[Quantitizing<br/>Qual → Quant]
        DT3[Data Consolidation<br/>Merge datasets]
        DT4[Data Comparison<br/>Side-by-side]
    end

    subgraph "Analysis Integration"
        AI1[Sequential Explanatory<br/>Quant → Qual]
        AI2[Sequential Exploratory<br/>Qual → Quant]
        AI3[Concurrent Triangulation<br/>Parallel comparison]
        AI4[Concurrent Nested<br/>One embedded in other]
    end

    subgraph "Interpretation Methods"
        IM1[Narrative Weaving<br/>Integrated story]
        IM2[Joint Displays<br/>Side-by-side tables]
        IM3[Data Matrices<br/>Convergence grids]
        IM4[Mixed Tables<br/>Quan → Qual → Meta]
    end

    DT1 --> AI1
    DT2 --> AI2
    DT3 --> AI3
    DT4 --> AI4

    AI1 --> IM1
    AI2 --> IM2
    AI3 --> IM3
    AI4 --> IM4

    style DT1 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style DT2 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style DT3 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style DT4 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style IM1 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style IM2 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style IM3 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style IM4 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
```

## Convergence Analysis Matrix

```mermaid
graph LR
    subgraph "Qualitative Findings"
        QF1[Theme A: User Frustration]
        QF2[Theme B: Feature Importance]
        QF3[Theme C: Context Usage]
    end

    subgraph "Quantitative Results"
        QR1[85% report difficulties]
        QR2[Feature X highest rated]
        QR3[Mobile usage patterns]
    end

    subgraph "Integration Status"
        IS1[✓ CONVERGENT<br/>Strong agreement]
        IS2[✓ CONVERGENT<br/>Aligned priorities]
        IS3[~ PARTIAL<br/>Need clarification]
    end

    QF1 --> IS1
    QR1 --> IS1
    QF2 --> IS2
    QR2 --> IS2
    QF3 --> IS3
    QR3 --> IS3

    style IS1 fill:#c8e6c9,stroke:#4caf50,stroke-width:2px
    style IS2 fill:#c8e6c9,stroke:#4caf50,stroke-width:2px
    style IS3 fill:#fff3e0,stroke:#ff9800,stroke-width:2px
```

---

# Cross-Workflow Analysis

## Methodology Selection Decision Tree

```mermaid
flowchart TD
    Start([Research Need Identified]) --> Time{Timeline Available?}

    Time -->|<1 week| Rapid[Rapid Discovery<br/>Sprint]
    Time -->|1-3 weeks| Duration{Research Depth?}
    Time -->|>3 weeks| Scope{Research Scope?}

    Duration -->|Surface insights| Rapid
    Duration -->|Preference analysis| Conjoint[Conjoint Analysis]
    Duration -->|Deep understanding| Scope

    Scope -->|Broad + Validation| Mixed[Mixed Methods<br/>Research]
    Scope -->|Cultural context| Ethno[Ethnographic<br/>Research]
    Scope -->|User insights| Interview[User Interview<br/>Research]

    %% Decision criteria
    Rapid -.-> RC[Criteria: Speed > Depth]
    Conjoint -.-> CC[Criteria: Quantify Preferences]
    Mixed -.-> MC[Criteria: Validation + Breadth]
    Ethno -.-> EC[Criteria: Cultural Understanding]
    Interview -.-> IC[Criteria: User Insights]

    style Start fill:#a5d6a7,stroke:#388e3c,stroke-width:2px
    style Rapid fill:#ffeb3b,stroke:#f57f17,stroke-width:2px
    style Conjoint fill:#2196f3,stroke:#0d47a1,stroke-width:2px
    style Mixed fill:#9c27b0,stroke:#4a148c,stroke-width:2px
    style Ethno fill:#ff5722,stroke:#bf360c,stroke-width:2px
    style Interview fill:#4caf50,stroke:#1b5e20,stroke-width:2px
```

## Quality Gates Across Workflows

```mermaid
graph TB
    subgraph "Universal Quality Gates"
        UQG1[Stakeholder Alignment<br/>Approval >75%]
        UQG2[Sample Size Adequate<br/>Power >0.8 or Saturation]
        UQG3[Data Quality High<br/>Accuracy >95%]
        UQG4[Analysis Reliable<br/>Kappa >0.7 or Consensus]
        UQG5[Insights Actionable<br/>ACTIONABLE Framework]
        UQG6[Report Complete<br/>All Sections Present]
        UQG7[Stakeholder Acceptance<br/>Satisfaction >4/5]
    end

    subgraph "Workflow-Specific Gates"
        WSG1[Interview: Pilot Success<br/>4/4 metrics pass]
        WSG2[Rapid: Timeline Adherence<br/>5-day limit strict]
        WSG3[Conjoint: Model Convergence<br/>RLH >0.6]
        WSG4[Ethnographic: Member Validation<br/>Participant feedback]
        WSG5[Mixed Methods: Triangulation<br/>Convergence validated]
    end

    UQG1 --> WSG1
    UQG2 --> WSG2
    UQG3 --> WSG3
    UQG4 --> WSG4
    UQG5 --> WSG5
    UQG6 --> WSG1
    UQG7 --> WSG5

    style UQG1 fill:#e1f5fe,stroke:#0277bd,stroke-width:2px
    style UQG2 fill:#e1f5fe,stroke:#0277bd,stroke-width:2px
    style UQG3 fill:#e1f5fe,stroke:#0277bd,stroke-width:2px
    style UQG4 fill:#e1f5fe,stroke:#0277bd,stroke-width:2px
    style UQG5 fill:#e1f5fe,stroke:#0277bd,stroke-width:2px
    style UQG6 fill:#e1f5fe,stroke:#0277bd,stroke-width:2px
    style UQG7 fill:#e1f5fe,stroke:#0277bd,stroke-width:2px
    style WSG1 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style WSG2 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style WSG3 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style WSG4 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style WSG5 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
```

---

# Technical Implementation Details

## Agent Communication Protocol

```mermaid
sequenceDiagram
    participant Agent1 as Sending Agent
    participant Validator as Artifact Validator
    participant Storage as Artifact Storage
    participant Agent2 as Receiving Agent

    Note over Agent1,Agent2: Handoff Initiation
    Agent1->>Validator: Submit artifact + metadata
    Validator->>Validator: Schema validation
    Validator->>Validator: Format check
    Validator->>Validator: Quality gate check

    alt Validation Passes
        Validator->>Storage: Store validated artifact
        Storage->>Agent2: Notify artifact available
        Agent2->>Storage: Retrieve artifact
        Agent2->>Agent1: Confirm receipt
    else Validation Fails
        Validator->>Agent1: Return error details
        Agent1->>Agent1: Fix issues
        Agent1->>Validator: Resubmit artifact
    end

    Note over Agent1,Agent2: Quality Assurance
    Agent2->>Agent2: Process artifact
    Agent2->>Validator: Report processing success
    Validator->>Storage: Update artifact status
```

## Error Escalation Hierarchy

```mermaid
graph TD
    TaskLevel[Task Level Error<br/>Response: 1 hour<br/>Owner: Agent] --> PhaseLevel{Resolved?}
    PhaseLevel -->|No| PhaseEscalate[Phase Level Error<br/>Response: 4 hours<br/>Owner: Orchestrator]
    PhaseLevel -->|Yes| Resolved[Error Resolved]

    PhaseEscalate --> ProjectLevel{Resolved?}
    ProjectLevel -->|No| ProjectEscalate[Project Level Error<br/>Response: Immediate<br/>Owner: Research Lead]
    ProjectLevel -->|Yes| Resolved

    ProjectEscalate --> Decision{Decision}
    Decision -->|Continue| AdjustPlan[Adjust Project Plan]
    Decision -->|Abort| ProjectStop[Project Terminated]
    Decision -->|Modify| ChangeScope[Change Scope/Timeline]

    AdjustPlan --> Resolved
    ChangeScope --> Resolved

    style TaskLevel fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style PhaseEscalate fill:#ffeb3b,stroke:#f57f17,stroke-width:2px
    style ProjectEscalate fill:#f44336,stroke:#c62828,stroke-width:2px
    style Resolved fill:#4caf50,stroke:#2e7d32,stroke-width:2px
    style ProjectStop fill:#ffcdd2,stroke:#d32f2f,stroke-width:2px
```

## Data Lineage & Traceability

```mermaid
flowchart LR
    subgraph "Raw Data"
        RD1[Interview Recordings]
        RD2[Survey Responses]
        RD3[Observation Notes]
        RD4[Cultural Artifacts]
    end

    subgraph "Processed Data"
        PD1[Transcripts JSON]
        PD2[Cleaned Dataset]
        PD3[Coded Field Notes]
        PD4[Artifact Catalog]
    end

    subgraph "Analysis Outputs"
        AO1[Themes & Patterns]
        AO2[Statistical Results]
        AO3[Cultural Models]
        AO4[Integrated Insights]
    end

    subgraph "Final Deliverables"
        FD1[Research Report]
        FD2[Personas]
        FD3[Journey Maps]
        FD4[Recommendations]
    end

    RD1 --> PD1 --> AO1 --> FD1
    RD2 --> PD2 --> AO2 --> FD2
    RD3 --> PD3 --> AO3 --> FD3
    RD4 --> PD4 --> AO4 --> FD4

    %% Cross-connections for mixed methods
    AO1 -.-> AO4
    AO2 -.-> AO4
    AO3 -.-> AO4

    style RD1 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style RD2 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style RD3 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style RD4 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style FD1 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style FD2 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style FD3 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style FD4 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
```

---

# Workflow Comparison Matrix

| Aspect | User Interview | Rapid Discovery | Conjoint Analysis | Ethnographic | Mixed Methods |
|--------|----------------|-----------------|-------------------|--------------|---------------|
| **Duration** | 3-6 weeks | 5 days | 2-3 weeks | 4-8 weeks | 4-6 weeks |
| **Sample Size** | 12-20 | 8-10 | 200+ | 10-20 | 15-25 + 200+ |
| **Primary Output** | Personas, Journey Maps | Quick insights | Utility scores | Cultural patterns | Validated insights |
| **Quality Focus** | Comprehensive | Speed | Statistical rigor | Cultural validity | Triangulation |
| **Error Tolerance** | Low | Medium | Very Low | Low | Low |
| **Automation Level** | High | Very High | Medium | Low | Medium |
| **Stakeholder Involvement** | Moderate | High | Low | Low | High |
| **Skill Requirements** | UX Research | UX Research | Statistics | Anthropology | Multi-disciplinary |

---

# Success Metrics & KPIs

## Workflow Performance Metrics

```mermaid
graph TB
    subgraph "Efficiency Metrics"
        EM1[Time to Completion<br/>vs. Estimated Duration]
        EM2[Resource Utilization<br/>% of Allocated Budget]
        EM3[Error Rate<br/>Errors per Phase]
        EM4[Rework Frequency<br/>Quality Gate Failures]
    end

    subgraph "Quality Metrics"
        QM1[Stakeholder Satisfaction<br/>Score >4/5]
        QM2[Insight Actionability<br/>Implementation Rate]
        QM3[Data Quality<br/>Accuracy & Completeness]
        QM4[Recommendation Uptake<br/>% Accepted by Stakeholders]
    end

    subgraph "Impact Metrics"
        IM1[Business Decision Support<br/>Decisions Enabled]
        IM2[User Understanding<br/>Knowledge Gained]
        IM3[Product Improvement<br/>Changes Implemented]
        IM4[Strategic Alignment<br/>Goal Achievement]
    end

    EM1 --> QM1
    EM2 --> QM2
    EM3 --> QM3
    EM4 --> QM4

    QM1 --> IM1
    QM2 --> IM2
    QM3 --> IM3
    QM4 --> IM4

    style EM1 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style EM2 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style EM3 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style EM4 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style QM1 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style QM2 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style QM3 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style QM4 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style IM1 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style IM2 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style IM3 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    style IM4 fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
```

---

# Conclusion

This User Research Multi-Agent System provides a comprehensive framework for conducting high-quality research across multiple methodologies. The system's strength lies in its:

1. **Systematic Approach**: Each workflow follows established research best practices with clear quality gates
2. **Flexibility**: Five different approaches to match various research needs and constraints
3. **Quality Assurance**: Built-in error handling, validation, and recovery mechanisms
4. **Coordination**: Seamless agent handoffs with standardized artifact specifications
5. **Measurable Outcomes**: Clear success metrics and continuous improvement feedback loops

The workflows are designed to be both rigorous and practical, enabling research teams to deliver actionable insights that drive informed decision-making and user-centered design.