from machine import Pin
import utime

led_verde = Pin(15, Pin.OUT)
led_amarelo = Pin(14, Pin.OUT)
led_vermelho = Pin(13, Pin.OUT)


cenarios = [
    (4000, 1500),   # Situacao 1 - energia suficiente
    (1800, 1500),   # Situacao 2 - energia limitada
    (1000, 1800),   # Situacao 3 - energia insuficiente
]


POTENCIA_RECARGA_COMPLETA = 2000  


def apagar_leds():
    led_verde.value(0)
    led_amarelo.value(0)
    led_vermelho.value(0)


def para_binario(valor):
    if valor < 0:
        return "-" + bin(abs(valor))[2:]
    return bin(valor)[2:]


def para_hexadecimal(valor):
    if valor < 0:
        return "-" + hex(abs(valor))[2:].upper()
    return hex(valor)[2:].upper()


def calcular_estado(geracao, consumo):
    """Processa os dados de entrada e decide o estado da sessao.

    Aqui e onde o 'processamento' do sistema acontece: os dados de
    entrada (geracao e consumo) sao combinados em uma unica
    informacao de saida (energia disponivel + estado).
    """
    disponivel = geracao - consumo

    if disponivel >= POTENCIA_RECARGA_COMPLETA:
        estado = "RECARGA AUTORIZADA"
    elif disponivel >= 0:
        estado = "RECARGA REDUZIDA"
    else:
        estado = "RECARGA BLOQUEADA"

    return disponivel, estado


def acionar_led(estado):
    apagar_leds()
    if estado == "RECARGA AUTORIZADA":
        led_verde.value(1)
    elif estado == "RECARGA REDUZIDA":
        led_amarelo.value(1)
    else:
        led_vermelho.value(1)


def exibir_dados(geracao, consumo, disponivel, estado):
    print("-" * 55)
    print("GERACAO: {} W   CONSUMO: {} W   DISPONIVEL: {} W".format(
        geracao, consumo, disponivel))
    print("STATUS: {}".format(estado))
    print("Representacao da potencia disponivel ({} W):".format(disponivel))
    print("  Decimal:     {}".format(disponivel))
    print("  Binario:     {}".format(para_binario(disponivel)))
    print("  Hexadecimal: {}".format(para_hexadecimal(disponivel)))
    print("-" * 55)


def processar_sessao(geracao, consumo):
    disponivel, estado = calcular_estado(geracao, consumo)
    acionar_led(estado)
    exibir_dados(geracao, consumo, disponivel, estado)


def main():
    while True:
        for geracao, consumo in cenarios:
            processar_sessao(geracao, consumo)
            utime.sleep(4)


main()
