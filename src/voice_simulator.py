# src/voice_simulator.py
from dataclasses import dataclass
import time
import random

@dataclass
class AudioData:
    """Clase para simular las propiedades del archivo de audio generado."""
    data: bytes
    format: str
    duration_ms: int
    size_bytes: int

class VoiceSimulator:
    """Simula la conversión ASR (Voz a Texto) y TTS (Texto a Voz)."""
    
    def tts(self, text: str) -> AudioData:
        """Simula la conversión de Texto a Voz (TTS)."""
        
        # Simular la duración y el tamaño basado en la longitud del texto
        text_length = len(text)
        # Asignar un rango de duración y tamaño proporcional
        duration_ms = text_length * random.randint(50, 80) 
        size_bytes = text_length * random.randint(100, 150) 
        
        mock_audio_content = f"mock_audio_for_{text}".encode('utf-8') 
        
        return AudioData(
            data=mock_audio_content,
            format="mp3", # Validar que el formato es mp3
            duration_ms=duration_ms,
            size_bytes=size_bytes
        )

    def asr(self, audio_data: AudioData, expected_text: str) -> str:
        """Simula la conversión de Voz a Texto (ASR).
        
        Para propósitos de QA, simulamos que el ASR recupera el texto esperado
        para validar el ciclo completo.
        """
        
        # Simular un pequeño tiempo de procesamiento ASR (<5ms)
        time.sleep(0.005) 
        
        # Simular la transcripción perfecta para la prueba de "roundtrip"
        return expected_text

voice_agent = VoiceSimulator()