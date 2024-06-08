import tkinter as tk
import random
import string

def gerar_senha():
    tamanho = 12  # Tamanho da senha (você pode ajustar conforme necessário)
    caracteres = string.ascii_letters + string.digits + string.punctuation

    senha_aleatoria = ''.join(random.choice(caracteres) for _ in range(tamanho))
    label_resultado.config(text=f"Senha gerada: {senha_aleatoria}")

# Criar a janela
janela = tk.Tk()
janela.title("Gerador de Senhas Aleatórias")

# Botão "Gerar Senha"
botao_gerar_senha = tk.Button(janela, text="Gerar Senha", command=gerar_senha)
botao_gerar_senha.pack()

# Resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

# Iniciar a janela
janela.mainloop()
