#importamos la libreria y su clase FastAPI
from fastapi import FastAPI
#instanciamos la clase
app=FastAPI()

#direciones a donde puede acceder el cliente
@app.get("/")
def main():
  return {"mensaje":"esta es una pedicion get al servidor"}

@app.get("/modulos")
def modulos():
  return {"mensaje":"esta es una pedicion get al servidor"}

@app.put("/user/update")
def update_user(q:str=None):
  if q:
    return {q:"se ejecuto"}
  return {"mensaje":"no tengo ninguna query"}