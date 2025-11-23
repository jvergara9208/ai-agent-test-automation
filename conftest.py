import pytest
from src.agent_simulator import AgentSimulator
from src.voice_simulator import VoiceSimulator

# Esta función se llama una 'fixture'
@pytest.fixture(scope="session")
def agent_client():
    # Inicializa el Agente una sola vez por sesión de pruebas
    return AgentSimulator() 

@pytest.fixture(scope="session")
def voice_client():
    # Inicializa el Agente de Voz una sola vez por sesión de pruebas
    return VoiceSimulator()