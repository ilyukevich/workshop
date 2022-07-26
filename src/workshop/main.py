from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {'message': 'Hello!'}


@app.get("/{name}")
def read_item(name: str):
    return {"name": f'HELLO, {name} !',
            'user': name}
