from decimal import Decimal

from pydantic import BaseModel


class Transaction(BaseModel):
    account_id: str
    amount: Decimal


def get_totals_by_account_id(
    transactions: list[Transaction],
) -> dict[str, Decimal]:
    totals_by_account: dict[str, Decimal] = {}

    for transaction in transactions:
        account_id = transaction.account_id

        totals_by_account[account_id] = (
            totals_by_account.get(account_id, Decimal("0"))
            + transaction.amount
        )

    return totals_by_account


def main() -> None:
    transactions: list[Transaction] = [
        Transaction(account_id="AR101", amount=Decimal("75")),
        Transaction(account_id="AR102", amount=Decimal("100")),
        Transaction(account_id="AR101", amount=Decimal("20")),
        Transaction(account_id="AR102", amount=Decimal("30")),
        Transaction(account_id="AR103", amount=Decimal("43")),
    ]

    totals = get_totals_by_account_id(transactions)
    print(totals)


if __name__ == "__main__":
    main()