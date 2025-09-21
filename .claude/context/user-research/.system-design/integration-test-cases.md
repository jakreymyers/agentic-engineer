# Integration Test Cases for User Research System

## Purpose
Validate end-to-end functionality of the User Research Multi-Agent System through comprehensive integration testing. These test cases verify data flow, agent coordination, tool integration, and quality gate validation.

## Critical Test Suites

### Test Suite 1: End-to-End User Interview Workflow

#### Test Case 1.1: Complete Happy Path
```yaml
test_id: E2E-001
name: Complete user interview workflow execution
priority: CRITICAL

setup:
  - Create test research project
  - Mock 3 participant profiles
  - Prepare sample audio files

execution_steps:
  1. Initiate workflow:
     - Input: Research objectives
     - Expected: Research brief created
     - Validation: SMART criteria met (5/5)

  2. Participant recruitment:
     - Input: Screening criteria
     - Expected: 3 participants qualified
     - Validation: Quota tracking accurate

  3. Interview execution:
     - Input: Discussion guide
     - Expected: Transcripts generated
     - Validation: Speaker diarization >85% accuracy

  4. Transcript analysis:
     - Input: Transcripts (3)
     - Expected: Coded data in JSON
     - Validation: >95% coverage, format valid

  5. DATA FORMAT CONVERSION (CRITICAL):
     - Input: Markdown analysis output
     - Expected: JSON for affinity mapper
     - Validation: Schema compliance 100%

  6. Affinity mapping:
     - Input: JSON insights (30+)
     - Expected: Clustered themes
     - Validation: All insights mapped

  7. Synthesis:
     - Input: Affinity clusters
     - Expected: Personas, journeys
     - Validation: Evidence links preserved

  8. Reporting:
     - Input: Synthesized insights
     - Expected: Report + presentation
     - Validation: All sections complete

expected_results:
  - Duration: <5 days
  - Quality gates passed: 12/12
  - Data integrity: 100%
  - Artifacts generated: 8

failure_points:
  - Step 5: Format conversion MUST succeed
  - Step 4: If coverage <85%, workflow stops
  - Step 1: If SMART fails, cannot proceed
```

#### Test Case 1.2: Quality Gate Failure Recovery
```yaml
test_id: E2E-002
name: Quality gate failure and recovery
priority: HIGH

scenario: Coding reliability fails (kappa < 0.7)

execution_steps:
  1. Trigger failure:
     - Introduce coding inconsistency
     - Expected: Gate fails at analysis phase
     - Validation: Error message clear

  2. Recovery process:
     - Action: Recoding with second analyst
     - Expected: Kappa recalculated
     - Validation: New value >0.7

  3. Resume workflow:
     - Expected: Continues from checkpoint
     - Validation: No data loss

expected_results:
  - Recovery successful
  - Audit trail complete
  - Quality maintained
```

### Test Suite 2: Rapid Discovery Sprint

#### Test Case 2.1: 5-Day Timeline Validation
```yaml
test_id: RD-001
name: Rapid discovery sprint timing
priority: HIGH

constraints:
  - Hard deadline: 5 days
  - Minimum insights: 10

execution_steps:
  1. Day 1: Planning (4 hours max)
  2. Day 2-3: Interviews (8 total)
  3. Day 4: Analysis (rapid coding)
  4. Day 5: Synthesis & presentation

validation_points:
  - Each phase within time limit
  - Quality trade-offs documented
  - Minimum viable insights achieved
```

### Test Suite 3: Tool Integration

#### Test Case 3.1: Transcription → Analysis Pipeline
```yaml
test_id: TOOL-001
name: Transcription to analysis data flow
priority: CRITICAL

test_data:
  - Audio file: 45 minutes
  - Expected segments: ~50

execution:
  1. Submit to transcription service
  2. Verify JSON output format
  3. Pass to analysis task
  4. Verify markdown output
  5. Convert to affinity format
  6. Validate JSON schema

validation:
  - No data loss at any step
  - Formats compatible
  - Metadata preserved
```

#### Test Case 3.2: Multi-Tool Orchestration
```yaml
test_id: TOOL-002
name: Parallel tool execution
priority: HIGH

scenario: Mixed methods with parallel streams

execution:
  1. Launch survey (stats analyzer)
  2. Conduct interviews (transcription)
  3. Run sentiment analysis
  4. Merge in synthesis

validation:
  - Tools run in parallel
  - Data synchronized correctly
  - No race conditions
```

### Test Suite 4: Agent Coordination

#### Test Case 4.1: Agent Handoff Validation
```yaml
test_id: AGENT-001
name: Agent handoff with artifacts
priority: HIGH

test_sequence:
  1. Orchestrator → Strategist
     - Artifact: Research brief
     - Format: Markdown
     - Validation: All sections present

  2. Strategist → Specialist
     - Artifact: Study design
     - Format: YAML + MD
     - Validation: Quotas defined

  3. Specialist → Analyst
     - Artifact: Transcripts
     - Format: JSON
     - Validation: Speaker tags present

  4. Analyst → Synthesizer
     - Artifact: Coded data
     - Format: JSON (converted)
     - Validation: Schema valid

  5. Synthesizer → Reporter
     - Artifact: Insights
     - Format: Structured JSON
     - Validation: Evidence linked

validation:
  - Each handoff successful
  - Formats compatible
  - No data loss
```

