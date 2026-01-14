"""
Concluded schema from exploration
"""

SILVER_SCHEMA = {
    "actors": {"id": "int64", "name": "str", "role": "str"},
    "countries": {"id": "int64", "country": "category"},
    "crews": {"id": "int64", "role": "category", "name": "object"},
    "genres": {"id": "int64", "genre": "category"},
    "languages": {"id": "int64", "type": "category", "language": "category"},
    "movies": {
        "id": "int64",
        "name": "str",
        "date": "DateTime",
        "tagline": "str",
        "description": "str",
        "minute": "int64",
        "rating": "float64",
    },
    "releases": {
        "id": "int64",
        "country": "category",
        "date": "Datetime",
        "type": "category",
        "rating": "category",
    },
    "studios": {"id": "int64", "studio": "str"},
}
