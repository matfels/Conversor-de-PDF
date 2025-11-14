import os
# Função para salvar o arquivo enviado na pasta 
def salvar_arquivo(arquivo, save_path):
    file_name = os.path.basename(arquivo.name)
    print(file_name, "asdasda")
    with open(save_path, "wb") as f:
        f.write(arquivo.getbuffer())
        print(f"Arquivo salvo em: {save_path}")
