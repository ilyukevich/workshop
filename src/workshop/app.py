from fastapi import FastAPI

from .api import router

app = FastAPI()
app.include_router(router)

#
# @app.get('/')
# def root():
#     return {'message': 'Hello!'}


# @app.get("/{name}")
# def item(name: str):
#     return {"name": f'HELLO, {name} !',
#             'user': name}
