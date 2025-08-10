# API Automation Project (ReqRes) — Pytest + Requests + Allure

![allure-report](https://private-user-images.githubusercontent.com/43462082/476374417-3b8d23b7-6739-4a7f-91b3-22eda221f721.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTQ4NDgxMjMsIm5iZiI6MTc1NDg0NzgyMywicGF0aCI6Ii80MzQ2MjA4Mi80NzYzNzQ0MTctM2I4ZDIzYjctNjczOS00YTdmLTkxYjMtMjJlZGEyMjFmNzIxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA4MTAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwODEwVDE3NDM0M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTBhZjc3ZjczMTYxNzgzOTM4Mjg1YzdmMjY4OWQ3ZWU1NDQwN2E0YTNkODg4OGJiNjQxOGFjMTFlNzFkZjkyMDkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.lyYWZ1_Tban_Bg9KkSwoVkPCsCxLiWYepFGdxuadVJc)
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
