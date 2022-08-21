from project import create_app
from decouple import config

PORT = config("PORT", default=8080, cast=int)
DEBUG = config("DEBUG", default=False, cast=bool)

if __name__ == "__main__":
    app = create_app()
    app.run(debug=DEBUG, port=PORT)
