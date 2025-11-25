import os
import subprocess
import shutil

def converter_docx_para_pdf(nome_arquivo):
    caminho_soffice = shutil.which("soffice") or shutil.which("libreoffice")

    pasta = "uploads"
    caminho_arquivo = os.path.join(pasta, nome_arquivo)

    # Verifica se o LibreOffice está instalado no caminho especificado
    if not os.path.exists(caminho_soffice):
        print(f"Arquivo {caminho_soffice} não encontrado.")
        return None

    # Passando os caminhos da pasta de entrada e saída
    arquivo_entrada = os.path.abspath(caminho_arquivo) # Define o caminho do arquivo de entrada
    pasta_saida = "PDF" # Define a pasta de saída
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)
    print("Convertendo arquivo DOCX para PDF...")

    # Comando para chamar o LibreOffice em modo headless
    comando = [
        caminho_soffice,
        '--headless',
        '--convert-to', 'pdf',
        '--outdir', pasta_saida,
        arquivo_entrada
    ]


    try:

        resultado = subprocess.run(comando, check=True, capture_output=True, text=True, timeout=30)
        caminho_arquivo_pdf = os.path.join("PDF")
        print(f"Arquivo convertido salvo em: {caminho_arquivo_pdf}")
        return None
    except FileNotFoundError:
        print("Erro: LibreOffice não encontrado. Verifique o caminho do executável.")   
        return None
    except subprocess.CalledProcessError as e:
        print("Erro durante a conversão:", e.stderr)
        return None
    except subprocess.TimeoutExpired:
        print("Erro: A conversão demorou muito tempo e foi cancelada.")
        return None
    