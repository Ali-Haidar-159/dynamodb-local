from table_create import dynamodb

table = dynamodb.Table("Products")

def updateSingleData() : 
    table.update_item(
        Key = {
            "productId" : 102
        } ,
        UpdateExpression = "SET price = :newPrice , product_name = :newProductName" ,
        ExpressionAttributeValues = {
            ":newPrice" : 69000 ,
            ":newProductName" : "computer-pc"   
        }
    )
    print("data is updated")