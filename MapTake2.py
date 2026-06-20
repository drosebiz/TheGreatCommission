from flask import Flask, render_template, request, jsonify
from db import locations
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        api_key=os.getenv("GOOGLE_MAPS_API_KEY")
    )


@app.route("/api/locations")
def get_locations():

    start = request.args.get("start")
    end = request.args.get("end")

    query = {}

    # If both dates provided, filter
    if start and end:
        start_date = datetime.fromisoformat(start)
        end_date = datetime.fromisoformat(end)

        query["event_date"] = {
            "$gte": start_date,
            "$lte": end_date
        }

    results = list(
        locations.find(query, {"_id": 0})
    )

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)