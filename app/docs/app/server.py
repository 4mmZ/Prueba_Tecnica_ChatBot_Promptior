from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from chatbot import chain

from dotenv import load_dotenv
load_dotenv()
app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/chat_bot/playground")


# Edit this to add the chain you want to add
add_routes(app, chain, path="/chat_bot")



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)