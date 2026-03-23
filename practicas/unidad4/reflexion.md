# Reflexión - Práctica Evaluable Unidad 4
## Agente de IA con n8n

### ¿Qué caso práctico elegiste y por qué?

Elegí el **Caso 3: Asistente Personal con Búsqueda y Cálculo** por ser el más accesible técnicamente. A diferencia de los otros casos que requieren configuraciones complejas con OAuth2 y servicios externos (Google Sheets o Gmail), este caso utilizaba herramientas integradas en n8n (Wikipedia y Calculator), lo que minimizaba los puntos de fallo técnico y me permitía concentrarme en los aspectos fundamentales del diseño de agentes de IA.

### ¿Qué dificultades encontraste durante el desarrollo?

La principal dificultad fue la **limitación de las APIs gratuitas**. Inicialmente intenté usar OpenAI (gpt-4o-mini) pero rápidamente excedí la cuota. Al cambiar a Google Gemini (gemini-1.5-flash), pude completar la configuración inicial, pero los límites restrictivos impidieron realizar las 5 conversaciones de prueba completas requeridas. Esto resalta un problema real en entornos académicos: la dependencia de servicios externos limita significativamente las posibilidades de experimentación.

Otra dificultad menor fue la configuración del **System Prompt efectivo**. Requirió varias iteraciones para lograr que el agente utilizara correctamente las herramientas disponibles y citara las fuentes apropiadamente.

### ¿Qué mejoras añadirías al agente si tuvieras más tiempo?

1. **Memoria persistente**: Implementar una base de datos PostgreSQL o Supabase para que el agente mantenga contexto entre sesiones diferentes.

2. **Más herramientas especializadas**: Integrar APIs de noticias, clima, o servicios financieros para ampliar las capacidades del asistente.

3. **Validación de respuestas**: Implementar verificación cruzada entre múltiples fuentes para mejorar la precisión de la información.

4. **Canal externo**: Desplegar el agente en Telegram o WhatsApp para uso real.

5. **Manejo de errores**: Mejorar la gestión de fallos de APIs y respuestas de contingencia.

### ¿Cómo aplicarías este tipo de agentes en un contexto profesional real?

Los agentes de IA con esta arquitectura (LLM + Memoria + Herramientas) tienen múltiples aplicaciones profesionales:

1. **Soporte técnico interno**: Agente que consulte la documentación empresarial y bases de conocimiento para resolver dudas del equipo.

2. **Asistente de análisis financiero**: Combinando APIs financieras con capacidades de cálculo para generar reportes automáticos.

3. **Automatización de ventas**: Integrado con CRM, podría consultar datos de clientes y generar propuestas personalizadas.

4. **Investigación y desarrollo**: Para consultores o investigadores que necesiten combinar búsquedas de información con análisis cuantitativo.

La clave está en la **especialización**: cada agente debe diseñarse para un dominio específico con herramientas relevantes, no como un asistente genérico.