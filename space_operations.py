



def savings_goal_transfer(access_token,space_name,amount,direction):
    # Generate a transfer UUID
    transfer_uuid = str(uuid.uuid4())
    account_uuid = os.environ.get("STARLING_ACCOUNT_ID")
    savings_goal_uuid = get_savings_goal_uuid(account_uuid, saving_goal_name)
    amount_mini_units = amount * 100
    endpoint = f"savings-goals/{savings_goal_uuid}/{direction}-money/{transfer_uuid}"

    # Prepare request body
    body = {
        "amount": {
            "currency": "GBP",
            "minorUnits": amount_mini_units
        }
    }
    status =starling_call(account_uuid, endpoint, body, method="POST")
    time.sleep(2)
    if status == False:
        #send_notification()

def space_name_to_uuid(account, space_name):
    """Converts from a space name to uuid
    args:
        account (str): The account ID
        space_name (str): The name of the goal
    """
    data = starling_call(
        account=account,
        endpoint="savings-goals",
        body=None,
        method="GET"
    )
    if data == False:
        logger.error("")
        #send_notification()

    else:
        for goal in data.get("savingsGoalList", []):
            if goal["name"].lower() == space_name.lower():
                return goal["savingsGoalUid"]
            else:
                logger.error(f"Goal not found: {goal_name}")
                return None
