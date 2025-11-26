# 🔒 Conversor de PDF Seguro (Secure PDF Converter)

> Uma ferramenta desenvolvida para garantir a privacidade e segurança na conversão de documentos corporativos.

## 🎯 O Problema & A Solução

**O Cenário:** Trabalhando na área de infraestrutura, identifiquei um risco recorrente de segurança: colaboradores utilizavam sites públicos e não homologados para converter arquivos internos em PDF. Isso expunha documentos com informações sensíveis a servidores de terceiros sem garantia de confidencialidade.

**A Solução:** Desenvolvi esta aplicação em Python que realiza a conversão de arquivos (DOCX, Imagens e TXT) para PDF localmente ou em um ambiente controlado. O objetivo é oferecer a praticidade das ferramentas online, mas com a segurança de que os dados não serão armazenados ou processados por terceiros desconhecidos.

## 🚀 Funcionalidades

O sistema suporta a conversão dos seguintes formatos para PDF:

* **Documentos de Texto:** `.docx` (Utilizando a engine do LibreOffice para manter a formatação original).
* **Imagens:** `.jpg`, `.jpeg`, `.bmp`.
* **Texto Simples:** `.txt` (Conversão direta preservando a quebra de linhas).
* **Download Seguro:** O arquivo é processado e disponibilizado para download imediato, sem persistência desnecessária.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.11+
* **Interface (Frontend):** [Streamlit](https://streamlit.io/)
* **Manipulação de DOCX:** LibreOffice (Headless mode) & `subprocess`
* **Manipulação de Imagens:** Pillow (PIL)
* **Manipulação de Texto:** FPDF

## ⚙️ Como Executar o Projeto

### Pré-requisitos
1. Python instalado.
2. **LibreOffice** instalado na máquina (necessário para conversão de DOCX).
   - O script busca automaticamente por `soffice` ou `libreoffice` no PATH do sistema.


### Instalação
1. Clone este repositório:
   ```bash
   git clone [https://github.com/seu-usuario/conversor-pdf-seguro.git](https://github.com/seu-usuario/conversor-pdf-seguro.git)
   cd conversor-pdf-seguro
   
2. Instale as dependências:
```bash
   pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
   streamlit run app.py
```
4. Acesse no seu navegador (geralmente em http://localhost:8501).

   
### Teste do projeto

Projeto para teste On-line:
   https://conversor-de-pdf-gznaedwrwscwqsxl2flmse.streamlit.app/
