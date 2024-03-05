"""
4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente.
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser.
Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada
lâmpada?
"""
RESPOSTA = """
    Deixaria o interruptor 1 ligado, o interruptor 2 ligado por 12 minutos e interruptor 3 desligado.
    eu iria até as 3 salas e verificaria: 
        - se a sala estiver com lâmpada acesa então é interruptor 1
        - se a sala estiver com lâmpada apagado e quente então é interruptor 2 
        - se a sala estiver com lâmpada apagado e fria então é interruptor 3
"""
