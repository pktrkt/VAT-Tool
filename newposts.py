import boto3
import os
import uuid

def lambda_handler(event, context):
    
    recordId = str(uuid.uuid4())
    userName = event["userName"]
    taxField1 = event["taxField1"]
    taxField2 = event["taxField2"]
    taxField3 = event["taxField3"]
    taxField4 = event["taxField4"]

    print('Generating new DynamoDB record, with ID: ' + recordId)
    print('User creating record: ' + userName)
    print('Input Text: ' + taxField1)
    print('Input Text: ' + taxField2)
    print('Input Text: ' + taxField3)
    print('Input Text: ' + taxField4)
    
    
    #Creating new record in DynamoDB table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])
    table.put_item(
        Item={
            'id' : recordId,
            'userName' : userName,
            'taxField1' : taxField1,
            'taxField2' : taxField2,
            'taxField3' : taxField3,
            'taxField4' : taxField4
        }
    )
    
    return recordId
