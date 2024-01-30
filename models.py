from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Dealer(Base):
    __tablename__ = "dealers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)

    cars = relationship("Car", back_populates="dealers")


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String)
    price = Column(Integer)
    dealer_id = Column(Integer, ForeignKey("dealers.id", ondelete="CASCADE"))

    dealers = relationship("Dealer", back_populates="cars")
