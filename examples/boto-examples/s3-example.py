import boto3

s3 = boto3.resource('s3')
# for bucket in s3.list_buckets.all():
    # print(bucket.name)


# listing objects

s3_client = boto3.client('s3')
list_buckets = s3_client.list_buckets()
print(list_buckets)
