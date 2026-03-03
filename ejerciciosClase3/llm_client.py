"""
Cliente Multi-Proveedor para LLMs.
Clase unificada que abstrae las diferencias entre OpenAI, Gemini, Claude y OpenRouter.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class LLMClient:
    """Cliente unificado para múltiples proveedores de LLMs."""

    DEFAULT_MODELS = {
        "openai": "gpt-4o-mini",
        "gemini": "gemini-1.5-flash",
        "claude": "claude-3-5-haiku-latest",
        "openrouter": "z-ai/glm-4.5-air:free",
    }

    def __init__(self, provider: str, model: str = None):
        """
        Inicializa el cliente.

        Args:
            provider: Proveedor a usar ("openai", "gemini", "claude", "openrouter").
            model: Modelo específico. Si es None, usa el modelo por defecto.
        """
        if provider not in self.DEFAULT_MODELS:
            raise ValueError(
                f"Proveedor no soportado: {provider}. Usa: {list(self.DEFAULT_MODELS.keys())}"
            )

        self.provider = provider
        self.model = model or self.DEFAULT_MODELS[provider]
        self._client = None

        if provider == "openai":
            from openai import OpenAI
            self._client = OpenAI()

        elif provider == "openrouter":
            from openai import OpenAI
            self._client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=os.getenv("OPENROUTER_API_KEY"),
            )

        elif provider == "gemini":
            import google.generativeai as genai
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
            self._client = genai

        elif provider == "claude":
            import anthropic
            self._client = anthropic.Anthropic()

    def _adapt_messages(self, messages):
        """
        Adapta los mensajes al formato que espera cada proveedor.

        Returns:
            dict con las claves necesarias para cada API.
        """
        if self.provider in ("openai", "openrouter"):
            return {"messages": messages}

        elif self.provider == "gemini":
            system_text = ""
            gemini_messages = []
            for msg in messages:
                if msg["role"] == "system":
                    system_text = msg["content"]
                else:
                    role = "user" if msg["role"] == "user" else "model"
                    gemini_messages.append({"role": role, "parts": [msg["content"]]})

            if system_text and gemini_messages and gemini_messages[0]["role"] == "user":
                gemini_messages[0]["parts"][0] = (
                    f"[Instrucciones del sistema: {system_text}]\n\n"
                    f"{gemini_messages[0]['parts'][0]}"
                )

            return {"system": system_text, "messages": gemini_messages}

        elif self.provider == "claude":
            system_text = ""
            claude_messages = []
            for msg in messages:
                if msg["role"] == "system":
                    system_text = msg["content"]
                else:
                    claude_messages.append(
                        {"role": msg["role"], "content": msg["content"]}
                    )
            return {"system": system_text, "messages": claude_messages}

    def chat(self, messages, **kwargs):
        """
        Envía mensajes al LLM y retorna la respuesta.

        Args:
            messages: Lista de mensajes en formato unificado.
            **kwargs: Parámetros adicionales (temperature, max_tokens, etc.)

        Returns:
            str: Texto de la respuesta.
        """
        adapted = self._adapt_messages(messages)

        if self.provider in ("openai", "openrouter"):
            response = self._client.chat.completions.create(
                model=self.model,
                messages=adapted["messages"],
                **kwargs,
            )
            return response.choices[0].message.content

        elif self.provider == "gemini":
            gen_model = self._client.GenerativeModel(self.model)
            response = gen_model.generate_content(
                adapted["messages"],
                generation_config=self._client.types.GenerationConfig(
                    temperature=kwargs.get("temperature", 0.7),
                    max_output_tokens=kwargs.get("max_tokens", 1024),
                ),
            )
            return response.text

        elif self.provider == "claude":
            response = self._client.messages.create(
                model=self.model,
                max_tokens=kwargs.get("max_tokens", 1024),
                system=adapted["system"],
                messages=adapted["messages"],
                temperature=kwargs.get("temperature", 0.7),
            )
            return response.content[0].text

    def stream(self, messages, **kwargs):
        """
        Envía mensajes al LLM y retorna un generador de tokens.

        Yields:
            str: Cada token/fragmento de la respuesta.
        """
        adapted = self._adapt_messages(messages)

        if self.provider in ("openai", "openrouter"):
            response = self._client.chat.completions.create(
                model=self.model,
                messages=adapted["messages"],
                stream=True,
                **kwargs,
            )
            for chunk in response:
                if chunk.choices and chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content

        elif self.provider == "gemini":
            gen_model = self._client.GenerativeModel(self.model)
            response = gen_model.generate_content(
                adapted["messages"],
                stream=True,
                generation_config=self._client.types.GenerationConfig(
                    temperature=kwargs.get("temperature", 0.7),
                    max_output_tokens=kwargs.get("max_tokens", 1024),
                ),
            )
            for chunk in response:
                if chunk.text:
                    yield chunk.text

        elif self.provider == "claude":
            with self._client.messages.stream(
                model=self.model,
                max_tokens=kwargs.get("max_tokens", 1024),
                system=adapted["system"],
                messages=adapted["messages"],
                temperature=kwargs.get("temperature", 0.7),
            ) as stream:
                for text in stream.text_stream:
                    yield text
