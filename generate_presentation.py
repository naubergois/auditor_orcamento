from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, Image, PageBreak
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from PIL import Image as PILImage
import os

def get_image_with_aspect(path, target_width):
    if not os.path.exists(path):
        return None
    try:
        img = PILImage.open(path)
        w, h = img.size
        return Image(path, width=target_width, height=target_width * h / w)
    except:
        return None

def create_presentation_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='SectionHeader', 
                              parent=styles['Heading2'], 
                              fontSize=14, 
                              spaceAfter=10, 
                              textColor=colors.HexColor("#1f77b4")))
    styles.add(ParagraphStyle(name='SubSection',
                              parent=styles['Heading3'],
                              fontSize=12,
                              textColor=colors.HexColor("#2c3e50")))

    Story = []
    
    # Logo
    logo = get_image_with_aspect("logo.png", 120)
    if logo:
        Story.append(logo)
        Story.append(Spacer(1, 12))

    # Title
    title = "AUDITOR ORÇAMENTO: Auditoria Inteligente com Agentes Autônomos"
    Story.append(Paragraph(title, styles['Title']))
    Story.append(Spacer(1, 12))
    
    subtitle = "14º Prêmio SOF - Categoria: Soluções em dados orçamentários"
    Story.append(Paragraph(subtitle, styles['Heading2']))
    Story.append(Spacer(1, 24))

    # 1. Problema orçamentário
    Story.append(Paragraph("1. Problema Orçamentário Claramente Delimitado", styles['SectionHeader']))
    text_problem = """
    A <b>gestão pública</b> enfrenta desafios críticos como a <b>fragmentação de dados</b>, 
    a complexidade legislativa e a dificuldade de auditoria tempestiva. A falta de ferramentas modernas 
    gera baixa previsibilidade e dificulta o <b>controle social</b>. O problema central é a incapacidade 
    de processar o volume massivo de documentos orçamentários (LOA, LDO) em tempo hábil para evitar 
    desperdícios, resultando em ineficiência e riscos fiscais.
    """
    Story.append(Paragraph(text_problem, styles['Justify']))
    Story.append(Spacer(1, 12))

    # 2. Descrição da Solução
    Story.append(Paragraph("2. Descrição da Solução", styles['SectionHeader']))
    
    Story.append(Paragraph("Arquitetura e Tecnologias", styles['SubSection']))
    text_arch = """
    A solução é uma plataforma de <b>Auditoria Inteligente</b> baseada em Agentes Autônomos. 
    <b>Tecnologias usadas:</b> Inteligência Artificial Generativa (LLM Google Gemini 2.0 Flash), 
    Processamento de Linguagem Natural (NLP), automação em Python e dashboards interativos (Streamlit).
    """
    Story.append(Paragraph(text_arch, styles['Justify']))
    Story.append(Spacer(1, 6))

    # 2.1 Visual Architecture Slide
    Story.append(Paragraph("Arquitetura Visual", styles['SubSection']))
    im_arch = get_image_with_aspect("architecture_didactic.png", 500)
    if im_arch:
        Story.append(im_arch)
    Story.append(Spacer(1, 12))

    Story.append(Paragraph("Fluxo de Funcionamento", styles['SubSection']))
    text_flow = """
    1. <b>Upload:</b> Gestor ou cidadão envia o arquivo (PDF da Lei Orçamentária).<br/>
    2. <b>Processamento:</b> O sistema extrai dados não estruturados.<br/>
    3. <b>Agentes de IA:</b> Quatro agentes especializados analisam riscos, auditoria, compliance e consistência.<br/>
    4. <b>Orquestração:</b> Consolidação dos achados.<br/>
    5. <b>Visualização:</b> Apresentação amigável para tomada de decisão.
    """
    Story.append(Paragraph(text_flow, styles['Justify']))
    Story.append(Spacer(1, 12))

    # 3. Demonstração de Funcionalidade
    Story.append(Paragraph("3. Demonstração de Funcionalidade", styles['SectionHeader']))
    text_demo = """
    A solução possui foco total em <b>demonstração prática</b> e usabilidade:<br/><br/>
    <b>O que já funciona hoje:</b> Leitura de documentos, identificação de riscos orçamentários, validação da LRF e geração de relatórios simplificados.<br/>
    <b>O que está em protótipo avançado:</b> Cruzamento de dados com bases do SIAFI e análise preditiva de receitas.
    """
    Story.append(Paragraph(text_demo, styles['Justify']))
    Story.append(Spacer(1, 12))

    # 4. Impacto Esperado
    Story.append(Paragraph("4. Impacto Esperado", styles['SectionHeader']))
    
    impact_items = ListFlowable([
        ListItem(Paragraph("<b>Transparência:</b> Traduz o 'economês' para linguagem simples, ampliando o entendimento do cidadão.", styles['Normal'])),
        ListItem(Paragraph("<b>Eficiência:</b> Reduz meses de trabalho manual de auditoria para poucos segundos.", styles['Normal'])),
        ListItem(Paragraph("<b>Controle Social:</b> Gera alto <b>impacto social</b> ao empoderar a sociedade com dados auditados.", styles['Normal'])),
        ListItem(Paragraph("<b>Apoio à Decisão:</b> Fornece insumos técnicos rápidos para gestores corrigirem rumos.", styles['Normal'])),
    ], bulletType='bullet', start='circle')
    Story.append(impact_items)
    Story.append(Spacer(1, 12))

    # 5. Viabilidade
    Story.append(Paragraph("5. Viabilidade", styles['SectionHeader']))
    text_viab = """
    <b>Execução em infraestrutura comum:</b> A solução roda 100% em nuvem (SaaS), acessível de qualquer navegador, sem custos com servidores físicos.<br/>
    <b>Uso de software livre:</b> Todo o código base é Open Source (Python/Streamlit).<br/>
    """
    Story.append(Paragraph(text_viab, styles['Justify']))
    Story.append(Spacer(1, 6))

    Story.append(Paragraph("Aderência ao ciclo orçamentário", styles['SubSection']))
    text_cycle = """
    A ferramenta adere perfeitamente às fases de <b>Planejamento</b> (análise prévia da LOA) e <b>Avaliação</b> (auditoria de contas), fortalecendo a governança pública.
    """
    Story.append(Paragraph(text_cycle, styles['Justify']))
    
    # Footer info
    Story.append(Spacer(1, 36))
    Story.append(Paragraph("Documento técnico gerado automaticamente para o 14º Prêmio SOF", styles['Italic']))

    doc.build(Story)

if __name__ == "__main__":
    output_pdf = "Apresentacao_Solucao_Auditor_Orcamento.pdf"
    create_presentation_pdf(output_pdf)
    print(f"PDF de apresentação gerado: {output_pdf}")
