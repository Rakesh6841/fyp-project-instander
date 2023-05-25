from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    # Get the form data
    category = request.form["category"]
    time = request.form["time"]
    followers = request.form["followers"]
    posts = request.form["posts"]

    # Load the model and column transformer
    with open('saved_model.pkl', 'rb') as file:
        data = pickle.load(file)

    model_loaded = data["model"]
    ct_loaded = data["ct"]
    scaler_loaded = data["scaler"]

    # Make predictions on new data
    # category_encoded = ct_loaded.transform([[category]])
    category_encoded = ct_loaded.transform([[category, time, followers, posts]])
    new_features_encoded = category_encoded.tolist()[0][2:] # extract numerical features from encoded values
    new_features_scaled = scaler_loaded.transform([new_features_encoded])
    predicted_likes = model_loaded.predict(new_features_scaled)

    # Return the prediction
    return jsonify({"predicted_likes": predicted_likes})

if __name__ == "__main__":
    app.run(debug=True)
