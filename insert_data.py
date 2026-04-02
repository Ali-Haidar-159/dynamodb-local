import boto3
import random
from table_create import dynamodb

table = dynamodb.Table('Products')

categories = ["Tech", "Gear", "Gadget", "Pro", "Smart"]
types = ["Monitor", "Keyboard", "Hub", "Speaker", "Camera", "Mic", "Drive"]

items = []

for i in range(1, 101):
    # Generates names like "Tech-Drive-1"
    name = f"{random.choice(categories)}-{random.choice(types)}-{i}"
    
    # Generates a price between 500 and 10000 in steps of 100
    price = random.randint(5, 100) * 100 
    
    items.append({
        'productId': i,
        'name': name,
        'price': price
    })

def insertData():
    
    table.put_item(
        Item = {
            "productId" :102 ,
            "product_name" : "Computer" ,
            "price" : "55000"
        }
    )

    print("data is inserted successfully")


def insertMultipleData():
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)

    print("all data is inserted")