from flask import Flask, render_template, jsonify
from config import Config
from routes.weather_routes import bp
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Cache setup
    app.cache = Cache(app, config={"CACHE_TYPE": "SimpleCache"})

    # Rate limiter setup
    app.limiter = Limiter(key_func=get_remote_address, default_limits=[Config.RATELIMIT_DEFAULT])
    app.limiter.init_app(app)

    # Register blueprints
    app.register_blueprint(bp)

    # Root endpoint
    @app.route("/")
    def index():
        return jsonify({
            "message": "Weather Forecast API. Use /api/weather or /api/forecast"
        })

    # Frontend page
    @app.route("/home")
    def home():
        return render_template("index.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
