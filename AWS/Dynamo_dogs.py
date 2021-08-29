import json
from decimal import Decimal

import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError


def create_dogs_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.create_table(
        TableName='dogs',
        KeySchema=[
            {
                'AttributeName': 'breed',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'breed',
                'AttributeType': 'S'
            }

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


def create_bunch_of_dogs(dogs):
        dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

        table = dynamodb.Table('dogs')

        for n in dogs:
            breed =  n['breed']
            breedType = n['breedType']
            origin = n['origin']
            popularity = n['popularity']
            temperament = n['temperament']
            hypoallergenic = n['hypoallergenic']
            intelligence = int(n['intelligence'])
            photo= n['photo']
            table.put_item(Item=n)

def delete_dog(d_name):
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

    table = dynamodb.Table('dogs')

    try:
        response = table.delete_item(
            Key={
                "breed": {"S": f"{d_name}"}
            }
        )
    except ClientError as err:
        print(err)
    else:
        return response

def query_dogs(intelligence):
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

    table = dynamodb.Table('dogs')
    response = table.scan(
        FilterExpression=Attr('intelligence').eq(intelligence)
    )
    items = response['Items']
    print(items)


def delete_dogs_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('dogs')
    table.delete()

if __name__ == "__main__":
   query_dogs(9)
   #delete_dogs_table()
   delete_dog('German Shepard')
   #create_dogs_table()
   #with open("dogs.json") as json_file:
   #     dog_list = json.load(json_file, parse_float=Decimal)
   #create_bunch_of_dogs(dog_list)