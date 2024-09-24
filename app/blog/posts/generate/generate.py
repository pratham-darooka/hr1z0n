# python app/blog/posts/generate/generate.py
from icecream import ic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from get_blog_content import get_video_summary
import glob
import time
import os
from dotenv import load_dotenv
load_dotenv()

BLOG_POST_DIRECTORY = 'app/blog/posts'
YT_LINKS_FILE = 'app/blog/posts/generate/youtube_links.txt' 

TOPIC = input("Enter topic: ")
REQUIREMENTS = input("Enter additional requirements: ")

################################################################################
# Read Existing Blog Posts
def create_blog_examples(directory):
    blog_posts = glob.glob(f"{directory}/*.mdx")
    example_blog = ""
    for i, post_path in enumerate(blog_posts[:5]):
        example_blog += f"# Example Blog Post {i+1}\n\n"
        with open(post_path, "r") as f:
            example_blog += f.read()
        example_blog += "\n\n\n################\n\n\n"
    return example_blog
################################################################################
def get_yt_links(yt_links_file = YT_LINKS_FILE):
    with open(yt_links_file, "r") as f:
        yt_links = f.read().splitlines()
    return yt_links

def get_yt_summaries(yt_links = get_yt_links()):
    summaries = []
    for yt_link in yt_links:
        video_summary = get_video_summary(yt_link)
        time.sleep(60)
        summaries.append(video_summary)
        print("##########")
        print("Youtube video summary for", yt_link, "is:", video_summary)
        print("##########")
    return summaries
################################################################################
# Create a blog post
def create_blog(topic, requirements, content, blog_post_directory):
    llm = ChatGoogleGenerativeAI(
            model='gemini-1.5-flash',
            # model='gemini-1.5-pro-exp-0801',
            api_key=os.environ['GOOGLE_API_KEY'], 
            temperature=0,
        )

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", """Act like an expert blogger and marketer. \
Given a topic and some content, I want you to create a blog post article in markdown format. \
You will use relatable language for gen z, avoid long boring paragraphs, make the blog engaging. give personal examples wherever possible. \
You will match the tone (don't make it sound very meta), format and writing style (all lower cases unless emphasis) of the example blogs. \
Please follow the example blog's format, use --- separators, headings, add a tldr, lowercases unless you want emphasis. Do not avoid the metadata. Feel free to make the summary clickbait. \
You are allowed to veer off the content provided, but you must not deviate too much from it. You must not mention words like 'videos', 'episodes', etc. \
Title should be short, clickbait, catchy and engaging. You can use the topic as the title. \
You can mention the experts but make me sound very intelligent and that i have watched all their interviews/podcasts to write this blog.\n
{example_blog}"""),
        ("user", "{topic}\nAdditional Requirements for blog: {requirements}\nContent you may use:{content}"),
    ])
    input_dict = {
        "example_blog": create_blog_examples(blog_post_directory),
        "topic": topic,
        "requirements": requirements,
        "content": content,
    }
    return llm.invoke(prompt_template.invoke(input_dict)).content
################################################################################

print(create_blog(TOPIC, REQUIREMENTS, get_yt_summaries(), BLOG_POST_DIRECTORY))