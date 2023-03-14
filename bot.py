import pyautogui as py
import time

time.sleep(5)

py.press('win')
py.write('edge')
py.press('enter')
time.sleep(2)
py.write('https://login.microsoftonline.com/f8c68086-b95c-49cb-9d38-ed37940abef5/oauth2/authorize?client_id=e95c4605-aeab-48d9-9c36-1a262ef8048e&redirect_uri=https%3A%2F%2Faccounts.cloud.com%2Fcore%2Flogin-azuread&resource=https%3A%2F%2Fgraph.microsoft.com%2F&response_type=code%20id_token&scope=openid%20email&response_mode=form_post&nonce=638144144362233522.YWNmMGRiYmYtM2MyNS00NWNlLTg1ZDItMTgyZmNiMmY4NGU5OTBiOTg3YzMtZmU1NC00NzRlLTllMzItMTAzZTY1MTdiZThj&prompt=login&state=CfDJ8LclyOhazMdJkkZzS2eIseVfXT8lv_pcJjKfQxVUlrgeAcdQ9JjVAGtRAS_lafCrNxLdVDTYAWX_vkn7jkr2KUnSmUWffmwUqJtEvRha6eaI8F3mB5hQQdOVe763xLTguzIQyvIAHrGEHTGMMi4eNXB7HD-s6UTCazlKg0eWRJSh&x-client-SKU=ID_NET461&x-client-ver=5.3.0.0')
py.press('enter')

resposta = input('deseja iniciar a segunda fase? y/n')
if resposta != 'n':
    print('Por favor, responda com apenas (n) ou (y)')

if resposta != 'y':
    print('Por favor, responda com apenas (n) ou (y)')

if resposta == 'y':
    time.sleep(5)
    py.press('2')
    py.press('2')
    py.write('18')
    py.press('enter')
    py.write('13')
    py.press('enter')
    py.write('448')
    py.press('enter')
    py.press('enter')
    py.press('enter')
if resposta == 'n':
    print('processo encerrado')

