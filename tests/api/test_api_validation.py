 # tests/api/test_api_validation.py
import time
from datetime import datetime
import pytest
from jsonschema import validate
from config.schemas import response_schema, error_schema # Importamos los schemas definidos en config/schemas.py

# --- Simulación de API Mockeada ---
def mock_api_call(payload=None, expected_code=200):
    """Simula la respuesta de un endpoint REST de un restaurante El gran Chanchito."""
    start_time = time.time()
    
    if expected_code == 200:
        # Respuesta exitosa simulada (200 OK)
        response_data = {
            "restaurant_id": "RESTA-007",
            "api_status": "operacional",
            "timestamp": datetime.now().isoformat(),
            "data": {
                "intent": "CONSULTA_MENU",
                "message": "La Bandeja Paisa del día viene con chicharrón crocante y aguacate fresco."
            }
        }
    elif expected_code == 400:
        # Respuesta de error de validación (400 Bad Request)
        response_data = {"error": "El payload no incluye el token de autenticación requerido para la orden.", "code": 400}
    
    end_time = time.time()
    elapsed_time_ms = (end_time - start_time) * 1000
    
    return expected_code, response_data, elapsed_time_ms
# --- Pruebas de Validación de la API ---
@pytest.mark.api
def test_successful_api_response_and_schema():
    """Valida respuesta 200, schema JSON y rendimiento."""
    status_code, response_body, elapsed_time = mock_api_call(expected_code=200)

    # ASSERT 1: Validación del Status Code
    assert status_code == 200, f"Se esperaba 200, se recibió {status_code}"

    # ASSERT 2: Validación del tiempo de respuesta (<500 ms)
    MAX_TIME_MS = 500
    assert elapsed_time < MAX_TIME_MS, f"Tiempo de respuesta ({elapsed_time:.2f} ms) excedió el límite de {MAX_TIME_MS} ms"

    # ASSERT 3: Validación del Schema JSON
    try:
        validate(instance=response_body, schema=response_schema)
    except Exception as e:
        pytest.fail(f"Falla en la validación del schema JSON: {e}")
# --- Prueba de Rechazo de Payload Inválido ---
@pytest.mark.api
def test_invalid_payload_rejection():
    """Valida la respuesta con un payload inválido (esperamos 400)."""
    status_code, response_body, elapsed_time = mock_api_call(expected_code=400)

    # ASSERT 1: Validación de código de error esperado
    assert status_code == 400, f"Se esperaba 400 Bad Request, se recibió {status_code}"
    
    # ASSERT 2: Validación del Schema JSON de error
    try:
        validate(instance=response_body, schema=error_schema)
    except Exception as e:
        pytest.fail(f"Falla en la validación del schema JSON de error: {e}")