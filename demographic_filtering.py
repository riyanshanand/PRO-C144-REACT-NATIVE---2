
import pandas as pd

df = pd.read_csv("flask_project/articles.csv")
df_sorted = df.sort_values(by="total_events", ascending=False)

top_articles = df_sorted.head(20).to_dict(orient="records")
