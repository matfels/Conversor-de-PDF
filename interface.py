import streamlit as st
import os
from imagem import converter_imagem_para_pdf
from txt import converter_txt_para_pdf
from office import salvar_arquivo

# Configuração da interface do Streamlit
st.set_page_config(
    page_title="Converter para PDF",
    page_icon="📄",
    layout="centered"
)

st.title("Conversor de PDF 📄") # Título do aplicativo
st.header("-----------------------------------") # Cabeçalho
st.write("Objetivo converter arquivo em PDF de forma segura.") # Texto simples


# Seleção do tipo de conversão e upload do arquivo
tipo = st.selectbox("Selecione o tipo de conversão que deseja:", ["JPEG","JPG" , "BMP","TXT", "DOCX", ])
arquivo = st.file_uploader(f"Escolha um arquivo {tipo} para converter em PDF", type=[tipo])



# Condiconal para processar o arquivo enviado
if arquivo is not None:

# ---------------------- JPEG/JPG/BMP ----------------------
    if tipo == "JPEG" or tipo == "JPG" or tipo == "BMP":
        converter_imagem_para_pdf(arquivo)
        st.download_button(
            label="Baixar PDF convertido",
            data=open("PDF/documento_final.pdf", "rb").read(),
            file_name="documento_final.pdf",
            mime="application/pdf"
        )
        print("Conversão concluída com sucesso!")


# -------------------------- TXT ----------------------------
    elif tipo == "TXT":
        
        texto = arquivo.read() #converter "objeto arquivo" para "bytes"
        texto = texto.decode("utf-8") #converter "bytes" para "string"

        converter_txt_para_pdf(texto)
        st.download_button(
            label="Baixar PDF convertido",
            data=open("PDF/documento_final.pdf", "rb").read(),
            file_name="documento_final.pdf",
            mime="application/pdf"
        )
        
        print("Conversão concluída com sucesso!")

# -------------------------- DOCX ---------------------------
    elif tipo == "DOCX":
        upload_diretory = "uploads"
        os.makedirs(upload_diretory, exist_ok=True) #cria a pasta "uploads", caso não exista
        
        file_name = os.path.basename(arquivo.name) # Pega o nome do arquivo enviado
        save_path = os.path.join(upload_diretory, file_name) # Cria o caminho completo para salvar o arquivo
        salvar_arquivo(arquivo, save_path)



