from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "rutwik"}

@app.get('/jay')
def callJay():
    return {"Name":"Jayansh"}

@app.get('/love')
def calllove():
    return('hi')
@app.put('/name')
def callname():
    x = input("What is your name?")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)   
