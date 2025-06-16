from fastapi import FastAPI

from bugpal_app.api.v1.routes import users, health

app = FastAPI(title="BugPal")
app.include_router(health.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "Welcome to BugPal!"}
