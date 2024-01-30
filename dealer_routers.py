from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models import Dealer
from schemas import DealerSchema


router = APIRouter(prefix="/dealers")


@router.post("/addDealer", status_code=status.HTTP_201_CREATED)
async def add_dealer(request: DealerSchema, db: Session = Depends(get_db)):
    try:
        dealer = Dealer(name=request.name, address=request.address)
        db.add(dealer)
        db.commit()
        db.refresh(dealer)
        return dealer

    except SQLAlchemyError as err:
        db.rollback()
        print(f"An error occurred: {err}")


@router.get("/")
async def get_dealers(db: Session = Depends(get_db)):
    dealers = db.query(Dealer).all()
    if not dealers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No Dealers found")

    return dealers


@router.get("/{id}")
async def get_dealer_by_id(id: str, db: Session = Depends(get_db)):
    dealer = db.query(Dealer).get(id)
    if not dealer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Dealer with ID {id} not found")

    return dealer


@router.put("/{id}")
async def update_dealer(id: int, request: DealerSchema, db: Session = Depends(get_db)):
    dealer = db.query(Dealer).get(id)

    ## Alternate way to update dealer
    # dealer = db.query(Dealer).filter(Dealer.id == id).update({**request.dict()})

    if not dealer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Dealer with ID {id} not found")

    try:
        dealer.name = request.name
        dealer.address = request.address
        
        db.commit()
        return dealer

    except SQLAlchemyError as err:
        db.rollback()
        print(f"An error occurred: {err}")
    

@router.delete("/{id}")
async def delete_dealer_by_id(id: int, db: Session = Depends(get_db)):
    dealer = db.query(Dealer).get(id)
    if not dealer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Dealer with ID {id} not found")

    try:
        db.delete(dealer)
        db.commit()
        return dealer

    except SQLAlchemyError as err:
        db.rollback()
        print(f"An error occurred: {err}")
