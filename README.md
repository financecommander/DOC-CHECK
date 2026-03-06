# Hive + Frady Investigative Intelligence System

## Overview

This project adds a two-stage investigative workflow to the Swarm platform:

1. **Hive Detection System**
   - Screens private equity firms and related entities
   - Detects structural, behavioral, and timing tells
   - Builds entity, personnel, and timeline intelligence
   - Produces normalized firm-level risk profiles

2. **Frady SEC Review System**
   - Reviews Hive findings at document and evidence level
   - Validates or downgrades candidate tells
   - Assesses SEC-readiness and evidentiary sufficiency
   - Produces filing-oriented review outputs and counsel-ready packets

Hive is the discovery and prioritization layer.
Frady is the validation and review layer.

---

## System Goals

- Screen PE firms for high-risk misconduct patterns
- Use public and licensed datasets to build structured intelligence
- Rank targets using multi-dimension scoring
- Escalate only qualified cases to deep evidentiary review
- Package validated findings for whistleblower, regulatory, or counsel workflows

---

## Core Workflow

```text
Universe of PE firms
→ Hive screen
→ tell detection
→ graph + timeline assembly
→ risk profile
→ Frady review trigger
→ evidentiary validation
→ SEC-readiness scoring
→ dossier / counsel package
```

---

## Hive Responsibilities

Hive is responsible for:

- entity discovery
- affiliate mapping
- personnel graph construction
- timeline construction
- tell detection
- convergence scoring
- watchlist ranking
- investigation escalation logic

Hive uses three tell dimensions:

- **A / Structural**
- **B / Behavioral**
- **C / Timing**

Composite risk score is normalized to a 0–100 scale with convergence weighting when signals appear across multiple dimensions.

---

## Frady Responsibilities

Frady is responsible for:

- source-by-source review
- document extraction
- contradiction detection
- evidentiary sufficiency checks
- validation of Hive tells
- legal-risk-aware narrative shaping
- SEC-readiness assessment

Frady does **not** perform broad universe screening.
Frady operates only on cases escalated by Hive or directly queued by an analyst.

---

## Core Data Objects

### HiveCasePacket

```python
HiveCasePacket = {
    "firm_profile": "...",
    "top_tells": [],
    "entity_map": {},
    "personnel_graph": {},
    "timeline": [],
    "evidence_bundle": [],
    "data_completeness": 0.0,
    "open_questions": []
}
```

### FradyReviewResult

```python
FradyReviewResult = {
    "review_status": "supported|mixed|weak|not_ready",
    "validated_tells": [],
    "rejected_tells": [],
    "missing_evidence": [],
    "litigation_risk_notes": [],
    "sec_readiness_score": 0.0,
    "recommended_next_steps": []
}
```

---

## Hive Drone Architecture

Hive drones gather structured intelligence from external sources.

Initial drone set:

- `edgar_drone`
- `delaware_drone`
- `brokercheck_drone`
- `enforcement_drone`
- `timeline_drone`
- `personnel_drone`
- `dealdata_drone`
- `news_drone`

All drones must implement a shared task/result contract.

---

## Swarm Roles for this Project

### Acquisition Swarm
- EDGAR retrieval
- Delaware lookup
- BrokerCheck retrieval
- Enforcement search
- News and court scan
- Deal intelligence

### Resolution Swarm
- entity deduplication
- alias normalization
- person/entity linking
- relationship confidence scoring

### Detection Swarm
- structural tell detection
- behavioral tell detection
- timing tell detection
- LP clause extraction
- valuation anomaly analysis

### Challenge Swarm
- false-positive challenge
- innocent-explanation generation
- evidentiary gap review
- escalation veto / downgrade recommendation

### Dossier Swarm
- chronology generation
- evidence table assembly
- source validation
- filing packet formatting

---

## Escalation Rules

A case may move from Hive to Frady when:

- Hive risk tier is `elevated`, `high`, or `critical`
- at least two tell dimensions are active
- data completeness exceeds configured threshold
- there is at least one documentary evidence path

Recommended default thresholds:

- `elevated+`
- `dimensions_active >= 2`
- `data_completeness >= 0.70`

---

## Storage Architecture

- **Postgres** for structured entities, tells, scores, case states
- **Neo4j** for personnel/entity relationship graph
- **Redis** for task queue, caching, and rate-limit protection

---

## API / Source Policy

Supported source classes include:

- SEC EDGAR
- Delaware SOS
- FINRA BrokerCheck
- DOJ / FDA / state enforcement sources
- PACER / court data
- licensed PE deal data providers

All source adapters must:

- log provenance
- store raw response references when allowed
- preserve timestamps
- expose confidence and error fields

---

## Project Phases

### Phase 1
- implement base task/result interfaces
- build EDGAR + Delaware drones
- load Centre Partners ground truth
- implement baseline tell detection and scoring

### Phase 2
- implement BrokerCheck + Enforcement + Personnel graph
- add Frady review handoff
- add challenge swarm

### Phase 3
- implement timeline, news, dossier generation
- add dashboard surfaces
- add case management lifecycle

### Phase 4
- add licensed data sources
- add continuous monitoring
- add model calibration and outcome feedback

---

## Non-Goals

- no autonomous publication of accusations
- no final legal conclusions from Hive
- no direct filing submission by default
- no case can be marked filing-ready without Frady review

---

## Logging Requirements

Every case action must log:

- task id
- source
- target entity
- drone / swarm role
- confidence
- evidence references
- score delta
- escalation decision
- reviewer outcome

---

## Repo Ownership

See `docs/hive-frady-repo-assignments.md` for authoritative ownership and implementation boundaries.