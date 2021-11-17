from fastapi import FastAPI, Path
import json
from  typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    release_date : Optional[str] = None 
    isdn : str
    price : float
class UpdateItem(BaseModel):
    name : Optional[str] = None
    release_date : Optional[str] = None 
    isdn : Optional [str] = None
    price : Optional [float] = None





book_db = {
        1 : {"name" : "Linux for dummies" , "release_date" : "Feb2021" , "isdn" : "A2002021" , "price" : 2.50 },
        2 : {"name" : "Java for dummies" , "release_date" : "Mar2021" , "isdn" : "A2012021" , "price" : 4.50},
        3 : {"name" : "PHP for dummies" , "release_date" : "Apr2021" , "isdn" : "A2022021" , "price" : 5.00},
        4 : {"name" : "AWS for dummies" , "release_date" : "May2021" , "isdn" : "A2032021" , "price" : 2.20},
        5 : {"name" : "Python for dummies" , "release_date" : "Feb2021" , "isdn" : "A2042021" , "price" : 4.50}
        }

# book_db = {}

@app.get("/")   #path paramater example
def get_item():
    return book_db

@app.get("/get_item/{book_id}")   #path paramater example
def get_item(book_id : int):
    return book_db[book_id]

@app.get("/get_by_name")
def get_item_by_name(name : Optional[str] = None): # None made the "name" parameter not mandatory (optional) then instead of error msg it returns "Item not found" data / playtime 31:36
    for book_id in book_db:
        if book_db[book_id]["name"] == name:
            return book_db[book_id]
    return {"data" : "Item not found"}


# Create items ----------------------------------------------------
@app.post("/add_book/{item_id}")
def create_item(item_id: int , item : Item):
    if item_id in book_db:
        return {"Error" : "Item ID alreday exists."}
    # book_db[book_id] = {"name" : clsbook.name , "release_date" : clsbook.release_date , "isdn" : clsbook.isdn , "price" : clsbook.price}
    book_db[item_id] = item
    return book_db[item_id]

# Update items ----------------------------------------------------
@app.post("/update_book/{item_id}")
def update_item(item_id: int, item : UpdateItem):
    if item_id not in book_db:
        return {"Error" : "Item ID does not exists."}
            # book_db[book_id] = {"name" : clsbook.name , "release_date" : clsbook.release_date , "isdn" : clsbook.isdn , "price" : clsbook.price}
    if item.name != None:
        # book_db[item_id].name = item.name
        book_db[item_id]["name"] = item.name
    if item.release_date != None:
        # book_db[item_id].release_date = item.release_date
        book_db[item_id]["release_date"] = item.release_date
    if item.isdn != None:
        # book_db[item_id].isdn = item.isdn
        book_db[item_id]["isdn"] = item.isdn
    if item.price != None:
        # book_db[item_id].price = item.price
        book_db[item_id]["price"] = item.price
    # book_db[item_id]= []
    return book_db[item_id]

#  Delete item -------------------------------------------------------
@app.delete("/delete_item")
def delete_item(item_id : int ):
    if item_id not in book_db:
        return {"Error" : "ID does not exist."}
    
    del book_db[item_id]
    return {"Sucess" : "Item deleted!"}



  #  pip install fastapi  
#  pip install uvicorn  
#  -m pip install --upgrade pip
#  pip install --upgrade 
# uvicorn myapp_final:app --reload 
