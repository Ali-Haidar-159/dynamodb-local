from table_create import dynamodb
from boto3.dynamodb.conditions import Key

table = dynamodb.Table("Products")


def filter_operations() :
    response = table.scan(
        FilterExpression=Key('productId').between(50, 100)
    )

    items = response.get('Items', [])
    for item in items:
        print(item.get('name'))
