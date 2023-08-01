
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("flask_project/articles.csv").dropna(subset=["title"])


def get_recommendation(article_id):
    pass
