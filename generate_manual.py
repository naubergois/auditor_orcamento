from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

def create_manual_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    
    Story = []
    
    # Title
    title = "AUDITOR ORÇAMENTO: Manual de Uso e Arquitetura"
    Story.append(Paragraph(title, styles['Title']))
    Story.append(Spacer(1, 12))
    
    # 1. Access
    Story.append(Paragraph("1. Acesso à Aplicação", styles['Heading2']))
    text_access = """
    A aplicação está disponível online e pode ser acessada gratuitamente através do link abaixo:
    """
    Story.append(Paragraph(text_access, styles['Normal']))
    Story.append(Spacer(1, 10))
    
    link = '<link href="https://auditororcamento.streamlit.app/"><u>https://auditororcamento.streamlit.app/</u></link>'
    Story.append(Paragraph(link, styles['Heading3']))
    Story.append(Spacer(1, 24))

    # 2. Architecture
    Story.append(Paragraph("2. Arquitetura do Sistema", styles['Heading2']))
    text_arch = """
    O sistema utiliza uma arquitetura baseada em microsserviços de Agentes de IA. O fluxo de dados
    começa com o upload do usuário, passa pelo processamento local do Streamlit e é enviado via API
    segura para o modelo Google Gemini 2.0 Flash.
    """
    Story.append(Paragraph(text_arch, styles['Justify']))
    Story.append(Spacer(1, 12))
    
    try:
        # Embed Architecture Image
        im = Image("architecture_diagram.png", width=400, height=300)
        Story.append(im)
        Story.append(Paragraph("Figura 1: Diagrama de Arquitetura em Agentes", styles['Center']))
    except:
        Story.append(Paragraph("[Imagem da Arquitetura não disponível]", styles['Center']))

    Story.append(Spacer(1, 24))

    # 3. Usage Guide
    Story.append(Paragraph("3. Como Usar", styles['Heading2']))
    
    steps = [
        "<b>Passo 1:</b> Acesse o link da aplicação.",
        "<b>Passo 2:</b> No menu lateral, escolha 'Usar Exemplo (Mock)' para um teste rápido ou 'Upload PDF' para analisar seu próprio arquivo.",
        "<b>Passo 3:</b> Clique no botão 'Executar Auditoria Inteligente'.",
        "<b>Passo 4:</b> Aguarde alguns segundos enquanto os agentes processam.",
        "<b>Passo 5:</b> Navegue pelas abas 'Riscos', 'Compliance', 'Consistência' e 'Explicação' para ver os resultados detalhados."
    ]
    
    for step in steps:
        Story.append(Paragraph(step, styles['Normal']))
        Story.append(Spacer(1, 8))

    doc.build(Story)

if __name__ == "__main__":
    create_manual_pdf("Manual_Uso_Auditor_Orcamento.pdf")
    print("PDF Manual gerado com sucesso.")
