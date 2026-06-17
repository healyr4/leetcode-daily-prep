# Group transaction totals by account
# Assume input is list of dicts with account_id and amount

def get_totals_by_account_id(transactions: list[dict[str, int | str]]) -> dict[str, int]:
    totals_by_account = {}
    for transaction in transactions:
        account_id = transaction["account_id"]
        amount = transaction["amount"]
        if account_id in totals_by_account:
            totals_by_account[account_id] += int(amount)
        else:
            totals_by_account[account_id] = int(amount)
    return totals_by_account

def main():
    transactions = [{"account_id": "AR101", "amount": 75},
                    {"account_id": "AR102", "amount": 100},
                    {"account_id": "AR101", "amount": 20},
                    {"account_id": "AR102", "amount": 30},
                    {"account_id": "AR103", "amount": 43}]

    totals = get_totals_by_account_id(transactions)
    print(totals)

if __name__ == '__main__':
    main()



