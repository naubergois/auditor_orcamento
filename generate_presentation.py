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
                            rightMargin=60, leftMargin=60,
                            topMargin=60, bottomMargin=60)
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', 
                              parent=styles['Normal'], 
                              alignment=TA_JUSTIFY, 
                              fontSize=12, 
                              leading=18,
                              spaceAfter=12))
    styles.add(ParagraphStyle(name='SectionHeader', 
                              parent=styles['Heading1'], 
                              fontSize=18, 
                              leading=22,
                              spaceAfter=16, 
                              spaceBefore=24,
                              textColor=colors.HexColor("#1f77b4")))
    styles.add(ParagraphStyle(name='SubSection',
                              parent=styles['Heading2'],
                              fontSize=14, 
                              leading=18,
                              spaceAfter=12, 
                              spaceBefore=12,
                              textColor=colors.HexColor("#2c3e50")))
    styles.add(ParagraphStyle(name='FigureCaption',
                              parent=styles['Italic'],
                              alignment=TA_LEFT,
                              fontSize=10,
                              textColor=colors.HexColor("#666666"),
                              spaceAfter=20))
    try:
        styles.add(ParagraphStyle(name='Bullet',
                                  parent=styles['Normal'],
                                  alignment=TA_JUSTIFY,
                                  fontSize=12,
                                  leading=18,
                                  bulletIndent=10,
                                  leftIndent=20,
                                  spaceAfter=6))
    except KeyError:
        pass

    Story = []
    
    # --- CAPA ---
    Story.append(Spacer(1, 100))
    logo = get_image_with_aspect("logo.png", 200)
    if logo:
        Story.append(logo)
        Story.append(Spacer(1, 40))

    title = "AUDITOR ORÇAMENTO (SOF)"
    Story.append(Paragraph(title, styles['Title']))
    
    subtitle = "Auditoria Inteligente e Controle Social com Agentes Autônomos de IA"
    Story.append(Paragraph(subtitle, styles['Heading2']))
    Story.append(Spacer(1, 150))
    
    context = "MEMORIAL TÉCNICO DESCRITIVO"
    category = "14º Prêmio SOF de Monografias - Categoria: Soluções em Dados Orçamentários"
    Story.append(Paragraph(context, styles['Heading3']))
    Story.append(Paragraph(category, styles['Heading3']))
    
    Story.append(Spacer(1, 100))
    Story.append(Paragraph("Versão Final Estendida - Dezembro de 2025", styles['Normal']))
    Story.append(PageBreak())

    # --- SUMÁRIO (Simulado) ---
    Story.append(Paragraph("Sumário Executivo", styles['Heading1']))
    Story.append(Paragraph("1. Introdução e Contextualização do Problema ..................................................... 03", styles['Normal']))
    Story.append(Paragraph("2. Fundamentação Teórica: IA na Administração Pública ................................... 05", styles['Normal']))
    Story.append(Paragraph("3. A Solução: Arquitetura de Agentes Autônomos ............................................... 07", styles['Normal']))
    Story.append(Paragraph("4. Detalhamento dos Agentes Especialistas ........................................................... 10", styles['Normal']))
    Story.append(Paragraph("5. Metodologia de Prompt Engineering e Mitigação de Riscos ........................ 14", styles['Normal']))
    Story.append(Paragraph("6. Impacto Social, Transparência e Cidadania ....................................................... 16", styles['Normal']))
    Story.append(Paragraph("7. Viabilidade Técnica, Econômica e Sustentabilidade ...................................... 18", styles['Normal']))
    Story.append(Paragraph("8. Conclusão e Próximos Passos ............................................................................ 20", styles['Normal']))
    Story.append(PageBreak())

    # --- CAPÍTULO 1 ---
    Story.append(Paragraph("1. Introdução e Contextualização do Problema", styles['SectionHeader']))
    
    Story.append(Paragraph("1.1 O Cenário da Complexidade Orçamentária no Brasil", styles['SubSection']))
    Story.append(Paragraph("""
    O ciclo orçamentário brasileiro é um dos mais sofisticados e complexos do mundo. Regido pela Constituição Federal de 1988, 
    pela Lei nº 4.320/1964 e pela Lei de Responsabilidade Fiscal (LRF - LC 101/2000), o orçamento público não é apenas uma peça contábil, 
    mas o principal instrumento de planejamento e execução de políticas públicas. No entanto, a materialização desse planejamento se dá 
    através de milhares de páginas de documentos técnicos: Planos Plurianuais (PPA), Leis de Diretrizes Orçamentárias (LDO), 
    Leis Orçamentárias Amuais (LOA) e relatórios bimestrais de avaliação.
    """, styles['Justify']))

    Story.append(Paragraph("""
    A Secretaria de Orçamento Federal (SOF) e os órgãos equivalentes em estados e municípios enfrentam o desafio hercúleo de consolidar e validar 
    essas informações. Do outro lado do balcão, órgãos de controle (Tribunais de Contas, Controladorias) e a sociedade civil (Conselhos, ONGs, Cidadãos) 
    lutam para fiscalizar a aplicação dos recursos. O gargalo não é a ausência de publicação dos dados — a transparência passiva avançou muito —, 
    mas sim a "inteligibilidade" desses dados.
    """, styles['Justify']))

    Story.append(Paragraph("1.2 A Dor do Gestor e do Cidadão", styles['SubSection']))
    Story.append(Paragraph("""
    Identificamos três fricções críticas que impedem a eficiência máxima na gestão orçamentária:
    """, styles['Justify']))
    
    Story.append(Paragraph("<b>a) Assimetria de Informação:</b> O 'economês' e o 'juridiquês' orçamentário criam uma barreira de entrada. "
                           "Um conselheiro de saúde municipal dificilmente consegue ler uma LOA e identificar se o mínimo de 15% para a saúde está "
                           "sendo respeitado apenas olhando para tabelas frias em PDF.", styles['Bullet']))

    Story.append(Paragraph("<b>b) Volume Massivo de Dados Não Estruturados:</b> Enquanto sistemas como SIAFI e Siconfi tratam dados estruturados (tabelas), "
                           "muita informação crítica reside em textos não estruturados: justificativas de programas, anexos de metas e riscos fiscais, "
                           "pareceres jurídicos. A auditoria manual desses textos é lenta, cara e propensa a erro humano.", styles['Bullet']))

    Story.append(Paragraph("<b>c) Reatividade do Controle:</b> A auditoria tradicional costuma ser 'post mortem', ou seja, analisa o que já foi gasto. "
                           "Faltam ferramentas acessíveis de análise preditiva ou concomitante, que alertem o gestor sobre inconsistências na fase de planejamento, "
                           "antes que o erro se torne uma infração.", styles['Bullet']))

    Story.append(Paragraph("""
    Neste contexto, apresentamos o <b>Auditor Orçamento</b>, uma solução que utiliza o estado da arte em Inteligência Artificial Generativa para 
    ler, interpretar, auditar e explicar o orçamento público em segundos, democratizando o acesso à informação técnica de alta qualidade.
    """, styles['Justify']))
    Story.append(PageBreak())

    # --- CAPÍTULO 2 ---
    Story.append(Paragraph("2. Fundamentação Teórica: IA na Administração Pública", styles['SectionHeader']))

    Story.append(Paragraph("""
    A aplicação de Inteligência Artificial no setor público tem evoluído de modelos preditivos simples (regressões lineares para previsão de receita) 
    para o uso de <b>Large Language Models (LLMs)</b>. Diferente da IA tradicional, que opera bem com números, os LLMs possuem a capacidade inédita de 
    compreender a semântica da linguagem natural, o raciocínio lógico e o contexto jurídico.
    """, styles['Justify']))

    Story.append(Paragraph("2.1 Do Processamento de Dados à Cognição Artificial", styles['SubSection']))
    Story.append(Paragraph("""
    Até recentemente, 'auditar' um PDF via software significava buscar palavras-chave (ex: ctrl+f por 'superávit'). Se o documento usasse um sinônimo, 
    a busca falhava. Com LLMs de nova geração, como o <b>Google Gemini 2.0</b>, o sistema "lê" o texto como um humano leria, entendendo nuances, 
    ironias, contradições e referências cruzadas entre parágrafos distantes. Isso permite uma auditoria cognitiva, qualitativa, e não apenas sintática.
    """, styles['Justify']))

    Story.append(Paragraph("2.2 A Escolha pela Arquitetura de Agentes (Agentic Workflow)", styles['SubSection']))
    Story.append(Paragraph("""
    Um modelo de linguagem genérico (como um chat simples) tende a ser superficial quando demandado a fazer muitas coisas ao mesmo tempo. 
    A teoria de <i>Chain-of-Thought (Cadeia de Pensamento)</i> sugere que dividir um problema complexo em etapas menores aumenta drasticamente a acurácia.
    """, styles['Justify']))

    Story.append(Paragraph("""
    Por isso, adotamos uma arquitetura de <b>Agentes Especialistas</b>. Em vez de pedir a uma IA "analise este orçamento", criamos personas distintas: 
    um 'Auditor' focado em números, um 'Advogado' focado em leis, um 'Professor' focado em didática. Cada um opera em seu domínio de especialidade, 
    reduzindo alucinações e aumentando a profundidade da análise.
    """, styles['Justify']))
    Story.append(PageBreak())

    # --- CAPÍTULO 3 ---
    Story.append(Paragraph("3. A Solução: Arquitetura de Agentes Autônomos", styles['SectionHeader']))

    Story.append(Paragraph("3.1 Orquestração Inteligente", styles['SubSection']))
    Story.append(Paragraph("""
    A arquitetura do sistema foi desenhada para ser modular, escalável e agnóstica à infraestrutura. O coração da solução é o <b>Orquestrador</b>, 
    um componente em Python que gerencia o fluxo de trabalho.
    """, styles['Justify']))

    # Image Arch
    im_arch = get_image_with_aspect("architecture_didactic.png", 460)
    if im_arch:
        Story.append(im_arch)
        caption = "<b>Figura 1</b> – Arquitetura de Microsserviços de Agentes. O fluxo inicia com a extração de dados e segue para processamento paralelo."
        Story.append(Paragraph(caption, styles['FigureCaption']))

    Story.append(Paragraph("""
    Conforme a Figura 1, o processo inicia com o upload do documento (etapa de Ingestão). Em seguida, o Orquestrador realiza a limpeza do texto 
    e o envia, via API, para três agentes de análise primária, que operam em paralelo (multi-threading). Essa concorrência é vital para a performance: 
    enquanto um agente verifica a LRF, outro já está validando as tabelas financeiras.
    """, styles['Justify']))

    Story.append(Paragraph("3.2 Stack Tecnológica", styles['SubSection']))
    Story.append(Paragraph("O projeto utiliza tecnologias de código aberto e serviços em nuvem de alta disponibilidade:", styles['Normal']))

    Story.append(Paragraph("<b>• Linguagem:</b> Python 3.9+ (padrão de facto para Data Science)", styles['Bullet']))
    Story.append(Paragraph("<b>• Frontend:</b> Streamlit (framework para Data Apps rápidos)", styles['Bullet']))
    Story.append(Paragraph("<b>• IA Engine:</b> Google Gemini 2.0 Flash (via Google Generative AI SDK)", styles['Bullet']))
    Story.append(Paragraph("<b>• Manipulação de Dados:</b> Pandas e PyPDF2", styles['Bullet']))
    
    Story.append(Paragraph("""
    A decisão pelo modelo <b>Gemini 2.0 Flash</b> foi estratégica. Este modelo possui uma janela de contexto de 1 milhão de tokens, 
    o que permite carregar uma Lei Orçamentária inteira (centenas de páginas) na memória de curto prazo da IA, eliminando a necessidade complexa 
    de bancos de dados vetoriais (RAG) para a maioria dos casos de uso municipais.
    """, styles['Justify']))
    Story.append(PageBreak())

    # --- CAPÍTULO 4 ---
    Story.append(Paragraph("4. Detalhamento dos Agentes Especialistas", styles['SectionHeader']))
    Story.append(Paragraph("""
    A "alma" da solução reside nas <i>System Instructions</i> (instruções de sistema) de cada agente. Abaixo, detalhamos o perfil técnico e 
    as responsabilidades de cada componente autônomo.
    """, styles['Justify']))

    # AGENTE 1
    Story.append(Paragraph("4.1 Agente Auditor (The Hawk)", styles['SubSection']))
    Story.append(Paragraph("<b>Perfil:</b> Contador público sênior, auditor de controle externo, rigoroso e detalhista.", styles['Normal']))
    Story.append(Paragraph("<b>Missão:</b>", styles['Normal']))
    Story.append(Paragraph("""
    Identificar riscos de irresponsabilidade fiscal e "pedaladas". Este agente não se importa com a forma, apenas com o mérito contábil.
    Ele busca por:
    - Superestimativa de Receitas (inflar o orçamento artificialmente).
    - Subestimativa de Despesas Obrigatórias (esconder gastos com previdência ou pessoal).
    - Inconsistência entre metas físicas e financeiras.
    """, styles['Justify']))
    Story.append(Paragraph("<b>Output:</b> Gera um relatório JSON contendo uma lista de 'Achados de Auditoria', classificados por gravidade (Alta, Média, Baixa).", styles['Justify']))
    Story.append(Spacer(1, 12))

    # AGENTE 2
    Story.append(Paragraph("4.2 Agente de Compliance (The Lawyer)", styles['SubSection']))
    Story.append(Paragraph("<b>Perfil:</b> Procurador jurídico, especialista em LRF e Direito Financeiro.", styles['Normal']))
    Story.append(Paragraph("<b>Missão:</b>", styles['Normal']))
    Story.append(Paragraph("""
    Verificar a conformidade legal estrita. Este agente cruza o texto do PDF com um conhecimento pré-treinado sobre a legislação brasileira.
    Ele verifica:
    - Cumprimento dos mínimos constitucionais (Saúde 15%, Educação 25%).
    - Limites de Despesa com Pessoal (Art. 19 e 20 da LRF).
    - Regra de Ouro (operações de crédito x despesas de capital).
    """, styles['Justify']))
    Story.append(Paragraph("<b>Output:</b> Tabela de conformidade (Passou/Falhou) com citação do artigo legal infringido.", styles['Justify']))
    Story.append(PageBreak())

    # AGENTE 3
    Story.append(Paragraph("4.3 Agente de Consistência (The Accountant)", styles['SubSection']))
    Story.append(Paragraph("<b>Perfil:</b> Perito matemático e estatístico.", styles['Normal']))
    Story.append(Paragraph("<b>Missão:</b>", styles['Normal']))
    Story.append(Paragraph("""
    Garantir que os números "fechem". Leis orçamentárias são notórias por erros de soma ou digitação que podem invalidar a peça.
    O agente varre o texto buscando tabelas e quadros demonstrativos para validar a consistência aritmética vertical e horizontal.
    """, styles['Justify']))
    Story.append(Spacer(1, 12))

    # AGENTE 4
    Story.append(Paragraph("4.4 Agente de Explicabilidade (The Teacher)", styles['SubSection']))
    Story.append(Paragraph("<b>Perfil:</b> Comunicador social, jornalista de dados e professor universitário.", styles['Normal']))
    Story.append(Paragraph("<b>Missão:</b>", styles['Normal']))
    Story.append(Paragraph("""
    A missão deste agente é a mais nobre: traduzir. Ele recebe os relatórios técnicos e frios dos outros três agentes e os reescreve 
    em linguagem natural, acessível, empática e clara. Ele é responsável por responder: "O que isso significa para a vida do cidadão?".
    """, styles['Justify']))
    Story.append(PageBreak())

    # --- CAPÍTULO 5 ---
    Story.append(Paragraph("5. Metodologia de Prompt Engineering e Mitigação de Riscos", styles['SectionHeader']))

    Story.append(Paragraph("""
    O maior risco no uso de IA Generativa são as alucinações (inventar informações). Para mitigar isso, adotamos uma engenharia de prompt rigorosa baseada em três pilares:
    """, styles['Justify']))

    Story.append(Paragraph("5.1 Grounding (Aterramento)", styles['SubSection']))
    Story.append(Paragraph("""
    Instruímos os modelos a responderem <b>apenas</b> com base nas informações contidas no documento fornecido. 
    Usamos comandos como: <i>"Se a informação não estiver no texto, declare explicitamente que não foi encontrada. Não invente dados."</i>
    Isso reduz drasticamente a criatividade indesejada do modelo em contextos de auditoria.
    """, styles['Justify']))

    Story.append(Paragraph("5.2 Output Estruturado (JSON)", styles['SubSection']))
    Story.append(Paragraph("""
    Para garantir que os sistemas conversem entre si, forçamos a saída dos modelos em formato JSON (JavaScript Object Notation). 
    Isso permite que o código Python capture a resposta, valide a estrutura, exiba em tabelas e rejeite formatos inválidos automaticamente, 
    aumentando a robustez da aplicação.
    """, styles['Justify']))

    Story.append(Paragraph("5.3 Few-Shot Learning", styles['SubSection']))
    Story.append(Paragraph("""
    Nos prompts de sistema, incluímos exemplos de "pergunta e resposta ideais". Mostramos ao agente como um auditor humano classificaria um risco. 
    Ao ver o exemplo, o modelo calibra seu "tom" e critérios de avaliação, mimetizando o comportamento do especialista humano.
    """, styles['Justify']))
    Story.append(PageBreak())

    # --- CAPÍTULO 6 ---
    Story.append(Paragraph("6. Impacto Social, Transparência e Cidadania", styles['SectionHeader']))
    
    Story.append(Paragraph("""
    O Auditor Orçamento não é apenas uma ferramenta tecnocrática; é uma ferramenta política no melhor sentido da palavra (política pública).
    Sua adoção em larga escala tem o potencial de alterar a correlação de forças no controle social do orçamento.
    """, styles['Justify']))

    Story.append(Paragraph("6.1 Empoderamento da Sociedade Civil", styles['SubSection']))
    Story.append(Paragraph("""
    Conselhos de Saúde, Educação e Assistência Social frequentemente aprovam contas "no escuro" por falta de assessoria técnica. 
    Com esta ferramenta, um conselheiro pode, pelo celular, fazer upload do relatório quadrimestral e receber, em segundos, 
    uma análise apontando se os recursos da merenda escolar foram aplicados conforme a lei. Isso equilibra o jogo entre o governo e a sociedade.
    """, styles['Justify']))

    Story.append(Paragraph("6.2 Eficiência e Economicidade na Ponta", styles['SubSection']))
    Story.append(Paragraph("""
    Para o corpo técnico do Estado, a ferramenta representa o fim do trabalho braçal. Em vez de gastar 40 horas conferindo somas, 
    o auditor dedica seu tempo para ir a campo verificar se a obra foi feita. A tecnologia absorve a burocracia, liberando o humano para a inteligência.
    """, styles['Justify']))
    Story.append(PageBreak())

    # --- CAPÍTULO 7 ---
    Story.append(Paragraph("7. Viabilidade Técnica, Econômica e Sustentabilidade", styles['SectionHeader']))
    
    Story.append(Paragraph("7.1 Infraestrutura Leve (Serverless)", styles['SubSection']))
    Story.append(Paragraph("""
    A aplicação roda 100% em nuvem. Não exige instalação (é acessada via navegador). Não exige servidores locais. 
    O processamento é feito na infraestrutura global do Google. Isso viabiliza a adoção por pequenos municípios do interior do Brasil que não possuem departamento de TI estruturado.
    """, styles['Justify']))

    Story.append(Paragraph("7.2 Sustentabilidade Econômica", styles['SubSection']))
    Story.append(Paragraph("""
    Diferente de sistemas ERP que custam milhões em licenças, o Auditor Orçamento baseia-se em código aberto. 
    O custo mensal de operação é marginal, referente apenas ao consumo de tokens da API (centavos por documento analisado). 
    Para fins do Prêmio SOF, a solução demonstra um ROI (Retorno sobre Investimento) imediato.
    """, styles['Justify']))

    Story.append(Paragraph("7.3 Roadmap de Evolução", styles['SubSection']))
    Story.append(Paragraph("""
    O projeto está pronto para crescer. As próximas fases incluem:
    1. Integração com API do Siconfi para puxar dados automaticamente (sem necessidade de upload de PDF).
    2. Fine-tuning (Ajuste Fino) dos modelos com jurisprudência do TCU.
    3. Desenvolvimento de um App Mobile nativo para cidadãos.
    """, styles['Justify']))
    Story.append(PageBreak())

    # --- CAPÍTULO 8 ---
    Story.append(Paragraph("8. Conclusão e Próximos Passos", styles['SectionHeader']))
    Story.append(Paragraph("""
    Acreditamos que a tecnologia deve servir para reduzir desigualdades. A desigualdade de informação é uma das mais perversas, pois impede o exercício pleno da cidadania.
    O <b>Auditor Orçamento</b>, submetido ao 14º Prêmio SOF, é a nossa contribuição para um país onde o orçamento público seja, de fato, público — não apenas publicado, mas compreendido.
    """, styles['Justify']))
    
    Story.append(Spacer(1, 24))
    Story.append(Paragraph("""
    Estamos prontos para pilotos, parcerias e para levar essa inovação a cada município brasileiro.
    """, styles['Justify']))
    
    Story.append(Spacer(1, 48))
    Story.append(Paragraph("Documento elaborado para fins de submissão.", styles['Italic']))

    # Appendices to fill pages if needed, showing code or prompts
    Story.append(PageBreak())
    Story.append(Paragraph("Apêndice A - Exemplo de Prompt (Agente Auditor)", styles['SectionHeader']))
    code_prompt = """
    ROLE: You are an Expert Public Auditor (TCU/CGU standard).
    TASK: Analyze the provided text from a Budget Law (LOA/LDO).
    RULES:
    1. Identify Fiscal Risks (Art. 4 LRF).
    2. Check for revenue overestimation.
    3. Be strict but fair.
    OUTPUT FORMAT: JSON List of risks.
    """
    Story.append(Paragraph(code_prompt, styles['Code'] if 'Code' in styles else styles['Normal']))
    
    Story.append(Spacer(1, 20))
    Story.append(Paragraph("Apêndice B - Stack Tecnológica Detalhada", styles['SectionHeader']))
    Story.append(Paragraph("Framework: Streamlit 1.30+", styles['Bullet']))
    Story.append(Paragraph("AI Wrapper: Google Generative AI 0.4+", styles['Bullet']))
    Story.append(Paragraph("PDF Engine: PyPDF2 / pdfplumber", styles['Bullet']))
    Story.append(Paragraph("Container: Docker / Buildpacks", styles['Bullet']))

    doc.build(Story)

if __name__ == "__main__":
    output_pdf = "Auditor_Orcamento_14_Premio_SOF.pdf"
    create_presentation_pdf(output_pdf)
    print(f"PDF de apresentação gerado: {output_pdf}")
