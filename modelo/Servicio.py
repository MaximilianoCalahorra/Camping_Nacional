from abc import ABC, abstractclassmethod
import datetime

#Clase Servicio:
class Servicio(ABC):
    #Constructor:
    def __init__(self, id_servicio, cod_ingreso, fecha_ingreso, check_out, responsable):
        self._id_servicio = id_servicio
        self.set_codigo_ingreso(cod_ingreso)
        self._fecha_ingreso = fecha_ingreso
        self._check_out = check_out
        self._responsable = responsable
    
    #Getters:
    def get_id_servicio(self):
        return self._id_servicio
    
    def get_cod_ingreso(self):
        return self._cod_ingreso
    
    def get_fecha_ingreso(self):
        return self._fecha_ingreso
    
    def get_check_out(self):
        return self._check_out
    
    def get_responsable(self):
        return self._responsable
    
    #Setters:
    def set_id_servicio(self, nuevo_id_servicio):
        self._id_servicio = nuevo_id_servicio
        
    def set_codigo_ingreso(self, nuevo_cod_ingreso):
        if not(self.es_valido_digito_control(nuevo_cod_ingreso)):
            raise Exception(f"Error! El código de ingreso #{nuevo_cod_ingreso} no es válido\n")
        self._cod_ingreso = nuevo_cod_ingreso
        
    def set_fecha_ingreso(self, nueva_fecha_ingreso):
        self._fecha_ingreso = nueva_fecha_ingreso
        
    def set_check_out(self, nuevo_check_out):
        self._check_out = nuevo_check_out
        
    def set_responsable(self, nuevo_responsable):
        self._responsable = nuevo_responsable   
    
    #__str__:
    def __str__(self):
        id = f"ID: #{self._id_servicio}\n"
        cod_ingreso = f"Código de ingreso: #{self._cod_ingreso}\n"
        fecha_ingreso = f"Fecha de ingreso: {self._fecha_ingreso}\n"
        check_out = f"Checkout: {self._check_out}\n"
        responsable = f"Responsable: \n{self._responsable}"
        return id + cod_ingreso + fecha_ingreso + check_out + responsable
    
    #Métodos:
    #CU 3:
    def es_valido_digito_control(self, cod_ingreso):
        suma = 0
        for i in range(6):
            suma += int(cod_ingreso[i])
        ultimo_digito = suma % 10
        return ultimo_digito == int(cod_ingreso[6])
    
    #CU 7:
    @abstractclassmethod
    def calcular_precio_final(self):
        pass