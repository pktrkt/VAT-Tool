import boto3
import os
import uuid
import time
#import decimal

def lambda_handler( event, context ):
    
    # Generate a new record identifier
    recordId = str(uuid.uuid4())
    
    # Record the username
    userName = event["userName"]
    
    # Calculate the current date
    curDate = time.strftime("%d/%m/%Y")
    
    # Set up taxBox variables
    taxBox1 = event["taxBox1"]
    taxBox2 = event["taxBox2"]
    taxBox4 = event["taxBox4"]
    taxBox6 = event["taxBox6"]
    taxBox7 = event["taxBox7"]
    taxBox8 = event["taxBox8"]
    taxBox9 = event["taxBox9"]
    
    # These taxBox variables are calculated from the others
    taxBox3 = taxBox1 + taxBox2
    taxBox5 = taxBox3 - taxBox4


    print('Generating new DynamoDB record, with ID: ' + recordId)
    print('User creating record: ' + userName)
    print('Current date: ') + curDate
    print('Input amount: ', + taxBox1)
    print('Input amount: ', + taxBox2)
    print('Calculated amount: ' + str(taxBox3))
    print('Input Text: ', + taxBox4)
    print('Calculated amount: ' + str(taxBox5))
    print('Input amount: ', + taxBox6)
    print('Input amount: ', + taxBox7)
    print('Input amount: ', + taxBox8)
    print('Input amount: ', + taxBox9)
    
    #Creating new record in DynamoDB table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])
    table.put_item(
        Item={
            'id' : recordId,
            'userName' : userName,
            'curDate' : curDate,
            'taxBox1' : str(taxBox1),
            'taxBox2' : str(taxBox2),
            'taxBox3' : str(taxBox3),
            'taxBox4' : str(taxBox4),
            'taxBox5' : str(taxBox5),
            'taxBox6' : str(taxBox6),
            'taxBox7' : str(taxBox7),
            'taxBox8' : str(taxBox8),
            'taxBox9' : str(taxBox9)
        }
    )
    
    return recordId
