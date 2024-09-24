from dotenv import load_dotenv
load_dotenv()
import time
from langchain.chains.summarize import load_summarize_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import YoutubeLoader
from tenacity import retry, stop_after_attempt, wait_fixed 

@retry(stop=stop_after_attempt(3), wait=wait_fixed(60))
def get_video_summary(video_url):
    loader = YoutubeLoader.from_youtube_url(
        video_url, 
        add_video_info=True,
        language=["en", "hi"],
        chunk_size_seconds=1200
    )

    docs = loader.load()

    llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-1.5-flash-latest")

    # Using Stuff
    chain = load_summarize_chain(llm, chain_type="stuff")
    # chain = load_summarize_chain(llm, chain_type="map_reduce")
    # chain = load_summarize_chain(llm, chain_type="refine")
    result = chain.invoke(docs)
    return result["output_text"]

if __name__ == "__main__":
    video_url = input("Enter video url: ")
    print(get_video_summary(video_url))