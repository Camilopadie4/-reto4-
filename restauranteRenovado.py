class Menu:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def calcular_precio(self):
        return self.precio

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} : ${self.precio}"


class Bebidas(Menu):
    def __init__(self, nombre: str, precio: float, tamaño: str):
        super().__init__(nombre, precio)
        self.tamaño = tamaño

    def get_tamaño(self):
        return self.tamaño

    def set_tamaño(self, tamaño: str):
        self.tamaño = tamaño

    def calcular_precio(self, descuento=False):
        if descuento:
            return self.precio * 0.85  
        return self.precio

    def __str__(self):
        return f"{self.nombre} {self.tamaño} : ${self.precio}"


class Aperitivo(Menu):
    def __init__(self, nombre: str, precio: float):
        super().__init__(nombre, precio)

    def __str__(self):
        return f"{self.nombre} : ${self.precio}"


class Plato_principal(Menu):
    def __init__(self, nombre: str, precio: float, cantidad: str):
        super().__init__(nombre, precio)
        self.cantidad = cantidad

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad: str):
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} Porc:{self.cantidad} = ${self.precio}"


class Orden:
    def __init__(self):
        self.elementos = []

    def agregar_elemento(self, elemento: Menu):
        self.elementos.append(elemento)

    def calcular_factura(self):
        hay_plato = any(isinstance(e, Plato_principal) for e in self.elementos)
        total = 0
        for e in self.elementos:
            if isinstance(e, Bebidas):
                total += e.calcular_precio(descuento=hay_plato)
            else:
                total += e.calcular_precio()
        return round(total, 2)

    def hacer_descuento(self):
        platos_principales = sum(1 for e in self.elementos if isinstance(e, Plato_principal))
        if platos_principales >= 3:
            return round(self.calcular_factura() * 0.9, 2)
        return self.calcular_factura()

    def mostrar_pedido(self):
        print("Orden y resumen de pago:")
        for e in self.elementos:
            print(f"{e}")
        print(f"Total: ${self.calcular_factura()}")
        print(f"Total con descuento: ${self.hacer_descuento()}")


class MedioPago:
    def __init__(self):
        pass

    def pagar(self, monto):
        raise NotImplementedError("Subclases deben implementar pagar()")


class Tarjeta(MedioPago):
    def __init__(self, numero, cvv):
        super().__init__()
        self.numero = numero
        self.cvv = cvv

    def pagar(self, monto):
        print(f"Pagando ${monto} con tarjeta terminada en {self.numero[-4:]}")


class Efectivo(MedioPago):
    def __init__(self, monto_entregado):
        super().__init__()
        self.monto_entregado = monto_entregado

    def pagar(self, monto):
        if self.monto_entregado >= monto:
            cambio = self.monto_entregado - monto
            print(f"Pago realizado en efectivo. Cambio: ${round(cambio, 2)}")
        else:
            faltante = monto - self.monto_entregado
            print(f"Fondos insuficientes. Faltan ${round(faltante, 2)} para completar el pago.")


class Pago:
    def __init__(self, orden: Orden, metodo_pago: MedioPago):
        self.orden = orden
        self.metodo_pago = metodo_pago

    def procesar_pago(self):
        total = self.orden.hacer_descuento()
        print("\nProcesando pago...")
        self.metodo_pago.pagar(total)
