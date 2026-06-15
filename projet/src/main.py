from pathlib import Path

from finance_assistant import build_ai_prompt, load_json, summarize_company


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "ressources" / "donnees" / "entreprises" / "alpha-industrie"


def main() -> None:
    company = load_json(DATA_DIR / "company.json")
    loan_request = load_json(DATA_DIR / "loan-request.json")

    print("=== Résumé du dossier ===")
    print(summarize_company(company, loan_request))

    print("\n=== Prompt pour assistant IA ===")
    print(build_ai_prompt(company, loan_request))


if __name__ == "__main__":
    main()
