from flask import Flask, render_template, request,  jsonify
from data import jokes
import random


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# joke generator
@app.route('/')
def home():
    return render_template('index.html')

# get all jokes (GET)
@app.route('/api/jokes', methods=['GET'])
def get_jokes():
    return jsonify(jokes), 200

# get a random joke 
@app.route('/api/jokes/<int:id>', methods=['GET'])
def get_joke(id):
    return jsonify(jokes[id]), 200
    
# get a joke by id 
@app.route('/api/jokes/random', methods=['GET'])
def get_random_joke():
    return jsonify({'joke': random.choice(jokes)}), 200

#add jokes (POST)
@app.route('/api/jokes', methods=['POST'])
def add_joke():
    new_joke = {
        'id': len(jokes) + 1,
        'joke': request.json['joke'],
        'punchline': request.json['punchline']
    }
    jokes.append(new_joke)
    return jsonify({'message': 'Joke Added Succesfully', 'Jokes': jokes}), 201

# update jokes (PUT)
@app.route('/api/jokes/<int:id>', methods=['PUT'])
def update_joke(id):
    joke_found = [joke for joke in jokes if joke['id'] == id]
    if len(joke_found) > 0:
        joke_found[0]['joke'] = request.json.get('joke', joke_found[0]['joke'])
        joke_found[0]['punchline'] = request.json.get('punchline', joke_found[0]['punchline'])
    else:
        return jsonify({'message': 'Joke Not Found'}), 404

    return jsonify({'message': 'Joke Updated Succesfully', 'Jokes': jokes}), 200


# delete jokes (DELETE)
@app.route('/api/jokes/<int:id>', methods=['DELETE'])
def delete_joke(id):
    joke_found = [joke for joke in jokes if joke['id'] == id]
    if len(joke_found) > 0:
        jokes.remove(joke_found[0])
        return jsonify({'message': 'Joke Deleted Succesfully', 'Jokes': jokes}), 200
    else:
        return jsonify({'message': 'Joke Not Found'}), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
    
    
   