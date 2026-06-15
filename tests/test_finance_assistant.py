import sys
from pathlib import Path

PROJECT_SRC = Path(__file__).resolve().parents[1] / "projet" / "src"
sys.path.append(str(PROJECT_SRC))

from finance_assistant import (  # noqa: E402
    build_ai_prompt,
    is_company_complete,
    missing_loan_documents,
    summarize_company,
)


def test_company_is_complete() -> None:
    company = {
        "name": "Alpha Industrie",
        "country": "France",
        "sector": "Industrie",
        "employees": 120,
        "turnover_eur": 4_200_000,
    }

    assert is_company_complete(company) is True


def test_company_is_incomplete_without_country() -> None:
    company = {
        "name": "Alpha Industrie",
        "country": "",
        "sector": "Industrie",
        "employees": 120,
        "turnover_eur": 4_200_000,
    }

    assert is_company_complete(company) is False


def test_missing_loan_documents() -> None:
    loan_request = {
        "has_business_plan": True,
        "has_financial_statements": True,
        "has_identity_documents": False,
    }

    assert missing_loan_documents(loan_request) == ["Documents d'identité"]


def test_summarize_company_contains_company_name() -> None:
    company = {
        "name": "Alpha Industrie",
        "country": "France",
        "sector": "Industrie",
        "employees": 120,
        "turnover_eur": 4_200_000,
    }
    loan_request = {
        "requested_amount_eur": 250_000,
        "purpose": "Achat de machines",
        "duration_months": 48,
        "has_business_plan": True,
        "has_financial_statements": True,
        "has_identity_documents": False,
    }

    summary = summarize_company(company, loan_request)

    assert "Alpha Industrie" in summary
    assert "Documents d'identité" in summary


def test_build_ai_prompt_does_not_decide_credit() -> None:
    company = {
        "name": "Alpha Industrie",
        "country": "France",
        "sector": "Industrie",
        "employees": 120,
        "turnover_eur": 4_200_000,
    }
    loan_request = {
        "requested_amount_eur": 250_000,
        "purpose": "Achat de machines",
        "duration_months": 48,
        "has_business_plan": True,
        "has_financial_statements": True,
        "has_identity_documents": False,
    }

    prompt = build_ai_prompt(company, loan_request)

    assert "Ne prends pas de décision de crédit" in prompt
