# python app/blog/posts/generate/generate.py
from icecream import ic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import glob
import os
from dotenv import load_dotenv
load_dotenv()

BLOG_POST_DIRECTORY = 'app/blog/posts'

TOPIC = input("Enter topic: ")
REQUIREMENTS = input("Enter additional requirements: ")

################################################################################
# Read Existing Blog Posts
def create_blog_examples(directory):
    blog_posts = ic(glob.glob(f"{directory}/*.mdx"))
    example_blog = ""
    for i, post_path in enumerate(blog_posts[:5]):
        example_blog += f"# Example Blog Post {i+1}\n\n"
        with open(post_path, "r") as f:
            example_blog += f.read()
        example_blog += "\n\n\n################\n\n\n"
    return example_blog
################################################################################

################################################################################
# Create a blog post
def create_blog(topic, requirements, directory):
    llm = ChatGoogleGenerativeAI(
            model='gemini-1.5-flash',
            # model='gemini-1.5-pro-exp-0801',
            api_key=os.environ['GOOGLE_API_KEY'], 
            temperature=0,
        )

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", """Act like an expert blogger and marketer. Given a topic, I want you to create a blog post article in markdown format. \
You will use relatable language for gen z, avoid long boring paragraphs, make the blog engaging. give personal examples wherever possible. \
You will match the tone, format and writing style (all lower cases unless emphasis) of the example blogs. \
Please follow a blog format, use --- separators, headings, add a tldr. Do not avoid the metadata. Feel free to make the summary clickbait.         
{example_blog}"""),
        ("user", "{topic}\nAdditional Requirements for blog: {requirements}"),
    ])
    input_dict = {
        "example_blog": create_blog_examples(directory),
        "topic": topic,
        "requirements": requirements
    }
    return llm.invoke(prompt_template.invoke(input_dict)).content
################################################################################