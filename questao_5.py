"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

    a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente
    definida no código;

    b) Evite usar funções prontas, como, por exemplo, reverse;
"""
n = str(input("Digite a palavra para inverter: "))


def inverta_string(string: str):
    str_ = ""
    for char in string:
        str_ = char + str_
    return str_


print(inverta_string(n))
