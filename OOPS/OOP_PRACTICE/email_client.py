class EmailClient:

    def __init__(self, api_key):
        self.api_key = api_key

    def send_email(self, email, subject, body):

        print(f"Using API KEY: {self.api_key}")
        print(f"To: {email}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")


email_client = EmailClient("asfnjhwtg76nk")

email_client.send_email(
    "JAVSADASD123@gmail.com",
    "Motivation of death",
    "Please die as soon as possible all of my negative energy",
)
