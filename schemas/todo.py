from pydantic import BaseModel


class CreateTodo(BaseModel):
    
    text : str
    completed : bool

class UpdateTodo(CreateTodo):
    id: int


