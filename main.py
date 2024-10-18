
from flask import Flask, render_template, request, jsonify
from igtest import get_travel_recommendations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button_click', methods=['POST'])
def button_click():
    # Backend functionality when button is clicked
        result = "Button was clicked!"
        return jsonify({'result': result})

@app.route('/get_travel_recommendations', methods=['POST'])
def get_travel_recommendations_route():
    image_paths = ["ig.jpg", "ig2.jpg", "ig3.jpg"]
    recommendations = get_travel_recommendations(image_paths)
    print(recommendations)
    return jsonify({'recommendations': recommendations})


def create_app():
    return app


def main():
    app = create_app()
    app.run(debug=True)

if __name__ == "__main__":
    main()
