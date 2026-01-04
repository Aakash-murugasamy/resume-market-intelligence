def analyze_resume_gap(resume_text, market_skills):
    resume_text = resume_text.lower()
    matched = []
    missing = []

    for skill in market_skills:
        if skill in resume_text:
            matched.append(skill)
        else:
            missing.append(skill)

    score = (len(matched) / len(market_skills)) * 100
    return matched, missing, score
