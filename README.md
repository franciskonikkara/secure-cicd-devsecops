# Secure CI/CD Pipeline – FedRAMP-Aligned DevSecOps

## Problem Statement
Late discovery of vulnerabilities increases risk, cost, and audit complexity.

## Architecture
This pipeline enforces security at build time using SAST, container scanning,
and policy-as-code, producing audit-ready artifacts.

## Security Controls
- SAST: Semgrep
- Container Scanning: Trivy
- Policy Enforcement: OPA
- Immutable Builds: Docker

## Threat Model
See `/threat-model/STRIDE.md`

## Compliance Alignment
- NIST 800-53 (RA-5, SI-7, CM-2)
- FedRAMP Moderate readiness

## Metrics & Results
- Critical vulnerabilities blocked pre-deployment
- Mean time to detect: <5 minutes
- Audit prep effort reduced significantly

## How to Run
1. Push code to `main`
2. GitHub Actions triggers automatically
3. Pipeline blocks on policy violations
