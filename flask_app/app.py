from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from resources.user import RegisterResource,LoginResource
from flask_jwt_extended import JWTManager
from flask_admin import Admin
from flask_admin.contrib.pymongo import ModelView
from db import db
from wtforms import Form, StringField, SelectField, DateTimeField, validators, PasswordField
from bson.objectid import ObjectId
from datetime import datetime
from wtforms.validators import DataRequired
import re
from werkzeug.security import generate_password_hash, check_password_hash
from resources.article import ArticleResource, ArticleListResource
from flask_pymongo import PyMongo
from werkzeug.exceptions import NotFound
from resources.comment import GetCommentsResource, AddCommentResource

class UserForm(Form):
    username = StringField(
        'Username',
        [
            validators.DataRequired(message="Username is required"),
            validators.Length(min=1, max=50, message="Username must be between 1 and 50 characters")
        ]
    )
    email = StringField(
        'Email',
        [
            validators.DataRequired(message="Email is required"),
            validators.Email(message="Invalid email format")
        ]
    )
    password = PasswordField(
        'Password',
        [
            validators.DataRequired(message="Password is required"),
            validators.Length(min=5, message="Password must be at least 5 characters long")
        ]
    )

    def validate_username(self, field):
        if db.users.find_one({"username": field.data}):
            raise validators.ValidationError("Username already exists")

    def validate_email(self, field):
        email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.match(email_regex, field.data):
            raise validators.ValidationError("Invalid email format")
        if db.users.find_one({"email": field.data}):
            raise validators.ValidationError("Email already exists")
        
class UserView(ModelView):
    column_list = ('username', 'password', 'email')
    form = UserForm
    def on_model_change(self, form, model, is_created):
        if is_created:
            model['password'] = generate_password_hash(form.password.data)
    
class ArticleForm(Form):
    title = StringField('Title')
    content = StringField('Content')
    category = StringField('Category')
    cover = StringField('Cover')
    created_at = DateTimeField('Created At', default=datetime.utcnow)

class ArticleView(ModelView):
    column_list = ('title', 'content', 'category', 'cover', 'created_at')
    form = ArticleForm

class CommentForm(Form):
    content = StringField("Content", [DataRequired()])
    created_at = DateTimeField('Created At', default=datetime.utcnow)
    article_id = SelectField("Article", coerce=str, validators=[DataRequired()])
    user_id = SelectField("User", coerce=str, validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.article_id.choices = [
            (str(article["_id"]), article["title"]) for article in db.articles.find()
        ]
        self.user_id.choices = [
            (str(user["_id"]), user["username"]) for user in db.users.find()
        ]

class CommentView(ModelView):
    column_list = ('content', 'created_at', 'article_id', 'user_id', 'user_name')
    form = CommentForm

    column_formatters = {
        'user_name': lambda view, context, model, name: db.users.find_one(
            {"_id": model['user_id']}
        ).get('username', 'Unknown') if 'user_id' in model else 'Unknown',
    }

    def on_model_change(self, form, model, is_created):

        if is_created:

            article = db.articles.find_one({"_id": ObjectId(form.article_id.data)})
            if not article:
                raise NotFound(f"Article with ID {form.article_id.data} not found")
            
            user = db.users.find_one({"_id": ObjectId(form.user_id.data)})
            if not user:
                raise NotFound(f"User with ID {form.user_id.data} not found")
            
            model['article_id'] = ObjectId(form.article_id.data)
            model['user_id'] = ObjectId(form.user_id.data)

app = Flask(__name__)
app.config.from_object('config.Config')
api = Api(app)
CORS(app)
jwt = JWTManager(app)

admin = Admin(app, name="Blog Admin", template_mode="bootstrap3")
admin.add_view(ArticleView(db['articles']))
admin.add_view(UserView(db['users']))
admin.add_view(CommentView(db['comments']))



## login, register
api.add_resource(RegisterResource, '/register')
api.add_resource(LoginResource, '/login')

# article and comments

api.add_resource(ArticleListResource, '/articles')
api.add_resource(ArticleResource, '/articles/<string:article_id>')
api.add_resource(GetCommentsResource, '/getComments/<string:article_id>')
api.add_resource(AddCommentResource, '/addComments')
# api.add_resource(CommentListResource, '/articles/<string:article_id>/comments')
# api.add_resource(CommentResource, '/articles/<string:article_id>/comments/<string:comment_id>')

if __name__ == '__main__':
    app.run(debug=True)
