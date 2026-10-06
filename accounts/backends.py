import os
import requests

from django.core.mail.backends.base import BaseEmailBackend


class BrevoEmailBackend(BaseEmailBackend):

    api_url = "https://api.brevo.com/v3/smtp/email"

    def send_messages(self, email_messages):
        if not email_messages:
            return 0

        sent_count = 0

        for message in email_messages:
            if self._send(message):
                sent_count += 1

        return sent_count

    def _send(self, message):
        api_key = os.getenv("BREVO_API_KEY")

        if not api_key:
            raise ValueError("BREVO_API_KEY is not configured.")

        sender_email = os.getenv("EMAIL_HOST_USER")

        if not sender_email:
            raise ValueError("EMAIL_HOST_USER is not configured.")

        # Get sender name and email
        from_email = message.from_email or sender_email

        sender_name = "Brew & Bite"

        # Prepare recipients
        recipients = []

        for recipient in message.to:
            recipients.append({
                "email": recipient,
                "name": recipient,
            })

        if not recipients:
            return False

        # Prepare payload
        payload = {
            "sender": {
                "name": sender_name,
                "email": from_email,
            },
            "to": recipients,
            "subject": message.subject,
            "htmlContent": self._get_html_content(message),
            "textContent": message.body,
        }

        headers = {
            "accept": "application/json",
            "api-key": api_key,
            "content-type": "application/json",
        }

        response = requests.post(
            self.api_url,
            json=payload,
            headers=headers,
            timeout=15,
        )

        if not response.ok:
            print("BREVO EMAIL ERROR:", response.status_code)
            print("BREVO RESPONSE:", response.text)

            if not self.fail_silently:
                response.raise_for_status()

            return False

        print("BREVO EMAIL SENT:", response.json())

        return True

    def _get_html_content(self, message):
        """
        Use HTML alternative if EmailMultiAlternatives
        was used. Otherwise create a simple HTML body.
        """

        if hasattr(message, "alternatives") and message.alternatives:

            for content, mimetype in message.alternatives:
                if mimetype == "text/html":
                    return content

        # Escape basic HTML characters
        body = (
            message.body
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace("\n", "<br>")
        )

        return f"""
        <!DOCTYPE html>
        <html>
        <body>
            {body}
        </body>
        </html>
        """