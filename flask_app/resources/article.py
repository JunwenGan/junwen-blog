from flask_restful import Resource, reqparse
from bson.objectid import ObjectId
from bson.json_util import dumps
from flask import jsonify, request
from db import db



article_parser = reqparse.RequestParser()
article_parser.add_argument('title', required=True, help="Title is required")      
article_parser.add_argument('content', required=True, help="Content is required")  
article_parser.add_argument('category', required=False, help="Category of the article")  
article_parser.add_argument('cover', required=False, help="Cover image URL")  

class ArticleListResource(Resource):
    def get(self):
        try:
            page = int(request.args.get("page", 1))  
            limit = int(request.args.get("limit", 10))  
        except ValueError:
            return {"msg": "Invalid page or limit parameter"}, 400
        skip = (page - 1) * limit
        articles_cursor = db.articles.find().skip(skip).limit(limit)
        total_articles = db.articles.count_documents({})  
        articles = [
            {
                "id": str(article["_id"]),
                "title": article["title"],
                "content": article["content"],
                "category": article.get("category", "Uncategorized"),
                "cover": article.get("cover"),
                "created_at": article["created_at"].isoformat()
            }
            for article in articles_cursor
        ]

        return {
            "articles": articles,
            "pagination": {
                "current_page": page,
                "total_pages": (total_articles + limit - 1) // limit,  
                "total_items": total_articles,
                "page_size": limit,
            }
        }


class ArticleResource(Resource):
    def get(self, article_id):
        article = db.articles.find_one({"_id": ObjectId(article_id)})
        if not article:
            return {"msg": "Article not found"}, 404
        article["_id"] = str(article["_id"])
        article["created_at"] = article["created_at"].isoformat()
        # return article, 200
        return article, 200
