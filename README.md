<p align="center">
  <img src="./assets/banner.svg" width="100%" alt="Banner em pixel art: RAFAFRD, DevSecOps &amp; Purple Team" />
</p>

<div align="center">

# Opa, belezinha? 👋

Bem-vindo ao meu GitHub! Sou o **Rafa**, aprendiz de tecnologia atuando em **DevSecOps** e **Purple Team**, apaixonado por desenvolvimento de software, segurança de aplicações e engenharia de dados.

<img src="https://img.shields.io/github/followers/rafafrd?style=flat-square&labelColor=0b0b0c&color=7E30E1&logo=github&logoColor=white&label=seguidores" alt="Seguidores no GitHub" />
<img src="https://img.shields.io/badge/dynamic/json?style=flat-square&labelColor=0b0b0c&color=7E30E1&label=repos&query=public_repos&url=https%3A%2F%2Fapi.github.com%2Fusers%2Frafafrd" alt="Repositórios públicos" />
<img src="https://img.shields.io/github/stars/rafafrd?style=flat-square&labelColor=0b0b0c&color=7E30E1&label=estrelas" alt="Estrelas recebidas" />
<img src="https://api.visitorbadge.io/api/VisitorHit?user=rafafrd&repo=github-visitors-badge&label=visitas&labelColor=%230b0b0c&countColor=%237E30E1&style=flat-square" alt="Contador de visitas" />

</div>

<p align="center"><img src="./assets/divider.svg" width="100%" alt="" /></p>

## 01 · Sobre mim

```javascript
const rafa = {
  localização:      "Campinas, São Paulo — Brasil",
  emprego:          "DevSecOps & Purple Team",
  formação:         [
                      "Técnico em MSI — IFSP (concluído)",
                      "Técnico em Desenvolvimento de Sistemas — SENAI (em andamento)"
                    ],
  interesses:       ["DevSecOps & Cybersecurity", "Full Stack Development", "Data Engineering & AI", "Cloud"],
  construindoAgora: ["Vulnera — Gestão de Vulnerabilidades & DAST"],
  hobbies:          ["Codar", "Jogar", "Tocar Guitarra", "Aprendizado contínuo"],
  objetivo:         "Construir soluções que resolvem problemas reais — com segurança desde a fundação"
};
```

## 02 · CI/CD & DevSecOps

Segurança como etapa do pipeline, não como revisão no fim: todo push passa por testes e análise estática, e a aplicação rodando passa por DAST.

```mermaid
flowchart TB
  subgraph RUN["Aplicação rodando"]
    direction LR
    E[Build<br/>Docker] --> F[DAST<br/>ZAP · Burp Suite] --> G{{Purple Team<br/>Kali · Wireshark}}
  end
  subgraph CI["CI · antes do merge"]
    direction LR
    A([Commit]) --> B[Testes + cobertura<br/>Jest] --> C[SAST<br/>SonarQube · Snyk] --> D{Quality<br/>gate}
  end
  CI --> RUN
  RUN -. achados viram correção .-> CI

  classDef etapa fill:#0b0b0c,stroke:#7E30E1,color:#f2f2f2
  classDef seguranca fill:#7E30E1,stroke:#7E30E1,color:#ffffff
  class A,B,E etapa
  class C,D,F,G seguranca
  style CI fill:transparent,stroke:#6b6b6b,stroke-dasharray:4 4
  style RUN fill:transparent,stroke:#6b6b6b,stroke-dasharray:4 4
```

