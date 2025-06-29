import re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled 

class video_id:
    def __init__(self, url):
        self.url = url
        self.video_id  = self.fetch_video_id()



    def video_transcript(self):
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id= self.video_id, languages=['en', 'hi'])
            #flatten it to plain text
            transcript = " ".join(chunk["text"] for chunk in transcript_list)
            print(transcript)
        except TranscriptsDisabled:
            print("No Caption avilable for this video.")




    def fetch_video_id(self):
        match = re.search(r"(?:youtu\.be/|v=|embed/)([^&?#]+)", self.url)
        return match.group(1) if match else ""


    
if __name__ == "__main__":
    id = video_id("https://youtu.be/LPZh9BOjkQs?si=lBZRUXVSOVKCdiwI")
    print(id.video_transcript())