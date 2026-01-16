import pyautogui as pg
import time as tm
import pandas as pd

# Em cada operação ele vai esperar 0,2 segundos
pg.PAUSE = 0.5

# 1. Abre o menu iniciar
pg.press("win")

# 2 Escreve (Corrigi de "Egde" para "Edge")
pg.write("Edge")

# 3. Aperta enter
pg.press("enter")

# 4. Digitando na barra de URL do navegador
# setando um time de espera de 2 segundos para esperar o navegador entrar
tm.sleep(2.5)
url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pg.write(url)
pg.press("enter")

# 5. Clicando num campo específico
tm.sleep(2)
pg.click(x=888, y=369)
tm.sleep(2)
pg.write("testando@gmail.com")

# 6. Indo para o campo de senha   

pg.press("tab")
pg.write("testando")

# 7. Logando
pg.press("tab")
pg.press("enter")
tm.sleep(3)

# 8. abrindo base de dados
file = r"C:\Users\athos\OneDrive\Área de Trabalho\python\hashtag\imports\aula1\produtos.csv"
df = pd.read_csv(file)
print(df)

# 9. clicando no primeiro campo de cadastro
for linha in df.index:
    tm.sleep(3)
    pg.click(x=828, y=253)
    pg.write(str(df.loc[linha, 'codigo']))
    pg.press("tab")
    pg.write(str(df.loc[linha, 'marca']))
    pg.press("tab")
    pg.write(str(df.loc[linha, 'tipo']))
    pg.press("tab")
    pg.write(str(df.loc[linha, 'categoria']))
    pg.press("tab")
    pg.write(str(df.loc[linha, 'preco_unitario']))
    pg.press("tab")
    pg.write(str(df.loc[linha, 'custo']))
    pg.press("tab")
    if (str(df.loc[linha, 'obs']) != 'nan'):
        pg.write(str(df.loc[linha, 'obs']))
        pg.press("tab")
    else:
        pg.press("tab")
    pg.press("enter")

    #voltando para o inicio da tela
    pg.scroll(5000)