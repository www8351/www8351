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

<div dir="rtl">

## 👋 קצת עליי

אני עובד עם סוכני בינה מלאכותית בפיתוח תוכנה, לפי שיטה קבועה:

- 🧭 **אני מחליט**, הסוכן מבצע
- 🔒 **כל החלטה** נרשמת וננעלת
- ✅ **שום משימה** לא נסגרת בלי הוכחה

### 🛠️ מה עוד אני בונה

- ⚙️ כלי DevOps עם בדיקות אוטומטיות ו-Pipeline מלא
- 🐳 Docker Container: סריקת אבטחה, Images, כיסוי בדיקות מלא
- 🔁 Jenkins and GitHub Actions, מתחילת הפיתוח ועד הפריסה לפרודקשן.

</div>

<p align="center">
  <img alt="Claude Code" src="https://img.shields.io/badge/Claude_Code-AI_Workflows-D97757?style=for-the-badge" />
  <img alt="DevOps" src="https://img.shields.io/badge/DevOps-Tested_CI-2088FF?style=for-the-badge" />
  <img alt="MQL5" src="https://img.shields.io/badge/MQL5-Trading_Systems-F7B500?style=for-the-badge" />
</p>

<br/>

## 🚀 `ls ~/projects`

> 🟢 Released or complete<br/>
> 🟡 In development<br/>
> 🔵 Public showcase of a private codebase

### 📈 Trading Systems

