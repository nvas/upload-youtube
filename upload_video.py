from authenticate import get_youtube_client
from googleapiclient.http import MediaFileUpload

def upload_video(youtube, video_file, title, description, tags, category_id, privacy_status):
    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id
        },
        "status": {
            "privacyStatus": privacy_status
        }
    }

    # Use MediaFileUpload to upload the video file
    media = MediaFileUpload(video_file, resumable=True)

    # Upload the video
    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )

    response = request.execute()
    print(f"Video uploaded successfully: {response['id']}")

def main():
    youtube = get_youtube_client()
    upload_video(
        youtube,
        video_file="test.mp4",
        title="My Video Title",
        description="This is a description of my video.",
        tags=["tag1", "tag2"],
        category_id="22",  # Example category (22 for People & Blogs)
        privacy_status="public"
    )

if __name__ == '__main__':
    main()

