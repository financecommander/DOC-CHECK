# Hive + Frady Repo Assignments

## Project objective

Implement a two-stage investigative intelligence system on top of Swarm:

- **Hive** = detection, scoring, graphing, prioritization
- **Frady** = evidentiary review, validation, SEC-readiness analysis

---

## Repo map

### 1. super-duper-spork
**Role:** central orchestration and project control plane

**Owns:**
- top-level workflow orchestration
- task routing between Hive and Frady
- queue dispatch contracts
- escalation rules
- challenge swarm invocation
- case lifecycle states
- project-wide logging and audit trails

**Suggested paths:**
- `swarm/orchestrator.py`
- `swarm/governance.py`
- `swarm/cases/`
- `swarm/hive_frady_router.py`

**Implement here:**
- `route_hive_case()`
- `should_escalate_to_frady()`
- `run_challenge_swarm()`
- `finalize_case_state()`

---

### 2. calculus-tools
**Role:** source connectors and utility wrappers

**Owns:**
- SEC EDGAR wrapper
- Delaware lookup wrapper
- BrokerCheck wrapper
- DOJ/FDA/state enforcement wrappers
- PACER/news adapters
- shared retry, rate-limit, caching helpers
- source normalization utilities

**Suggested paths:**
- `connectors/sec_edgar.py`
- `connectors/delaware.py`
- `connectors/brokercheck.py`
- `connectors/enforcement.py`
- `connectors/news_court.py`
- `utils/provenance.py`
- `utils/rate_limit.py`

**Implement here:**
- raw source clients only
- no final tell scoring logic
- no dossier logic

---

### 3. swarm-gpu
**Role:** model serving and local inference

**Owns:**
- clause extraction models
- entity matching assist models
- valuation anomaly scoring models
- timeline reasoning models
- review / contradiction detection models
- local embedding inference if needed

**Suggested paths:**
- `models/hive_clause_extractor/`
- `models/entity_resolution/`
- `models/timeline_reasoner/`
- `models/frady_review/`

**Implement here:**
- model loading configs
- inference presets
- prompt templates for local review tasks
- GPU-serving configuration for Hive/Frady workloads

---

### 4. hive
**Role:** investigative detection engine

**Owns:**
- drone task contracts
- drone execution layer
- entity resolver
- tell detector
- scorer
- Queen Bee orchestration
- graph builder
- timeline builder
- Hive case packet generation

**Suggested structure:**
- `hive/config/`
- `hive/drones/`
- `hive/models/`
- `hive/engine/`
- `hive/storage/`
- `hive/tests/`

**Implement here:**
- `DroneTask`
- `DroneResult`
- `QueenBee`
- `TellDetection`
- `FirmRiskProfile`
- `compute_risk_score()`
- `generate_hive_case_packet()`

**Notes:**
This repo should remain focused on detection and prioritization, not final legal review.

---

### 5. frady-sec-review
**Role:** evidentiary validation and SEC review layer

**Owns:**
- Hive packet intake
- evidence verification
- quote/excerpt extraction
- contradiction analysis
- counter-explanation analysis
- SEC-readiness scoring
- filing-support packet generation
- reviewer notes and case downgrade/upgrade decisions

**Suggested structure:**
- `frady/intake/`
- `frady/review/`
- `frady/evidence/`
- `frady/output/`
- `frady/tests/`

**Implement here:**
- `review_hive_packet()`
- `validate_tells()`
- `extract_key_evidence()`
- `score_sec_readiness()`
- `generate_review_memo()`

---

### 6. shared schema repo or shared package
**Role:** common contracts across the system

**Owns:**
- case packet schemas
- enums and state models
- evidence reference schema
- provenance objects
- score explanation schema

**Suggested package name:**
- `swarm_contracts`
- or `hive_frady_contracts`

**Implement here:**
- `HiveCasePacket`
- `FradyReviewResult`
- `EvidenceRef`
- `CaseState`
- `SourceProvenance`

**Reason:**
Avoid schema drift across orchestration, Hive, and Frady.

---

## Functional boundaries

### Hive must do
- broad screening
- tell scoring
- graph and timeline assembly
- prioritization
- open-question generation

### Hive must not do
- final legal conclusions
- unsupported accusations
- final SEC-readiness decision

### Frady must do
- evidence-level validation
- challenge weak tells
- identify missing proof
- produce review outcomes
- return validated/downgraded tell set

### Frady must not do
- broad firm universe crawling
- replace source adapters
- override provenance logging rules

---

## Recommended handoff contract

### Hive output

```python
HiveCasePacket = {
    "case_id": "...",
    "firm_profile": {},
    "top_tells": [],
    "entity_map": {},
    "personnel_graph": {},
    "timeline": [],
    "evidence_bundle": [],
    "data_completeness": 0.0,
    "open_questions": [],
    "provenance_index": []
}
```

### Frady output

```python
FradyReviewResult = {
    "case_id": "...",
    "review_status": "supported|mixed|weak|not_ready",
    "validated_tells": [],
    "rejected_tells": [],
    "missing_evidence": [],
    "litigation_risk_notes": [],
    "sec_readiness_score": 0.0,
    "recommended_next_steps": [],
    "review_provenance": []
}
```

---

## Build order

### Sprint 1

* shared contracts
* EDGAR connector
* Delaware connector
* Hive base schemas
* baseline scorer
* Centre Partners fixture loader

### Sprint 2

* BrokerCheck connector
* enforcement connector
* personnel graph
* timeline builder
* Hive packet output
* Frady intake module

### Sprint 3

* challenge swarm
* Frady evidence validator
* clause extraction
* contradiction analysis
* case state transitions

### Sprint 4

* dashboard
* outcome feedback loop
* model calibration layer
* batch-screening operations

---

## Ownership recommendation

### super-duper-spork

Architecture owner

### hive

Detection owner

### frady-sec-review

Validation owner

### calculus-tools

Connector owner

### swarm-gpu

Inference owner

### shared contracts package

Schema owner

---

## Success criteria

The project is considered correctly implemented when:

1. Hive can screen a firm and produce a structured risk profile
2. Hive can emit a valid HiveCasePacket
3. super-duper-spork can decide whether Frady review is required
4. Frady can validate, reject, or downgrade tells
5. all evidence is provenance-linked
6. final case state is logged and auditable
