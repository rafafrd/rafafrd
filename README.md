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
  construindoAgora: ["VANGUARD — DAST Platform", "PanGuard — CVE Tracker"],
  hobbies:          ["Codar", "Jogar", "Tocar Guitarra", "Aprendizado contínuo"],
  objetivo:         "Construir soluções que resolvem problemas reais — com segurança desde a fundação"
};
```

## 02 · Na esteira

Segurança em cada etapa, do commit à produção, e de volta para o código quando o Purple Team encontra algo.

```mermaid
flowchart TB
  subgraph CI["CI · antes do merge"]
    direction LR
    A([Código]) --> B[SAST<br/>SonarQube] --> C[SCA · SBOM] --> D[Secret scanning]
  end
  subgraph CD["CD · depois do merge"]
    direction LR
    E[Build<br/>Docker] --> F[Deploy<br/>Azure] --> G[DAST<br/>Burp Suite · VANGUARD] --> H{{Purple Team<br/>Kali · Wireshark}}
  end
  CI --> CD
  CD -. achados viram correção .-> CI

  classDef etapa fill:#0b0b0c,stroke:#7E30E1,color:#f2f2f2
  classDef seguranca fill:#7E30E1,stroke:#7E30E1,color:#ffffff
  class A,E,F etapa
  class B,C,D,G,H seguranca
  style CI fill:transparent,stroke:#6b6b6b,stroke-dasharray:4 4
  style CD fill:transparent,stroke:#6b6b6b,stroke-dasharray:4 4
```

<sub>Em roxo, as etapas em que a segurança entra.</sub>

## 03 · Arsenal

O que uso no dia a dia. O resto fica recolhido logo abaixo.

<table>
  <tr>
    <td width="170"><b>🔐 Segurança</b></td>
    <td>
      <img src="https://img.shields.io/badge/OWASP-0b0b0c?style=flat-square&logo=owasp&logoColor=white" alt="OWASP" />
      <img src="https://img.shields.io/badge/Burp_Suite-0b0b0c?style=flat-square&logo=burpsuite&logoColor=white" alt="Burp Suite" />
      <img src="https://img.shields.io/badge/SonarQube-0b0b0c?style=flat-square&logo=sonarqubeserver&logoColor=white" alt="SonarQube" />
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
    <td width="170"><b>☁️ Cloud & infra</b></td>
    <td>
      <img src="https://img.shields.io/badge/Azure-0b0b0c?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTcgMTlhNSA1IDAgMCAxLS45LTkuOUE2LjUgNi41IDAgMCAxIDE4LjYgOWE1LjEgNS4xIDAgMCAxLS42IDEweiIvPjwvc3ZnPg%3D%3D" alt="Azure" />
      <img src="https://img.shields.io/badge/Docker-0b0b0c?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
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
      <img src="https://img.shields.io/badge/PostgreSQL-0b0b0c?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
      <img src="https://img.shields.io/badge/Prisma-0b0b0c?style=flat-square&logo=prisma&logoColor=white" alt="Prisma" />
    </td>
  </tr>
  <tr>
    <td width="170"><b>🎨 Front-end</b></td>
    <td>
      <img src="https://img.shields.io/badge/React-0b0b0c?style=flat-square&logo=react&logoColor=white" alt="React" />
      <img src="https://img.shields.io/badge/React_Native-0b0b0c?style=flat-square&logo=react&logoColor=white" alt="React Native" />
      <img src="https://img.shields.io/badge/Tailwind_CSS-0b0b0c?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind CSS" />
      <img src="https://img.shields.io/badge/Vite-0b0b0c?style=flat-square&logo=vite&logoColor=white" alt="Vite" />
    </td>
  </tr>
  <tr>
    <td width="170"><b>🎲 Dados & IA</b></td>
    <td>
      <img src="https://img.shields.io/badge/Databricks-0b0b0c?style=flat-square&logo=databricks&logoColor=white" alt="Databricks" />
      <img src="https://img.shields.io/badge/Apache_Spark-0b0b0c?style=flat-square&logo=apachespark&logoColor=white" alt="Apache Spark" />
      <img src="https://img.shields.io/badge/pandas-0b0b0c?style=flat-square&logo=pandas&logoColor=white" alt="pandas" />
      <img src="https://img.shields.io/badge/Streamlit-0b0b0c?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit" />
      <img src="https://img.shields.io/badge/Claude-0b0b0c?style=flat-square&logo=claude&logoColor=white" alt="Claude" />
      <img src="https://img.shields.io/badge/Gemini-0b0b0c?style=flat-square&logo=googlegemini&logoColor=white" alt="Gemini" />
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
  <img src="https://img.shields.io/badge/Expo-0b0b0c?style=flat-square&logo=expo&logoColor=white" alt="Expo" />
  <img src="https://img.shields.io/badge/HTML5-0b0b0c?style=flat-square&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS-0b0b0c?style=flat-square&logo=css&logoColor=white" alt="CSS" />
  <img src="https://img.shields.io/badge/Bootstrap-0b0b0c?style=flat-square&logo=bootstrap&logoColor=white" alt="Bootstrap" />
  <img src="https://img.shields.io/badge/MySQL-0b0b0c?style=flat-square&logo=mysql&logoColor=white" alt="MySQL" />
  <img src="https://img.shields.io/badge/SQLite-0b0b0c?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Drizzle-0b0b0c?style=flat-square&logo=drizzle&logoColor=white" alt="Drizzle" />
  <img src="https://img.shields.io/badge/Delta_Lake-0b0b0c?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTEyIDMgMiA4bDEwIDUgMTAtNXpNMiAxMmwxMCA1IDEwLTUtMi4yLTEuMUwxMiAxNC44IDQuMiAxMC45ek0yIDE2bDEwIDUgMTAtNS0yLjItMS4xTDEyIDE4LjggNC4yIDE0Ljl6Ii8%2BPC9zdmc%2B" alt="Delta Lake" />
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
    <td width="50%" valign="top">
      <h3>VANGUARD</h3>
      <p>Plataforma de DAST.</p>
      <img src="https://img.shields.io/badge/status-em_constru%C3%A7%C3%A3o-7E30E1?style=flat-square&labelColor=0b0b0c" alt="Status: em construção" />
      <!-- TODO: 1 ou 2 linhas sobre o problema que resolve, a stack e o link do repositório -->
    </td>
    <td width="50%" valign="top">
      <h3>PanGuard</h3>
      <p>Tracker de CVEs.</p>
      <img src="https://img.shields.io/badge/status-em_constru%C3%A7%C3%A3o-7E30E1?style=flat-square&labelColor=0b0b0c" alt="Status: em construção" />
      <!-- TODO: 1 ou 2 linhas sobre o problema que resolve, a stack e o link do repositório -->
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
