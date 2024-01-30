from fastapi import FastAPI

from database import engine, Base
from dealer_routers import router as dealer_routers
from car_routers import router as car_routers


Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(dealer_routers)
app.include_router(car_routers)


@app.get("/")
def home():
    return {"message": "Home Page"}
