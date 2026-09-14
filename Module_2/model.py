from pydantic import BaseModel, Basemodel


class MenuItem(BaseModel):
    id :int
    name: str
    category: str
    description: str
    availability: bool
    price: float


class MenuResponse(BaseModel):
    status: str = "success"
    count: int
    data: list[MenuItem]
      