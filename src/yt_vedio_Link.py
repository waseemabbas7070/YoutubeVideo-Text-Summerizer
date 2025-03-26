from youtube_transcript_api import YouTubeTranscriptApi
import re
class link_downloader:
    def __init__(self):
        pass
    def extract_video_id(self,video_url):
        if "youtube.com/watch?v=" in video_url:
            return video_url.split("v=")[-1].split("&")[0]
        elif "youtu.be/" in video_url:
            return video_url.split("youtu.be/")[-1].split("?")[0]
        elif "youtube.com/embed/" in video_url:
            return video_url.split("embed/")[-1].split("?")[0]
        elif "youtube.com/shorts/" in video_url:
            return video_url.split("shorts/")[-1].split("?")[0]
        else:
            match = re.search(r"([a-zA-Z0-9_-]{11})", video_url)
            return match.group(1) if match else None

    def get_transcript(self,video_id):
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(video_id)

        text = []
        for snippet in fetched_transcript:
            text.append(snippet.text)

        text = " ".join(text)
        return text