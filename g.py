from googleapiclient.discovery import build

def search_video(query):
    youtube = build("youtube", "v3", developerKey="AIzaSyBKjA3O0WWkwCOFHCfCHkBZzIh2mY9JGb8")

    request = youtube.search().list(
        part="id",
        type='video',
        q=query,
        maxResults=1
    )
    response = request.execute()

    video_id = response['items'][0]['id']['videoId']
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    return video_url
