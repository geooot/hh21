from flask import Flask, render_template
import scratch

app = Flask(__name__)

@app.route("/")
def hello_world():
    browse_result = scratch.get_pokemon(0, 20)
    pokemon_list = browse_result["results"]
    return render_template("index.html", pokemon_list=pokemon_list)

if __name__ == "__main__":
    app.run(port=5000)