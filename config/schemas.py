 # config/schemas.py
 # Schemas JSON para validación de respuestas de la API con respuesta exitosa (200) y de error (400).
response_schema = {
    "type": "object",
    "properties": {
        "restaurant_id": {"type": "string"},
        "api_status": {"type": "string", "enum": ["operacional", "mantenimiento"]},
        "timestamp": {"type": "string", "format": "date-time"},
        "data": {
            "type": "object",
            "properties": {
                "intent": {"type": "string", "enum": ["CONSULTA_MENU", "ORDEN_PLACED"]},
                "message": {"type": "string"}
            },
            "required": ["intent", "message"]
        }
    },
    "required": ["restaurant_id", "api_status", "timestamp", "data"],
    "additionalProperties": False 
}

error_schema = {
    "type": "object",
    "properties": {
        "error": {"type": "string"},
        "code": {"type": "integer"}
    },
    "required": ["error", "code"],
    "additionalProperties": False
}
