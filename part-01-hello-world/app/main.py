from fastapi import FastAPI, APIRouter


app = FastAPI(title="Book Store API", openapi_url="/openapi.json")

api_router = APIRouter()


@app.get("/", status_code=200)
def root():
    return {"message": "Hello, World!"}