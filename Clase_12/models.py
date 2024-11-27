class Avisos:
    def __init__(self):
    
        self.avisos = [
            {"id": 1, "titulo":"Aviso 1", "contenido":"Hola mundo" },
            {"id": 2,  "titulo": "Aviso 2", "contenido": "Lorem ipsum asdasd"  },
            {"id": 3, "titulo":"Aviso 3", "contenido": "Contenido 3"}
        ]
    
    def all(self):
        return self.avisos
