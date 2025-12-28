# Arquitetura

1. **Camada de ingestão**: conectores para portais de transparência, SIAFI/SICONFI e bases locais, com validação e versionamento de dados.
2. **Data Lake governado**: armazenamento padronizado por exercício, unidade orçamentária e categoria econômica, garantindo rastreabilidade.
3. **Motor analítico**: rotinas de detecção de anomalias, regras contábeis configuráveis e simulações de cenários (cortes, reclassificações, atrasos).
4. **Orquestração de IA/LLM**: prompts especializados para revisão de conformidade, geração de explicações e sumarização executiva.
5. **APIs e dashboards**: camadas REST/GraphQL e painéis interativos para **gestão pública** e controle social.
6. **Trilha de auditoria**: logs assinados, evidências reproduzíveis e exportação para órgãos de controle.
