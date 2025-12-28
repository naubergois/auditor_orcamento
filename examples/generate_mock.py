from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def generate_pdf(filepath):
    c = canvas.Canvas(filepath, pagesize=A4)
    width, height = A4
    
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Projeto de Lei Orçamentária Anual - Exemplo 2025")
    
    c.setFont("Helvetica", 12)
    text_lines = [
        "Este documento é um exemplo fictício para demonstração de auditoria via IA.",
        "Art. 1º Estima a Receita e fixa a Despesa para o exercício financeiro de 2025.",
        "",
        "CAPÍTULO I - DOS ORÇAMENTOS FISCAL E DA SEGURIDADE SOCIAL",
        "A Receita Orçamentária é estimada em R$ 10.000.000,00 (dez milhões de reais).",
        "",
        "As despesas serão fixadas conforme discriminação abaixo:",
        "1. Pessoal e Encargos Sociais: R$ 6.500.000,00",
        "2. Investimentos: R$ 1.000.000,00",
        "3. Amortização da Dívida: R$ 500.000,00",
        "4. Custeio da Máquina: R$ 3.000.000,00",
        "",
        "OBSERVAÇÃO DO ESTAGIÁRIO (ERRO INTENCIONAL):",
        "A soma das despesas (6.5 + 1.0 + 0.5 + 3.0 = 11.0) ultrapassa a receita (10.0).",
        "Isso gera um déficit não previsto de R$ 1.000.000,00, descumprindo a LRF.",
        "",
        "Art. 5º Fica o Poder Executivo autorizado a abrir créditos suplementares até o limite de 20%.",
        "§ 1º O limite para gasto com pessoal será de 65% da Receita Corrente Líquida.",
        "(Nota: O limite legal pela LRF para Executivo Municipal é 54%, aqui há uma impropriedade).",
        "",
        "Art. 9º As operações de crédito ficam limitadas a R$ 5.000.000,00.",
    ]
    
    y = height - 100
    for line in text_lines:
        c.drawString(50, y, line)
        y -= 20
        
    c.save()

if __name__ == "__main__":
    output_path = "examples/exemplo_orcamento.pdf"
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    generate_pdf(output_path)
    print(f"PDF gerado em: {output_path}")
