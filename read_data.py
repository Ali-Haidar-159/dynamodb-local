from table_create import dynamodb

table = dynamodb.Table("Products")

def readSingleData () :
    data = table.get_item(
        Key = {
            "productId" : 101
        }
    )   
    print("The products is : ",data)


def readAllData() :
    allData = table.scan()
    print("All data : ",allData)