from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="My FastAPI App",
    description="A simple FastAPI server deployed on DigitalOcean",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"Hello from FastAPI developed by Manjari Bisht on DigitalOcean for Enterprise Software Class, Wohooo!! Project launched!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}


@app.post("/echo")
async def echo(body: dict):
    return {"you_sent": body}
