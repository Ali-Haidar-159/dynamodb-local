import boto3

dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url="http://localhost:8000", 
    region_name="us-east-1",               
    aws_access_key_id="test",             
    aws_secret_access_key="test"
)


def create_table():
    table = dynamodb.create_table(
        TableName='Products',
        KeySchema=[
            {
                'AttributeName': 'productId',
                'KeyType': 'HASH'  
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'productId',
                'AttributeType': 'N'  
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    table.meta.client.get_waiter('table_exists').wait(TableName='Products')
    print("Table created successfully!")

    

if __name__ == "__main__":
    create_table()