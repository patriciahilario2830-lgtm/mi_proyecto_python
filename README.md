Sobre mí:

Mi nombre es Carla Castillo, soy estudiante de 6to de Informática en el Instituto Tecnológico México, en Santiago de los Caballeros, República Dominicana.
Me interesa el área de la informática, especialmente la ciberseguridad, y este proyecto forma parte de mi aprendizaje y práctica en el desarrollo de soluciones tecnológicas.

¿Qué problema resuelve la IA?

El proyecto busca solucionar el problema del robo de contraseñas y datos personales mediante ataques de phishing. Muchas personas pueden recibir enlaces falsos que aparentan pertenecer a sitios legítimos y, al entrar en ellos, podrían proporcionar información como contraseñas o datos de sus cuentas.

El sistema ayuda a detectar señales de riesgo en una URL antes de que el usuario confíe en ella. De esta manera, puede advertir al usuario cuando un enlace presenta características que podrían estar relacionadas con phishing y recomendarle que tenga precaución.

¿Qué hace el código?

El código crea un detector de phishing desarrollado completamente en Python, sin utilizar librerías externas.

Cuando el usuario introduce una URL, el programa analiza diferentes características del enlace, como:

-Si utiliza HTTPS.

-La longitud de la URL.

-La presencia del símbolo @.

-Si utiliza una dirección IP en lugar de un dominio.

-La cantidad de guiones.

-La cantidad de subdominios.

-La presencia de palabras sospechosas como login, verify, password, account, security o bank.

-La cantidad de números que contiene la URL.

Después del análisis, el programa asigna una puntuación de riesgo. Dependiendo de esa puntuación, clasifica el enlace como:
Riesgo bajo: no se detectaron señales claras.
Riesgo medio: URL sospechosa.
Riesgo alto: posible phishing.
