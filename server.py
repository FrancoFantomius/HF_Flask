from flask_app import new_app

app = new_app()

if __name__ == "__main__":
    app.run(debug=True)