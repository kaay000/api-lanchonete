from fastapi import FastAPI

from api.routes.pedidos import router

app = FastAPI()

app.include_router(router)
