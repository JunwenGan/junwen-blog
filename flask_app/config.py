

class Config:
    MONGO_URI = "mongodb+srv://junonegan:spain1104@cluster0.1gfa1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    JWT_SECRET_KEY = "qIYWaO8ouoKcBEFOwa0nIOCcCkZlOvsl"
    SECRET_KEY = 'mysecret'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
