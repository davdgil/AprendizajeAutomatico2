"""
Tests para el cliente multi-proveedor LLMClient.
"""

from llm_client import LLMClient

# Mensajes de prueba
messages = [
    {"role": "system", "content": "Eres un asistente conciso. Responde en máximo 2 oraciones."},
    {"role": "user", "content": "¿Qué es Python?"},
]

# Probar los proveedores disponibles
# Cambia esta lista según las API keys que tengas configuradas
proveedores = ["openrouter"]  # Añade "openai", "gemini", "claude" si tienes API keys

for provider in proveedores:
    print(f"\n{'='*40}")
    print(f"Proveedor: {provider}")
    print(f"{'='*40}")

    try:
        client = LLMClient(provider)
        response = client.chat(messages, temperature=0.7)
        print(f"Modelo: {client.model}")
        print(f"Respuesta: {response}")
    except Exception as e:
        print(f"Error: {e}")

# Probar streaming con OpenRouter
print(f"\n{'='*40}")
print("Streaming con OpenRouter")
print(f"{'='*40}")

try:
    client = LLMClient("openrouter")
    print("Respuesta: ", end="")
    for token in client.stream(messages, temperature=0.7):
        print(token, end="", flush=True)
    print()
except Exception as e:
    print(f"Error en streaming: {e}")
