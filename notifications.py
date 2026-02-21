def send_pushover(level: int, message: str):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request(
        "POST",
        "/1/messages.json",
        urllib.parse.urlencode(
            {
                "token": "your_pushover_token",
                "user": "your_pushover_user_key",
                "message": message,
                "priority": level,
            }
        ),
        {"Content-type": "application/x-www-form-urlencoded"},
    )
    response = conn.getresponse()
    print(response.status, response.reason)
    return response.status == 200
