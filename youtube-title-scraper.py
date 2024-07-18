import googleapiclient.discovery
import googleapiclient.errors
import csv

def get_video_statistics(youtube, video_ids):
    # Retrieve video statistics for a list of video IDs
    request = youtube.videos().list(
        part="snippet,statistics",
        id=','.join(video_ids)
    )
    response = request.execute()
    
    video_data = []
    for item in response['items']:
        title = item['snippet']['title']
        views = item['statistics'].get('viewCount', 0)
        likes = item['statistics'].get('likeCount', 0)
        video_data.append([title, views, likes])
    
    return video_data

def main():
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyAGCUyWrzRObDips806OHnoxu-dft6u9lw"  # Replace with your actual API key

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    request = youtube.search().list(
        part="snippet",
        type="video",
        maxResults=50,
        order="relevance",  
        relevanceLanguage="en",
        regionCode = "US"
    )

    response = request.execute()

    video_ids = [item['id']['videoId'] for item in response['items']]
    video_data = get_video_statistics(youtube, video_ids)

    with open('yt-title-data.csv', mode='w', newline='',encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Views', 'Likes'])
        writer.writerows(video_data)
    
    print("Data has been written to youtube_video_statistics.csv")

if __name__ == "__main__":
    main()