def verificar_limites(dados_telemetria: dict) -> list:
    """
    Aplica regras de decisão (thresholds) sobre os dados de telemetria.
    Retorna uma lista de alertas caso parâmetros estejam fora do limite seguro.
    """
    alertas = []
    
    # 1. Regra de Temperatura (Threshold Crítico: > 85°C)
    if dados_telemetria.get("temperatura_transponder_c", 0) > 85.0:
        alertas.append({
            "severidade": "CRITICO",
            "parametro": "temperatura_transponder_c",
            "valor_atual": dados_telemetria["temperatura_transponder_c"],
            "mensagem": "Superaquecimento detectado no transponder. Risco iminente de falha de hardware."
        })
        
    # 2. Regra de Comunicação (Threshold de Alerta: Latência > 100ms)
    if dados_telemetria.get("comunicacao_latencia_ms", 0) > 100.0:
        alertas.append({
            "severidade": "ALERTA",
            "parametro": "comunicacao_latencia_ms",
            "valor_atual": dados_telemetria["comunicacao_latencia_ms"],
            "mensagem": "Latência de uplink elevada. Degradação perceptível em serviços de telemedicina."
        })
        
    # 3. Regra de Energia (Threshold de Aviso: Bateria < 75%)
    if dados_telemetria.get("energia_bateria_pct", 100) < 75.0:
        alertas.append({
            "severidade": "AVISO",
            "parametro": "energia_bateria_pct",
            "valor_atual": dados_telemetria["energia_bateria_pct"],
            "mensagem": "Nível de bateria caindo mais rápido que o esperado. Verificar alinhamento dos painéis solares."
        })
        
    return alertas

if __name__ == "__main__":
    # Teste de execução direta com dados controlados
    dados_teste = {
        "temperatura_transponder_c": 90.5, # Deve disparar CRITICO
        "comunicacao_latencia_ms": 110.2,  # Deve disparar ALERTA
        "energia_bateria_pct": 70.0        # Deve disparar AVISO
    }
    
    print("Avaliando dados de teste...")
    resultado_alertas = verificar_limites(dados_teste)
    for alerta in resultado_alertas:
        print(f"[{alerta['severidade']}] {alerta['mensagem']}")