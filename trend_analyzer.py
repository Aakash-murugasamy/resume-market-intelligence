import pandas as pd

def analyze_trends(skill_data_by_year):
    trend_df = pd.DataFrame(skill_data_by_year).fillna(0)
    trend_df["trend_score"] = trend_df.iloc[:, -1] - trend_df.iloc[:, 0]
    return trend_df.sort_values(by="trend_score", ascending=False)
