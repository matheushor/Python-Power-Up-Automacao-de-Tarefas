# passo a passo do projeto
# passo 1: entrar no sistema da empresa  
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# passo 2: fazer login
# passo 3: importar a base de dados de produtos
# passo 4: cadastrar um produto
# passo 5: repetir cadastro para todos os produtos

# pyautogui.click > clicar com o mouse
# pyautogui.write > escrever texto
# pyautogui.press > apertar 1 tecla
# pyautogui.hotkey > combinação de teclas

#----------------------------------------------------------------

#importando blibioteca 
import pyautogui
import time
import pandas

#pausa do tempo para inicar cada tarefa
pyautogui.PAUSE = 0.7

#passo 1:
#apertar windows
#ecrever nome do navegador
#apertar enter

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

#entrando no link
# clicks = 2 (exemplo de click duplo)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#esperando o site carregar
time.sleep(2)

#login
pyautogui.click(x=1355, y=342)
pyautogui.write("matheushenriqueor@gmail.com")
pyautogui.press("tab")
pyautogui.write("matheus1234")
pyautogui.press("tab")
pyautogui.press("enter")

#esperando o site carregar
time.sleep(2)

#importando a base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    #cadastrar um produto
    pyautogui.click(x=1222, y=236)



    #prencher os campos
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("Tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("Tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("Tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("Tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("Tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("Tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
       pyautogui.write(str(obs))

    #apertar para enviar

    pyautogui.press("Tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000)
    


    