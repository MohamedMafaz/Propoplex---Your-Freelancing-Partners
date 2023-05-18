from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

# Additional routes and functionality can be added here

if __name__ == '__main__':
    app.run()

application = app  # Add this line to expose the Flask app as 'application' attribute
