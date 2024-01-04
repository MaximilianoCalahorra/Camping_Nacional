#Clase Persona:
class Persona:
    #Constructor:
    def __init__(self, id_persona, apellido, nombre, dni):
        self.__id_persona = id_persona
        self.__apellido = apellido
        self.__nombre = nombre
        self.__dni = dni
    
    #Getters:
    def get_id_persona(self):
        return self.__id_persona
    
    def get_apellido(self):
        return self.__apellido
    
    def get_nombre(self):
        return self.__nombre
    
    def get_dni(self):
        return self.__dni
    
    #Setters:
    def set_id_persona(self, nuevo_id_persona):
        self.__id_persona = nuevo_id_persona
        
    def set_apellido(self, nuevo_apellido):
        self.__apellido = nuevo_apellido
        
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    def set_dni(self, nuevo_dni):
        self.__dni = nuevo_dni
        
    #__str__:
    def __str__(self):
        titulo = "Persona:\n"
        id = f"ID: #{self.__id_persona}\n"
        apellido = f"Apellido: {self.__apellido}\n"
        nombre = f"Nombre: {self.__nombre}\n"
        dni = f"DNI: #{self.__dni}\n"
        return titulo + id + apellido + nombre + dni