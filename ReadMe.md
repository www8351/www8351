# Hi, I'm www8351 👋

### Software Engineer · Trading Systems · Full-Stack SaaS · DevOps / Cloud

Systems-focused engineer who builds performance-critical, production-shaped software across three
domains that rarely meet in one portfolio: **algorithmic trading engineering**, **full-stack SaaS**,
and **DevOps / cloud infrastructure**. Event-driven architecture, strict testing and typing
discipline, security-by-default and unusually honest documentation: I ship the code *and* the
verdict on whether it actually works.

<sub>מהנדס עם ראייה מערכתית הבונה תוכנה ביצועית ברמת production בשלושה תחומים שנדיר למצוא יחד:
הנדסת מסחר אלגוריתמי, SaaS פול-סטאק, ותשתיות DevOps/ענן. ארכיטקטורה מונחית-אירועים,
משמעת בדיקות וטיפוסים, אבטחה כברירת מחדל ותיעוד כן: אני מפרסם גם את הקוד וגם את המסקנה אם הוא באמת עובד.</sub>

---

## 🧭 Three pillars · שלושה עמודי תווך

| Pillar | What I build | Evidence |
| :--- | :--- | :--- |
| 📈 **Trading Systems** | Signal engines, account-level risk enforcement, broker integration, copy trading | [Gold_BOT_Alaret](https://github.com/www8351/Gold_BOT_Alaret) · [Account_Guardian_V2](https://github.com/www8351/Account_Guardian_V2) · [Vertex Command](https://github.com/www8351/Vertex_Command_Showcase) |
| 🌐 **Full-Stack SaaS** | Typed end-to-end web apps, real-time streaming, payments, auth | [Vertex Command Showcase](https://github.com/www8351/Vertex_Command_Showcase) · [Syncer_Q](https://github.com/www8351/Syncer_Q) · [Trades_Journal](https://github.com/www8351/Trades_Journal) · [Tradezella-Example](https://github.com/www8351/Tradezella-Example) |
| 🛠️ **DevOps / Cloud** | Hardened containers, IaC, CI/CD, supply-chain security, observability | [Docker-DevOps-Tooling](https://github.com/www8351/Docker-DevOps-Tooling) · [Build-Deploy-Test](https://github.com/www8351/Build-Deploy-Test) · [Linux-Hardening-and-System](https://github.com/www8351/Linux-Hardening-and-System) · [5-DevOps-Toolkit](https://github.com/www8351/5-DevOps-Toolkit) |

---

## 📂 Every public project, and what state it's actually in

| Project | What it is | Language | State |
| :--- | :--- | :--- | :--- |
| [**Gold_BOT_Alaret**](https://github.com/www8351/Gold_BOT_Alaret) | XAUUSD Quarterly-Theory engine: a deterministic Python core (quarters, HTF bias, SMC, volume profile, risk) plus a Claude vision report, routed to Telegram, a token-gated dashboard, and MT5 | Python | **143 tests passing.** Live MT5 order placement is implemented but gated off by default (`LIVE_TRADING=false`); DXY correlation not wired |
| [**Account_Guardian_V2**](https://github.com/www8351/Account_Guardian_V2) | Account-level lockout Expert Advisor for MetaTrader 5 — watches cumulative daily loss across the whole account and locks it, persisted so a restart can't clear it early | MQL5 | **Phase 2: detects and locks; does not yet close positions.** The sweep engine is Phase 3. Open defects tracked in `LEDGER.md` |
| [**Vertex_Command_Showcase**](https://github.com/www8351/Vertex_Command_Showcase) | Trade-execution & copy-trading SaaS: copy engine, risk/rule engines, live broker WebSockets, Stripe billing, WebGL control center, Pandas analytics service | TypeScript · Python | Sanitized public code showcase of a private production codebase — 26 pages, 55 server modules, typed end-to-end with Drizzle + Zod |
| [**Syncer_Q**](https://github.com/www8351/Syncer_Q) | The same platform in its deployment shape: hybrid Vercel SPA + single-VPS Docker Compose backend, Nginx WAF + TLS, gated GitHub Actions deploy | TypeScript · Python | 45 Postgres tables across 5 Drizzle schemas. App lives in the `Vertex_Command-main/` subdirectory |
| [**Trades_Journal**](https://github.com/www8351/Trades_Journal) | Trading journal — imports broker/exchange executions, reconstructs every trade (average-cost, exact decimal math), and computes per-trade metrics | TypeScript | Sanitized public mirror. **48 tests passing**, Next.js 16 + Supabase RLS |
| [**Tradezella-Example**](https://github.com/www8351/Tradezella-Example) | The same journal as a full build record: multi-asset import (crypto, MT4/MT5, futures, equities), analytics dashboard, deployed on Vercel | TypeScript | **v1 build-complete, 48 tests passing.** Known limitations listed in the README rather than hidden |
| [**Docker-DevOps-Tooling**](https://github.com/www8351/Docker-DevOps-Tooling) | `dockerctl` — a typed Typer CLI plus a read-only / non-root / cap-dropped compose stack and a supply-chain-gated pipeline | Python | **v0.2.1 released.** mypy strict, **45 tests at 100% coverage**, Trivy gate, CycloneDX SBOMs, multi-arch cosign-signed GHCR images |
| [**Linux-Hardening-and-System**](https://github.com/www8351/Linux-Hardening-and-System) | `ossys` — common Linux admin tasks as pure, testable Python behind a non-interactive Typer CLI, replacing `os.system(...format())` injection holes | Python | **All six phases complete. 206 tests, 82% coverage**, mypy strict. Plugin system + an MCP tool server that is closed by default |
| [**Build-Deploy-Test**](https://github.com/www8351/Build-Deploy-Test) | DevOps lab growing from interactive menus to a Jenkins delivery pipeline: 6 build jobs plus 8 security/cloud jobs (CVE gates, FIM, firewall lockdown, IAM audit) | Python · Shell | **40 Python tests at 93% coverage + 16 bats tests.** 2026 toolchain: uv, OpenTofu, Cilium, Falco, Trivy SBOMs |
| [**5-DevOps-Toolkit**](https://github.com/www8351/5-DevOps-Toolkit) | 25 single-purpose Linux/Docker/AWS tools across 5 themed folders, all on one shared engine (`lib/common.sh`) with `--help`, dry-run and root guards | Shell · Python | **53 tests (24 bats + 29 pytest), 5 green CI checks**, all VM-free |
| [**Python-Mentoring-Labs**](https://github.com/www8351/Python-Mentoring-Labs-for-Junior-Engineers) | Seven guided labs taking a junior from `input()` scripts to pure, typed, tested functions behind a clean CLI — each paired with the real beginner bug it replaced | Python | Complete. mypy strict + ruff + pytest gated in CI |
| [**Claude_Quota_Line**](https://github.com/www8351/Claude_Quota_Line) | Two-line PowerShell status line for Claude Code: context window, 5-hour and weekly limits, and one per-model bucket, in the terminal | PowerShell | Working. Reads the status-line payload from stdin, falls back to the OAuth usage endpoint for the per-model figure |

Two projects are private: **Vertex_Command** (the production codebase behind the two showcases
above) and **The-Binary-Ledger** (a Knesset voting-transparency index).

---

## ⚡ Technical Domain

* **Core Backend & Automation:** **Python 3.11+**, advanced **Linux/Bash** scripting, robust **API**
  design (REST, WebSockets, FastAPI), event-driven async systems, **PowerShell**.
* **Full-Stack SaaS:** **TypeScript** across **React 19 / Next.js 16**, **Node/Express 5**,
  **PostgreSQL** via **Drizzle / Supabase (RLS)**, **Stripe** billing, **Three.js/WebGL** interfaces.
* **DevOps & Infrastructure:** **Docker** hardening, **OpenTofu/Terraform** IaC, **Jenkins /
  GitHub Actions** CI/CD, **Prometheus/Grafana/Loki** observability, **Cilium** eBPF network policy,
  **Falco** runtime detection, supply-chain security (Trivy, CycloneDX SBOMs, SHA-pinning, cosign).
* **Trading Engineering:** Event-driven architecture, low-latency execution loops, MetaTrader 5 /
  MQL5, copy-trading & drawdown risk engines, SMC/ICT strategy design.

---

## 🛠️ Core Stack & Tools

| Category | Technologies |
| :--- | :--- |
| **Languages** | Python 3.11+, TypeScript, Bash, SQL, MQL5, PowerShell |
| **Frontend / SaaS** | React 19, Next.js 16, Three.js/WebGL, Tailwind, Framer Motion, Stripe |
| **Backend / Realtime** | Node/Express 5, FastAPI, aiohttp, WebSockets, Drizzle ORM, Supabase, PostgreSQL |
| **DevOps & Cloud** | Docker/Compose, OpenTofu, Jenkins, GitHub Actions, nginx, GHCR, Task/Make |
| **Observability & Security** | Prometheus, Grafana, Loki, Vector, Trivy, CycloneDX SBOM, cosign, gitleaks, UFW/SSH hardening |
| **Quality** | pytest, vitest, bats, mypy (strict), ruff, coverage gates, TDD |
| **Trading** | MetaTrader 5 API, MQL5, TwelveData, Tradovate / TopstepX / Rithmic |

---

## 🎯 Engineering Philosophy

> **Production-Ready by Default:** every codebase is written with exhaustive error handling, strict
> validation layers, and dependency injection to guarantee full offline testability.

* **Decoupled & async** background workers ensure blocking I/O or remote IPC never halts execution;
  pure logic stays I/O-free so it can be tested without a broker, a socket, or a VM.
* **Security-first** secrets never enter version control (`.env.example` only), credentials
  encrypted at rest, an explicit off-by-default gate on anything touching real money, hardened
  SSH/containers, and tool surfaces that are closed until a reviewable config opens them.
* **Verifiable rigor** mypy-strict, coverage-gated test suites (the Docker CLI holds **100%
  coverage** over 45 tests; `ossys` runs **206 tests at 82%**; the Gold engine **143**), CI that
  gates on every push.
* **Honest documentation** I state what a build does *not* do yet — Account Guardian locks but does
  not close, the Gold engine's live trading ships off by default — and track every system with a
  file-based lifecycle protocol (`STATUS.md`, `DECISIONS.md`, `PROGRESS.md`, `LEDGER.md`).

---

## 📈 Featured Architecture Profiles

### 🔹 [Vertex Command — Trade-Execution & Copy-Trading SaaS](https://github.com/www8351/Vertex_Command_Showcase)
Full-stack prop-trading platform: React 19 · Three.js/WebGL · Express 5 · Drizzle/Postgres · Stripe.
Live broker WebSocket streaming, master→follower copy engine, risk/rule engines, encrypted-at-rest
credentials, and a Pandas analytics microservice — typed end-to-end with Drizzle + Zod.

### 🔹 [Gold_BOT_Alaret — XAUUSD Quarterly-Theory Engine](https://github.com/www8351/Gold_BOT_Alaret)
A deterministic Smart-Money engine where the *algorithm* decides and the *model* only narrates:
True Day anchors, 90-minute cycles, Judas sweeps, MSS, IFVG/OTE retests and RRR≥3 sizing across 143
tests — with live MT5 execution behind a single explicit gate, off by default.

### 🔹 [ossys — Small System Tasks as Safe Python](https://github.com/www8351/Linux-Hardening-and-System)
Turns `os.system('... {} ...'.format(user_input))` into a validated, non-interactive Typer CLI with
an exit-code taxonomy, per-endpoint TOML config, systemd/cron scheduling on both privileged and
unprivileged paths, an entry-point plugin system, and an MCP tool server that exposes nothing
destructive without two independent opt-ins.

### 🔹 [Docker-DevOps-Tooling — Hardened Container Toolkit](https://github.com/www8351/Docker-DevOps-Tooling)
Typed Typer CLI (mypy strict, 100% coverage) + read-only/non-root/cap-dropped compose stack +
SHA-pinned CI with Trivy scanning, CycloneDX SBOMs, cosign-signed multi-arch GHCR publishing, and a
CI job that boots the whole stack so every healthcheck becomes an assertion.

---

### 📬 Connect With Me

* **GitHub:** [@www8351](https://github.com/www8351)
* **Environment:** Operating primarily via PowerShell Terminal / Hardened Linux systems.

*"No filler, no pleasantries — just clean architecture and deterministic performance."*
