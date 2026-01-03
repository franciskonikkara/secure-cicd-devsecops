#  1. Secure CI/CD Pipeline with Enforced Security Gates

Implemented a SOC 2 and ISO 27001–aligned CI/CD security pipeline using GitHub Actions, Semgrep, Trivy, and Gitleaks, generating SIEM-ready audit evidence and enforcing automated security gates on every commit.

## Overview

This repository demonstrates a **production-grade secure CI/CD pipeline** built with **GitHub Actions** and aligned with **SOC 2** and **ISO/IEC 27001** security controls.

The pipeline embeds:

* Static Application Security Testing (SAST)
* Dependency & container vulnerability scanning
* Secret detection
* Enforced security gates
* SIEM-ready logging

Security failures **intentionally block the pipeline**.

---

## Security Tooling

| Category            | Tool           |
| ------------------- | -------------- |
| CI/CD               | GitHub Actions |
| SAST                | Semgrep        |
| Dependency Scanning | Trivy          |
| Container Scanning  | Trivy          |
| Secrets Detection   | Gitleaks       |
| SIEM Export         | JSON Artifacts |

---

## 🔥 Intentional Failure Scenarios

### ❌ Semgrep Rule Misconfiguration

* Missing `languages` field
* Pipeline failed due to an invalid schema

### ❌ Vulnerable Dependency

* Flask 0.12 introduced known CVEs
* Trivy blocked the build
![Alt text](architecture/Flask_vulnerability_image.png?raw=true "Flask Version vulnerability with known CVEs")

### ❌ Secrets Exposure

* Hardcoded AWS secret detected
* Gitleaks failed the pipeline
![Alt text](architecture/aws_secret_1.png?raw=true "AWS secret key")
![Alt text](architecture/aws_secret_2.png?raw=true)

### ❌ Runtime Compatibility Failure (Python Version Mismatch)

The container build initially failed due to a mismatch between the base Python image (3.7) and upgraded application dependencies (Flask 2.3.3 requires Python ≥ 3.8).

This demonstrated:
- Dependency upgrades can introduce platform compatibility risks
- CI/CD correctly prevented the deployment of a broken runtime
- Secure upgrades must be coordinated with base image updates

The issue was resolved by upgrading the container base image to Python 3.9-slim.

![Alt text](architecture/python_version.png?raw=true)

###❌ Failure: Pipeline broke due to non-deterministic tooling download  
###✅ Fix: Pinned Gitleaks binary version to ensure deterministic CI execution

## ✅ Remediation

* Fixed Semgrep rule schema
* Upgraded vulnerable dependencies
* Removed hardcoded secrets
* Hardened container base image

Pipeline passes **only after remediation**.

---

## SOC 2 & ISO 27001 Alignment

### SOC 2 Controls

* **CC7.1** – Continuous vulnerability detection
* **CC7.2** – Monitoring & alerting
* **CC8.1** – Secure change management

### ISO/IEC 27001 Controls

* **A.8.8** – Technical vulnerability management
* **A.8.9** – Configuration management
* **A.8.15** – Logging & monitoring

This repository generates **audit-ready evidence** via immutable CI logs and artifacts.

---

## SIEM Integration

Security scan results are exported in JSON format and uploaded as CI artifacts.

These artifacts can be ingested into:

* Datadog
* Splunk (HEC)
* ELK Stack (Filebeat)

This enables centralized security monitoring and alerting.

---

## Key Outcomes

* Security is enforced, not advisory
* CI/CD blocks insecure code automatically
* Vulnerabilities are detected, documented, and remediated
* Logs are SIEM-ready and audit-defensible
