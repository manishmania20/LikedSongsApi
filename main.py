import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(CLIENT_ID,
                                               CLIENT_SECRET,
                                               REDIRECT_URI,
                                               scope=scope))

# Call the current_user() method to prompt the user to grant permission
user = sp.current_user()

# Once the user grants permission, you can use the API as usual
results = sp.current_user_saved_tracks()
tracks = results['items']

# Loop through each track and print the name and artist
for track in tracks:
    print(track['track']['name'] + ' - ' + track['track']['artists'][0]['name'])
