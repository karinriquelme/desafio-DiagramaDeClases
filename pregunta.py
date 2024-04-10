# from alternativa import Alternativa


class Pregunta:
    def __init__(self,enunciado, alternativas,ayuda=None, si_es_requerida=False) -> None:
        self.enunciado=enunciado
        self.ayuda=ayuda
        self.si_es_requerida=si_es_requerida
        self.__alternativas=alternativas
    
    @property
    def alternativas(self):
        return self.__alternativas
    
    def mostrar_preguntas(self):
        print(f"Este es el enunciado de la pregunta {self.enunciado}")
        print(f"si es requerida: {'sí'if self.si_es_requerida==True else 'no'}")
        if self.ayuda:
            print("Ayuda: ",self.ayuda)
        print("sus alternativas son:")
        for alt in self.__alternativas:
            alt.mostrar_una_alternativa()
        