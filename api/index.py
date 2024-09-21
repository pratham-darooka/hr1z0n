from fastapi import FastAPI, APIRouter

app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")
api_router = APIRouter(prefix="/api/py")

@api_router.get("/ping", tags=["Health Check"])
def ping():
    return {"status": "success", "message": "this works!"}

app.include_router(api_router)