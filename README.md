# PubmedCompanyPapers
CLI tool to fetch PubMed papers with company-affiliated authors
# get-papers

A command-line Python tool to fetch PubMed research papers with at least one author affiliated with a pharmaceutical or biotech company.

---

## 📌 Features

- Fetches papers from PubMed using flexible search query syntax
- Filters out academic-only affiliations using keyword heuristics
- Outputs the results as CSV or prints to the console
- CLI options: `--debug`, `--file`, and `--help`

---

## 🚀 Installation

Make sure [Poetry](https://python-poetry.org/docs/#installation) is installed.

```bash
poetry install
