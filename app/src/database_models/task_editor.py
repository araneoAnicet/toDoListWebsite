class TaskEditor:
    def __init__(self, name: str = None, description: str = None, priority: int = None) -> None:
        self.name = name
        self.description = description
        self.priority = priority

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_priority(self) -> int:
        return self.priority