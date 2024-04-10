from encuesta import Encuesta,EncuestaLimitadaEdad,EncuestaLimitadaRegion
from listado_respuestas import ListadoDeRespuesta
from typing import Union



class Usuario:
    def __init__(self, correo, edad, region):
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    @property
    def correo(self):
        return self.__correo
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def region(self):
        return self.__region
    
    @correo.setter
    def correo(self,correo):
        self.__correo=correo
        
    @edad.setter
    def edad(self, edad):
        self.__edad=edad
        
    @region.setter
    def region(self,region):
        self.__region=region
    
    def contestar_encuesta(self,encuesta:Union[Encuesta,EncuestaLimitadaEdad,EncuestaLimitadaRegion],respuestas:list):
        encuesta.agregar_respuesta(ListadoDeRespuesta(self.__correo, respuestas))
        
u=Usuario("correo@correo.cl",22,5)
u.contestar_encuesta("hola",[1,2,3])