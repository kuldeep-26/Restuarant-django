import os
import requests


BREVO_API_URL = "https://api.brevo.com/v3/smtp/email"


def send_brevo_email(
    to_email,
    subject,
    html_content,
    text_content=None,
    to_name=None,
):
    import os
    import requests

    api_key = os.getenv("BREVO_API_KEY")
    sender_email = os.getenv("EMAIL_HOST_USER")

    payload = {
        "sender": {
            "name": "Brew & Bite",
            "email": sender_email,
        },
        "to": [
            {
                "email": to_email,
                "name": to_name or to_email,
            }
        ],
        "subject": subject,
        "htmlContent": html_content,
    }

    if text_content:
        payload["textContent"] = text_content

    headers = {
        "accept": "application/json",
        "api-key": api_key,
        "content-type": "application/json",
    }

    response = requests.post(
        "https://api.brevo.com/v3/smtp/email",
        json=payload,
        headers=headers,
        timeout=15,
    )

    print("STATUS CODE:", response.status_code)
    print("BREVO RESPONSE:", response.text)

    return response



