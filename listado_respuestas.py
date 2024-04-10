from usuario import Usuario



class ListadoDeRespuesta:
    def __init__(self, usuario: Usuario,respuesta) -> None:
        self.__usuario = Usuario
        self.__respuesta=respuesta
    
        
        
    @property
    def respuesta(self):
        return self.__respuesta
    
    @property
    def usuario(self):
        return self.__usuario