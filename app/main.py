from flask import Flask
from app.api.routes import swift_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(swift_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=3000, debug=True)