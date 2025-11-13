import subprocess
import os


# Função para salvar o arquivo enviado na pasta 
def salvar_arquivo(arquivo, save_path):
    with open(save_path, "wb") as f:
        f.write(arquivo.getbuffer())
        print(f"Arquivo salvo em: {save_path}")





















#def office_para_pdf(arquivo):
    #diretório_saida = os.path.join("PDF", "documento_final.pdf")
    #caminho_soffice = r"C:\Program Files\LibreOffice\program\soffice.exe"