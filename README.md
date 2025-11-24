# 🍲 AI Agent Test Automation Challenge (El Gran Chanchito)

Este repositorio contiene la solución técnica al Reto de Automatización de Pruebas de QA, enfocado en validar un agente de pedidos simulado para un restaurante de comida colombiana.

El proyecto implementa un framework de pruebas robusto que cubre la validación de API, el flujo conversacional E2E (End-to-End) y la integridad de los componentes de voz (ASR/TTS), utilizando Pytest y el principio de normalización de entrada.

---

## 🚀 1. Configuración e Instalación del Entorno

Sigue estos pasos para configurar tu entorno de desarrollo y poder ejecutar las pruebas.

**### 1.1. Requisitos Previos**

Necesitas tener **\*\*Python 3.8+\*\*** instalado en tu sistema.

**### 1.2. Instalación del Entorno Virtual y Dependencias**

Es una buena práctica aislar las dependencias del proyecto usando un entorno virtual (`venv`).



### 1. Crear el entorno virtual (solo la primera vez)
```bash
python -m venv venv
```
### 2. Activar el entorno virtual

#### En Windows (CMD/PowerShell):
```bash
.\venv\Scripts\activate
```
#### En Linux/macOS:
```bash
source venv/bin/activate
```
### 3. Instalar las dependencias listadas en requirements.txt

pip install -r [requirements.tx](./requirements.txt)



-----
## <a name="_xut6zxwj4s4z"></a>**📦 2. Librerías Utilizadas y Justificación**
Las siguientes librerías fueron instaladas a través de requirements.txt:

|**Librería**|**Propósito**|**Justificación**|
| :- | :- | :- |
|**pytest**|Framework principal de pruebas.|Estándar de la industria en Python. Permite crear tests modulares, usar *fixtures* y marcadores.|
|**jsonschema**|Validación de API.|Utilizada para asegurar que las respuestas *mockeadas* de la API sigan una estructura JSON predefinida.|
|**pytest-html**|Generación de reportes.|Permite generar reportes visuales en formato HTML para compartir el estado de QA fácilmente.|

-----
## <a name="_p7e78x4egwgq"></a>**🧪 3. Ejecución de Pruebas**
Todas las pruebas se ejecutan usando el comando pytest.
### <a name="_o8pjtqfis2q1"></a>**3.1. Ejecución Completa de Todos los Requisitos (Recomendado)**
Este comando ejecuta todas las pruebas (API, E2E y Voz) y genera un reporte detallado:

```bash
pytest -v --html=reporte\_qa.html --self-contained-html --durations=0
```
- **Resultado esperado:** **8 tests pasados** (2 API + 4 E2E + 2 Voz).
- El reporte reporte\_qa.html se generará en la raíz del proyecto.
### <a name="_lum7fhyw8z5h"></a>**3.2. Ejecución de Pruebas Individuales por Requisito**
Puedes ejecutar conjuntos de pruebas específicos usando los **marcadores** definidos en los archivos:

|**Requisito**|**Comando de Ejecución (Usando Marcadores)**|
| :- | :- |
|**API (@pytest.mark.api)**|pytest -m api -v|
|**E2E (@pytest.mark.e2e)**|pytest -m e2e -v|
|**Voz (@pytest.mark.voice)**|pytest -m voice -v|

-----
## <a name="_ntmhjr5easv7"></a>**🛠️ 4. Estructura del Proyecto y Metodología**
### <a name="_dkq4c66u4uco"></a>**4.1. Filosofía de Desarrollo y QA**
El proyecto se basa en la simulación de componentes reales (Agente AI, API REST y ASR/TTS) para lograr una cobertura del 100% de los requisitos:

