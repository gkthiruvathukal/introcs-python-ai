class Contact:
    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        return (f"Name:  {self.name}\n"
                f"Phone: {self.phone}\n"
                f"Email: {self.email}")

    def set_email(self, new_email: str) -> None:
        self.email = new_email


if __name__ == '__main__':
    contacts = [
        Contact("Marie Ortiz", "773-508-7890", "mortiz2@luc.edu"),
        Contact("Otto Heinz",  "773-508-9999", "oheinz@luc.edu"),
    ]
    for contact in contacts:
        print(contact)
        print()
