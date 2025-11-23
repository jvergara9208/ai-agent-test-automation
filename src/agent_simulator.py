# src/agent_simulator.py 
# -*- coding: utf-8 -*-
import string 

class AgentSimulator:
    """
    Simula la lógica de reconocimiento de intención y respuesta de un Agente AI 
    enfocado en pedidos del El gran Chanchito.
    """
    def __init__(self):
        self.knowledge_base = {
            "buenas tardes": {"intent": "GREETING", "response": "¡Bienvenido al El gran Chanchito! ¿Desea consultar el menú o realizar un pedido?"},
            "ajiaco": {"intent": "CONSULTA_PLATO", "response": "El Ajiaco Santaferño está recién hecho, con pollo desmenuzado, mazorca y cremoso aguacate."},
            "bandeja paisa": {"intent": "INICIAR_ORDEN", "response": "¡Excelente elección! La Bandeja Paisa está confirmada. ¿Desea agregar una Kola Román?"},
            "no gracias": {"intent": "FINALIZAR_ORDEN", "response": "De acuerdo. Su Bandeja Paisa estará lista en 25 minutos. ¡Gracias por su pedido!"},
            "a que hora llega": {"intent": "CONSULTA_TIEMPO", "response": "El tiempo de entrega estimado es de 25 minutos desde la confirmación."},
            "gracias": {"intent": "FINALIZAR_ORDEN", "response": "De nada, ¡vuelve pronto!"}, 
        }
        self.default_response = {"intent": "FALLBACK_COCINA", "response": "Disculpe, esa solicitud no está en el menú. ¿Podría repetir su pedido?"}

    def process_message(self, message: str) -> dict:
        """Procesa el mensaje del usuario y devuelve la respuesta simulada."""
        
        message_lower = message.lower()
        
        
        punctuation_to_remove = string.punctuation + '¿¡' 
        
        translator = str.maketrans('', '', punctuation_to_remove)
        message_cleaned = message_lower.translate(translator).strip()

        for key, value in self.knowledge_base.items():
            if key in message_cleaned: 
                return value
        
        return self.default_response

agent = AgentSimulator()
