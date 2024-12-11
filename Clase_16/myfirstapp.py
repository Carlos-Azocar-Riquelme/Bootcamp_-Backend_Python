# uvicorn myfirstapp:app –-host 127.0.0.1 –-port 8000 --reload

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/{name}/{autor}/{date}")
def read_root(name: str, autor: str, date : str):
    # if len(name) < 3 or len(lastname) < 3:
    #     raise HTTPException(status_code=400, detail="Hey! I was supposed tosee your name!")
    html_response = """
    <html>
        <title>Hello</title>
        <body>
            <p>Nombre del libro, {name} </p>
            <p>Autor del libro, {autor}!</p>
            <p>Fecha de publicación, {date}!</p>
        </body>
    </html>
""".format(name=name, autor=autor, date=date)
        
    return HTMLResponse(html_response, status_code=200)



@app.get("/json/{name}/{autor}/{date}")
def read_root_json(name: str, autor: str, date : str):
    # if len(name) < 3 or len(lastname) < 3:
    #     raise HTTPException(status_code=400, detail="Hey! I was supposed tosee your name!")
    
        
    return {"name" : name ,"autor": autor, "date":date}


class Profile(BaseModel):
 name: str
 date_init: int
 date_last: int


 libros = [
    {
        "nombre": "Don Quijote de la Mancha",
        "fecha_inicial": 1605,
        "fecha_final": 1615
    },
    {
        "nombre": "Cien años de soledad", 
        "fecha_inicial": 1967,
        "fecha_final": 1967
    },
    {
        "nombre": "El Señor de los Anillos",
        "fecha_inicial": 1954,
        "fecha_final": 1955
    },
    {
        "nombre": "Harry Potter y la Piedra Filosofal",
        "fecha_inicial": 1997,
        "fecha_final": 1997
    },
    {
        "nombre": "El Principito",
        "fecha_inicial": 1943,
        "fecha_final": 1943
    },
    {
        "nombre": "1984",
        "fecha_inicial": 1949,
        "fecha_final": 1949
    },
    {
        "nombre": "La Divina Comedia",
        "fecha_inicial": 1304,
        "fecha_final": 1321
    },
    {
        "nombre": "Orgullo y Prejuicio",
        "fecha_inicial": 1813,
        "fecha_final": 1813
    },
    {
        "nombre": "El Código Da Vinci",
        "fecha_inicial": 2003,
        "fecha_final": 2003
    }
    ]




@app.post("/books/search/{date}")
def find_book(profile: Profile):
   
    for libro in libros:
        if (libro['fecha_inicial'] < date & libro['fecha_final'] > date):
            return libro
    
    return {"name": profile.name, "Fecha inicial de publicación": profile.date_init, "Fecha final de publicación": profile.date_last}