class Empleado:
    def __init__(self, rfc, apellidos, nombres):
        self.rfc = rfc    
        self.apellidos = apellidos       
        self.nombres = nombres 


class EmpleadoVendedor:
    def __init__(self, monto_vendido, tasa_comision):
        self.monto_vendido = monto_vendido    
        self.tasa_comision = tasa_comision  

    def calcular_ingresos(self, tasa_comision):
        self.monto_vendido *= tasa_comision 

    def bonificacion(self, monto_vendido):
        if monto_vendido <= 1000:
            print("No hay bonificacion")
        else:

    
