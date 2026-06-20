from db import locations
import datetime

locations.insert_one({
    "name": "Dan's Baptism",
    "slug": "dans-baptism",
    "location": {
        "latitude": 38.319549,
        "longitude": -77.468865
    },
    "event_date": datetime.datetime(2023, 3, 31),
    "description": "Dan died to sin and was raised in the life of Jesus Christ, no longer a slave to sin but to righteousness. Joined by his girlfriend, his brother, and sister-in-law at the Rappahannock.",
    "tags": ["personal"],
    "images": [],
    "created_at": datetime.datetime.now()
})

locations.insert_one({
    "name": "Dan's First Sermon",
    "slug": "dans-first-sermon",
    "location": {
        "latitude": 38.844633,
        "longitude": -77.310519
    },
    "event_date": datetime.datetime(2026, 6, 7),
    "description": "Dan preached his first sermon to the inmates at Fairfax County Adult Detention Center. The message was on Colossians 4:2-6. Joined by Elder Mike.",
    "tags": ["personal"],
    "images": [],
    "created_at": datetime.datetime.now()
})

locations.create_index([
    ("location", "2dsphere")
])