from fpdf import FPDF


def converter_txt_para_pdf(arquivo):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    tamanho = len(arquivo)
    cont = 0

    while cont < tamanho:
        if arquivo[cont] != "\n":
            linha = ""
            while cont < tamanho and arquivo[cont] != "\n":
                linha += arquivo[cont]
                cont += 1
            pdf.cell(200, 10, txt=linha, ln=True)
            
        else:
            cont += 1



            
    pdf.output("PDF/documento_final.pdf")