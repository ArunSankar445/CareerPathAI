from sklearn.metrics.pairwise import cosine_similarity


def compare_embeddings(resume_emb, role_emb):
    """
    Returns cosine similarity score between resume and role.
    """
    return cosine_similarity([resume_emb], [role_emb])[0][0]


def find_skill_gaps(resume_text, role_skills):
    """
    Compares resume text with expected skills and returns matched & missing.
    """
    resume_text_lower = resume_text.lower()
    matched = [skill for skill in role_skills if skill.lower() in resume_text_lower]
    missing = [skill for skill in role_skills if skill.lower() not in resume_text_lower]
    return matched, missing
