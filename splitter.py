from langchain.text_splitter import RecursiveCharacterTextSplitter
from transcript import Transcript


class transcript_splitter:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 100):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size = chunk_size,
            chunk_overlap=chunk_overlap
        )
        
    def split(self, transcript: str) -> list[dict]:
        return self.splitter.create_documents([transcript])



if __name__ =="__main__":
    ts = transcript_splitter()
    transcript1 = Transcript("https://youtu.be/LPZh9BOjkQs?si=lBZRUXVSOVKCdiwI")

    print(ts.split(transcript1.video_transcript()))
    