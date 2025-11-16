from fastapi import APIRouter
from Blog import schemas, database
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, status
from Blog.repository import blog
from Blog.oauth2 import get_current_user

router = APIRouter(tags=['Blogs'], prefix='/blog')
get_db = database.get_db

# Retrieve all blogs from the database 
@router.get('/', response_model = List[schemas.ShowBlog])
def retrieve_blogs(db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)

# Add a new blog to the database
@router.post('/', status_code=status.HTTP_201_CREATED) 
def create_blog(request : schemas.Blog, db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)): # Depends converts Session to pydantic function
    return blog.create(request, db)

# Retrieve a blog by ID
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def retrieve_one_blog(id, db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_one(id, db)

# Delete a blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.delete(id, db)

# Update a blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.update(id, request, db)