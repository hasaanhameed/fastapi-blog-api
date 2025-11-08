from fastapi import FastAPI


app = FastAPI() #Creating an instance of fastAPI
# To run server: uvicorn main:app --reload

#Use fastapi instance as decorator 
@app.get('/')
def index(): 
    return {'data' : {'name' : 'Hasaan'}}