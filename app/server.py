from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from chatbot import chain

app = FastAPI()

""" Re-direcciona la raiz de langserve a el playground de langserve """
@app.get("/")
async def redirect_root_to_playground():
    return RedirectResponse("/chat_bot/playground")

""" Agrega el chatbot como endpoint de la aplicación """
add_routes(app, chain, path="/chat_bot")



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