### Test Suite 5: Error Handling

#### Test Case 5.1: Tool Failure Recovery
```yaml
test_id: ERROR-001
name: Transcription service failure
priority: HIGH

failure_injection:
  - Point: Transcription API timeout
  - Type: Network error

expected_behavior:
  1. Retry mechanism (3 attempts)
  2. Fallback to manual transcription
  3. Notification to orchestrator
  4. Checkpoint preservation

validation:
  - Graceful degradation
  - No data loss
  - Clear error messages
```

#### Test Case 5.2: Data Format Mismatch
```yaml
test_id: ERROR-002
name: Format conversion failure
priority: CRITICAL

failure_injection:
  - Invalid JSON from analysis
  - Missing required fields

expected_behavior:
  1. Validation catches error
  2. Detailed error report
  3. Suggested fixes provided
  4. Manual intervention option

validation:
  - Error caught before propagation
  - Recovery path clear
  - Audit trail maintained
```

### Test Suite 6: Quality Gate Automation

#### Test Case 6.1: Measurable Gate Validation
```yaml
test_id: QG-001
name: SMART criteria automation
priority: HIGH

input:
  objectives:
    - "Understand user needs" (FAILS)
    - "Identify 5 usability issues by March 1" (PASSES)

validation:
  - Automated checker identifies failure
  - Specific feedback provided
  - Suggestions for improvement
```

#### Test Case 6.2: Statistical Validation
```yaml
test_id: QG-002
name: Power analysis automation
priority: MEDIUM

input:
  - Effect size: 0.5
  - Alpha: 0.05
  - Desired power: 0.8

validation:
  - Sample size calculated (n=64)
  - Passes quality gate
  - Documentation generated
```

## Performance Test Cases

### Test Case P1: Concurrent Workflow Execution
```yaml
test_id: PERF-001
name: Multiple concurrent workflows
load: 5 simultaneous workflows

metrics:
  - Response time <5s per operation
  - No deadlocks
  - Resource utilization <80%
  - All workflows complete
```

### Test Case P2: Large Data Volume
```yaml
test_id: PERF-002
name: High volume transcript processing
load: 100 transcripts, 50 pages each

metrics:
  - Processing time <2 hours
  - Memory usage <16GB
  - No data corruption
  - Quality maintained
```

## Security Test Cases

### Test Case S1: Data Privacy
```yaml
test_id: SEC-001
name: PII handling in transcripts

validation:
  - PII detected and flagged
  - Anonymization applied
  - Audit trail maintained
  - Access controlled
```

## Regression Test Suite

### Critical Path Tests (Run on Every Change)
1. E2E-001: Complete happy path
2. TOOL-001: Transcription pipeline
3. AGENT-001: Agent handoffs
4. ERROR-002: Format conversion
5. QG-001: Quality gate validation

### Weekly Full Suite
- All test cases executed
- Performance benchmarks verified
- Security scans completed

## Test Data Requirements

### Sample Data Sets
```yaml
transcripts:
  - clean_audio_45min.mp3
  - poor_quality_30min.mp3
  - multiple_speakers_60min.mp3

participants:
  - mock_profiles_diverse.json (20)
  - edge_cases.json (5)

templates:
  - valid_research_brief.md
  - invalid_smart_objectives.md
```

## Automation Framework

### Test Execution
```python
class IntegrationTestRunner:
    def setup(self):
        # Initialize test environment
        # Load test data
        # Mock external services

    def execute_test(self, test_case):
        # Run test steps
        # Capture results
        # Validate outcomes

    def teardown(self):
        # Clean test data
        # Reset environment
        # Generate reports
```

### Continuous Integration
```yaml
ci_pipeline:
  triggers:
    - on_commit: Critical path tests
    - nightly: Full regression suite
    - weekly: Performance tests

  reporting:
    - Test results dashboard
    - Failure notifications
    - Trend analysis
```

## Success Criteria

### System Release Criteria
- Critical path tests: 100% pass
- All test suites: >95% pass
- Performance targets: Met
- Security scans: Clean
- Documentation: Complete

### Quality Metrics
- Test coverage: >80%
- Defect escape rate: <5%
- Mean time to recovery: <30min
- System availability: >99.9%

## Known Issues & Workarounds

### Issue 1: Conjoint workflow task reference
- Status: FIXED
- Workaround: Updated to correct task name

### Issue 2: Format conversion critical gap
- Status: FIXED
- Solution: Data format converter implemented

### Issue 3: Unmeasurable quality gates
- Status: FIXED
- Solution: Measurable criteria defined

## Test Report Template

```markdown
# Integration Test Report
Date: [DATE]
Version: [VERSION]
Environment: [ENV]

## Summary
- Tests Executed: X/Y
- Pass Rate: X%
- Critical Failures: [LIST]

## Details
[Per test case results]

## Recommendations
[Actions needed]
```