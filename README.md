# 🧩 Patchwork AI

### An AI-powered debugging assistant for Java codebases.

Patchwork AI is an AI-powered developer tool designed to help engineers investigate bugs in unfamiliar codebases.

It combines repository inspection, code retrieval and LLM-powered reasoning to identify potentially relevant code, investigate root causes and generate evidence-backed debugging reports.

**The goal:** Reduce the time developers spend understanding and investigating bugs.

> 🚧 Currently in early development. This project is being built in public, with its architecture, implementation progress and engineering decisions documented along the way.

---

## 🎯 The Problem

Debugging unfamiliar or large codebases can be time-consuming.

Developers often spend considerable time:

- Understanding bug reports and stack traces.
- Identifying relevant files and code paths.
- Understanding dependencies and application behaviour.
- Investigating potential root causes.
- Determining what changes could resolve the issue.

Patchwork AI aims to streamline this investigation process by combining codebase understanding with AI-powered analysis.

## 💡 The Solution

Patchwork AI accepts a bug report and a local Java repository, investigates the codebase and generates a structured debugging report.

### Proposed Workflow

1. **Bug Intake:** Accept a bug description, stack trace and relevant error details.
2. **Repository Inspection:** Scan the Java repository and build an inventory of source files.
3. **Code Retrieval:** Identify and rank potentially relevant files, classes, methods and code snippets.
4. **AI Investigation:** Provide the LLM with the bug report and relevant repository context.
5. **Investigation Report:** Generate a structured report containing likely root causes, supporting evidence and suggested fixes.

## ✨ MVP Features

- [ ] Bug report intake.
- [ ] Java repository scanning.
- [ ] Source file filtering and exclusion rules.
- [ ] Relevant code and snippet retrieval.
- [ ] Code relevance ranking.
- [ ] Context-aware LLM investigation.
- [ ] Structured debugging reports.
- [ ] Command-line interface.
- [ ] Web interface.
- [ ] Evidence-backed investigation results.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application |
| Typer | CLI |
| FastAPI | Backend API |
| Streamlit | Web interface |
| Pydantic | Data validation and structured outputs |
| OpenAI API | LLM-powered investigation |
| pytest | Automated testing |
| Git | Version control |

The entire application is being developed in Python.

## 🏗️ Architecture

The application is designed around a shared investigation engine.

Both the CLI and web interface will communicate with the same underlying application services.

Planned core components:

- **Bug Intake Service:** Validates and normalises bug reports.
- **Repository Scanner:** Traverses and indexes Java source files.
- **Code Retrieval Engine:** Searches and ranks relevant code.
- **Context Builder:** Prepares relevant repository context for the LLM.
- **AI Investigation Engine:** Analyses the bug report and retrieved code.
- **Report Generator:** Produces structured investigation results.

## 🗺️ Development Roadmap

### M1 — Repository Scanner
- [ ] CLI foundation.
- [ ] Bug report input.
- [ ] Java repository traversal.
- [ ] File filtering and inventory.

### M2 — Code Retrieval Engine
- [ ] Source code search.
- [ ] Relevant file identification.
- [ ] Relevance ranking.
- [ ] Code snippet extraction and context building.

### M3 — AI Investigation Engine
- [ ] LLM API integration.
- [ ] Repository-aware prompt construction.
- [ ] Structured AI responses.
- [ ] Root-cause hypotheses and evidence references.

### M4 — Web Interface
- [ ] FastAPI integration.
- [ ] Streamlit frontend.
- [ ] Investigation workflow through the web UI.
- [ ] Investigation report presentation.

### M5 — Quality and Release
- [ ] Unit and integration testing.
- [ ] Security hardening.
- [ ] Investigation quality evaluation.
- [ ] Documentation and first release.

## 🔒 Engineering Principles

- **Evidence over assumptions:** AI findings should reference actual repository code.
- **Human-in-the-loop:** Developers remain responsible for reviewing recommendations.
- **Controlled context:** Only relevant code should be sent to the LLM.
- **Security first:** Protect source code, credentials and local repositories.
- **Transparency:** Clearly distinguish observed code facts from AI-generated hypotheses.
- **Read-only MVP:** No automatic source code modifications or execution of arbitrary repository code.

## 📌 Current Status

Early development.

The initial focus is building the Python foundations, repository scanner and code retrieval engine.

Features in the roadmap are planned and should not be considered implemented until completed.

---

**Building Patchwork AI in public.**

