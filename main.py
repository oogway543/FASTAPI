from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return{"item_id": item_id}

#query parameter
@app.get_("/raspberry/")
async def read_item(time:datetime = datetime.now(),light: flat = 0.0, temerature: flat = 0.0):
    return{
        "時間":time,
        "光線":light,
        "溫度":temperature
    }

