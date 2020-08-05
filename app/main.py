from app import app
import view
from app import db
from movies.movie import movies

app.register_blueprint(movies, url_prefix='/movies')
if __name__ == "__main__":
    app.run()