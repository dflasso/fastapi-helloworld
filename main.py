#  Dependencias.
from typing import Dict
from fastapi import FastAPI

#  Instancia de la clase.
app:FastAPI = FastAPI()

#  Path Operator Decoration.
@app.get("/")
def home() -> Dict:
   #  Return JSON.
   return {"Message": "Hello World"}