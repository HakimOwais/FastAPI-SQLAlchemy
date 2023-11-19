from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(
    prefix='/blog', 
    tags=['blog']
    )

class Image(BaseModel):
    url: str
    alias: str

#Request Body ---- POST method ---- Pydantic BaseModel
class BlogModel(BaseModel):
    title : str
    content : str
    nb_comments : int
    published : Optional[bool]
    tags: List[str] = []
    metadata: Dict[str,str] = {'key1': 'val1'}
    image: Optional[Image] = None

@router.post('/new/{id}')
def create_blog(blog : BlogModel, id: int, version: int):
    return {
        'id': id,
        'data': blog,
        'version': version
    }
    

@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int, 
                   comment_title: int = Query(None,
                        title="Title of the comment",
                        description='Some description for comment_title',
                        alias='commentTitle',
                        deprecated=True
                        ),
                        content: str = Body(...,                #Elipsis or 3 dots ...
                                            min_length=10,
                                            max_length=50,
                                            regex='^[a-z].+$'),   
                        v: Optional[List[str]] = Query(None)
                   ):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'content': content,
        'version': v
    }
    
