#pydantic_04.py
from pydantic import BaseModel, Field, ValidationError
from typing import Optional

class User(BaseModel):
    username: str = Field(..., description="The user's username", example="john_doe")
    email: str = Field(..., description="The user's email address", example="john.doe@example.com")
    password: str = Field(..., min_length=8, description="The user's password")
    age: Optional[int] = Field(None, ge=0, le=120, description="The user's age, must be between 0 and 120", example=30)
    is_active: bool = Field(default=True, description="Is the user currently active?", example=True)

# Example usage
try:
    user = User(username="john_doe", email="john.doe@example.com", password="Secret123")
    print(user)
except ValidationError as e:
    print(e.json())

class Foo(BaseModel):
    positive: int = Field(gt=0)
    non_negative: int = Field(ge=0)
    negative: int = Field(lt=0)
    non_positive: int = Field(le=0)
    even: int = Field(multiple_of=2)
    love_for_pydantic: float = Field(allow_inf_nan=True)


foo = Foo(
    positive=1,
    non_negative=0,
    negative=-1,
    non_positive=0,
    even=2,
    love_for_pydantic=float('inf'),
)
print(foo)

class Foo(BaseModel):
    short: str = Field(min_length=3)
    long: str = Field(max_length=10)
    regex: str = Field(pattern=r'^\d*$')  


foo = Foo(short='foo', long='foobarbaz', regex='123')
print(foo)

from decimal import Decimal

class Foo(BaseModel):
    precise: Decimal = Field(max_digits=5, decimal_places=2)


foo = Foo(precise=Decimal('123.45'))
print(foo)