# Hi, I'm Refael Malka 👋

### DevOps Engineer | Container Security & CI/CD Supply Chain

I build infrastructure that proves itself: hardened containers, pipelines that boot the
stack before merging, signed and attested images, and automation that runs unattended.

---

## Infrastructure & Platform

### 🐳 [Docker-DevOps-Tooling](https://github.com/www8351/Docker-DevOps-Tooling) — hardened Docker operations toolkit

- Cut one image from **78 MB to ~7 MB** with a hardened multi-stage rebuild (dropped
  unused `openssh-server`, `sshpass`, `tcpdump` — the removed packages *were* the attack
  surface).
- Read-only containers, `cap_drop: ALL`, non-root by construction, network tiers, pinned
  images — rebuilt from a legacy interactive bash lab into a hardened, CI-verified,
  [released](https://github.com/www8351/Docker-DevOps-Tooling/releases/tag/v0.2.1) toolkit.
- CI **boots the whole stack** on every PR (healthchecks as merge gates), scans with Trivy,
  publishes **multi-arch images to GHCR, cosign-signed with provenance + SBOM attestations**.
- The live socket smoke test caught a real bug on its first cloud run: the non-root CLI
  container couldn't reach the runner's Docker socket (Docker Desktop is permissive; a
  Linux host is `root:docker`). Fixed with `--group-add` — non-root intact.
- Typed Python CLI (`dockerctl`): mypy strict, 45 tests, 100% coverage — see the
  [CHANGELOG](https://github.com/www8351/Docker-DevOps-Tooling/blob/main/CHANGELOG.md).

### ☁️ [MLops-AWS-Go-Infrastructure](https://github.com/www8351/MLops-AWS-Go-Infrastructure)

Terraform-provisioned AWS/EKS infrastructure with Go services — the IaC and Kubernetes
side of the toolbox.

### 🛡️ [Linux-Hardening-and-System](https://github.com/www8351/Linux-Hardening-and-System)

System hardening playbooks: SSH lockdown, UFW, least-privilege provisioning on
Debian-family hosts.

---

## Performance-Critical Systems

### [ORB Engine (FreqTrading)](https://github.com/www8351/FreqTrading)

Event-driven trading execution engine for MT5 — asynchronous candle ingestion decoupled
from a synchronous decision core, so order logic never blocks on broker round-trips.

---

## Core Stack

| Category | Technologies |
| :--- | :--- |
| **Containers & CI/CD** | Docker, Docker Compose, GitHub Actions, Trivy, cosign, SBOM/provenance, GHCR |
| **Languages** | Python 3.11+ (typed, mypy strict), Bash/POSIX sh, SQL, PowerShell |
| **Infrastructure** | Linux (hardened Debian), Terraform, AWS/EKS, UFW, SSH hardening |
| **Observability** | Prometheus, Grafana, cAdvisor |

---

## How I Work

- **Prove it in CI** — if the pipeline didn't boot it, scan it, and probe it, it isn't done.
- **Non-interactive everything** — flags and env vars, meaningful exit codes, no prompts.
- **Documented decisions** — changelogs, design docs, and decision logs live in the repo.

---

## Connect

- **GitHub:** [@www8351](https://github.com/www8351)
- **Email:** www8351@gmail.com
