import spotipy
from spotipy.oauth2 import SpotifyClientCredentials;

cid = '327e3e90c83144669b385f32b3f58c6b'
secret = 'ff8f4ba0f3564f7382f0a51cde8659db'
client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret= secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager);

def call_playlist(creator,playlist_id):
    playlist_features_list = ["artist", "album", "track_name", "track_id"]
    playlist_dif = pd.DataFrame(columns = playlist_features_list)

    playlist = sp.user_playlist_tracks(creator, playlist_id)["items"]
    for track in playlist:
        playlist_features = {};
        play