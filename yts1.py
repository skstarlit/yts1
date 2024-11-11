import requests

# YouTube Data API v3 키 설정 (발급받은 API 키 입력)
API_KEY = '유튜브API-KEY' #유튜브 api key를 발급받아서 사용하세요.

# 인기 동영상 목록을 조회하는 함수
def get_popular_videos():
    url = 'https://www.googleapis.com/youtube/v3/videos'
    params = {
        'part': 'snippet,statistics',
        'chart': 'mostPopular',
        'regionCode': 'KR',  # 한국 지역 설정 (필요에 따라 변경 가능)
        'maxResults': 5,     # 원하는 인기 영상 수
        'key': API_KEY
    }
    response = requests.get(url, params=params)
    return response.json()

# 채널의 구독자 수 조회하는 함수
def get_channel_subscriber_count(channel_id):
    url = 'https://www.googleapis.com/youtube/v3/channels'
    params = {
        'part': 'statistics',
        'id': channel_id,
        'key': API_KEY
    }
    response = requests.get(url, params=params)
    channel_data = response.json()
    if 'items' in channel_data and len(channel_data['items']) > 0:
        return channel_data['items'][0]['statistics'].get('subscriberCount')
    return None

# 프로그램 실행
if __name__ == "__main__":
    # 인기 동영상 정보 가져오기
    popular_videos = get_popular_videos()
    
    # 인기 동영상 목록 출력
    for video in popular_videos['items']:
        video_id = video['id']
        title = video['snippet']['title']
        view_count = video['statistics'].get('viewCount', 'N/A')
        like_count = video['statistics'].get('likeCount', 'N/A')
        comment_count = video['statistics'].get('commentCount', 'N/A')
        channel_id = video['snippet']['channelId']
        channel_subscriber_count = get_channel_subscriber_count(channel_id)

        # 영상 URL 생성
        video_url = f'https://www.youtube.com/watch?v={video_id}'

        # 결과 출력
        print(f"영상 제목: {title}")
        print(f"영상 URL: {video_url}")
        print(f"조회수: {view_count}")
        print(f"좋아요 수: {like_count}")
        print(f"댓글 수: {comment_count}")
        print(f"채널 구독자 수: {channel_subscriber_count}")
        print("-" * 50)
