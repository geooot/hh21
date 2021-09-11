from flask import Flask, render_template, request
import scratch

app = Flask(__name__)

@app.route("/")
def hello_world():
    offset = request.args.get('offset')
    limit = request.args.get('limit')

    if offset == None:
        offset = 0
    else:
        offset = int(offset)
    
    if limit == None:
        limit = 20
    else:
        limit = int(limit)

    browse_result = scratch.get_pokemon(offset, limit)
    pokemon_list = browse_result["results"]
    return render_template("index.html", pokemon_list=pokemon_list, offset=offset, limit=limit, next_api_url=browse_result['next'], prev_api_url=browse_result['previous'])

if __name__ == "__main__":
    app.run(port=5000)