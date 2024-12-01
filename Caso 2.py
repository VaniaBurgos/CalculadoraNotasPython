class Notas:
    def __init__(self):
        self.notas = None
        self.nota1 = []

    def agregar_notas(self, cantidad):
        import numpy
        notas= numpy.array([])
        for i in range(cantidad):
            while True:
                try:
                    nota= float (input("Ingrese las notas: ["+str (cantidad)+"]: "))
                    if 0<= nota <= 7.0:
                        self.nota1.append(nota)
                        print(notas)
                        break
                    else:
                        print("Nota inválida, intente nuevamente.")
                except ValueError:
                        print("Nota inválida, debe ingresar un número.")
    def promedio(self):
        if not self.nota1:
            return None
        return round (sum(self.nota1) / len(self.nota1),1)

    def nota_mas_alta(self):
        if not self.nota1:
            return None
        return round (max(self.nota1),1)

    def nota_mas_baja(self):
        if not self.nota1:
            return None
        return round (min(self.nota1),1)

    def opciones(self):
        print("1 Obtener el promedio")
        print("2 Obtener la nota más alta")
        print("3 Obtener la nota más baja")
        print("4 Salir")

    def ejecutar(self):
        while True:
           self.opciones()
           opcion = input("¿Qué operación desea realizar? ")
           if opcion== "1":
              promedio = self.promedio()
              if promedio is not None:
                 print(f"El promedio obtenido es: {promedio:.1f}")
              else:
                 print("No se puede calcular el promedio.")
           elif opcion =="2":
              nota_mas_alta = self.nota_mas_alta()
              if nota_mas_alta is not None:
                 print(f"La nota más alta es {nota_mas_alta:.1f}")
              else:
                 print("No se puede calcular la nota más alta")

           elif opcion =="3":
              nota_mas_baja = self.nota_mas_baja()
              if nota_mas_baja is not None:
                 print(f"La nota más baja es {nota_mas_baja:.1f}")
              else:
                 print("No se puede calcular la nota más baja.")

           elif opcion =="4":
                print("Hasta pronto.")
                break

           else:
                print("Debe escoger una opción válida.")

class Datos:
    def __init__(self):
        self.gestion= Notas()

if __name__ == "__main__":
    datos=Datos()
    cantidad_notas= int(input("Ingrese la cantidad de notas con las cuales obtendrá el promedio: "))
    datos.gestion.agregar_notas(cantidad_notas)
    datos.gestion.ejecutar()
