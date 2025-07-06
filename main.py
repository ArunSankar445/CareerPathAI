import json
from embeddings.embedding_engine import get_embedding
from program.resume_parser import extract_resume_text
from program.skill_matcher import compare_embeddings, find_skill_gaps
from program.llm_prompter import load_prompt, get_completion
from program.report_generator import save_report

resume_path = "resumes/sample_resume.pdf"  # <-- Your resume file here
role_template_path = "roles/ml_engineer.json"  # <-- Job role template

print("📄 Loading resume...")
resume_text = extract_resume_text(resume_path)

print("🎯 Loading job role template...")
with open(role_template_path, "r") as file:
    role_data = json.load(file)
role_name = role_data["role"]
role_skills = role_data["skills"]
role_text = " ".join(role_skills)  # for embedding

print("🧠 Generating embeddings...")
resume_embedding = get_embedding(resume_text)
role_embedding = get_embedding(role_text)

print("📊 Calculating similarity...")
similarity_score = compare_embeddings(resume_embedding, role_embedding)

print("🔍 Finding skill gaps...")
matched_skills, missing_skills = find_skill_gaps(resume_text, role_skills)

print("📚 Generating learning advice...")
advice_prompt = load_prompt("prompts/learning_advice_prompt.txt")
advice_prompt = advice_prompt.replace("[RESUME]", resume_text)
advice_prompt = advice_prompt.replace("[SKILLS]", ", ".join(missing_skills))
advice_prompt = advice_prompt.replace("[ROLE]", role_name)
learning_advice = get_completion(advice_prompt)

print("🎤 Generating mock interview questions...")
question_prompt = load_prompt("prompts/interview_q_prompt.txt")
question_prompt = question_prompt.replace("[ROLE]", role_name)
question_prompt = question_prompt.replace("[SKILLS]", ", ".join(missing_skills))
question_prompt = question_prompt.replace("[RESUME]", resume_text)
interview_questions = get_completion(question_prompt)

print("💾 Saving output report...")
save_report(
    role_name,
    similarity_score,
    matched_skills,
    missing_skills,
    learning_advice,
    interview_questions,
)

print("\n✅ Done! Gap report saved to: outputs/gap_report.md")
