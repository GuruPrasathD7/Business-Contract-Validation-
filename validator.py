from datetime import datetime


def validate_contract(contract):
    try:
        contract_id = contract.get("contract_id")
        if not contract_id:
            return "Invalid contract: Missing contract_id."

        party_a = contract.get("party_a")
        party_b = contract.get("party_b")
        if not party_a or not party_b:
            return "Invalid contract: Missing party names."

        effective_date = datetime.strptime(
            contract.get("effective_date"), "%Y-%m-%d")
        termination_date = datetime.strptime(
            contract.get("termination_date"), "%Y-%m-%d")
        if termination_date <= effective_date:
            return "Invalid contract: Termination date must be after effective date."

        return "Contract is valid."
    except KeyError as e:
        return f"Invalid contract: Missing key {e}."
    except ValueError as e:
        return f"Invalid contract: Date format error {e}."
