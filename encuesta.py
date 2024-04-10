from pregunta import Pregunta
from listado_respuestas import ListadoDeRespuesta
from typing import List

class Encuesta:
    def __init__(self,nombre:str,preguntas:List[dict]) -> None:
        
        self.nombre=nombre
        self.__preguntas=[Pregunta(p["enunciado"],
                                            p["ayuda"],
                                            p["alternativas"],
                                            p["requerido"])for p in preguntas]
        self.__listado_de_respuestas=[]
    
    
        
    @property
    def listado_De_preguntas(self):
        return self.__preguntas
    
    @property
    def listado_de_respuestas(self):
        return self.__listado_de_respuestas
    
    def mostrar_encuesta(self):
        print(self.nombre)
        for p in self.__preguntas:
            p.mostrar_preguntas()
    
    
        
    def agregar_listado_de_respuesta(self,listado_respuesta):
        self.listado_de_respuestas.append(listado_respuesta)
        
    
class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, edad_minima,edad_maxima,nombre, pregunta) -> None:
        self.__edad_minima=edad_minima
        self.__edad_maxima=edad_maxima
        super().__init__(nombre, pregunta)
        
    @property
    def edad_minima(self):
        return self.__edad_minima
    
    @property
    def edad_maxima(self):
        return self.__edad_maxima
    
    @edad_minima.setter
    def edad_minima(self, edad_minima):
        self.__edad_minima=edad_minima
    
    @edad_maxima.setter
    def edad_maxima(self, edad_maxima):
        self.__edad_maxima=edad_maxima
    
    
    def agregar_respuesta(self,respuestas:ListadoDeRespuesta):    #agregacion
        if self.__edad_minima <= respuestas.usuario.edad <=self.__edad_maxima:
            super().agregar_listado_de_respuesta(respuestas)
            
    
class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, regiones:list,nombre,preguntas) -> None:
        self.__regiones=regiones
        super().__init__(nombre, preguntas)
        
    @property
    def regiones(self):
        return self.__regiones
    
    @regiones.setter
    def regiones(self,regiones):
        self.__regiones=regiones
        
    def agregar_respuesta(self,respuestas:ListadoDeRespuesta):
        if respuestas.usuario.region in self.__regiones:
            super().agregar_listado_de_respuesta(respuestas)
        
    