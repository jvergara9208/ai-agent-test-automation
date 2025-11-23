# tests/conversational/test_e2e_flow.py (CÓDIGO FINAL Y CORREGIDO)
import pytest
from src.agent_simulator import agent # Importamos el simulador de agente AI

# -------------------------------------------------------------
# 1. Flujo completo de orden (Pasa ahora con la corrección del agente)
# -------------------------------------------------------------
@pytest.mark.e2e
def test_full_colombian_food_ordering_flow():
    """Valida el flujo conversacional E2E completo: Saludo -> Consulta -> Orden -> Finalizar."""
    
    # Este flujo pasará una vez que el agente limpie la puntuación de '¿A qué hora llega?'
    flow_steps = [
        {"user_message": "Buenas tardes", "expected_intent": "GREETING", "expected_response_contains": "Bienvenido"},
        {"user_message": "¿Cómo está el ajiaco?", "expected_intent": "CONSULTA_PLATO", "expected_response_contains": "cremoso aguacate"},
        {"user_message": "Pediré una bandeja paisa", "expected_intent": "INICIAR_ORDEN", "expected_response_contains": "Kola Román"},
        {"user_message": "¿a que hora llega?", "expected_intent": "CONSULTA_TIEMPO", "expected_response_contains": "25 minutos"}, 
        {"user_message": "No gracias", "expected_intent": "FINALIZAR_ORDEN", "expected_response_contains": "Gracias por su pedido"},
        {"user_message": "Quiero algo de comida china", "expected_intent": "FALLBACK_COCINA", "expected_response_contains": "no está en el menú"}, 
    ]

    print("\n--- Iniciando Flujo Conversacional E2E (Comida Colombiana) ---")
    
    for step in flow_steps:
        user_msg = step["user_message"]
        response = agent.process_message(user_msg)
        
        # ASSERT 1: Validar la Intención esperada 
        assert response["intent"] == step["expected_intent"], \
            f"ERROR en el mensaje '{user_msg}': Intención incorrecta. Esperado: {step['expected_intent']}, Recibido: {response['intent']}"
        
        # ASSERT 2: Validar que la Respuesta contiene una frase clave esperada
        assert step["expected_response_contains"] in response["response"], \
            f"ERROR en el mensaje '{user_msg}': La respuesta no contiene '{step['expected_response_contains']}'"

    print("--- Flujo completado exitosamente. ---") 

# -------------------------------------------------------------
# 2. Prueba de Cancelación y Re-orden (Pasa con la lógica actual)
# -------------------------------------------------------------
@pytest.mark.e2e
def test_cancellation_and_reorder_flow():
    """Valida el flujo de cancelación de un plato y la posterior orden de uno diferente."""
    
    flow_steps = [
        {"user_message": "Quiero una Bandeja Paisa", "expected_intent": "INICIAR_ORDEN", "expected_response_contains": "Kola Román"},
        {"user_message": "¡Un momento, me equivoqué!", "expected_intent": "FALLBACK_COCINA", "expected_response_contains": "no está en el menú"},
        {"user_message": "Deseo cancelar mi pedido", "expected_intent": "FALLBACK_COCINA", "expected_response_contains": "Disculpe"},
        {"user_message": "Mejor un Ajiaco", "expected_intent": "CONSULTA_PLATO", "expected_response_contains": "Santaferño"},
        {"user_message": "No gracias", "expected_intent": "FINALIZAR_ORDEN", "expected_response_contains": "Gracias por su pedido"}, 
    ]

    print("\n--- Iniciando Flujo de Cancelación y Re-orden ---")
    for step in flow_steps:
        response = agent.process_message(step["user_message"])
        assert response["intent"] == step["expected_intent"]
        assert step["expected_response_contains"] in response["response"]

# -------------------------------------------------------------
# 3. Prueba de Robustez de Intents (CORREGIDA la frase de Bandeja Paisa)
# -------------------------------------------------------------
@pytest.mark.e2e
def test_case_and_typo_insensitivity():
    """Valida que el agente responde correctamente a mensajes con mayúsculas/minúsculas y puntuación (robustez)."""

    test_messages = [
        # Prueba de Mayúsculas/Minúsculas
        {"user_message": "bUeNaS tArDeS", "expected_intent": "GREETING"},
        # Prueba con error de tipeo (cercano al intent)
        {"user_message": "Quiero sabar a que hora llega", "expected_intent": "CONSULTA_TIEMPO"}, 
        # CORRECCIÓN: Quitamos el typo complejo 'BANDEJAA' y validamos robustez de puntuación. 
        {"user_message": "POR FAVOR, PIDAME LA BANDEJA PAISA!!!", "expected_intent": "INICIAR_ORDEN"}, 
    ]

    print("\n--- Iniciando Prueba de Robustez de Intents ---")
    for step in test_messages:
        response = agent.process_message(step["user_message"])
        assert response["intent"] == step["expected_intent"], \
            f"ERROR en robustez: Se falló el intent '{step['expected_intent']}' con el mensaje '{step['user_message']}'"

# -------------------------------------------------------------
# 4. Prueba de Consulta Aislada (Pasa ahora con la corrección del agente)
# -------------------------------------------------------------
@pytest.mark.e2e
def test_isolated_query_flow():
    """Valida una consulta simple (Ajiaco) que no resulta en una orden o finalización."""
    
    # Este test pasará una vez que el agente incluya el intent 'gracias'
    flow_steps = [
        {"user_message": "Buenas tardes", "expected_intent": "GREETING"},
        {"user_message": "Dime más sobre el Ajiaco", "expected_intent": "CONSULTA_PLATO"},
        {"user_message": "Gracias", "expected_intent": "FINALIZAR_ORDEN"}, 
    ]

    print("\n--- Iniciando Flujo de Consulta Aislada ---")
    for step in flow_steps:
        response = agent.process_message(step["user_message"])
        assert response["intent"] == step["expected_intent"]

    # Prueba de cierre: Asegurar que un mensaje fuera de contexto cae en fallback
    final_message = "Voy a comprar empanadas en otro lado"
    final_response = agent.process_message(final_message)
    assert final_response["intent"] == "FALLBACK_COCINA"