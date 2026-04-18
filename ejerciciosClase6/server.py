from fastmcp import FastMCP
import math
import string
import random
import json
from datetime import datetime
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from datetime import timedelta

# Crear instancia del servidor
mcp = FastMCP(
    name="Herramientas Básicas",
    instructions="Servidor MCP con calculadora científica, conversor de unidades y generador de contraseñas."
)

@mcp.tool()
def calculadora(operacion: str, a: float, b: float = 0.0) -> str:
    """Realiza operaciones matemáticas."""
    operaciones = {
        "suma": lambda: a + b,
        "resta": lambda: a - b,
        "multiplicacion": lambda: a * b,
        "division": lambda: a / b if b != 0 else "Error: división por cero",
        "potencia": lambda: a ** b,
        "raiz": lambda: math.sqrt(a) if a >= 0 else "Error: raíz de número negativo",
        "seno": lambda: math.sin(math.radians(a)),
        "coseno": lambda: math.cos(math.radians(a)),
        "logaritmo": lambda: math.log(a) if a > 0 else "Error: logaritmo de número no positivo",
    }

    if operacion not in operaciones:
        return f"Operación '{operacion}' no reconocida."

    resultado = operaciones[operacion]()
    return f"{operacion}({a}, {b}) = {resultado}"

@mcp.tool()
def conversor_unidades(valor: float, de: str, a: str) -> str:
    """Convierte entre diferentes unidades de medida."""
    longitud_a_metros = {
        "km": 1000, "m": 1, "cm": 0.01, "mm": 0.001,
        "mi": 1609.34, "ft": 0.3048, "in": 0.0254
    }

    peso_a_gramos = {
        "kg": 1000, "g": 1, "mg": 0.001,
        "lb": 453.592, "oz": 28.3495
    }

    if de in longitud_a_metros and a in longitud_a_metros:
        resultado = valor * longitud_a_metros[de] / longitud_a_metros[a]
        return f"{valor} {de} = {resultado:.4f} {a}"

    if de in peso_a_gramos and a in peso_a_gramos:
        resultado = valor * peso_a_gramos[de] / peso_a_gramos[a]
        return f"{valor} {de} = {resultado:.4f} {a}"

    return f"No se puede convertir de '{de}' a '{a}'."

@mcp.tool()
def generar_contrasena(longitud: int = 16, incluir_simbolos: bool = True) -> str:
    """Genera una contraseña aleatoria segura."""
    if longitud < 8:
        return "Error: la longitud mínima es 8 caracteres."
    if longitud > 128:
        return "Error: la longitud máxima es 128 caracteres."

    caracteres = string.ascii_letters + string.digits
    if incluir_simbolos:
        caracteres += "!@#$%^&*()-_=+[]{}|;:,.<>?"

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

@mcp.resource("config://servidor")
def obtener_configuracion() -> str:
    """Configuración actual del servidor MCP y sus capacidades."""
    config = {
        "nombre": "Herramientas Básicas",
        "version": "1.0.0",
        "herramientas_disponibles": [
            "calculadora",
            "conversor_unidades",
            "generar_contrasena"
        ],
        "unidades_soportadas": {
            "longitud": ["km", "m", "cm", "mm", "mi", "ft", "in"],
            "peso": ["kg", "g", "mg", "lb", "oz"],
            "temperatura": ["celsius", "fahrenheit", "kelvin"]
        },
        "operaciones_calculadora": [
            "suma", "resta", "multiplicacion", "division",
            "potencia", "raiz", "seno", "coseno", "logaritmo"
        ]
    }
    return json.dumps(config, indent=2, ensure_ascii=False)

@mcp.resource("status://servidor")
def obtener_estado() -> str:
    """Estado actual del servidor incluyendo timestamp y métricas básicas."""
    estado = {
        "estado": "activo",
        "timestamp": datetime.now().isoformat(),
        "uptime_info": "Servidor funcionando correctamente",
        "version_python": f"{__import__('sys').version}",
        "modulos_cargados": ["math", "string", "random", "json", "datetime"]
    }
    return json.dumps(estado, indent=2, ensure_ascii=False)

@mcp.prompt()
def analizar_conversion(valor: float, unidad_origen: str, contexto: str = "general") -> str:
    """Prompt para analizar una conversión de unidades en contexto."""
    return f"""Eres un experto en unidades de medida y conversiones.

Se te proporciona el siguiente valor: {valor} {unidad_origen}

Contexto de uso: {contexto}

Por favor:
1. Convierte este valor a las 3 unidades más relevantes para el contexto indicado.
   Usa la herramienta 'conversor_unidades' para cada conversión.
2. Explica en qué situaciones prácticas del contexto '{contexto}' se usaría cada unidad.
3. Indica si el valor proporcionado está dentro de rangos habituales para ese contexto.

Responde de forma clara y estructurada."""

@mcp.prompt()
def generar_informe_seguridad(longitud_minima: int = 12, num_contrasenas: int = 5) -> str:
    """Prompt para generar un informe de seguridad de contraseñas."""
    return f"""Eres un experto en ciberseguridad y gestión de contraseñas.

Realiza las siguientes tareas:

1. Genera {num_contrasenas} contraseñas usando la herramienta 'generar_contrasena':
   - 2 contraseñas de {longitud_minima} caracteres SIN símbolos
   - 2 contraseñas de {longitud_minima} caracteres CON símbolos
   - 1 contraseña de {longitud_minima + 8} caracteres CON símbolos

2. Para cada contraseña generada, analiza:
   - Fortaleza reportada por la herramienta
   - Tiempo estimado de cracking por fuerza bruta
   - Vulnerabilidades potenciales

3. Elabora un informe con:
   - Tabla comparativa de las contraseñas
   - Recomendaciones de mejores prácticas
   - Política de contraseñas sugerida para una organización

Presenta el informe de forma profesional y estructurada."""

@mcp.middleware()
def autenticar(token: str):
    """Middleware para autenticar solicitudes usando JWT."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload  # Si el token es válido, continuar con la solicitud
    except ExpiredSignatureError:
        return "Error: El token ha expirado."
    except InvalidTokenError:
        return "Error: Token inválido."

@mcp.tool()
def generar_token(usuario: str) -> str:
    """Genera un token JWT para un usuario."""
    payload = {
        "sub": usuario,
        "exp": datetime.utcnow() + timedelta(hours=1),
        "iat": datetime.utcnow()
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

@mcp.tool()
def verificar_token(token: str) -> str:
    """Verifica la validez de un token JWT."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return f"Token válido para el usuario: {payload['sub']}"
    except ExpiredSignatureError:
        return "Error: El token ha expirado."
    except InvalidTokenError:
        return "Error: Token inválido."

if __name__ == "__main__":
    mcp.run()