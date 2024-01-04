from Servicio import Servicio

#Clase Campamento:
class Campamento(Servicio):
    #Constructor:
    def __init__(self, id_servicio, cod_ingreso, fecha_ingreso, check_out, responsable, fecha_egreso, cant_carpas, precio_carpa):
        super().__init__(id_servicio, cod_ingreso, fecha_ingreso, check_out, responsable)
        self.__fecha_egreso = fecha_egreso
        self.__cant_carpas = cant_carpas
        self.__precio_carpa = precio_carpa
        
    #Getters:
    def get_fecha_egreso(self):
        return self.__fecha_egreso
    
    def get_cant_carpas(self):
        return self.__cant_carpas
    
    def get_precio_carpa(self):
        return self.__precio_carpa
    
    #Setters:
    def set_fecha_egreso(self, nueva_fecha_egreso):
        self.__fecha_egreso = nueva_fecha_egreso
        
    def set_cant_carpas(self, nueva_cant_carpas):
        self.__cant_carpas = nueva_cant_carpas
        
    def set_precio_carpa(self, nuevo_precio_carpa):
        self.__precio_carpa = nuevo_precio_carpa
        
    #__str__:
    def __str__(self):
        titulo = "Campamento:\n"
        fecha_egreso = f"Fecha de egreso: {self.__fecha_egreso}\n"
        cant_carpas = f"Cantidad de carpas: {self.__cant_carpas}\n"
        precio_carpa = f"Precio por carpa: ${self.__precio_carpa}\n"
        return titulo + super().__str__() + fecha_egreso + cant_carpas + precio_carpa
    
    #Métodos:
    #CU 6:
    def cantidad_dias(self):
        return (self.__fecha_egreso - super().get_fecha_ingreso()).days
    
    #CU 7:
    def calcular_precio_final(self):
        return self.__cant_carpas * self.__precio_carpa * self.cantidad_dias()