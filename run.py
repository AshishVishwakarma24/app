# Import create_app function and db object from app package
from app import create_app, db

# Import Task model from models.py
from app.models import Task

# Create a Flask app instance
app = create_app()

# Create database tables inside the app context


# Run the app in debug mode if this file is executed directly
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
