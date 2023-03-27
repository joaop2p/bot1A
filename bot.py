# Importei as bibliotecas
import pandas as pd
import pyautogui as py
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# para esconder a janela principal
Tk().withdraw() 
while True:
# mostra uma caixa de diálogo para o usuário selecionar um arquivo
    NomeArquivo = askopenfilename()
    # Pegando uma tebela, transformando tudo em string para poder digitar e colocar todos os itens de uma coluna em uma lista
    df = pd.DataFrame(pd.read_csv(NomeArquivo))
    ordem = df.sort_values(by='UC')
    df = ordem.applymap(str)
    lista = df['NCT'].tolist()

    # Obtendo a quantidade de repetição com base na quantidade de itens
    QuantidadeFeita = len(lista)
    resposta = input('Você tem certeza que deseja realizar toda a digitação desse aquivo?[S/N]')

    if resposta == 'S':
        print('Você tem 5 segundos para colocar no local em quer realizar a digitação')
        time.sleep(5)
        
        start_time = time.time()
        # Loop para realizar a digitação
        for item in lista:
            py.write(item)
            py.press('enter')
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('finalizado! Foram Realizadas:', QuantidadeFeita, ' preenchimentos.')
        print(f'Tempo de execução: {elapsed_time:.2f} segundos')
        time.sleep(5)

    else:
        exit()
    contiuar = input('Deseja realizar um novo procedimento?[S/N]')
    if contiuar != 'S':
        break