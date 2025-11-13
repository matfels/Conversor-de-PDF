import streamlit as st
from imagem import converter_imagem_para_pdf
from txt import converter_txt_para_pdf

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
        

