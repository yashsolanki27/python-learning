class EmailClient:

    def __init__(self, api_key):
        self.api_key = api_key

    def send_email(self, email):
        self.email = email
        print(f"Using API KEY: {self.api_key}")
        print(f"To: {self.email}")
        print("Subject : Hello")
        print("Body: How are you?")


email1 = EmailClient("asfnjhwtg76nksdhf3bkhjcsdnaUY34G254MGHABDTBU3Y327NUHknJb")

email1.send_email("JAVSADASD123@gmail.com")
