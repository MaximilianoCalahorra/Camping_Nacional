from Persona import Persona
from Recreo import Recreo
from Campamento import Campamento

#Clase CampingNacional:
class CampingNacional:
    #Constructor:
    def __init__(self):
        self.__lst_personas = []
        self.__lst_servicios = []
    
    #Getters:
    def get_lst_personas(self):
        return self.__lst_personas
    
    def get_lst_servicios(self):
        return self.__lst_servicios
    
    #__str__:
    def __str__(self):
        titulo = "Camping Nacional:\n"
        personas = "Personas:\n"
        for persona in self.__lst_personas:
            personas += persona.__str__()
        servicios = "Servicios:\n"
        for servicio in self.__lst_servicios:
            servicio += servicio.__str__()
        return titulo + personas + servicios
    
    #Métodos:
    #CU 1:
    def traer_persona(self, dni):
        persona_auxiliar = None
        persona_buscada = None
        i = 0
        while persona_buscada == None and i < len(self.__lst_personas):
            persona_auxiliar = self.__lst_personas[i]
            if persona_auxiliar.get_dni() == dni:
                persona_buscada = persona_auxiliar
            i += 1
        return persona_buscada
    
    #CU 2:
    def agregar_persona(self, apellido, nombre, dni):
        if self.traer_persona(dni) != None:
            raise Exception(f"Error! Ya existe una persona con el DNI #{dni} en la lista de personas.")
        id = 1
        if len(self.__lst_personas) > 0:
            tamanio = len(self.__lst_personas)
            id = self.__lst_personas[tamanio - 1].get_id_persona() + 1
        return self.__lst_personas.append(Persona(id, apellido, nombre, dni))
    
    #CU 4:
    def agregar_recreo(self, cod_ingreso, fecha_ingreso, check_out, responsable, cant_personas, precio_persona):
        id = 1
        if len(self.__lst_servicios) > 0:
            tamanio = len(self.__lst_servicios)
            id = self.__lst_servicios[tamanio - 1].get_id_servicio() + 1
        return self.__lst_servicios.append(Recreo(id, cod_ingreso, fecha_ingreso, check_out, responsable, cant_personas, precio_persona))
    
    #CU 5:
    def agregar_campamento(self, cod_ingreso, fecha_ingreso, check_out, responsable, fecha_egreso, cant_carpas, precio_carpa):
        id = 1
        if len(self.__lst_servicios) > 0:
            tamanio = len(self.__lst_servicios)
            id = self.__lst_servicios[tamanio - 1].get_id_servicio() + 1
        return self.__lst_servicios.append(Campamento(id, cod_ingreso, fecha_ingreso, check_out, responsable, fecha_egreso, cant_carpas, precio_carpa))
    
    #CU 8:
    def traer_servicios_por_precio_final(self, mayor_igual_a):
        servicios_que_cumplen = []
        for servicio in self.__lst_servicios:
            if servicio.calcular_precio_final() >= mayor_igual_a and servicio.get_check_out():
                servicios_que_cumplen.append(servicio)
        return servicios_que_cumplen
    
    #CU 9:
    def traer_campamentos_por_dias(self, mayor_igual_a):
        campamentos_que_cumplen = []
        for servicio in self.__lst_servicios:
            if isinstance(servicio, Campamento):
                if servicio.cantidad_dias() >= mayor_igual_a:
                    campamentos_que_cumplen.append(servicio)
        return campamentos_que_cumplen