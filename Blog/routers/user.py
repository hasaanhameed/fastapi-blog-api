from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Blog import schemas, database
from Blog.repository import user

router = APIRouter(tags=['Users'], prefix='/user')
get_db = database.get_db

# Operations for USER 
# Create a user
@router.post('/', response_model=schemas.ShowUser)
def create_user(request : schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

# Get a user by ID
@router.get('/{id}', response_model= schemas.ShowUser)
def get(id : int, db : Session = Depends(get_db)):
    return user.get(id, db)