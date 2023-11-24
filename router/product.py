from fastapi import APIRouter, Header
from typing import Optional, List
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

router = APIRouter(
    prefix = '/product',
    tags = ['product']
)

products = ['watch','camera','phone']

@router.get('/all')
def get_all_products():
    # return products
    data = " ".join(products)
    return Response(content=data, media_type='text/plain')

@router.get('/withheaders')
def get_products(
    response: Response,
    custom_header: Optional[List[str]] = Header(None)
    ):
    response.headers['custom_response_header'] = ", ".join(custom_header)
    return products

@router.get('/{id}', responses={
    200: {
        "content": {
            "text/html": {
               "example": "<div>Product</div>"
            }
        },
        "description": "Return the HTML fo an object"
    },
    404: {
       "content": {
            "text/plain": {
              "example": "Product not available"
            }
        },
        "description": "A clear text error message" 
    }
})
def get_product(id: int):
    if 0 < id < len(products):
        product = products[id]
        out = f"""
        <head>
            <style>
            .product{{
                width: 500px;
                height: 30px;
                border: 2px insert green;
                background-color: lightblue;
                text-align: centre;
            }}
            </style>
        </head>
        <div class="product">{product}</div>
        """
        return HTMLResponse(content=out, media_type="text/html")
    else:
        out = "Product not available"
        return PlainTextResponse(status_code=404, content=out, media_type='text/plain')
    
