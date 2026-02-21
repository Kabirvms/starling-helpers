from api_client import StarlingClient
import logging

class AccountOperations:
    def __init__(self):
        self.api_client = StarlingClient()

    def choose_account(self):
        endpoint = "/api/v2/accounts"
        response = self.api_client(endpoint)
        for index in range(len(response["accounts"])):
            print(f"{index+1}. The Account name is: {response['accounts'][index]['name']} type: {response['accounts'][index]['type']} and currency: {response['accounts'][index]['currency']}")
        choice = int(input("Choose an account: ")) - 1
        print(f"You have chosen account: {response['accounts'][choice]['name']}")
        return response["accounts"][choice]

    def account_balance(self, account_id):
        endpoint = f"/api/v2/accounts/{account_id}/balance"
        response = self.api_client(endpoint)
        return response["balance"]["value"]

    def account_fund_confirm(self,account_id,amount):
        endpoint = f"/api/v2/accounts/{account_id}/fund-confirm"
        response = self.api_client(endpoint, method="POST", data={"amount": amount})
        return response["status"] == "SUCCESS"
    
    def account_feed(self, account_id):
        endpoint = f"/api/v2/accounts/{account_id}/feed-export"
        response = self.api_client(endpoint)
        return response["feed"]



if __name__ == "__main__":
    account_ops = AccountOperations()
    account = account_ops.choose_account()
    balance = account_ops.account_balance(account["id"])
    print(f"Account balance: {balance}")
    amount = float(input("Enter amount to fund: "))
    if account_ops.account_fund_confirm(account["id"], amount):
        print("Funding successful")
    else:
        print("Funding failed")
    feed = account_ops.account_feed(account["id"])
    print(f"Account feed: {feed}")