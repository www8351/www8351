<div align="center">

<img src="assets/whoami.svg" width="100%" alt="refael@github whoami: ASCII portrait of Refael Malka beside a system info card. Systems Engineer, Trading, SaaS and DevOps, based in Israel."/>

<br/><br/>

<img src="assets/contrib-heatmap.svg" width="100%" alt="GitHub contribution graph for the last year, refreshed daily."/>

<h3><code>refael@github ~ $ ./links.sh</code></h3>

<a href="https://github.com/www8351"><img src="https://img.shields.io/badge/GitHub-www8351-181717?style=for-the-badge&logo=github" alt="GitHub"/></a>
<a href="https://www.linkedin.com/in/refael8351"><img src="https://img.shields.io/badge/LinkedIn-refael8351-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<img src="https://img.shields.io/badge/Based%20in-Israel-3fb950?style=for-the-badge" alt="Based in Israel"/>

</div>

<br/>

## 🚀 `ls ~/projects`

> 🟢 Released or complete &nbsp;·&nbsp; 🟡 In development &nbsp;·&nbsp; 🔵 Public showcase of a private codebase

### 📈 Trading Systems

| | Project | What it does | Stack |
| :-: | :-- | :-- | :-- |
| 🟡 | [**Gold_BOT_Alaret**](https://github.com/www8351/Gold_BOT_Alaret) | XAUUSD Quarterly-Theory engine. Deterministic core for quarters, HTF bias, SMC, volume profile and risk, routed to Telegram, a dashboard and MT5. **143 tests.** Live orders built but off by default | `Python` |
| 🟡 | [**Account_Guardian_V2**](https://github.com/www8351/Account_Guardian_V2) | Expert Advisor that watches cumulative daily loss across the whole account and locks it, persisted so a restart cannot clear it early. Earlier work: [V1](https://github.com/www8351/Account_Guardian-V1) · [Release](https://github.com/www8351/AccountGuardian-Release) | `MQL5` |

### 🌐 Full-Stack SaaS

| | Project | What it does | Stack |
| :-: | :-- | :-- | :-- |
| 🔵 | [**Vertex_Command_Showcase**](https://github.com/www8351/Vertex_Command_Showcase) | Trade-execution and copy-trading platform. Copy engine, risk engines, live broker WebSockets, Stripe billing, WebGL control center. 26 pages, 55 server modules | `TS` `Python` |
| 🟡 | [**Syncer_Q**](https://github.com/www8351/Syncer_Q) | The same platform in deployment shape. Vercel SPA plus a single-VPS Docker Compose backend, Nginx WAF and TLS. 45 Postgres tables | `TS` `Python` |
| 🔵 | [**Trades_Journal**](https://github.com/www8351/Trades_Journal) | Trading journal that rebuilds every trade from raw executions with exact decimal math. Next.js 16, Supabase RLS. **48 tests** | `TS` |
| 🟢 | [**Tradezella-Example**](https://github.com/www8351/Tradezella-Example) | The journal as a full build record. Crypto, MT4/MT5, futures and equities import, analytics dashboard, deployed on Vercel. **48 tests** | `TS` |

### 🛠️ DevOps & Systems

| | Project | What it does | Stack |
| :-: | :-- | :-- | :-- |
| 🟢 | [**Docker-DevOps-Tooling**](https://github.com/www8351/Docker-DevOps-Tooling) | `dockerctl` typed CLI with a read-only, non-root, cap-dropped compose stack. Trivy gate, SBOMs, cosign-signed multi-arch images. **v0.2.1, 45 tests, 100% coverage** | `Python` |
| 🟢 | [**Linux-Hardening-and-System**](https://github.com/www8351/Linux-Hardening-and-System) | `ossys` turns shell-injection admin scripts into a safe, testable CLI. Plugin system and a closed-by-default tool server. **206 tests, 82% coverage** | `Python` |
| 🟢 | [**Build-Test-Deploy**](https://github.com/www8351/Build-Test-Deploy) | DevOps lab from interactive menus to a Jenkins pipeline. 6 build jobs plus 8 security and cloud jobs. **40 tests at 93% + 16 bats** | `Python` `Shell` |
| 🟢 | [**5-DevOps-Toolkit**](https://github.com/www8351/5-DevOps-Toolkit) | Single-purpose Linux, Docker and AWS tools on one shared engine, each with `--help`, dry-run and root guards. **53 tests, 5 green CI checks** | `Shell` `Python` |

### 🧰 Tools & Teaching

| | Project | What it does | Stack |
| :-: | :-- | :-- | :-- |
| 🟢 | [**Python-Mentoring-Labs**](https://github.com/www8351/Python-Mentoring-Labs-for-Junior-Engineers) | Seven labs taking a junior from `input()` scripts to pure, typed, tested functions. Each lab pairs with the real beginner bug it replaced | `Python` |
| 🟢 | [**Claude_Quota_Line**](https://github.com/www8351/Claude_Quota_Line) | Two-line terminal status line showing context window, 5-hour and weekly usage limits | `PowerShell` |

<sub>🔒 Two private repositories: <b>Vertex_Command</b>, the production codebase behind the showcases, and <b>The-Binary-Ledger</b>, a Knesset voting-transparency index.</sub>

<br/>

## 🧪 `./run-tests --all`

| 🧪 Project | Tests | Coverage | Gate |
| :-- | :-: | :-: | :-- |
| Linux-Hardening-and-System | **206** | 82% | mypy strict |
| Gold_BOT_Alaret | **143** | | pytest |
| 5-DevOps-Toolkit | **53** | | bats + pytest, 5 CI checks |
| Trades_Journal · Tradezella | **48** | | vitest |
| Docker-DevOps-Tooling | **45** | **100%** | mypy strict, Trivy |
| Build-Test-Deploy | **40 + 16** | 93% | pytest + bats |

<br/>

## 🛠️ `cat stack.txt`

| | |
| :-- | :-- |
| 💬 **Languages** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) ![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white) ![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=flat-square&logo=powershell&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-336791?style=flat-square&logo=postgresql&logoColor=white) ![MQL5](https://img.shields.io/badge/MQL5-0B3D91?style=flat-square) |
| 🌐 **Frontend & SaaS** | ![React 19](https://img.shields.io/badge/React%2019-20232A?style=flat-square&logo=react&logoColor=white) ![Next.js 16](https://img.shields.io/badge/Next.js%2016-000000?style=flat-square&logo=nextdotjs&logoColor=white) ![Three.js](https://img.shields.io/badge/Three.js-000000?style=flat-square&logo=threedotjs&logoColor=white) ![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white) ![Stripe](https://img.shields.io/badge/Stripe-635BFF?style=flat-square&logo=stripe&logoColor=white) ![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white) |
| ⚙️ **Backend & Realtime** | ![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white) ![Express 5](https://img.shields.io/badge/Express%205-000000?style=flat-square&logo=express&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white) ![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white) ![Drizzle](https://img.shields.io/badge/Drizzle-C5F74F?style=flat-square&logo=drizzle&logoColor=black) |
| ☁️ **DevOps & Cloud** | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white) ![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white) ![OpenTofu](https://img.shields.io/badge/OpenTofu-FFDA18?style=flat-square&logo=opentofu&logoColor=black) ![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black) |
| 🔭 **Observability** | ![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white) ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white) ![Loki](https://img.shields.io/badge/Loki-F46800?style=flat-square&logo=grafana&logoColor=white) ![Vector](https://img.shields.io/badge/Vector-1F6FEB?style=flat-square) |
| 🛡️ **Security** | Trivy · CycloneDX SBOM · cosign · gitleaks · UFW and SSH hardening · Cilium · Falco |
| ✅ **Quality** | pytest · vitest · bats · mypy strict · ruff · coverage gates · TDD |
| 📈 **Trading** | MetaTrader 5 API · TwelveData · Tradovate · TopstepX · Rithmic |

<br/>

## 🎯 `man refael`

| | Principle | In practice |
| :-: | :-- | :-- |
| 🧱 | **Pure core** | Logic stays free of I/O, so it runs without a broker, a socket or a VM |
| 🔐 | **Security first** | `.env.example` only, credentials encrypted at rest, real-money paths off by default |
| 🧪 | **Verifiable** | Strict typing, coverage-gated suites, CI that blocks every push |
| 📝 | **Honest docs** | Each README says what the build does not do yet |

<br/>

<div dir="rtl" align="right">

## 🇮🇱 בקצרה בעברית

מהנדס מערכות שבונה תוכנה ברמת ייצור בשלושה תחומים שנדיר למצוא יחד: מערכות מסחר אלגוריתמי, פלטפורמות ווב מלאות, ותשתיות ענן מאובטחות.
כל פרויקט כאן כולל בדיקות אוטומטיות, אבטחה כברירת מחדל, ותיעוד כן שאומר מה עובד היום ומה עוד לא.

</div>

<br/>

<div align="center">

<sub><i>"No filler. Clean architecture and deterministic performance."</i></sub>

<code>refael@github ~ $ exit</code>

</div>
