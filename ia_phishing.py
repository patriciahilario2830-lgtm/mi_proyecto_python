from urllib.parse import urlparse
import re

def analizar_url(url):

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    partes = urlparse(url)

    dominio = partes.netloc.lower()
    url_minuscula = url.lower()

    riesgo = 0

    razones = []

    if partes.scheme != "https":

        riesgo += 2

        razones.append(
            "La página no utiliza HTTPS."
        )

    if len(url) > 100:

        riesgo += 2

        razones.append(
            "La URL es demasiado larga."
        )

    if "@" in url:

        riesgo += 3

        razones.append(
            "La URL contiene el símbolo @."
        )

    if re.match(
        r"^\d{1,3}(\.\d{1,3}){3}$",
        dominio
    ):

        riesgo += 3

        razones.append(
            "La URL utiliza una dirección IP "
            "en lugar de un dominio."
        )

    cantidad_guiones = url.count("-")

    if cantidad_guiones >= 3:

        riesgo += 2

        razones.append(
            "La URL contiene muchos guiones."
        )

    cantidad_puntos = dominio.count(".")

    if cantidad_puntos >= 3:

        riesgo += 2

        razones.append(
            "La URL tiene una cantidad elevada "
            "de subdominios."
        )

    palabras_sospechosas = [

        "login",
        "verify",
        "verification",
        "account",
        "password",
        "secure",
        "security",
        "update",
        "confirm",
        "bank",
        "signin",
        "authenticate",
        "wallet"
    ]


    palabras_encontradas = []


    for palabra in palabras_sospechosas:

        if palabra in url_minuscula:

            palabras_encontradas.append(palabra)


    if len(palabras_encontradas) > 0:

        riesgo += len(palabras_encontradas)

        razones.append(
            "Contiene palabras relacionadas "
            "con cuentas o verificación: "
            + ", ".join(palabras_encontradas)
        )

    cantidad_numeros = sum(
        caracter.isdigit()
        for caracter in url
    )


    if cantidad_numeros >= 8:

        riesgo += 2

        razones.append(
            "La URL contiene una cantidad "
            "elevada de números."
        )

    if riesgo >= 7:

        nivel = "ALTO"
        resultado = "⚠️ POSIBLE PHISHING"

    elif riesgo >= 4:

        nivel = "MEDIO"
        resultado = "🟠 URL SOSPECHOSA"

    else:

        nivel = "BAJO"
        resultado = "✅ NO SE DETECTARON SEÑALES CLARAS"


    return riesgo, nivel, resultado, razones

print()
print("==============================================")
print("       🛡️ DETECTOR DE PHISHING")
print("==============================================")
print()
print("Sistema de análisis de URLs")
print("Desarrollado completamente en Python.")
print()


while True:

    print("----------------------------------------------")

    url = input(
        "Introduce una URL para analizar\n"
        "(escribe 'salir' para terminar): "
    )

    if url.lower() == "salir":

        print()
        print("Programa finalizado. 👋")
        break

    riesgo, nivel, resultado, razones = analizar_url(url)

    print()
    print("==============================================")
    print("                 RESULTADO")
    print("==============================================")

    print()
    print("URL analizada:")
    print(url)

    print()
    print("Resultado:")
    print(resultado)

    print()
    print("Nivel de riesgo:")
    print(nivel)

    print()
    print("Puntuación de riesgo:")
    print(riesgo)

    if razones:

        print()
        print("Características detectadas:")

        for razon in razones:

            print("• " + razon)

    else:

        print()
        print(
            "No se encontraron características "
            "sospechosas."
        )

    print()

    if nivel == "ALTO":

        print("🚨 RECOMENDACIÓN:")
        print(
            "No introduzcas contraseñas ni "
            "información personal."
        )

    elif nivel == "MEDIO":

        print("⚠️ RECOMENDACIÓN:")
        print(
            "Verifica cuidadosamente el sitio "
            "antes de introducir información."
        )

    else:

        print("💡 RECOMENDACIÓN:")
        print(
            "Aunque el riesgo sea bajo, "
            "mantén precaución al navegar."
        )


    print()
    print("==============================================")
