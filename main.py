import pandas as pd
from skill_extractor import extract_skills
from trend_analyzer import analyze_trends
from resume_gap_analyzer import analyze_resume_gap

# Load datasets
years = ["2022", "2023", "2024"]
skill_data = {}

for year in years:
    df = pd.read_csv(f"data/jobs_{year}.csv")
    skill_data[year] = extract_skills(df["description"])

# Trend analysis
trend_df = analyze_trends(skill_data)

print("\n📈 SKILL TREND ANALYSIS:")
print(trend_df)

# Resume analysis
with open("data/resume.txt") as f:
    resume_text = f.read()

market_skills = trend_df.index.tolist()
matched, missing, score = analyze_resume_gap(resume_text, market_skills)

print("\n✅ MATCHED SKILLS:", matched)
print("\n❌ MISSING SKILLS:", missing)
print(f"\n🎯 RESUME READINESS SCORE: {score:.2f}%")
