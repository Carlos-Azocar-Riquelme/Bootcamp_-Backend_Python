class Pago:
    def __init__(self, tarjeta):
        self.tarjeta = tarjeta

    def autoriza_pago(self, nombre):
        if self.tarjeta.get_nombre() == nombre:
            return True
        else:
            return False

class ProductoBancario:
    def __init__(self, p_id):
        self.p_id = p_id

class TarjetaCredito(ProductoBancario):
    def __init__(self, nombre, fecha_vto, numero, codigo):
        super().__init__("122")
        self.nombre = nombre
        self.fecha_vto = fecha_vto
        self.numero = numero
        self.codigo = codigo

    def get_numero(self):
        return self.numero

    def get_nombre(self):
        return self.nombre

    def check_codigo(self, codigo):
        if self.codigo == codigo:
            return True
        else:
            return False

tarjeta_natalia = TarjetaCredito("Natalia", "09/25", "41909839876546738", "789")
print(tarjeta_natalia.get_nombre())

pago_compra_a = Pago(tarjeta_natalia)
print(pago_compra_a.autoriza_pago("Natalia"))