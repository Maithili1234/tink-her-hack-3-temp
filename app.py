from app import create_app  # Import the Flask app instance from your main app

app = create_app()

if __name__ == '__main__':
    # Run the app
    app.run(debug=True)