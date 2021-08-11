"""entry point"""

from fastapi import FastAPI, Depends

app = FastAPI()


# Routes for interacting with the API
@app.post('/user/', response_model=User)
def CreateUser(user: User, db: Session = Depends(get_db)):
     = create_place(db, place)
    return db_place

@app.get('/places/', response_model=List[Place])
def get_places_view(db: Session = Depends(get_db)):
    return get_places(db)

@app.get('/place/{place_id}')
def get_place_view(place_id: int, db: Session = Depends(get_db)):
    return get_place(db, place_id)

@app.get('/')
async def root():
    return {'message': 'Hello World!'}
