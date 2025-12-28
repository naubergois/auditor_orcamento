from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT

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
    
    # Title
    title = "AUDITOR ORÇAMENTO: Auditoria Inteligente com Agentes Autônomos"
    Story.append(Paragraph(title, styles['Title']))
    Story.append(Spacer(1, 12))
    
    subtitle = "14º Prêmio SOF - Categoria: Soluções em dados orçamentários"
    Story.append(Paragraph(subtitle, styles['Heading2']))
    Story.append(Spacer(1, 24))

    # 1. Problema orçamentário
    Story.append(Paragraph("1. Problema Orçamentário", styles['SectionHeader']))
    text_problem = """
    A gestão orçamentária pública enfrenta desafios críticos como a <b>fragmentação de dados</b>, 
    a <b>complexidade legislativa</b> (milhares de páginas de LOA, LDO e Notas Técnicas) e a 
    <b>dificuldade de auditoria em tempo real</b>. Atualmente, a identificação de riscos e 
    inconsistências depende de revisão manual exaustiva, lenta e propensa a erros humanos, 
    comprometendo a previsibilidade e a eficiência do gasto público.
    """
    Story.append(Paragraph(text_problem, styles['Justify']))
    Story.append(Spacer(1, 12))

    # 2. Descrição da Solução
    Story.append(Paragraph("2. Descrição da Solução", styles['SectionHeader']))
    
    Story.append(Paragraph("Arquitetura e Tecnologias", styles['SubSection']))
    text_arch = """
    A solução é uma plataforma web baseada em <b>Agentes de Inteligência Artificial Generativa (LLMs)</b>.
    Utiliza o modelo <b>Google Gemini 2.0 Flash</b> pela sua alta capacidade de contexto e raciocínio lógico.
    A arquitetura é modular, composta por:
    """
    Story.append(Paragraph(text_arch, styles['Justify']))
    
    bullet_list = ListFlowable([
        ListItem(Paragraph("<b>AuditorAgent:</b> Identifica riscos fiscais e impropriedades.", styles['Normal'])),
        ListItem(Paragraph("<b>ComplianceAgent:</b> Verifica aderência à LRF e Constituição.", styles['Normal'])),
        ListItem(Paragraph("<b>ConsistencyAgent:</b> Valida integridade numérica e lógica.", styles['Normal'])),
        ListItem(Paragraph("<b>ExplainabilityAgent:</b> Traduz achados técnicos para linguagem cidadã.", styles['Normal'])),
        ListItem(Paragraph("<b>Orchestrator:</b> Coordena a execução paralela dos agentes.", styles['Normal'])),
    ], bulletType='bullet', start='circle')
    Story.append(bullet_list)
    Story.append(Spacer(1, 12))

    Story.append(Paragraph("Fluxo de Funcionamento", styles['SubSection']))
    text_flow = """
    1. O usuário faz upload do PDF (ex: Projeto de Lei Orçamentária).<br/>
    2. O sistema extrai o texto e o distribui para os agentes especializados.<br/>
    3. Cada agente analisa o documento sob sua ótica (risco, lei, matemática).<br/>
    4. O Orchestrator consolida os resultados.<br/>
    5. A interface Streamlit apresenta um painel interativo com alertas e relatórios.
    """
    Story.append(Paragraph(text_flow, styles['Justify']))
    Story.append(Spacer(1, 12))

    # 3. Demonstração de Funcionalidade
    Story.append(Paragraph("3. Demonstração de Funcionalidade", styles['SectionHeader']))
    text_demo = """
    <b>O que já funciona hoje (MVP):</b><br/>
    - Upload e leitura de PDFs orçamentários.<br/>
    - Análise completa via API do Google Gemini (Agentes ativos).<br/>
    - Identificação automática de déficits e violações da LRF.<br/>
    - Geração de explicação didática para leigos.<br/><br/>
    <b>Protótipo Avançado:</b><br/>
    - Integração com bases de dados do SIAFI (planejado).<br/>
    - Ajuste fino (Fine-tuning) com histórico de pareceres do TCU.
    """
    Story.append(Paragraph(text_demo, styles['Justify']))
    Story.append(Spacer(1, 12))

    # 4. Impacto Esperado
    Story.append(Paragraph("4. Impacto Esperado", styles['SectionHeader']))
    
    impact_items = ListFlowable([
        ListItem(Paragraph("<b>Transparência:</b> Permite que qualquer cidadão 'audite' o orçamento e entenda seus riscos.", styles['Normal'])),
        ListItem(Paragraph("<b>Eficiência:</b> Reduz o tempo de primeira análise de dias para segundos.", styles['Normal'])),
        ListItem(Paragraph("<b>Controle Social:</b> Empodera conselhos e ONGs com pareceres técnicos automáticos.", styles['Normal'])),
        ListItem(Paragraph("<b>Apoio à Decisão:</b> Gestores recebem alertas preventivos antes da execução da despesa.", styles['Normal'])),
    ], bulletType='bullet', start='circle')
    Story.append(impact_items)
    Story.append(Spacer(1, 12))

    # 5. Viabilidade
    Story.append(Paragraph("5. Viabilidade e Aderência", styles['SectionHeader']))
    text_viab = """
    <b>Infraestrutura Comum:</b> Roda em nuvem padrão (Streamlit Cloud, AWS, GCP) sem necessidade de GPUs dedicadas (uso de API).<br/>
    <b>Software Livre:</b> Desenvolvido em Python (Open Source).<br/>
    <b>Aderência ao Ciclo:</b> Atua transversalmente no Planejamento (análise da LOA/LDO) e na Avaliação (relatórios de gestão).
    """
    Story.append(Paragraph(text_viab, styles['Justify']))
    
    # Footer info
    Story.append(Spacer(1, 36))
    Story.append(Paragraph("Documento gerado automaticamente pelo Auditor Orçamento", styles['Italic']))

    doc.build(Story)

if __name__ == "__main__":
    output_pdf = "Apresentacao_Solucao_Auditor_Orcamento.pdf"
    create_presentation_pdf(output_pdf)
    print(f"PDF de apresentação gerado: {output_pdf}")
