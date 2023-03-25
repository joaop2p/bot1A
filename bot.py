# Importei as bibliotecas
import pandas as pd
import pyautogui as py
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # para esconder a janela principal
NomeArquivo = askopenfilename() # mostra uma caixa de diálogo para o usuário selecionar um arquivo
# Pegando uma tebela, transformando tudo em string para poder digitar e colocar todos os itens de uma coluna em uma lista
df = pd.DataFrame(pd.read_csv(NomeArquivo))
ordem = df.sort_values(by='UC')
df = ordem.applymap(str)
lista = df['NCT'].tolist()
# Obtendo a quantidade de repetição com base na quantidade de itens
QuantidadeFeita = len(lista)
resposta = input('Você tem certeza que deseja realizar toda a digitação desse aquivo?')
if resposta == 'S':
    print('Você tem 5 segundos para colocar no local em quer realizar a digitação')
    time.sleep(5)
    # Loop para realizar a digitação
    for item in lista:
        py.write(item)
        py.press('enter')
    print('finalizado! Foram Realizadas:', QuantidadeFeita, ' preenchimentos.')
    time.sleep(5)
else:
    exit()