# GitHub Repo Health Analyzer

A simple Python tool that checks if a GitHub repo is healthy or not.

## What it does?
- **Worker 1:** Checks if important files like `main.py`, `README.md`, `requirements.txt` exist
- **Worker 2:** Checks if README is too short
- **Worker 3:** Checks if commit messages are useless like "fix", "asdf"
- **Boss:** Combines all checks and gives a Final Score

## How to Run?
```python
python analyzer.py

## Output
Final Score: 100.0% - Issues: All good

##Built with
Python
 Built  fully on phone
 
 
 ## Author
 Built by me - my first python project