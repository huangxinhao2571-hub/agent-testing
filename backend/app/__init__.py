from flask import Flask
from flask_cors import CORS
from backend.app.api.v1.user_api import user_api_bp
from backend.app.api.v1.project_api import project_api_bp
from backend.common import verify_token

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.before_request(verify_token.verify_token)
    app.register_blueprint(user_api_bp,url_prefix="/api/v1/user")
    app.register_blueprint(project_api_bp,url_prefix="/api/v1/project")
    return app