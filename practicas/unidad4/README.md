# Práctica Evaluable - Unidad 4: Agente de IA con n8n

**Estudiante:** David
**Caso práctico elegido:** Caso 3 - Asistente Personal con Búsqueda y Cálculo
**Fecha:** Marzo 2026

---

## Contenido de la entrega

### 📄 Archivos incluidos:

1. **`asistente-personal-caso3.json`** - Workflow exportado desde n8n
2. **`capturas-pantalla.pdf`** - Documento con capturas de pantalla de:
   - Workflow completo en n8n
   - Configuración del nodo AI Agent (System Prompt, Memoria, Herramientas)
   - Conversaciones de prueba realizadas
3. **`reflexion.md`** - Reflexión personal (400 palabras máximo)

### 🤖 Configuración del agente:

**Modelo de IA:** Google Gemini (gemini-1.5-flash)
**Memoria:** Window Buffer Memory (contexto de 10 mensajes)
**Herramientas:** Wikipedia + Calculator

### ✅ Funcionalidades implementadas:

- ✅ Búsqueda de información factual en Wikipedia
- ✅ Cálculos matemáticos complejos
- ✅ Memoria conversacional
- ✅ Citas de fuentes
- ✅ Combinación de búsqueda + cálculo

### 📝 Pruebas realizadas:

1. **Búsqueda en Wikipedia:** "¿Dónde comenzó la revolución industrial?" ✅
2. **Cálculo matemático:** Operaciones aritméticas complejas
3. **Búsqueda + Cálculo:** Consultas que requieren ambas herramientas
4. **Contexto mantenido:** Preguntas encadenadas
5. **Razonamiento complejo:** Combinación de múltiples operaciones

---

## Notas técnicas

**Limitación encontrada:** Los límites de API gratuitas (OpenAI y Google) restringieron significativamente el número de pruebas que se pudieron realizar durante el desarrollo.

**Solución adoptada:** Se completó la configuración técnica y se documentó el funcionamiento con las pruebas realizadas antes de alcanzar los límites.