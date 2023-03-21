# Importei as bibliotecas

import pandas as pd
import pyautogui as py
import time
# Dando as opções para o usuário escolher seu arquivo/coluna
arquivo = input('Coloque o Arquivo na pasta e digite o nome dele.')
coluna = input('Nome Coluna: ')
# Pegando uma tebela, transformando tudo em string para poder digitar e colocar todos os itens de uma coluna em uma lista
df = pd.DataFrame(pd.read_csv(arquivo))
df = df.applymap(str)
lista = df[coluna].tolist()

# Obtendo a quantidade de repetição com base na quantidade de itens
total = len(lista)
i = 0

time.sleep(5)
# Loop para realizar a digitação
while i <= total:
    py.write(lista[0])
    py.press('enter')
    lista.pop(0)
    i = i + 1
    if i == total:
        print('acabou')
        break
print('finalizado!')
