def calcular_costo_total(frutas):
    costo_total = 0
    for fruta in frutas:
        costo_total += fruta['precio'] * fruta['cantidad']
    return costo_total

def mostrar_frutas_ordenadas(frutas):
    frutas_ordenadas = sorted(frutas, key=lambda x: x['precio'], reverse=True)
    for fruta in frutas_ordenadas:
        print(f"{fruta['nombre']}: ${fruta['precio']:.2f}")

def mostrar_fruta_mas_barata(frutas):
    fruta_mas_barata = min(frutas, key=lambda x: x['precio'])
    print(f"La fruta más barata es {fruta_mas_barata['nombre']} con un precio de ${fruta_mas_barata['precio']:.2f}")

def main():
    N = int(input("Ingrese la cantidad de frutas para el salpicón: "))
    frutas = []

    for i in range(N):
        id_fruta = i + 1
        nombre = input(f"Ingrese el nombre de la fruta {id_fruta}: ")
        precio = float(input(f"Ingrese el precio de la fruta {nombre}: "))
        cantidad = int(input(f"Ingrese la cantidad de {nombre} que desea agregar: "))

        fruta = {'id': id_fruta, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        frutas.append(fruta)

    costo_total = calcular_costo_total(frutas)
    print(f"\nEl costo total del salpicón es: ${costo_total:.2f}\n")

    print("Frutas ordenadas de mayor a menor costo:")
    mostrar_frutas_ordenadas(frutas)
    print()

    print("Información de la fruta más barata:")
    mostrar_fruta_mas_barata(frutas)

if __name__ == "__main__":
    main()