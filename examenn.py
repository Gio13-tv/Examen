class Empleado:
    def __init__(self, rfc, apellidos, nombres):
        self.rfc = rfc    
        self.apellidos = apellidos       
        self.nombres = nombres 

    def mostrar_informacion(self):
        return f"RFC: {self.rfc}, Nombre: {self.nombres}, Apellidos: {self.apellidos}"

class EmpleadoVendedor(Empleado):
    def __init__(self,  rfc, apellidos, nombres, monto_vendido, tasa_comision):
        super().__init__(rfc, apellidos, nombres)
        self.monto_vendido = monto_vendido    
        self.tasa_comision = tasa_comision  

    def calcular_ingresos(self):
        return self.monto_vendido * self.tasa_comision

    def calcular_bonificacion(self):
        ingresos = self.calcular_ingresos()
        if self.monto_vendido < 1000:
            print("No hay bonificacion :(")
        elif self.monto_vendido <= 5000:
            return ingresos * 0.05
        else:
            return ingresos * 0.10
        
    def calcular_descuento(self):
        ingresos = self.calcular_ingresos()
        if ingresos < 1000:
            return ingresos * 0.11
        else:
            return ingresos * 0.15
        
    def calcular_sueldo_neto(self):
        ingresos = self.calcular_ingresos()
        bonificacion = self.calcular_bonificacion()
        descuento = self.calcular_descuento()
        return ingresos + bonificacion - descuento

class EmpleadoPermanente(Empleado):
    def __init__(self, rfc, apellidos, nombres, sueldo_base, nss):
        super().__init__(rfc, apellidos, nombres)
        self.sueldo_base = sueldo_base
        self.nss = nss

    def ingresos(self):
        return self.sueldo_base

    def calcular_descuento(self):
        return self.sueldo_base * 0.11

    def calcular_sueldo_neto(self):
        return self.ingresos() - self.calcular_descuento()
    
print("empleado_g4")
empleado = EmpleadoVendedor("GAGG060531MMCRRVA4", "García", "Giovanna", 1000, 0.10)
print(empleado.mostrar_informacion())
print(f"Ingresos: {empleado.calcular_ingresos()}")
print(f"Bonificación: {empleado.calcular_bonificacion()}")
print(f"Descuento: {empleado.calcular_descuento()}")
print(f"Sueldo neto: {empleado.calcular_sueldo_neto()}")
