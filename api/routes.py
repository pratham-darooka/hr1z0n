from fastapi import FastAPI, APIRouter
# from app.blog.posts.generate import generate

app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")
api_router = APIRouter(prefix="/api/py")

@api_router.get("/ping", tags=["Health Check"])
def ping():
    return {"message": "this works!"}

# @api_router.post("/generate", tags=["Blog Posts"])
# def generate(topic: str, requirements: str, directory: str = generate.BLOG_POST_DIRECTORY):
#     return {"blog":generate.create_blog(topic, requirements, directory)}

app.include_router(api_router)