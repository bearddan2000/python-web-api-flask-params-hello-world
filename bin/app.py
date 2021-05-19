from flask import Flask, jsonify, request
app = Flask(__name__)

greetings = [
    {'id': 'en', 'msg': 'hello world'}
    , {'id': 'es', 'msg': 'hola'}
    , {'id': 'fr', 'msg': 'salute'}
    , {'id': 'de', 'msg': 'tag'}
]

@app.route('/')
def hello():
    return jsonify(greetings)

@app.route('/lang')
def params():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = str(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for greeting in greetings:
        if greeting['id'] == id:
            results.append(greeting)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
