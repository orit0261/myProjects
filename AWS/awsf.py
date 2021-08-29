import os

import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

import os

path = "C:\\Users\\Orit\\Pictures\\Saved Pictures\\"

# Check current working directory.
retval = os.getcwd()

print ("Current working directory %s" % retval)

# Now change the directory
os.chdir( path )

# Check current working directory.
retval = os.getcwd()

print("Directory changed successfully")

data = open('maxresdefault.jpg', 'rb')
s3.Bucket('orit-bucket').put_object(Key='test.jpg', Body=data)
