from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router
from database.connection import Settings
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


@app.on_event("startup")
async def startup_db_client():
    settings = Settings()
    await settings.initialize_database()


app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


#A another way to run the app
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
