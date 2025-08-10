# API Automation Project (ReqRes) — Pytest + Requests + Allure

## Overview
This repository contains API tests (full CRUD) against the public ReqRes API (https://reqres.in). It follows best practices, uses a reusable API client, and generates Allure-compatible results.

## Structure
```bash
api_automation_project/
├── config/
├── data/
├── tests/
├── utils/
├── .github/
├── requirements.txt
└── README.md
```


## Setup
1. Create & activate a virtualenv:
```bash
python -m venv .venv
source .venv/bin/activate   # mac / linux
.venv\Scripts\activate      # windows
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
## Run tests and collect Allure results
```bash
pytest --alluredir=reports
```
- View Allure report locally
You need Allure CLI installed, check instructions here: https://allurereport.org/docs/

```bash
allure serve reports

```