| Etapa | Ferramentas | Onde roda |
| --- | --- | --- |
| Testes e cobertura | Jest | CI do [Vulnera](https://github.com/guimunizzz/Vulnera-TCC/blob/main/.github/workflows/build.yml) |
| SAST | SonarQube Cloud · Snyk | SonarQube no CI do [Vulnera](https://github.com/guimunizzz/Vulnera-TCC/blob/main/.github/workflows/build.yml) e do [StockPlus](https://github.com/rafafrd/Atividade-Situacao-de-aprendizado/blob/main/.github/workflows/build.yaml) · Snyk em todos os projetos |
| Quality gate | SonarQube Cloud | Vulnera · StockPlus |
| Build | Docker | Imagens da API e da web do Vulnera |
| DAST | ZAP · Burp Suite | O ZAP é o motor de DAST do Vulnera |

<sub>Em roxo, as etapas em que a segurança entra.</sub>

## 03 · Arsenal

O que uso no dia a dia. O resto fica recolhido logo abaixo.

<table>
  <tr>
    <td width="170"><b>🔐 Segurança</b></td>
    <td>
      <img src="https://img.shields.io/badge/OWASP-0b0b0c?style=flat-square&logo=owasp&logoColor=white" alt="OWASP" />
      <img src="https://img.shields.io/badge/ZAP-0b0b0c?style=flat-square&logo=zap&logoColor=white" alt="ZAP" />
      <img src="https://img.shields.io/badge/Burp_Suite-0b0b0c?style=flat-square&logo=burpsuite&logoColor=white" alt="Burp Suite" />
      <img src="https://img.shields.io/badge/SonarQube-0b0b0c?style=flat-square&logo=sonarqubeserver&logoColor=white" alt="SonarQube" />
      <img src="https://img.shields.io/badge/Snyk-0b0b0c?style=flat-square&logo=snyk&logoColor=white" alt="Snyk" />
      <img src="https://img.shields.io/badge/Wireshark-0b0b0c?style=flat-square&logo=wireshark&logoColor=white" alt="Wireshark" />
      <img src="https://img.shields.io/badge/Kali_Linux-0b0b0c?style=flat-square&logo=kalilinux&logoColor=white" alt="Kali Linux" />
    </td>
  </tr>
  <tr>
    <td width="170"><b>⌨️ Linguagens</b></td>
    <td>
      <img src="https://img.shields.io/badge/Python-0b0b0c?style=flat-square&logo=python&logoColor=white" alt="Python" />
      <img src="https://img.shields.io/badge/PowerShell-0b0b0c?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTMgNS41IDQuNSA0bDcgNy03IDdMMyAxNi41IDguNSAxMXpNMTIgMTdoOXYyaC05eiIvPjwvc3ZnPg%3D%3D" alt="PowerShell" />
      <img src="https://img.shields.io/badge/TypeScript-0b0b0c?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
      <img src="https://img.shields.io/badge/JavaScript-0b0b0c?style=flat-square&logo=javascript&logoColor=white" alt="JavaScript" />
    </td>
  </tr>
  <tr>
    <td width="170"><b>☁️ Cloud, infra & CI</b></td>
    <td>
      <img src="https://img.shields.io/badge/Azure-0b0b0c?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTcgMTlhNSA1IDAgMCAxLS45LTkuOUE2LjUgNi41IDAgMCAxIDE4LjYgOWE1LjEgNS4xIDAgMCAxLS42IDEweiIvPjwvc3ZnPg%3D%3D" alt="Azure" />
      <img src="https://img.shields.io/badge/Docker-0b0b0c?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
      <img src="https://img.shields.io/badge/GitHub_Actions-0b0b0c?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" />
      <img src="https://img.shields.io/badge/Linux-0b0b0c?style=flat-square&logo=linux&logoColor=white" alt="Linux" />
      <img src="https://img.shields.io/badge/NGINX-0b0b0c?style=flat-square&logo=nginx&logoColor=white" alt="NGINX" />
      <img src="https://img.shields.io/badge/Git-0b0b0c?style=flat-square&logo=git&logoColor=white" alt="Git" />
    </td>
  </tr>
  <tr>
    <td width="170"><b>⚡ Back-end</b></td>
    <td>
      <img src="https://img.shields.io/badge/Node.js-0b0b0c?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js" />
      <img src="https://img.shields.io/badge/Express-0b0b0c?style=flat-square&logo=express&logoColor=white" alt="Express" />
      <img src="https://img.shields.io/badge/MySQL-0b0b0c?style=flat-square&logo=mysql&logoColor=white" alt="MySQL" />
      <img src="https://img.shields.io/badge/Prisma-0b0b0c?style=flat-square&logo=prisma&logoColor=white" alt="Prisma" />
    </td>
  </tr>
  <tr>
    <td width="170"><b>🎨 Front-end & mobile</b></td>
    <td>
      <img src="https://img.shields.io/badge/React-0b0b0c?style=flat-square&logo=react&logoColor=white" alt="React" />
      <img src="https://img.shields.io/badge/React_Native-0b0b0c?style=flat-square&logo=react&logoColor=white" alt="React Native" />
      <img src="https://img.shields.io/badge/Expo-0b0b0c?style=flat-square&logo=expo&logoColor=white" alt="Expo" />
      <img src="https://img.shields.io/badge/Tailwind_CSS-0b0b0c?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind CSS" />
      <img src="https://img.shields.io/badge/Vite-0b0b0c?style=flat-square&logo=vite&logoColor=white" alt="Vite" />
      <img src="https://img.shields.io/badge/Three.js-0b0b0c?style=flat-square&logo=threedotjs&logoColor=white" alt="Three.js" />
    </td>
  </tr>
  <tr>
    <td width="170"><b>🎲 Dados</b></td>
    <td>
      <img src="https://img.shields.io/badge/Databricks-0b0b0c?style=flat-square&logo=databricks&logoColor=white" alt="Databricks" />
      <img src="https://img.shields.io/badge/Apache_Spark-0b0b0c?style=flat-square&logo=apachespark&logoColor=white" alt="Apache Spark" />
      <img src="https://img.shields.io/badge/Delta_Lake-0b0b0c?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTEyIDMgMiA4bDEwIDUgMTAtNXpNMiAxMmwxMCA1IDEwLTUtMi4yLTEuMUwxMiAxNC44IDQuMiAxMC45ek0yIDE2bDEwIDUgMTAtNS0yLjItMS4xTDEyIDE4LjggNC4yIDE0Ljl6Ii8%2BPC9zdmc%2B" alt="Delta Lake" />
      <img src="https://img.shields.io/badge/pandas-0b0b0c?style=flat-square&logo=pandas&logoColor=white" alt="pandas" />
      <img src="https://img.shields.io/badge/Streamlit-0b0b0c?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit" />
    </td>
  </tr>
  <tr>
    <td width="170"><b>🤖 IA</b></td>
    <td>
      <img src="https://img.shields.io/badge/Claude_Code-0b0b0c?style=flat-square&logo=claude&logoColor=white" alt="Claude Code" />
      <img src="https://img.shields.io/badge/Codex-0b0b0c?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTEyIDFjMSA2IDUgMTAgMTEgMTEtNiAxLTEwIDUtMTEgMTEtMS02LTUtMTAtMTEtMTEgNi0xIDEwLTUgMTEtMTF6Ii8%2BPC9zdmc%2B" alt="Codex" />
      <img src="https://img.shields.io/badge/Antigravity-0b0b0c?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTEyIDFjMSA2IDUgMTAgMTEgMTEtNiAxLTEwIDUtMTEgMTEtMS02LTUtMTAtMTEtMTEgNi0xIDEwLTUgMTEtMTF6Ii8%2BPC9zdmc%2B" alt="Antigravity" />
      <img src="https://img.shields.io/badge/OpenCode-0b0b0c?style=flat-square&logo=opencode&logoColor=white" alt="OpenCode" />
      <img src="https://img.shields.io/badge/Gemini_API-0b0b0c?style=flat-square&logo=googlegemini&logoColor=white" alt="Gemini API" />
    </td>
  </tr>
</table>

<details>
<summary><b>Também já usei</b></summary>
<br />
<p>
  <img src="https://img.shields.io/badge/VirtualBox-0b0b0c?style=flat-square&logo=virtualbox&logoColor=white" alt="VirtualBox" />
  <img src="https://img.shields.io/badge/Socket.IO-0b0b0c?style=flat-square&logo=socketdotio&logoColor=white" alt="Socket.IO" />
  <img src="https://img.shields.io/badge/Apache-0b0b0c?style=flat-square&logo=apache&logoColor=white" alt="Apache" />
  <img src="https://img.shields.io/badge/Insomnia-0b0b0c?style=flat-square&logo=insomnia&logoColor=white" alt="Insomnia" />
  <img src="https://img.shields.io/badge/pnpm-0b0b0c?style=flat-square&logo=pnpm&logoColor=white" alt="pnpm" />
  <img src="https://img.shields.io/badge/PostgreSQL-0b0b0c?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/SQLite-0b0b0c?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Drizzle-0b0b0c?style=flat-square&logo=drizzle&logoColor=white" alt="Drizzle" />
  <img src="https://img.shields.io/badge/HTML5-0b0b0c?style=flat-square&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS-0b0b0c?style=flat-square&logo=css&logoColor=white" alt="CSS" />
  <img src="https://img.shields.io/badge/Bootstrap-0b0b0c?style=flat-square&logo=bootstrap&logoColor=white" alt="Bootstrap" />
  <img src="https://img.shields.io/badge/Apache_Parquet-0b0b0c?style=flat-square&logo=apacheparquet&logoColor=white" alt="Apache Parquet" />
  <img src="https://img.shields.io/badge/Plotly-0b0b0c?style=flat-square&logo=plotly&logoColor=white" alt="Plotly" />
  <img src="https://img.shields.io/badge/Jupyter-0b0b0c?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter" />
  <img src="https://img.shields.io/badge/Anaconda-0b0b0c?style=flat-square&logo=anaconda&logoColor=white" alt="Anaconda" />
  <img src="https://img.shields.io/badge/Figma-0b0b0c?style=flat-square&logo=figma&logoColor=white" alt="Figma" />
  <img src="https://img.shields.io/badge/Tampermonkey-0b0b0c?style=flat-square&logo=tampermonkey&logoColor=white" alt="Tampermonkey" />
</p>
</details>

## 04 · Projetos

<table>
  <tr>
    <td colspan="2" valign="top">
      <h3>Vulnera</h3>
      <p><b>Gestão de vulnerabilidades, da descoberta à correção.</b> Scans DAST com ZAP, triagem com CVSS 3.1, remediação com SLA e isolamento por empresa, na web e no mobile.</p>
      <p><b>Tech lead</b> · TCC do técnico em Desenvolvimento de Sistemas (SENAI) · equipe de 3</p>
      <p><sub>TypeScript · Express · Prisma · MySQL · React · Three.js · Expo · ZAP · Docker · SonarQube Cloud · GitHub Actions</sub></p>
      <a href="https://github.com/guimunizzz/Vulnera-TCC"><b>Repositório →</b></a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>StockPlus</h3>
      <p><b>Sistema de gestão de estoque.</b> API REST em camadas (POO e padrões de projeto) com estoque por lotes, movimentações via trigger no MySQL, relatórios em PDF e autenticação JWT, mais um app em Expo.</p>
      <p>Situação de Aprendizagem (SENAI) · equipe de 3</p>
      <p><sub>TypeScript · Express · MySQL · PDFKit · JWT · Expo · SonarQube Cloud</sub></p>
      <a href="https://github.com/rafafrd/Atividade-Situacao-de-aprendizado"><b>Repositório →</b></a>
    </td>
    <td width="50%" valign="top">
      <h3>CAGED AI Analyst</h3>
      <p><b>Inteligência de mercado com IA.</b> Perguntas em linguagem natural sobre os microdados do CAGED viram SQL gerado pelo Gemini e executado no Databricks, com gráficos montados pela própria IA.</p>
      <p>Colaboração · arquitetura e documentação</p>
      <p><sub>Python · Streamlit · Gemini · Databricks · PySpark · Delta Lake</sub></p>
      <a href="https://github.com/mfarinazzo/caged-ai-analyst"><b>Repositório →</b></a>
    </td>
  </tr>
</table>

## 05 · Atividade

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/rafafrd/rafafrd/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/rafafrd/rafafrd/output/github-snake.svg" />
    <img alt="Animação de uma cobrinha comendo o gráfico de contribuições" src="https://raw.githubusercontent.com/rafafrd/rafafrd/output/github-snake.svg" />
  </picture>
</p>

<p align="center"><img src="./assets/divider.svg" width="100%" alt="" /></p>

<p align="center"><sub>BUILD › BREAK › FIX · valeu pela visita! 👾</sub></p>