- **Normalización de Entrada:** Se implementó una lógica de limpieza en src/agent\_simulator.py (uso de .lower() y eliminación de string.punctuation + '¿¡') para asegurar la **robustez** del agente contra mayúsculas, *typos* y signos de puntuación españoles, resolviendo fallos en el flujo E2E.
- **Simulación de Voz:** Se utilizó src/voice\_simulator.py para *mockear* la capa de ASR/TTS, permitiendo validar las propiedades del audio (mp3, duración) y la integridad de la transcripción (*roundtrip*).
### <a name="_sxcehq3szh5g"></a>**4.2. Uso de Inteligencia Artificial (AI) en el Proceso**
Se utilizó un modelo de **Inteligencia Artificial (AI)** (Gemini) como copiloto de desarrollo y QA, enfocándose en las siguientes áreas:

- **Organización del Proyecto y Guías:** La AI fue crucial para definir la estructura de carpetas y para la creación de guías paso a paso de configuración y *debugging* (como esta guía README).
- **Corrección y Entendimiento de Código (Debugging):** La AI asistió en el proceso de **depuración (*debugging*)** del código del agente para resolver el error persistente de reconocimiento de intención, identificando la necesidad de añadir los caracteres ¿¡ a la lista de puntuación a eliminar.
### <a name="_nzeblambgewv"></a>**4.3. URLs de Consulta y Referencia**
Para el entendimiento del framework y la implementación de las validaciones, se consultaron las siguientes guías oficiales:

- **Pytest Markers:** https://docs.pytest.org/en/stable/how-to/mark.html
- **Pytest HTML Report:** https://pytest-html.readthedocs.io/en/latest/
- **Validación JSON Schema:** https://json-schema.org/
-----
## <a name="_5rjziz299cwz"></a>**⚙️ 5. Integración Continua (CI/CD)**
El proyecto incluye la configuración del *pipeline* de CI/CD para **GitHub Actions** en el archivo: .github/workflows/qa\_pipeline.yml.

Este *pipeline* se activa en cada *push* y *Pull Request* y ejecuta automáticamente todos los tests (pytest -v --junitxml=report.xml), garantizando que cualquier cambio futuro no rompa la funcionalidad existente.
# <a name="_b6kljwbyl905"></a>**Reporte Final de Pruebas - AI Agent Test Automation**
**Fecha de Ejecución:** [Colocar Fecha y Hora de la última ejecución] **Estado de la CI/CD:** PASSED **Total de Pruebas Ejecutadas:** 8 **Total de Pruebas Exitosas:** 8

**Resumen Ejecutivo y Hallazgos Clave**

El marco de automatización implementado logró una cobertura del 100% de los requisitos (API, E2E Conversacional y Componentes de Voz). Se confirma que el Agente de Pedidos está **funcional y robusto** bajo diversas condiciones.
### <a name="_79pm4jlmyjbb"></a>**1. Validación Crítica (E2E)**
- **Hallazgo clave:** Se identificó que el agente original fallaba al procesar mensajes con signos de puntuación de inicio (ej. "¿A qué hora llega?").
- **Solución y Validación:** Se implementó una capa de **Normalización de Entrada** en src/agent\_simulator.py (eliminando string.punctuation + '¿¡') que resolvió los 4 escenarios E2E. El agente ahora maneja correctamente mayúsculas, minúsculas y toda la puntuación española.
### <a name="_g0frye1pqch"></a>**2. Integridad de Componentes (Voz)**
- **Validación exitosa:** Las pruebas de voz confirmaron que la simulación de TTS (voice\_simulator.py) cumple con el contrato esperado:
  - El formato de salida es siempre **mp3**.
  - La duración y el tamaño en bytes son valores coherentes con el texto de entrada.
  - El ciclo completo ASR > Agente > TTS (roundtrip) se ejecuta sin errores.
### <a name="_al50l7q8f32j"></a>**3. Contrato de API**
- **Validación exitosa:** Las 3 pruebas de API confirman que la respuesta del Agente siempre devuelve la estructura esperada: un objeto JSON con las claves **intent** (string) y **response** (string), validando la integridad del contrato de datos.


