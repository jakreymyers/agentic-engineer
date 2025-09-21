# Data Format Converter Specification

## Tool Overview

**Name:** Data Format Converter
**ID:** data-format-converter
**Category:** Data Integration & Transformation
**Purpose:** Bridge format incompatibilities between research tools, ensuring seamless data flow across the analysis pipeline

## Critical Integration Gap Being Solved

The QA audit identified a **workflow-breaking issue**: the analyze-transcript task outputs markdown format, but the digital-affinity-mapper requires JSON input. This converter ensures data flows correctly through the pipeline.

## Core Conversions Required

### 1. Transcript Analysis → Affinity Mapper
```yaml
conversion:
  name: transcript_to_affinity
  source:
    tool: analyze-transcript
    format: markdown
    structure:
      - coded_segments
      - themes
      - quotes
      - memos

  target:
    tool: digital-affinity-mapper
    format: json
    schema:
      insights:
        - card_id: uuid
        - insight: string
        - evidence: string
        - theme: string
        - tags: array
        - participant: string
        - confidence: float
        - sentiment: enum
```

### 2. Affinity Mapper → Statistical Analyzer
```yaml
conversion:
  name: affinity_to_stats
  source:
    tool: digital-affinity-mapper
    format: json
    structure: clustered_insights

  target:
    tool: research-stats-analyzer
    format: csv
    columns:
      - cluster_id
      - insight_text
      - frequency
      - sentiment_score
```

### 3. Sentiment Analyzer → Visualization Generator
```yaml
conversion:
  name: sentiment_to_viz
  source:
    tool: research-sentiment-analyzer
    format: json
    structure: sentiment_analysis

  target:
    tool: research-viz-generator
    format: json
    schema: chart_data_specification
```

## Conversion Functions

### Markdown to JSON Converter
```javascript
function convertTranscriptToAffinity(markdownContent) {
  // Parse markdown structure
  const sections = parseMarkdownSections(markdownContent);

  // Extract coded segments
  const segments = sections['coded_segments'].map(segment => ({
    card_id: generateUUID(),
    insight: segment.text,
    evidence: segment.quote,
    theme: segment.primary_code,
    tags: segment.additional_codes,
    participant: segment.participant_id,
    confidence: segment.confidence || 0.85,
    sentiment: detectSentiment(segment.text)
  }));

  return {
    insights: segments,
    metadata: {
      source: 'transcript_analysis',
      timestamp: new Date().toISOString(),
      total_segments: segments.length
    }
  };
}
```

### JSON to CSV Converter
```javascript
function convertAffinityToStats(jsonData) {
  const rows = [];
  jsonData.clusters.forEach(cluster => {
    cluster.insights.forEach(insight => {
      rows.push({
        cluster_id: cluster.id,
        cluster_name: cluster.name,
        insight_id: insight.card_id,
        insight_text: insight.insight,
        frequency: cluster.insights.length,
        sentiment_score: insight.sentiment_value,
        confidence: insight.confidence
      });
    });
  });
  return convertToCSV(rows);
}
```

## Data Validation Rules

### Pre-Conversion Validation
```yaml
validation:
  input_checks:
    - file_exists: true
    - format_valid: true
    - required_fields: present
    - data_integrity: verified

  error_handling:
    - missing_field: use_default
    - invalid_format: attempt_repair
    - corrupt_data: reject_and_notify
```

### Post-Conversion Validation
```yaml
validation:
  output_checks:
    - schema_compliance: 100%
    - data_completeness: >95%
    - format_validity: strict
    - relationship_preservation: verified
```

## Integration Points

### Agent Command Interface
```yaml
commands:
  data_analyst:
    - "*convert-transcript-to-affinity <file> [--validate]"
    - "*prepare-for-synthesis <data> [--format=json]"

  insight_synthesizer:
    - "*convert-affinity-to-report <clusters> [--format=md]"
    - "*prepare-for-stats <insights> [--format=csv]"
```

### Automated Pipeline Triggers
```yaml
triggers:
  on_task_complete:
    - task: analyze-transcript
      action: auto_convert_to_affinity_format

  on_tool_handoff:
    - from: data-analyst
      to: insight-synthesizer
      action: ensure_format_compatibility
```

## Performance Requirements

### Conversion Speed
- Small files (<1MB): <100ms
- Medium files (1-10MB): <1 second
- Large files (10-100MB): <10 seconds
- Batch processing: Parallel execution

### Accuracy Requirements
- Data preservation: 100%
- Format compliance: 100%
- Semantic preservation: >99%
- Relationship integrity: 100%

## Error Recovery

### Common Issues and Solutions
```yaml
error_scenarios:
  missing_required_field:
    detection: schema_validation
    solution: use_intelligent_defaults
    notification: warn_user

  incompatible_encoding:
    detection: charset_detection
    solution: convert_to_utf8
    notification: log_conversion

  circular_reference:
    detection: graph_analysis
    solution: break_cycle_at_weakest_point
    notification: alert_user
```

## Quality Assurance

### Conversion Testing
```yaml
test_suite:
  unit_tests:
    - Each conversion function
    - Edge cases and errors
    - Performance benchmarks

  integration_tests:
    - Full pipeline flow
    - Multi-step conversions
    - Parallel processing

  validation_tests:
    - Schema compliance
    - Data integrity
    - Semantic preservation
```

### Monitoring Metrics
- Conversion success rate: >99.9%
- Data loss incidents: 0
- Format compliance: 100%
- Processing time: Within SLA

## Implementation Priority

This converter is **CRITICAL** for system functionality. Without it, the workflow breaks at the analysis → synthesis handoff point.

### Implementation Steps
1. Build core conversion engine
2. Implement transcript → affinity converter (PRIORITY)
3. Add validation framework
4. Create automated triggers
5. Integrate with orchestrator
6. Test end-to-end pipeline

## Success Criteria

- ✅ All workflow handoffs successful
- ✅ No data loss during conversion
- ✅ Format compatibility verified
- ✅ Performance targets met
- ✅ Error handling robust
- ✅ Integration seamless