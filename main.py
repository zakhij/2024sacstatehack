
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button_click', methods=['POST'])
def button_click():
    # Backend functionality when button is clicked
    result = "Button was clicked!"
    return jsonify({'result': result})

def create_app():
    return app


def main():
    app = create_app()
    app.run(debug=True)

if __name__ == "__main__":
    main()
