from fastapi import APIRouter
from config.db import conn
from models.joke import jokes 

router = APIRouter()

# Get all jokes
@router.get("/api/jokes")
def get_jokes():
    return conn.execute(jokes.select()).fetchall()

# Get the joke count
@router.get('/api/jokes/count')
def get_jokes_count():
    print(conn.execute(jokes.select()).scalar())
    

# Get a random joke
@router.get("/api/jokes/random")
def get_random_joke(id):
    return conn.execute(jokes.select())


# Get a joke by id
@router.get("/api/jokes/random")
def get_random_joke():
    return jsonify({"joke": random.choice(jokes)}), 200


# Add jokes
@router.post("/api/jokes")
def add_joke():
    new_joke = {
        "id": len(jokes) + 1,
        "joke": request.json["joke"],
        "punchline": request.json["punchline"],
    }
    jokes.append(new_joke)
    return jsonify({"message": "Joke Added Succesfully", "Jokes": jokes}), 201


# Update jokes
@router.put("/api/jokes/<int:id>")
def update_joke(id):
    joke_found = [joke for joke in jokes if joke["id"] == id]
    if len(joke_found) > 0:
        joke_found[0]["joke"] = request.json.get("joke", joke_found[0]["joke"])
        joke_found[0]["punchline"] = request.json.get(
            "punchline", joke_found[0]["punchline"]
        )
    else:
        return jsonify({"message": "Joke Not Found"}), 404

    return jsonify({"message": "Joke Updated Succesfully", "Jokes": jokes}), 200


# Delete jokes
@router.delete("/api/jokes/<int:id>")
def delete_joke(id):
    joke_found = [joke for joke in jokes if joke["id"] == id]
    if len(joke_found) > 0:
        jokes.remove(joke_found[0])
        return jsonify({"message": "Joke Deleted Succesfully", "Jokes": jokes}), 200
    else:
        return jsonify({"message": "Joke Not Found"}), 404
