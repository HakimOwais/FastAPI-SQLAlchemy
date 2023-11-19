# Routers (Separate operations into multiple files, Share prefix between multiple operations,share tags) 
# Refactoring the router ----Adding a second router
from fastapi import FastAPI, APIRouter, status, Response
from enum import Enum
from typing import Optional 

router = APIRouter(
    prefix='/blog', 
    tags=['blog']
    )

# Type parameters

# Path parameters
# @router.get("/blog/{id}")
# def get_blog(id):
#     return {"message" : f"Blog with id {id}"}

#Pydantic -----order is important
# @router.get("/blog/all")
# def get_all_blogs():
#     return {"message": "All blogs provided"}

# Query Parameters
@router.get(
        "/all",
         summary= "Retrieve all blogs",
         description= "This api simulates fetching all blogs.",
         response_description="The list of all available blogs"
         )
def get_all_blogs(page=1, page_size: Optional[int]=None):
    return {"message": f"All {page_size} blogs on page {page}"}

# #Status Code
# @router.get("/blog/{id}")
# def get_blog(id: int):
#     return {"message" : f"Blog with id {id}"}



# @router.get("/blog/all")
# def get_all_blogs(page=1, page_size: Optional[int]=None):
#     return {"message": f"All {page_size} blogs on page {page}"}

#Query and Path Parameters
@router.get("/{id}/comments/{comment_id}", tags=["comment"])
def get_comment(id: int,comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog
    
    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** query parameter
    - **username** optional query parameter
    """
    return {"message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"}


class BlogType(str, Enum):  
    short = "short"
    story = "story"
    howto = "howto"
    
@router.get("/type/{type}"
         )
def get_blog_type(type : BlogType):
    return {"message":f"Blog type {type}"}    

# #Status Code
# @router.get("/blog/{id}", status_code=status.HTTP_404_NOT_FOUND)
# def get_blog(id: int):
#     if id > 5:
#         return {"error" : f"Blog {id} not found"}
#     else:
#         return {"message" : f"Blog with id {id}"}

@router.get("/{id}", status_code=status.HTTP_200_OK
         )
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error" : f"Blog {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message" : f"Blog with id {id}"}