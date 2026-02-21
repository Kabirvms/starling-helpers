from datetime import datetime, timedelta
from api_client import StarlingClient

class AccountOperations:
    def __init__(self):
        self.api_client = StarlingClient()

    def choose_account(self):
        endpoint = "/api/v2/accounts"
        response = self.api_client(endpoint)
        print("Please choose from the following accounts: ")
        for index in range(len(response["accounts"])):
            print(f"{index+1}: {response["accounts"][index]["name"]} ")
        choice = int(input("Choose an account (enter the number): ")) -1
        print(f"You have chosen account: {response["accounts"][2]["name"]}")
        return response["accounts"][choice]

    def account_balance(self, account_id):
        endpoint = f"/api/v2/accounts/{account_id}/balance"
        response = self.api_client(endpoint)
        return response
   
    
    def account_feed(self, account_id,days_back: int =1):
        endpoint = f"/api/v2/feed/account/{account_id}/settled-transactions-between"
        
        start_date = datetime.now()- timedelta(days=days_back)
        end_date = datetime.now()
        
        payload = {
            'minTransactionTimestamp': start_date.isoformat() + 'Z',
            'maxTransactionTimestamp': end_date.isoformat() + 'Z'
        }
        response = self.api_client(endpoint,params=payload)
        return response



if __name__ == "__main__":
    account_ops = AccountOperations()
    account = account_ops.choose_account()
    balance = account_ops.account_balance(account["accountUid"])
    feed = account_ops.account_feed(account["accountUid"])
    print(f"Account feed: {feed}")