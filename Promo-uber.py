promo = input("¿Te gustaria ganar un cupon de descuento en Uber?")

if promo == si:
            print("Este asistente te ayudara a sacar el costo promedio de tus ultimos 3 viajes")
else:
            print("Gracias, podes volver cuando quieras")

nombre = input("Por favor, ingresa tu nombre: ")
viaje_uno = int(input("Hola " + nombre + ", introduce el costo de tu primer viaje: "))
viaje_dos = int(input("perfecto " + nombre + ", ahora introduce el valor de tu segundo viaje: "))
viaje_tres = int(input("por ultimo, introduce el valor del tercer viaje: "))
total = (viaje_uno + viaje_dos + viaje_tres) / 3
print("El monto promedio de tus viajes es: ", total)


if total >= 700:
          print("Felicidades, ganaste un cupon de $200")
else:
    print("Lo sentimos, para ganar un cupon, tus ultimos 3 viajes deben superar $700") 