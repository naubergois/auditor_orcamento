import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    # Define styles
    box_style = dict(boxstyle="round,pad=0.5", fc="#e1f5fe", ec="#0277bd", lw=2)
    center_style = dict(boxstyle="round,pad=0.5", fc="#0277bd", ec="#01579b", lw=2)
    arrow_props = dict(arrowstyle="->", color="#546e7a", lw=1.5)

    # Central Node: Orchestrator
    ax.text(50, 30, "Orchestrator\n(Coordenador)", size=14, ha="center", va="center", 
            bbox=center_style, color="white", weight="bold")
    
    # Agent Nodes positions
    agents = [
        ("Auditor Agent\n(Risco Fiscal)", 20, 50),
        ("Compliance Agent\n(Legal)", 80, 50),
        ("Consistency Agent\n(Dados)", 20, 10),
        ("Explainability Agent\n(Explicação)", 80, 10)
    ]
    
    for name, x, y in agents:
        ax.text(x, y, name, size=10, ha="center", va="center", bbox=box_style, color="#01579b")
        
        # Draw connections
        # Calculate start and end points roughly
        # Midpoint is (50, 30)
        
        # Connect Orchestrator to Agents (bidirectional flow conceptually, but drawn simply)
        ax.annotate("", xy=(x if x < 50 else x, y if y < 30 else y), xytext=(50, 30),
                    arrowprops=dict(arrowstyle="<->", connectionstyle="arc3,rad=0.1", color="#0277bd", lw=2))

    # Input / Output
    ax.text(50, 55, "Input: PDF (LOA/LDO)", size=10, ha="center", va="center", 
            bbox=dict(boxstyle="rarrow,pad=0.3", fc="#fff9c4", ec="#fbc02d", lw=1))
            
    ax.annotate("", xy=(50, 35), xytext=(50, 50), arrowprops=arrow_props)
    
    ax.text(50, 5, "Output: Relatório Auditado", size=10, ha="center", va="center", 
            bbox=dict(boxstyle="larrow,pad=0.3", fc="#c8e6c9", ec="#388e3c", lw=1))
            
    ax.annotate("", xy=(50, 25), xytext=(50, 10), arrowprops=arrow_props)

    plt.tight_layout()
    plt.savefig('architecture_v2.png', dpi=300, bbox_inches='tight')
    print("Architecture diagram created: architecture_v2.png")

if __name__ == "__main__":
    create_architecture_diagram()
