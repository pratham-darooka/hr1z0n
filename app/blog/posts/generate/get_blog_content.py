from dotenv import load_dotenv
load_dotenv()
import os
from langchain.chains.summarize import load_summarize_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import YoutubeLoader
from tenacity import retry, stop_after_attempt, wait_fixed 

def get_video_transcript(video_url):
    return YoutubeLoader.from_youtube_url(video_url).load()

@retry(stop=stop_after_attempt(3), wait=wait_fixed(60))
def get_video_summary(video_url):
    fn = f"docs_{video_url.split('=')[-1]}"
    if not os.path.exists(f"app/blog/posts/generate/cache/{fn}.txt"):
        try:
            loader = YoutubeLoader.from_youtube_url(
                video_url, 
                add_video_info=True,
                language=["en", "hi"],
                translation="en",
                chunk_size_seconds=1200
            )

            docs = loader.load()
            # save docs to disk
            if not os.path.exists("app/blog/posts/generate/cache"): 
                os.mkdir("app/blog/posts/generate/cache")
            
            print("saving!")
            with open(f"app/blog/posts/generate/cache/{fn}.txt", "w+") as f:
                for d in docs:
                    f.write(d.page_content)
            print("saved!")

            llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-1.5-flash-latest")

            # Using Stuff
            chain = load_summarize_chain(llm, chain_type="stuff")
            # chain = load_summarize_chain(llm, chain_type="map_reduce")
            # chain = load_summarize_chain(llm, chain_type="refine")
            result = chain.invoke(docs)
            with open(f"app/blog/posts/generate/cache/{fn}_summary.txt", "w+") as f:
                f.write(result["output_text"])
                f.write("\n")
            print("saved summary!")
            return result["output_text"]
        except Exception as e:
            print(e)
            raise SystemError("Error getting video summary")
    else:
        pass
        # use langchain text loader to load the file and save the summary

if __name__ == "__main__":
    pass
    # video_url = input("Enter video url: ")
    # print(get_video_summary(video_url))
    # print(get_video_transcript(video_url))