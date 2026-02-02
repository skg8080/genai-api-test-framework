# 🚀 GenAI‑Assisted API Automation Framework

## 📌 Overview

This project demonstrates a **GenAI‑assisted API automation framework** built using **Python and PyTest**. The framework consumes **Swagger / OpenAPI specifications** as input and leverages **Large Language Models (LLMs)** to automatically generate executable API test cases, significantly reducing manual scripting effort.

The project is designed as a **portfolio‑ready, interview‑grade implementation** suitable for Big4 / enterprise QA and SDET roles.

---

## 🎯 Key Objectives

* Eliminate manual API test case writing
* Generate PyTest test cases directly from Swagger
* Demonstrate practical GenAI usage (not theoretical AI)
* Produce real execution reports (HTML)
* Follow enterprise‑style framework design

---

## 🧠 High‑Level Architecture

```
Swagger / OpenAPI (JSON)
        ↓
Swagger Parser (Python)
        ↓
API Metadata Normalization
        ↓
Prompt Builder (Prompt Engineering)
        ↓
LLM Gateway (OpenRouter.ai)
        ↓
LLM Output Sanitization Layer
        ↓
Generated PyTest Test Files
        ↓
PyTest Execution Engine
        ↓
HTML Test Execution Report
```

---

## 🧩 Technology Stack

| Component      | Technology        |
| -------------- | ----------------- |
| Language       | Python 3.11       |
| Test Framework | PyTest            |
| API Client     | requests          |
| GenAI Gateway  | OpenRouter.ai     |
| Spec Format    | Swagger / OpenAPI |
| Reporting      | pytest‑html       |
| IDE            | VS Code           |

---

## 📂 Project Structure

```
├── src/
│   ├── swagger_parser.py      # Swagger parsing & filtering
│   ├── prompt_builder.py      # Prompt engineering logic
│   ├── llm_client.py          # OpenRouter LLM integration + sanitization
│   └── test_generator.py      # End‑to‑end test generation
│
├── swagger/
│   └── petstore_swagger.json  # Swagger input
│
├── tests/
│   └── generated/             # AI‑generated PyTest files
│
├── reports/
│   └── report.html            # HTML execution report
│
├── pytest.ini                 # PyTest logging configuration
├── .env                       # API keys (ignored by git)
├── requirements.txt
└── README.md
```

---

## 🔄 End‑to‑End Flow

1. Swagger JSON is provided as input
2. Swagger parser extracts API metadata
3. Metadata is converted into structured prompts
4. Prompts are sent to LLM via OpenRouter
5. LLM generates PyTest test code
6. Output sanitization removes markdown & fixes hallucinations
7. Test files are written to disk
8. PyTest executes generated tests
9. HTML execution report is generated

---

## 🧪 Test Execution

```bash
pytest tests/generated --html=reports/report.html --self-contained-html
```

---

## 🛡️ Key Engineering Considerations

* **LLM Provider Agnostic** – OpenRouter allows easy model switching
* **Sanitization Layer** – Fixes markdown artifacts and hallucinated APIs
* **Secure Secrets Handling** – API keys stored in `.env`
* **Enterprise Logging** – Logs visible even for passed tests
* **Extensible Design** – Easy to add auth, retries, CI/CD

---

## 💬 Interview‑Ready Summary

> Built a GenAI‑assisted API automation framework using Python and PyTest that parses Swagger specifications and leverages LLMs via OpenRouter to automatically generate executable API test cases, reducing manual effort and accelerating test coverage. Integrated output sanitization, structured logging, and HTML reporting to simulate real‑world enterprise QA workflows.

---

## 🚀 Future Enhancements

* CI/CD integration (GitHub Actions)
* Auth token handling
* Test data seeding
* Retry & flaky test handling
* Azure OpenAI support
