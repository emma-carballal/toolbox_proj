import requests
from toolbox_proj.api_key import your_client_access_token

def search_songs(artist):
    client_access_token = your_client_access_token
    search_term = artist
    genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"

    response = requests.get(genius_search_url)
    json_data = response.json()

    songs = []
    for song in json_data['response']['hits']:
        songs.append(song['result']['title'])
    return songs

if __name__ == "__main__":
    songs = search_songs("PJ Harvey")
    print(songs)
