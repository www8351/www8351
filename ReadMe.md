# Hi, I'm www8351 👋

### Software Engineer · Trading Systems · Full-Stack SaaS · DevOps / Cloud

Systems-focused engineer who builds performance-critical, production-shaped software across three
domains that rarely meet in one portfolio: **algorithmic trading engineering**, **full-stack SaaS**,
and **DevOps / cloud infrastructure**. Low-latency event-driven architecture, strict testing and
typing discipline, security-by-default and unusually honest documentation: I ship the code *and*
the verdict on whether it actually works.

<sub>מהנדס עם ראייה מערכתית הבונה תוכנה ביצועית ברמת production בשלושה תחומים שנדיר למצוא יחד:
הנדסת מסחר אלגוריתמי, SaaS פול-סטאק, ותשתיות DevOps/ענן. ארכיטקטורה מונחית-אירועים בזמן-תגובה נמוך,
משמעת בדיקות וטיפוסים, אבטחה כברירת מחדל ותיעוד כן: אני מפרסם גם את הקוד וגם את המסקנה אם הוא באמת עובד.</sub>

---

## 🧭 Three pillars · שלושה עמודי תווך

| Pillar | What I build | Evidence |
| :--- | :--- | :--- |
| 📈 **Trading Systems** | Low-latency execution engines, copy-trading, backtesting, broker integration | [FreqTrading](https://github.com/www8351/FreqTrading) · [Vertex Command](https://github.com/www8351/Vertex_Command_Showcase) · [HTF_Mirror](https://github.com/www8351/HTF_Mirror) · [Gold_BOT](https://github.com/www8351/Gold_BOT_Alaret) |
| 🌐 **Full-Stack SaaS** | Typed end-to-end web apps, real-time streaming, payments, auth | [Vertex Command Showcase](https://github.com/www8351/Vertex_Command_Showcase) · [Trades_Journal](https://github.com/www8351/Trades_Journal) |
| 🛠️ **DevOps / Cloud** | Hardened containers, IaC, CI/CD, supply-chain security, observability | [Docker-DevOps-Tooling](https://github.com/www8351/Docker-DevOps-Tooling) · [MLOps-AWS-Go](https://github.com/www8351/MLops-AWS-Go-Infrastructure) · [5-DevOps-Toolkit](https://github.com/www8351/5-DevOps-Toolkit) |

---

## ⚡ Technical Domain

* **Core Backend & Automation:** Expert-level **Python 3.11+**, advanced **Linux/Bash** scripting,
  robust **API** design (REST, WebSockets, FastAPI), event-driven async systems.
* **Full-Stack SaaS:** **TypeScript** across **React 19 / Next.js 16**, **Node/Express 5**,
  **PostgreSQL** via **Drizzle / Supabase (RLS)**, **Stripe** billing, **Three.js/WebGL** interfaces.
* **DevOps & Infrastructure:** **Docker** hardening, **AWS EKS + Terraform**, **Jenkins / GitHub
  Actions** CI/CD, **Prometheus/Grafana** observability, supply-chain security (Trivy, SBOMs, SHA-pinning).
* **Trading Engineering:** Event-driven architecture, low-latency execution loops ($O(1)$ state
  machines), MetaTrader 5 / MQL5, copy-trading & drawdown risk engines, SMC/ICT strategy design.

---

## 🛠️ Core Stack & Tools

| Category | Technologies |
| :--- | :--- |
| **Languages** | Python 3.11+, TypeScript, Go, Bash, SQL, MQL5, Pine Script, PowerShell |
| **Frontend / SaaS** | React 19, Next.js 16, Three.js/WebGL, Tailwind, Framer Motion, Stripe |
| **Backend / Realtime** | Node/Express 5, FastAPI, WebSockets, Drizzle ORM, Supabase, PostgreSQL |
| **DevOps & Cloud** | Docker/Compose, AWS EKS, Terraform, Jenkins, GitHub Actions, nginx, GHCR |
| **Observability & Security** | Prometheus, Grafana, Trivy, CycloneDX SBOM, UFW/SSH hardening |
| **Quality** | pytest, mypy (strict), ruff, coverage gates, TDD |
| **Trading & Hardware** | MetaTrader 5 API, MQL5, TradingView/Pine, HiveOS (ASIC/Crypto Ops) |

---

## 🎯 Engineering Philosophy

> **Production-Ready by Default:** every codebase is written with exhaustive error handling, strict
> validation layers, and dependency injection to guarantee full offline testability.

* **Low-latency & decoupled** async background workers ensure blocking I/O or remote IPC never
  halts execution; critical paths avoid allocation churn and GC spikes.
* **Security-first** secrets never enter version control (`.env.example` only), credentials
  encrypted at rest, demo-guards on anything touching real money, hardened SSH/containers.
* **Verifiable rigor** mypy-strict, coverage-gated test suites (FreqTrading ships **445 passing
  tests**; the Docker CLI holds **100% coverage**), CI that gates on every push.
* **Honest documentation** I record strategies that *lose* under realistic costs instead of
  hiding them, and track every system with a file-based lifecycle protocol
  (`STATUS.md`, `DECISIONS.md`, `PROGRESS.md`).

---

## 📈 Featured Architecture Profiles

### 🔹 [FreqTrading — ORB Execution Engine](https://github.com/www8351/FreqTrading)
Ultra-low-latency, event-driven MT5 execution engine. Decouples an async M1 candle feed from a pure
synchronous $O(1)$ state machine (`IDLE → RANGE_DEFINED → BREAKOUT → EXIT`), with ATR trailing,
daily-loss circuit breakers, a self-contained MQL5 EA port, and 445 passing tests.

### 🔹 [Vertex Command — Trade-Execution & Copy-Trading SaaS](https://github.com/www8351/Vertex_Command_Showcase)
Full-stack prop-trading platform: React 19 · Three.js/WebGL · Express 5 · Drizzle/Postgres · Stripe.
Live broker WebSocket streaming, master→follower copy engine, risk/rule engines, encrypted-at-rest
credentials — typed end-to-end with Drizzle + Zod.

### 🔹 [Docker-DevOps-Tooling — Hardened Container Toolkit](https://github.com/www8351/Docker-DevOps-Tooling)
Typed Typer CLI (mypy strict, 100% coverage) + read-only/non-root/cap-dropped compose stack +
SHA-pinned CI with Trivy scanning, CycloneDX SBOMs, and GHCR publishing.

### 🔹 [MLOps · AWS + Go Infrastructure](https://github.com/www8351/MLops-AWS-Go-Infrastructure)
Terraform-provisioned EKS (multi-AZ, GPU node group) serving a distroless Go inference microservice
instrumented with Prometheus p50/p95/p99 latency histograms.

---

### 📬 Connect With Me

* **GitHub:** [@www8351](https://github.com/www8351)
* **Environment:** Operating primarily via PowerShell Terminal / Hardened Linux systems.

*"No filler, no pleasantries — just clean architecture and deterministic performance."*
