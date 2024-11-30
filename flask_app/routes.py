from flask import Blueprint, jsonify, request
from extensions import db
from models import Article, Comment, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api = Blueprint("api", __name__)

@api.route("/articles", methods=["GET", "POST"])
def handle_articles():
    if request.method == "GET":
        articles = Article.query.all()
        return jsonify([{"id": a.id, "title": a.title, "content": a.content} for a in articles])
    elif request.method == "POST":
        data = request.json
        new_article = Article(title=data["title"], content=data["content"])
        db.session.add(new_article)
        db.session.commit()
        return jsonify({"id": new_article.id, "title": new_article.title, "content": new_article.content}), 201

@api.route("/comments", methods=["POST"])
@jwt_required()
def create_comment():
    data = request.json
    user_id = get_jwt_identity()
    new_comment = Comment(content=data["content"], article_id=data["article_id"], user_id=user_id)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"id": new_comment.id, "content": new_comment.content}), 201

@api.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.password == data["password"]:
        token = create_access_token(identity=user.id)
        return jsonify({"access_token": token})
    return jsonify({"msg": "Invalid credentials"}), 401