| | Project | What it does | Stack |
| :-: | :-- | :-- | :-- |
| 🟡 | [**Gold_BOT_Alaret**](https://github.com/www8351/Gold_BOT_Alaret) | XAUUSD signal engine on ICT Quarterly Theory | `Python` |
| 🟡 | [**Agent-AI**](https://github.com/www8351/Agent-AI) | Market intelligence for futures, gold and crypto, advisory only | `Python` |
| 🟢 | [**AccountGuardian**](https://github.com/www8351/AccountGuardian-Release) | Locks the whole MT5 account at its daily loss limit | `MQL5` |
| 🟢 | [**Account_Guardian-V1**](https://github.com/www8351/Account_Guardian-V1) | Source of the released guardian, with spec, test vectors and evidence | `MQL5` `PowerShell` |
| 🟡 | [**Account_Guardian_V2**](https://github.com/www8351/Account_Guardian_V2) | Next guardian version, adds an equity peak floor | `MQL5` |

### 🌐 Full-Stack SaaS

| | Project | What it does | Stack |
| :-: | :-- | :-- | :-- |
| 🔵 | [**Vertex_Command_Showcase**](https://github.com/www8351/Vertex_Command_Showcase) | Copy trading and trade execution platform | `TS` `Python` |
| 🟡 | [**Syncer_Q**](https://github.com/www8351/Syncer_Q) | The same platform, packaged for deployment | `TS` `Python` |
| 🔵 | [**Trades_Journal**](https://github.com/www8351/Trades_Journal) | Trading journal rebuilt from raw executions | `TS` |
| 🟢 | [**Tradezella-Example**](https://github.com/www8351/Tradezella-Example) | The journal as a full build, deployed on Vercel | `TS` |

### 🛠️ DevOps & Systems

| | Project | What it does | Stack |
| :-: | :-- | :-- | :-- |
| 🟢 | [**Docker-DevOps-Tooling**](https://github.com/www8351/Docker-DevOps-Tooling) | Typed Docker CLI with signed, scanned images | `Python` |
| 🟢 | [**Linux-Hardening-and-System**](https://github.com/www8351/Linux-Hardening-and-System) | Safe, testable CLI replacing admin shell scripts | `Python` |
| 🟢 | [**Build-Test-Deploy**](https://github.com/www8351/Build-Test-Deploy) | DevOps lab from shell menus to a Jenkins pipeline | `Python` `Shell` |
| 🟢 | [**5-DevOps-Toolkit**](https://github.com/www8351/5-DevOps-Toolkit) | Linux, Docker and AWS tools on one shared engine | `Shell` `Python` |
| 🟡 | [**Active_Directory**](https://github.com/www8351/Active_Directory) | Scripts for local users, groups and folder rights | `PowerShell` `Shell` |

### 🧰 Tools & Teaching

| | Project | What it does | Stack |
| :-: | :-- | :-- | :-- |
| 🟢 | [**Python-Mentoring-Labs**](https://github.com/www8351/Python-Mentoring-Labs-for-Junior-Engineers) | Seven labs from beginner scripts to tested code | `Python` |
| 🟢 | [**Claude_Quota_Line**](https://github.com/www8351/Claude_Quota_Line) | Terminal status line for usage limits | `PowerShell` |
| 🟢 | [**Kickoff**](https://github.com/www8351/Kickoff) | One command to set up a Claude Code workspace | `PowerShell` |

<sub>🔒 Two private repositories: <b>Vertex_Command</b>, the production codebase behind the showcases, and <b>The-Binary-Ledger</b>, a Knesset voting-transparency index.</sub>

<br/>

## 🧪 `./run-tests --all`

| 🧪 Project | Tests | Coverage | Gate |
| :-- | :-: | :-: | :-- |
| Linux-Hardening-and-System | **206** | 82% | mypy strict |
| Agent-AI | **198** | 99 to 100% | mypy strict, 95% gate |
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
| ⚙️ **Backend & Realtime** | ![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white) ![Express 5](https://img.shields.io/badge/Express%205-000000?style=flat-square&logo=express&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white) ![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white) ![Drizzle](https://img.shields.io/badge/Drizzle-C5F74F?style=flat-square&logo=drizzle&logoColor=black) ![Valkey](https://img.shields.io/badge/Valkey-6983FF?style=flat-square) |
| ☁️ **DevOps & Cloud** | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white) ![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white) ![OpenTofu](https://img.shields.io/badge/OpenTofu-FFDA18?style=flat-square&logo=opentofu&logoColor=black) ![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black) |
| 🔭 **Observability** | ![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white) ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white) ![Loki](https://img.shields.io/badge/Loki-F46800?style=flat-square&logo=grafana&logoColor=white) ![Vector](https://img.shields.io/badge/Vector-1F6FEB?style=flat-square) ![Sentry](https://img.shields.io/badge/Sentry-362D59?style=flat-square&logo=sentry&logoColor=white) |
| 🛡️ **Security** | ![Trivy](https://img.shields.io/badge/Trivy-1904DA?style=flat-square&logo=trivy&logoColor=white) ![CycloneDX SBOM](https://img.shields.io/badge/CycloneDX%20SBOM-2B3A67?style=flat-square) ![cosign](https://img.shields.io/badge/cosign-2E2F71?style=flat-square) ![gitleaks](https://img.shields.io/badge/gitleaks-B8312F?style=flat-square) ![UFW](https://img.shields.io/badge/UFW-E95420?style=flat-square&logo=ubuntu&logoColor=white) ![SSH hardening](https://img.shields.io/badge/SSH%20hardening-2E3440?style=flat-square) ![Cilium](https://img.shields.io/badge/Cilium-F8C517?style=flat-square&logo=cilium&logoColor=black) ![Falco](https://img.shields.io/badge/Falco-00AEC7?style=flat-square&logo=falco&logoColor=white) |
| ✅ **Quality** | ![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white) ![vitest](https://img.shields.io/badge/vitest-6E9F18?style=flat-square&logo=vitest&logoColor=white) ![bats](https://img.shields.io/badge/bats-4EAA25?style=flat-square&logo=gnubash&logoColor=white) ![mypy strict](https://img.shields.io/badge/mypy%20strict-2A6DB2?style=flat-square&logo=python&logoColor=white) ![ruff](https://img.shields.io/badge/ruff-D7FF64?style=flat-square&logo=ruff&logoColor=black) ![coverage gates](https://img.shields.io/badge/coverage%20gates-F01F7A?style=flat-square&logo=codecov&logoColor=white) ![TDD](https://img.shields.io/badge/TDD-2EA043?style=flat-square) |
| 📈 **Trading** | ![MetaTrader 5](https://img.shields.io/badge/MetaTrader%205-2C6FB7?style=flat-square) ![TradingView](https://img.shields.io/badge/TradingView-131622?style=flat-square&logo=tradingview&logoColor=white) ![Binance](https://img.shields.io/badge/Binance-F0B90B?style=flat-square&logo=binance&logoColor=black) ![Kraken](https://img.shields.io/badge/Kraken-5741D9?style=flat-square) ![TwelveData](https://img.shields.io/badge/TwelveData-1E3A8A?style=flat-square) ![Tradovate](https://img.shields.io/badge/Tradovate-00A3E0?style=flat-square) ![TopstepX](https://img.shields.io/badge/TopstepX-0F172A?style=flat-square) ![Rithmic](https://img.shields.io/badge/Rithmic-8B1E3F?style=flat-square) |

<br/>

## 🎯 `man refael`

| | Principle | In practice |
| :-: | :-- | :-- |
| 🧱 | **Pure core** | Logic stays free of I/O, so it runs without a broker, a socket or a VM |
| 🔐 | **Security first** | `.env.example` only, credentials encrypted at rest, real-money paths off by default |
| 🧪 | **Verifiable** | Strict typing, coverage-gated suites, CI that blocks every push |
| 📝 | **Honest docs** | Each README says what the build does not do yet |

<br/>

<div align="center">

<code>refael@github ~ $ exit</code>

</div>
