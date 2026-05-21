# The Austenian Way 📜✍🏼

## Is Jane Austen's writing style statistically distinctive enough that a machine can recognise it?

A supervised machine learning project comparing Jane Austen's writing style to her female contemporaries using Natural Language Processing.

---

## 🔍 Overview
This project uses TF-IDF vectorisation and machine learning classifiers to determine whether Austen's prose is statistically distinctive from other female authors of the Regency era. Two versions were trained — one with proper nouns and one without — to ensure the results reflect genuine stylistic differences rather than character name recognition.

---

## 📚 Dataset
**Austen novels:**
- Sense and Sensibility (1811)
- Pride and Prejudice (1813)
- Mansfield Park (1814)
- Emma (1815)
- Northanger Abbey (1817)
- Persuasion (1817)

**Contemporary novels:**
- Evelina (1778) — Fanny Burney
- Emmeline (1788) — Charlotte Smith
- A Sicilian Romance (1790) — Ann Radcliffe
- Belinda (1801) — Maria Edgeworth
- The Wild Irish Girl (1806) — Sydney Owenson
- Self-Control (1811) — Mary Brunton
- Frankenstein (1818) — Mary Shelley

All texts sourced from [Project Gutenberg](https://www.gutenberg.org).

---

## 🧮 Methodology
- **Preprocessing:** tokenisation, lemmatisation, punctuation removal, whitespace normalisation
- **Version 1:** with proper nouns
- **Version 2:** without proper nouns (proper nouns and numbers filtered via spaCy POS tagging)
- **Chunking:** 250 tokens per chunk, capped at 200 chunks per novel
- **Vectorisation:** TF-IDF (13,059 features)
- **Models:** Logistic Regression & Random Forest
- **Train/Test Split:** 80/20

---

## 📊 Results

| Model | Version | Accuracy |
|---|---|---|
| Logistic Regression | With Proper Nouns | 98.1% |
| Random Forest | With Proper Nouns | 91.5% |
| Logistic Regression | Without Proper Nouns | 95.6% |
| Random Forest | Without Proper Nouns | 84.8% |

---

## 🔤 Key Finding
Austen's style is characterised by **function words, modal verbs and intensifiers** — the vocabulary of psychological navigation. Her contemporaries lean toward **nouns of status, setting and emotion** — a more dramatic, aristocratic register. Two very different worlds, and apparently, different enough for a machine to tell apart.

---

## 🛠️ Tools
- Python, Pandas
- NLTK, spaCy
- Scikit-Learn (TF-IDF, Logistic Regression, Random Forest)
- Seaborn, Matplotlib
- Streamlit

---

## 🚀 Streamlit App
👉 [The Austenian Way](https://your-streamlit-url-here)

The app features:
- Model performance comparison (V1 vs V2)
- Top distinctive words visualisation
- Error analysis with interactive table
- Interactive predictor — paste any text and see if it reads like Austen!

---

## 📓 Notebooks
- `The_Austenian_Way.ipynb` — Version 1 (with proper nouns)
- `V2_The_Austenian_Way.ipynb` — Version 2 (without proper nouns)
