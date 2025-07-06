# 🤖 CareerPathAI – Personalized Career Navigator Bot

CareerPathAI is an AI-powered assistant that analyzes a user’s resume against a **target job role**, detects skill gaps, recommends **learning resources**, and generates **custom mock interview questions** using **Gemini API**.

---

## 🎯 Objective

Most job seekers don’t know how close they are to being job-ready. This project uses AI to:

- 🔍 Compare resume vs job description using embeddings
- 🧠 Identify missing and matched skills
- 📚 Suggest tools and courses using LLMs
- 🎤 Generate realistic interview questions

---

## 📂 Folder Structure

careerpathai/
├── resumes/
│ └── sample_resume.pdf
├── roles/
│ └── ml_engineer_template.json
├── embeddings/
│ └── embedding_engine.py
├── prompts/
│ ├── learning_advice_prompt.txt
│ └── interview_q_prompt.txt
├── outputs/
│ └── career_gap_report.md
├── notebooks/
│ ├── llm_prompter.py
│ ├── report_generator.py
│ ├── resume_parser.py
│ └── skill_matcher.py
├── .env
├── main.py
└── README.md


---

## ⚙️ How It Works

1. Parse resume from `.pdf`
2. Load job role template (`.json`)
3. Generate embeddings using **Sentence-BERT**
4. Compare similarity (cosine)
5. Detect matched & missing skills
6. Use **Gemini API** to generate:
   - 📚 Learning advice
   - 🎤 Mock interview questions
7. Save results to `outputs/`

---

## 📥 Input & 📤 Output

| Input File | Output File |
|------------|-------------|
| `sample_resume.pdf` | `career_gap_report.md` |
| `prompts/*.txt` | `mock_questions.txt` |

---

## 🛠️ Setup Instructions

### ✅ 1. Install Dependencies

```bash
pip install pdfplumber sentence-transformers google-generativeai python-dotenv scikit-learn
```

### ✅ 2. Create .env File

GEMINI_API_KEY=your_gemini_api_key_here

### ✅ 3. Enable Gemini API

1.Visit makersuite.google.com or AI Studio
2.Generate an API key and paste it into .env

## ✨ Sample Output

# 📄 Gap Report for **Machine Learning Engineer**

**🧮 Match Score:** `31%`

## ❌ Missing Skills
- Model Deployment
- MLOps

## 📚 Learning Advice
Arun, your resume is strong, showcasing good foundational skills.  To become a more competitive Machine Learning Engineer, let's address your missing skills in Model Deployment, MLOps, Docker, and APIs.  Here's a plan with specific tools and resources:

**Model Deployment:**

* **Tools/Platforms:**
    * **Flask/FastAPI (Python):**  These are lightweight web frameworks perfect for deploying simple ML models.  Start with Flask as it's easier to learn, then explore FastAPI for more advanced features.  Plenty of tutorials are available on YouTube and websites like Real Python.
    * **Streamlit:**  A great tool for creating interactive web apps for your models without needing extensive web development knowledge.  Their website has excellent documentation and examples.
    * **Heroku/AWS Elastic Beanstalk/Google Cloud Run:**  These are Platform as a Service (PaaS) options for deploying your Flask/FastAPI/Streamlit apps easily.  They handle server management for you, allowing you to focus on your code.  Each platform has free tiers to get started.  Look for their tutorials and quickstarts.
* **Learning Resources:**
    * **YouTube channels:** Search for "Flask ML deployment," "FastAPI ML deployment," "Streamlit deployment tutorial."
    * **Blogs/Articles:**  Look for articles on deploying ML models with specific frameworks (e.g., "Deploying a scikit-learn model with Flask").  Medium and Towards Data Science are good sources.
    * **Documentation:**  Always refer to the official documentation of the tools you choose.


**Roadmap:**

1. **Start with Flask/Streamlit and a simple model deployment.** This will give you immediate experience and build confidence.
2. **Learn Docker to containerize your application.** This makes deployment easier and more portable.
3. **Explore MLflow for MLOps practices.** Focus on experiment tracking and model versioning.
4. **Build a small project that integrates all these skills.** This could be a REST API serving your deployed model.

## 🎤 Mock Interview Questions
Here are some mock interview questions for a Machine Learning Engineer role, focusing on the missing skills (Model Deployment, MLOps, Docker, APIs):

1. **Model Deployment:** "Describe your experience deploying machine learning models to production.  Let's say you've trained a highly accurate image classification model.  Walk me through the steps involved in deploying it to a real-world application, considering factors like scalability, latency, and monitoring."  (This probes both technical knowledge and practical experience.)

2. **MLOps:** "Explain the concept of MLOps and how it differs from traditional DevOps.  Provide a specific example of how implementing MLOps principles improved a model's performance or deployment process in a past project." (This assesses understanding of MLOps philosophy and its practical application.)

## 📈 Key Features

1. **Embedding-based similarity (not keyword-only ✅)**

2. **Role-specific skill templates (swappable JSON ✅)**

3. **LLM-based responses (OpenAI GPT ✅)**

4. **Modular prompt design (clear separation ✅)**

5. **Output saved as structured Markdown/TXT ✅**

## 💡 Optional Extensions

* **Add Streamlit UI for resume upload and result preview**

* **Export reports as PDFs or Notion cards**

* **Analyze multiple resumes (batch mode)**

* **Categorize skills (technical, soft skills, tools)**
