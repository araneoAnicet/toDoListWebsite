class ProjectEditor:
    def __init__(self, name: str = None, description: str = None) -> None:
        self.name = name
        self.description = description

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description