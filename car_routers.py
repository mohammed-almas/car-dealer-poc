from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Car
from schemas import CarSchema


router = APIRouter(prefix="/cars")


@router.post("/addCar", status_code=status.HTTP_201_CREATED)
async def add_car(request: CarSchema, db: Session = Depends(get_db)):
    try:
        car = Car(model_name=request.model_name, price=request.price, dealer_id = request.dealer_id)
        db.add(car)
        db.commit()
        db.refresh(car)
        return car
   
    except SQLAlchemyError as err:
        db.rollback()
        print(f"An error occurred: {err}")


@router.get("/")
async def get_cars(db: Session = Depends(get_db)):
    cars = db.query(Car).all()
    if not cars:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No Cars found")

    return cars


@router.get("/{id}")
async def get_car(id: str, db: Session = Depends(get_db)):
    car = db.query(Car).get(id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Car with ID {id} not found")

    return car


@router.put("/{id}")
async def update_car(id: int, request: CarSchema, db: Session = Depends(get_db)):
    car = db.query(Car).get(id)

    ## Alternate ways to update car
    # car = db.query(Car).filter(Car.id == id).update({**request.dict()})
    # car = db.query(Car).filter(Car.id == id).update({
    #         "model_name":request.model_name,
    #         "price": request.price,
    #         "dealer_id": request.dealer_id})

    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Car with ID {id} not found")

    try:
        car.model_name = request.model_name
        car.price = request.price
        car.dealer_id = request.dealer_id

        db.commit()
        return car

    except SQLAlchemyError as err:
        db.rollback()
        print(f"An error occurred: {err}")


@router.delete("/{id}")
async def delete_car_by_id(id: int, db: Session = Depends(get_db)):
    car = db.query(Car).get(id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Car with ID {id} not found")

    try:
        db.delete(car)
        db.commit()
        return car

    except SQLAlchemyError as err:
        db.rollback()
        print(f"An error occurred: {err}")