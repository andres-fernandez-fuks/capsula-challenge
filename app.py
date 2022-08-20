from project import create_app

PORT = 8080 # mover a .env

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=PORT)
