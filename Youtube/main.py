from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Set up the YouTube API
CLIENT_ID = ""
API_NAME = "youtube"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

# Specify the redirect URI
REDIRECT_URI = "http://localhost:8080/redirect_uri"

def authenticate():
    flow = InstalledAppFlow.from_client_config(
        {
            "installed": {
                "client_id": CLIENT_ID,
                "client_type": "installed",
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://accounts.google.com/o/oauth2/token",
                "redirect_uris": [REDIRECT_URI],
            }
        },
        SCOPES,
    )
    credentials = flow.run_local_server(port=8080)  # Change port to 8080
    return build(API_NAME, API_VERSION, credentials=credentials)

def get_watch_history(api_service):
    request = api_service.videos().list(part="snippet,contentDetails,statistics", myRating="like")
    response = request.execute()

    for item in response.get("items", []):
        video_title = item["snippet"]["title"]
        video_id = item["id"]
        print(f"Video Title: {video_title}\nVideo ID: {video_id}\n")

def main():
    api_service = authenticate()
    get_watch_history(api_service)

if __name__ == "__main__":
    main()
