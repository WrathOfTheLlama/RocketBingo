from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route(rule="/", methods=["GET", "POST"])
def index():
    # The GET endpoint
    if request.method == "GET":
        return "This is the GET Endpoint of flask API."
    
    # The POST endpoint
    if request.method == "POST":
        # accesing the passed payload
        payload = request.get_json()

        # capitalizing the text
        cap_text = payload['text'].upper()

        # Creating a proper response
        response = {'cap-text': cap_text}

        # return the response as JSON
        return jsonify(response)
    
    #return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)