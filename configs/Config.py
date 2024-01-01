
class Config:
    id: int
    def __init__(self, id:int) -> None:
        self.id = id
        
    def getAsList(self) -> list:
        return [str(self.id)]
    