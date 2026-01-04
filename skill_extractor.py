from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

def extract_skills(descriptions, top_n=15):
    vectorizer = TfidfVectorizer(stop_words="english", max_features=top_n)
    X = vectorizer.fit_transform(descriptions)
    skills = vectorizer.get_feature_names_out()
    scores = np.mean(X.toarray(), axis=0)

    return dict(zip(skills, scores))
