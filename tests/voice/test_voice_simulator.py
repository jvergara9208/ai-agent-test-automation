# tests/voice/test_voice_validation.py
import pytest
from src.voice_simulator import voice_agent, AudioData 

@pytest.mark.voice
def test_tts_audio_generation_validation():
    """
    Valida que el proceso TTS (Texto a Voz) simule la generación de un 
    objeto de audio válido con propiedades esperadas (formato, duración, tamaño).
    """
    text_to_speak = "Pediré una bandeja paisa, ¿a qué hora llega?"
    expected_format = "mp3"
    
    # ACT: Simular la conversión TTS
    audio_output = voice_agent.tts(text_to_speak)
    
    # ASSERT 1: Verificar el tipo de objeto
    assert isinstance(audio_output, AudioData), "El TTS debe devolver un objeto AudioData."
    
    # ASSERT 2: Validar el formato requerido
    assert audio_output.format == expected_format, \
        f"ERROR: El formato de audio esperado era '{expected_format}', pero se recibió '{audio_output.format}'."
        
    # ASSERT 3: Validar que los datos de audio no están vacíos
    assert len(audio_output.data) > 0, "ERROR: Los datos de audio generados están vacíos."

    # ASSERT 4: Validar que la duración y el tamaño son proporcionales (no cero)
    # Usamos la longitud del texto como proxy para asegurar que no sean valores fijos.
    text_length = len(text_to_speak)
    assert audio_output.duration_ms > text_length * 50, \
        "ERROR: La duración simulada es muy corta o no proporcional al texto de entrada."
    assert audio_output.size_bytes > text_length * 100, \
        "ERROR: El tamaño de archivo simulado es muy pequeño o no proporcional al texto de entrada."


@pytest.mark.voice
def test_full_asr_tts_roundtrip_validation():
    """
    Valida el ciclo completo ASR/TTS: Texto -> Voz (simulada) -> Texto.
    El texto transcrito debe coincidir con el texto original.
    """
    original_text = "El Ajiaco Santaferño está listo para la orden."
    
    # 1. TTS: Convertir Texto a Audio (simulado)
    audio_data = voice_agent.tts(original_text)
    
    # 2. ASR: Convertir Audio de vuelta a Texto
    transcribed_text = voice_agent.asr(audio_data, original_text)
    
    # ASSERT 1: Validar la integridad de la transcripción
    assert transcribed_text == original_text, \
        f"ERROR: Fallo en el ciclo de voz. Original: '{original_text}', Transcrito: '{transcribed_text}'"
    
    # ASSERT 2: Validar insensibilidad a mayúsculas/minúsculas (robustez)
    assert original_text.lower() == transcribed_text.lower(), \
        "ERROR: La transcripción no coincide al comparar en minúsculas."
    
