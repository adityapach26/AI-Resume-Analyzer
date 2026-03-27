# AI Resume Analyzer

A small Streamlit app that extracts skills from PDF resumes and compares them to a list of required job skills to produce a match score and highlight missing skills.

## Features
- Upload a PDF resume and extract plain text using `pypdf`.
- Identify skills from a built-in skills database and basic synonym mapping.
- Compare resume skills to job-required skills and compute a percentage match.
- Display matching and missing skills in the Streamlit UI.

## Requirements
- Python 3.8 or newer
- `streamlit`
- `pypdf`

Install required libraries:

```
pip install streamlit pypdf
```

## Quick Start
1. Open a terminal in the project folder.
2. Run the app with Streamlit:

```
streamlit run app.py
```

3. In the web UI, upload a PDF resume and enter the required job skills in the text area (e.g. `python, machine learning, sql`).

The app will show a match percentage, useful (found) skills, and missing skills.

## How it Works (brief)
- `app.py` extracts text from the uploaded PDF using `PdfReader` from `pypdf`.
- The `text_extract_skills` function normalizes text, applies simple synonym mapping, and checks for skills from an internal `skills_db` list.
- The `main()` function computes the intersection and difference between resume and job skills and renders results with Streamlit.

## Development
- To extend the skills database, edit the `skills_db` list in [app.py](app.py#L1).
- To improve extraction or matching accuracy, consider adding NLP-based parsing or fuzzy matching.

## Contributing
PRs and issues are welcome. Please open an issue describing the enhancement or bug you want to address.

## License
MIT

---
