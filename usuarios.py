import tkinter as tk
import random

def gerar_usuario():
    nomes = ["Alice", "Bob", "Carol", "David", "Eva", "Frank", "Grace", "Helen", "Ivan", "Julia"]
    sobrenomes = ["Smith", "Johnson", "Brown", "Lee", "Garcia", "Wang", "Kim", "Lopez", "Chen", "Nguyen"]

    nome_aleatorio = random.choice(nomes)
    sobrenome_aleatorio = random.choice(sobrenomes)
    usuario_aleatorio = f"{nome_aleatorio} {sobrenome_aleatorio}"

    label_resultado.config(text=f"Usuário gerado: {usuario_aleatorio}")

# Criar a janela
janela = tk.Tk()
janela.title("Gerador de Usuários Aleatórios")

# Botão "Gerar"
botao_gerar = tk.Button(janela, text="Gerar", command=gerar_usuario)
botao_gerar.pack()

# Resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

# Iniciar a janela
janela.mainloop()
