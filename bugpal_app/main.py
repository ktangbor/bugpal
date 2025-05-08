from fastapi import FastAPI

from bugpal_app.routers import health

app = FastAPI(title="BugPal")
app.include_router(health.router)


@app.get("/")
def root():
    return {"message": "Welcome to BugPal!"}
