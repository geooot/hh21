from flask import Flask, render_template, send_file, request, Response
import scratch
import json
import os
import style
from uuid import uuid4

os.system("mkdir -p files")

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

@app.route("/<pokemon_id>")
def pokemon_detail_page(pokemon_id=None):
    pokemon_details = scratch.get_pokemon_details(pokemon_id)

    return render_template("detail.html", pokemon_details=pokemon_details)

@app.route("/become", methods=["POST"])
def become():
    pokemon_id = request.args.get('id')
    if pokemon_id is None:
        return Response(
            "Bad Request",
            status=400,
        )
    pokemon_image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_id}.png"
    image_data = request.files['image']
    uid = str(uuid4())
    image_data.save(f"files/{uid}.png")

    # hacky hacky
    os.system(f"curl -o files/{pokemon_id}.png \"{pokemon_image_url}\"")
    os.system(f"convert files/{pokemon_id}.png -background white -alpha background -alpha off files/{pokemon_id}.jpg")
    os.system(f"convert files/{uid}.png -background white -alpha background -alpha off files/{uid}.jpg")

    style.pokemonize(f"files/{uid}.jpg", f"files/{pokemon_id}.jpg", f"{uid}__done")

    return Response(
        json.dumps({ "creation": uid }),
        status=200
    )

@app.route("/became/<guid>")
def became(guid=None):
    if guid is None:
        return Response(
            "Bad Request",
            status=400,
        )
    return send_file(f"files/{guid}__done.png")

if __name__ == "__main__":
    app.run(port=5000)