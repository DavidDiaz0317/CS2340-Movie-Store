import json
import os
import django

# Setup Django so we can access models (if running as a standalone script)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MovieStore.settings")
django.setup()

from list.models import Movie

def load_data(json_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    for item in data:
        # item could be a dictionary that directly matches fields in your model
        obj = Movie(
            Title=item["Title"],
            Plot=item["Plot"],
            Director=item["Director"],
            Genre=item["Genre"],
            Poster=item["Poster"],
            Year=item["Year"],
            # ...
        )
        obj.save()

if __name__ == "__main__":
    load_data('movies-250.json')
