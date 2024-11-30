from datetime import datetime
from flask import request, jsonify
from flask_restful import Resource
from bson.objectid import ObjectId
from werkzeug.security import check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity
from db import db

class AddCommentResource(Resource):
    @jwt_required()  
    def post(self):
        user_id = get_jwt_identity()
        if not user_id:
            return {"msg": "Authentication required"}, 401
        
        user = db.users.find_one({"_id": ObjectId(user_id)})
        if not user:
            return {"msg": "User not found"}, 404
        
        data = request.json
        content = data.get("content")
        article_id = data.get("article_id")

        if not content or not article_id:
            return {"msg": "Content and article_id are required"}, 400

        article = db.articles.find_one({"_id": ObjectId(article_id)})
        if not article:
            return {"msg": "Article not found"}, 404

        new_comment = {
            "content": content,
            "article_id": ObjectId(article_id),
            "user_id": ObjectId(user_id),
            "created_at": datetime.utcnow(),
        }
        result = db.comments.insert_one(new_comment)

        return {
            "msg": "Comment added",
            "id": str(result.inserted_id),
            "content": content,
            "article_id": article_id,
            "user_id": user_id,
            "user_name": user.get("username"),
        }, 201
        
class GetCommentsResource(Resource):
    def get(self, article_id):
        article = db.articles.find_one({"_id": ObjectId(article_id)})
        if not article:
            return {"msg": "Article not found"}, 404

        comments = db.comments.find({"article_id": ObjectId(article_id)})
        result = []
        for comment in comments:
            user = db.users.find_one({"_id": ObjectId(comment["user_id"])})
            username = user["username"] if user else "Unknown"

            result.append({
                "id": str(comment["_id"]),
                "content": comment["content"],
                "user_id": str(comment["user_id"]),
                "created_at": comment["created_at"].isoformat(),
                "user_name": username,  
            })

        return jsonify(result)
