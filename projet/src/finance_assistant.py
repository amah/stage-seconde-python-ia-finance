import json
from pathlib import Path
from typing import Any


def load_json(path: str | Path) -> dict[str, Any]:
    """Charge un fichier JSON et retourne son contenu sous forme de dictionnaire."""
    file_path = Path(path)
    with file_path.open(encoding="utf-8") as file:
        return json.load(file)


def is_company_complete(company: dict[str, Any]) -> bool:
    """Vérifie que les informations minimales de l'entreprise sont présentes."""
    required_fields = ["name", "country", "sector", "employees", "turnover_eur"]
    return all(company.get(field) not in (None, "") for field in required_fields)


def missing_loan_documents(loan_request: dict[str, Any]) -> list[str]:
    """Retourne la liste des documents manquants dans une demande de financement."""
    checks = {
        "business_plan": "Business plan",
        "financial_statements": "États financiers",
        "identity_documents": "Documents d'identité"
    }

    missing: list[str] = []
    for field_suffix, label in checks.items():
        field_name = f"has_{field_suffix}"
        if not loan_request.get(field_name, False):
            missing.append(label)

    return missing


def summarize_company(company: dict[str, Any], loan_request: dict[str, Any]) -> str:
    """Produit un résumé simple d'un dossier de financement."""
    missing_documents = missing_loan_documents(loan_request)
    missing_text = ", ".join(missing_documents) if missing_documents else "aucun document manquant"

    return (
        f"{company['name']} est une entreprise située en {company['country']}, "
        f"dans le secteur {company['sector']}. "
        f"Elle compte {company['employees']} salariés et réalise "
        f"{company['turnover_eur']} euros de chiffre d'affaires. "
        f"Elle demande un financement de {loan_request['requested_amount_eur']} euros "
        f"sur {loan_request['duration_months']} mois pour : {loan_request['purpose']}. "
        f"Documents manquants : {missing_text}."
    )


def build_ai_prompt(company: dict[str, Any], loan_request: dict[str, Any]) -> str:
    """Prépare un prompt simple pour demander un résumé à un assistant IA."""
    summary = summarize_company(company, loan_request)
    return (
        "Tu es un assistant qui aide un analyste financier. "
        "Résume le dossier suivant en langage simple pour un élève de seconde. "
        "Ne prends pas de décision de crédit. Contente-toi d'expliquer les informations.\n\n"
        f"Dossier : {summary}"
    )
