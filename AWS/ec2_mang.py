import boto3

instance_id=("i-0e2bbdf4fc43bf6db")

ec2 = boto3.client('ec2', region_name='us-east-1')
response = ec2.describe_instances()
print(response)