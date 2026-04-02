from table_create import dynamodb

table = dynamodb.Table("Products")

def deleteData() :
    table.delete_item(
        Key = {
            "productId" : 106
        }
    )
    print("Ietem is deleted")