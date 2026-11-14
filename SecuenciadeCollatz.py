LIMITE = 1_000_000

def collatz_mas_larga(limite):
    # longitudes[i] = cantidad de términos de la cadena que empieza en i
    longitudes = [0] * limite
    longitudes[1] = 1

    mejor_inicio, mejor_longitud = 1, 1

    for inicio in range(2, limite):
        n = inicio
        pasos = 0

        
        while n >= limite or longitudes[n] == 0:
            n = n // 2 if n % 2 == 0 else 3 * n + 1
            pasos += 1

        total = pasos + longitudes[n]
        longitudes[inicio] = total

        if total > mejor_longitud:
            mejor_inicio, mejor_longitud = inicio, total

    return mejor_inicio, mejor_longitud


if __name__ == "__main__":
    inicio, longitud = collatz_mas_larga(LIMITE)
    print(f"Número inicial: {inicio}")
    print(f"Términos en la cadena: {longitud}")