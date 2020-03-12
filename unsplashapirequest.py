import requests
import os


def download_photo():
    # Unsplash API config
    client_id = os.environ.get("unsplash_client_id")
    url = 'https://api.unsplash.com/photos/random'

    # making request to unsplash api for random photo
    unsplash_data = requests.get(
        url, params={'client_id': client_id, 'query': 'animal'}).json()

    # retrieving the photo url
    unsplash_photo_url = unsplash_data['urls']['regular']

    # retrieving the photo source link
    unsplash_source = unsplash_data['links']['html']

    # making a get request to photo url
    img_data = requests.get(unsplash_photo_url).content

    # downloading photo into project folder
    with open("uphoto.jpg", "wb") as f:
        f.write(img_data)
        f.close()

    return unsplash_source
