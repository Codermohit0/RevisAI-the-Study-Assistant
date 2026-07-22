# RevisAI 📚

> An AI-powered study assistant that turns PDFs and web articles into revision notes, key terms, and quizzes — built for students who need to revise fast.

## Problem Statement

As students, we deal with long PDFs (notes, textbook chapters, research papers) and web articles (Wikipedia, blogs) while preparing for exams. Re-reading everything before an exam is time-consuming, and most existing summarization tools are built for generic news content, not student revision needs.

**RevisAI** aims to solve this by taking any PDF or website link and converting it into structured revision notes, key terms with definitions, and auto-generated quizzes — so revision becomes faster and more effective.

## Features

- ✅ PDF text extraction (page-wise, handles blank/image-only pages gracefully)
- 🔲 Website/URL text extraction
- 🔲 Text chunking for long documents (map-reduce style)
- 🔲 Abstractive summarization (BART / Groq LLM)
- 🔲 Summary length control (short / medium / detailed)
- 🔲 Key term & definition extraction (spaCy)
- 🔲 Auto quiz generator (MCQs)
- 🔲 Flashcard generator
- 🔲 Streamlit UI
- 🔲 Deployment on Hugging Face Spaces

## Tech Stack

| Component | Tool |
|---|---|
| PDF extraction | pdfplumber |
| Web scraping | newspaper3k |
| Orchestration | LangChain |
| Summarization | BART / Groq LLM API |
| Key term extraction | spaCy |
| UI | Streamlit |
| Deployment | Hugging Face Spaces |

## Project Structure

```
RevisAI/
│
├── app.py                      # Main Streamlit app (entry point)
├── utils/
│   ├── __init__.py
│   ├── pdf_extractor.py        # PDF text extraction
│   ├── web_scraper.py          # URL text extraction
│   ├── chunker.py              # Text chunking logic
│   ├── summarizer.py           # Summarization (map-reduce)
│   ├── term_extractor.py       # Key term/definition extraction
│   └── quiz_generator.py       # MCQ generation
├── data/                       # Sample/test PDFs (git-ignored)
├── .env                        # API keys (git-ignored)
├── .gitignore
├── requirements.txt
└── README.md


## Progress Log

### Day 1 — Setup
- Initialized project structure and virtual environment
- Installed dependencies (streamlit, pdfplumber, newspaper3k, langchain, spaCy, etc.)
- Set up Git repo, resolved PowerShell execution policy issue for venv activation

### Day 2 — PDF Extractor
- Built `extract_text_from_pdf()` in `utils/pdf_extractor.py` using `pdfplumber`
- Loops through all pages, extracts text, and safely handles pages that return `None` (blank/image-only pages) without crashing
- Cleaned up repo: removed accidentally committed venv folder and a copyrighted PDF from Git history using `git filter-repo`

### Day 3 — Testing the Extractor
- Tested extraction on multiple PDF types:
  - Text-based PDF — extracted cleanly
  - 2-column research paper (arXiv survey) — text from both columns gets interleaved/mixed since `pdfplumber`'s default extraction follows raw coordinate order, not column order
  - Scanned/image-based PDF — returns empty text as expected (no OCR yet), confirming the `None`-handling logic works correctly without crashing

## Known Limitations

- **2-column layouts**: Text from side-by-side columns (common in research papers) gets extracted out of order. Possible future fix: use `pdfplumber`'s `layout=True` option or split pages by column x-coordinates before extraction.
- **Scanned PDFs**: No text is extracted since there's no OCR step yet. Planned fix: integrate `pytesseract` for OCR support.

## How to Run

```bash
git clone <repo-url>
cd RevisAI
python -m venv revisai_env
revisai_env\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python utils/pdf_extractor.py
```

## Future Scope

- Web scraper for article/URL summarization
- Map-reduce based summarization pipeline
- Key term extraction and quiz/flashcard generation
- Full Streamlit UI and deployment