class UserEditor:
    def __init__(self, name: str = None, email: str = None, password: str = None) -> None:
        self.name = name
        self.email = email
        self.password = password

    def get_name(self) -> str:
        return self.name

    def get_email(self) -> str:
        return self.email

    def get_password(self) -> str:
        return self.password
