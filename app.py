"""Run script that creates the Flask app using the factory in the
`attendguard` package. This is a thin run wrapper (no app logic here).
"""
from attendguard import create_app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
