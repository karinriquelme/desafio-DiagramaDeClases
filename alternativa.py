


class Alternativa:
    def __init__(self,contenido:str,ayuda:str) -> None:
        self.contenido=contenido
        self.ayuda=ayuda
    
    def mostrar_una_alternativa(self):
        print("contenido:",self.contenido)
        if self.ayuda:
            print("Ayuda: ",self.ayuda)