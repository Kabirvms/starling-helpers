from tools import env
from api_client import StarlingClient

class SpaceOperations:
    def __init__(self,access_token):
        self.api_client = StarlingClient(access_token)

    def savings_goal_transfer(self,account_uuid,space_name,amount,direction):
        transfer_uuid = str(uuid.uuid4())
        savings_goal_uuid = get_savings_goal_uuid(account_uuid, space_name)
        amount_mini_units = amount * 100
        endpoint = f"/savings-goals/{savings_goal_uuid}/{direction}-money/{transfer_uuid}"
        payload = {
            "amount": {
                "currency": "GBP",
                "minorUnits": amount_mini_units
            }
        }
        response = self.api_client(endpoint, body=payload, method="POST")
        return response

    def space_name_to_uuid(self,account_uuid, space_name):
        endpoint = f"/api/v2/account/{account_uuid}/savings-goals"
        response = self.api_client(endpoint)
        for index in range(response)
            if space_name == response[index]["name"]
                return response[index]["savingsGoalUid"]

if __name__ == "__main__":
#    add tests
        
        
    
               