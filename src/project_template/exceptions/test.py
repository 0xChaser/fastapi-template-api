from project_template.exceptions.base import Conflict, NotFound

class TestNotFound(NotFound):
    def __init__(self) -> None:
        detail = "Test with the given id doesn't exist" 
        super().__init__(detail)

class TestLinkedToAnotherObject(Conflict):
    def __init__(self) -> None:
        detail = "Test is linked to another object and can't be deleted"
        super().__init__(detail)