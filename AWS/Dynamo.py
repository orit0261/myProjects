import boto3
from boto3.dynamodb.conditions import Key, Attr


def create_bunch_of_users():
        dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

        table = dynamodb.Table('Users')

        for n in range(3):
            table.put_item(Item={
                'id': n,
                'first_name': 'Jon',
                'last_name': 'Doe' + str(n),
                'email': 'jdoe' + str(n) + '@test.com'
            })

def put_item(n):
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

    table = dynamodb.Table('Users')

    table.put_item(Item={
        'id': n,
        'first_name': 'Jon',
        'last_name': 'Doe' + str(n),
        'email': 'jdoe' + str(n) + '@test.com'
    })





def get_item():
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

    table = dynamodb.Table('Users')

    resp = table.get_item(
        Key={
            'id': 1,
        }
    )

    if 'Item' in resp:
        print(resp['Item'])

def query():
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

    table = dynamodb.Table('Users')
    response = table.scan(
        FilterExpression=Attr('id').gte(1)
    )
    items = response['Items']
    print(items)



def delete_user():
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

    table = dynamodb.Table('Users')

    response = table.delete_item(
        Key={
            'id': 1,
        },
    )
if __name__ == "__main__":
    query()