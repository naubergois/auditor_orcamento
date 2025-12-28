import concurrent.futures
from agents import auditor, compliance, consistency, explainability

class AuditorOrchestrator:
    def __init__(self):
        pass

    def run_audit(self, text: str) -> dict:
        """
        Runs all agents on the provided text and aggregates results.
        """
        results = {}

        # Run analysis agents in parallel to save time
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_auditor = executor.submit(auditor.analyze_risks, text)
            future_compliance = executor.submit(compliance.verify_compliance, text)
            future_consistency = executor.submit(consistency.check_consistency, text)

            results['auditor'] = future_auditor.result()
            results['compliance'] = future_compliance.result()
            results['consistency'] = future_consistency.result()

        # Run explainability agent mostly sequentially as it needs context from others
        # (Though in this simple version, I'll feed it the raw findings)
        findings_summary = {
            "riscos": results['auditor'].get('riscos', []),
            "conformidade": results['compliance'].get('conformidade', []),
            "inconsistencias": results['consistency'].get('inconsistencias', [])
        }
        
        results['explainability'] = explainability.explain_findings(text, findings_summary)

        return results
