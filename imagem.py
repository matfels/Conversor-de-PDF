from PIL import Image


caminho_pdf = "PDF/documento_final.pdf"

def converter_imagem_para_pdf(arquivo):

    try:
        imagem = Image.open(arquivo)

        imagem_convertida = imagem.convert('RGB')

        imagem_convertida.save(caminho_pdf)
        print("Arquivo convertido e salvo como:", caminho_pdf)
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_pdf} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

        """
        imagem = Image.open(arquivo)
        imagem_convertida = imagem.convert('RGB')
        imagem_convertida.save(caminho_saida)
        """