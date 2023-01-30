from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/hello")
def root():
    return {"message": "Hello World1"}

lambda_handler = Mangum(app)