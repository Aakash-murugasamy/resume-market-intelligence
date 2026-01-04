import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# -----------------------------
# Load data
# -----------------------------
jobs = pd.read_csv("data/jobs.csv")

with open("data/resume.txt", "r") as f:
    resume_text = f.read()

# -----------------------------
# TF-IDF Skill Extraction
# -----------------------------
vectorizer = TfidfVectorizer(stop_words="english", max_features=20)
X = vectorizer.fit_transform(jobs["description"])

skills = vectorizer.get_feature_names_out()
skill_scores = np.mean(X.toarray(), axis=0)

market_skills = pd.DataFrame({
    "Skill": skills,
    "DemandScore": skill_scores
}).sort_values(by="DemandScore", ascending=False)

print("\n📊 TOP MARKET SKILLS:")
print(market_skills)

# -----------------------------
# Resume Skill Matching
# -----------------------------
resume_vector = vectorizer.transform([resume_text]).toarray()[0]

matched = []
missing = []

for skill, score in zip(skills, resume_vector):
    if score > 0:
        matched.append(skill)
    else:
        missing.append(skill)

print("\n✅ SKILLS FOUND IN RESUME:")
print(matched)

print("\n❌ SKILLS MISSING FROM RESUME:")
print(missing)

# -----------------------------
# Resume Readiness Score
# -----------------------------
readiness = (len(matched) / len(skills)) * 100
print(f"\n🎯 Resume Market Readiness Score: {readiness:.2f}%")
