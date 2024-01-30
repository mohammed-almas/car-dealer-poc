from pydantic import BaseModel


class DealerSchema(BaseModel):

    id: int
    name: str
    address: str


class CarSchema(BaseModel):

    id: int
    model_name: str
    price: int
    dealer_id: int
