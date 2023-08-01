
from flask import Flask, jsonify, request
from storage import all_articles, liked_articles, not_liked_articles
from demographic_filtering import top_articles
from content_filtering import get_recommendation




@app.route("/get_popular_articles", methods=["GET"])
def get_popular_articles():
    return jsonify(top_articles)



@app.route("/get_recommended_articles", methods=["GET"])
def get_recommended_articles():
    # Get the article_id from the request
    article_id = request.args.get("article_id")

    recommended_articles = get_recommendation(article_id)

    return jsonify(recommended_articles)


@app.route("/articles/en", methods=["GET"])
def get_english_articles():
    english_articles = [article for article in all_articles if article["lang"] == "en"]
    return jsonify(english_articles)


@app.route("/like/<int:article_id>", methods=["POST"])
def like_article(article_id):
    article = next((article for article in all_articles if article["id"] == article_id), None)
    if article:
        all_articles.remove(article)
        liked_articles.append(article)
        return jsonify({"message": "Article liked successfully."}), 200
    else:
        return jsonify({"message": "Article not found."}), 404

@app.route("/dislike/<int:article_id>", methods=["POST"])
def dislike_article(article_id):
    article = next((article for article in all_articles if article["id"] == article_id), None)
    if article:
        all_articles.remove(article)
        not_liked_articles.append(article)
        return jsonify({"message": "Article disliked successfully."}), 200
    else:
        return jsonify({"message": "Article not found."}), 404
