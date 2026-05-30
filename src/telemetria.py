import random
from datetime import datetime

def gerar_telemetria() -> dict:
    """
    Gera um payload simulado de telemetria do satélite ConnectSat.
    Monitora Comunicação, Energia e Temperatura.
    """
    payload = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        # Parâmetro 1: Comunicação (Latência em milissegundos)
        "comunicacao_latencia_ms": round(random.uniform(20.0, 150.0), 2),
        # Parâmetro 1.1: Comunicação (Throughput em Mbps)
        "comunicacao_throughput_mbps": round(random.uniform(50.0, 500.0), 2),
        # Parâmetro 2: Energia (Nível de bateria em porcentagem)
        "energia_bateria_pct": round(random.uniform(65.0, 100.0), 2),
        # Parâmetro 3: Temperatura (Carga térmica do transponder em Celsius)
        "temperatura_transponder_c": round(random.uniform(40.0, 95.0), 2)
    }
    
    return payload

if __name__ == "__main__":
    # Teste de execução direta
    print("Gerando telemetria de teste:")
    print(gerar_telemetria())