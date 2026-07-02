# Hi, I'm Refael Malka 👋

### DevOps Engineer | Container Security & CI/CD Supply Chain

I build infrastructure that proves itself: hardened containers, pipelines that boot the
stack before merging, signed and attested images, and automation that runs unattended.

---

## 🏗️ Infrastructure & Platform

### 🐳 [Docker-DevOps-Tooling](https://github.com/www8351/Docker-DevOps-Tooling) — hardened Docker operations toolkit

- Rebuilt a legacy interactive bash lab into a production-grade toolkit: read-only containers,
  `cap_drop: ALL`, non-root by construction, network tiers, pinned images — and cut one image
  from **78 MB of attack surface to ~7 MB**.
- CI **boots the whole stack** on every PR (healthchecks as merge gates), scans with Trivy,
  publishes **multi-arch images to GHCR, cosign-signed with provenance + SBOM attestations**.
- Typed Python CLI (`dockerctl`): mypy strict, **100% test coverage**, released and versioned —
  see [v0.2.1](https://github.com/www8351/Docker-DevOps-Tooling/releases/tag/v0.2.1) and the
  [CHANGELOG](https://github.com/www8351/Docker-DevOps-Tooling/blob/main/CHANGELOG.md).

### ☁️ [MLops-AWS-Go-Infrastructure](https://github.com/www8351/MLops-AWS-Go-Infrastructure)

Terraform-provisioned AWS/EKS infrastructure with Go services — the IaC and Kubernetes side
of the toolbox.

### 🛡️ [Linux-Hardening-and-System](https://github.com/www8351/Linux-Hardening-and-System)

System hardening playbooks: SSH lockdown, UFW, least-privilege provisioning on Debian-family
hosts.

---

## ⚙️ Performance-Critical Systems

### 🔹 [ORB Engine](https://github.com/www8351/FreqTrading)

Event-driven trading execution engine for MT5: an asynchronous M1 candle feed decoupled from
a pure, synchronous O(1) state machine, with thread-isolated state caching to eliminate
blocking IPC round-trips.

---

## 🛠️ Core Stack

| Category | Technologies |
| :--- | :--- |
| **Containers & CI/CD** | Docker, Docker Compose, GitHub Actions, Trivy, cosign, SBOM/provenance, GHCR |
| **Languages** | Python 3.11+ (typed, mypy strict), Bash/POSIX sh, SQL, PowerShell |
| **Infrastructure** | Linux (hardened Debian), Terraform, AWS/EKS, UFW, SSH hardening |
| **Observability** | Prometheus, Grafana, cAdvisor |

---

## 🎯 How I work

- **Prove it in CI** — if the pipeline didn't boot it, scan it, and probe it, it isn't done.
- **Non-interactive everything** — flags and env vars, meaningful exit codes, no prompts.
- **Hardened by default** — non-root, read-only, capability-dropped, pinned and signed.
- **Documented decisions** — changelogs, design docs, and decision logs live in the repo.

---

### 📬 Connect

- **GitHub:** [@www8351](https://github.com/www8351)
- **Email:** www8351@gmail.com
<!-- Add LinkedIn: - **LinkedIn:** [Refael Malka](https://www.linkedin.com/in/YOUR-HANDLE/) -->
