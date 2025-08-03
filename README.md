# 📊 Trainee Evaluation Automation Project

This project provides an automated pipeline for evaluating and labeling trainee data based on structured CV and resume content. The scripts perform preprocessing, scoring, and exporting final grades in a consistent format.

---

## 📁 Project Structure

```
4pi_project_CV_resume/
├── README.md
├── labelling_CV.py
├── labelling_resume.py
├── preprocessing_CV_json.py
├── preprocessing_resume_json.py
├── data.csv
├── data_resume.csv
├── graded_output.csv
├── graded_output_resume.csv
├── preprocessing_CV.csv
├── preprocessing_CV.json
├── preprocessing_resume.csv
└── preprocessing_resume.json
```

---

## 🔧 Scripts Overview

### 1. `preprocessing_CV_json.py`
- **Input:** `data.csv` (raw CV data)
- **Output:**
  - `preprocessing_CV.csv` (cleaned, selected fields)
  - `preprocessing_CV.json` (structured format for further use)
- **Key Processing:**
  - Cleans column names
  - Merges degree, experience, education, and certification data into unified columns
  - Converts the result to both CSV and JSON

### 2. `preprocessing_resume_json.py`
- **Input:** `data_resume.csv` (raw resume data)
- **Output:**
  - `preprocessing_resume.csv`
  - `preprocessing_resume.json`
- **Key Processing:**
  - Combines multiple fields like 성장과정, 성격의 장단점, etc. into unified columns
  - Exports in structured formats

### 3. `labelling_CV.py`
- **Input:** `data.csv`
- **Output:** `graded_output.csv`
- **Purpose:**
  - Assigns grades (A–E) for various CV criteria such as:
    - 학력 (Education)
    - 경력 (Work Experience)
    - 교육이력 (Training History)
    - 자격증 (Certifications)
- **Logic:**
  - Uses exact keyword-based mapping for each field
  - Iterates through trainees to construct a normalized grading sheet

### 4. `labelling_resume.py`
- **Input:** `data_resume.csv`
- **Output:** `graded_output_resume.csv`
- **Purpose:**
  - Labels subjective responses from resumes across categories like:
    - 성장과정 (Background)
    - 성격의 장단점 (Personality Traits)
    - 학창시절 (School Life)
    - 지원동기 (Motivation)
    - 입사 후 포부 (Aspirations)
    - 직무 경험 (Work Experience)
- **Logic:**
  - Matches each response against qualitative grading rubrics (A–E)

---

## 🧠 Grading System

All evaluations are normalized using structured rubrics for each category and subcategory. Each item is graded based on exact matches using predefined mappings such as:

```python
("학력", "최종 학위 수준"): [
    ("박사 이상", "A"),
    ("석사", "B"),
    ...
]
```

Unmatched or missing data are defaulted to `"E"` (lowest score).

---

## ✅ Example Output

Each output file (`graded_output.csv`, `graded_output_resume.csv`) has the following structure:

| trainee | id | cat     | subcat               | grade |
|---------|----|---------|----------------------|--------|
| 홍길동    | 001 | 학력    | 최종 학위 수준         | B      |
| 홍길동    | 001 | 경력    | 총 경력 연수           | A      |
| ...     | ...| ...     | ...                  | ...    |

---

## 📌 Requirements

- Python 3.7+
- pandas

Install dependencies (if needed):

```bash
pip install pandas
```

---

## 🏁 How to Run

Run each script in the following order:

1. **Preprocessing CV:**
   ```bash
   python preprocessing_CV_json.py
   ```

2. **Grading CV:**
   ```bash
   python labelling_CV.py
   ```

3. **Preprocessing Resume:**
   ```bash
   python preprocessing_resume_json.py
   ```

4. **Grading Resume:**
   ```bash
   python labelling_resume.py
   ```
