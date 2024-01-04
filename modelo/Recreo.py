from Servicio import Servicio

#Clase Recreo:
class Recreo(Servicio):
    #Constructor:
    def __init__(self, id_servicio, cod_ingreso, fecha_ingreso, check_out, responsable, cant_personas, precio_persona):
        super().__init__(id_servicio, cod_ingreso, fecha_ingreso, check_out, responsable)
        self.__cant_personas = cant_personas
        self.__precio_persona = precio_persona
        
    #Getters:
    def get_cant_personas(self):
        return self.__cant_personas
    
    def get_precio_persona(self):
        return self.__precio_persona
    
    #Setters:
    def set_cant_personas(self, nueva_cant_personas):
        self.__cant_personas = nueva_cant_personas
        
    def set_precio_persona(self, nuevo_precio_persona):
        self.__precio_persona = nuevo_precio_persona
        
    #__str__:
    def __str__(self):
        titulo = "Recreo:\n"
        cant_personas = f"Cantidad de personas: {self.__cant_personas}\n"
        precio_persona = f"Precio por persona: ${self.__precio_persona}\n"
        return titulo + super().__str__() + cant_personas + precio_persona
    
    #Métodos:
    #CU 7:
    def calcular_precio_final(self):
        return self.__cant_personas * self.__precio_persona