import boto3     #used to Import Boto3 in code
client = boto3.client('ec2')    # Create the EC2 client

response = client.run_instances(
    ImageId='ami-050cd642fd83388e4',
    InstanceType='t2.micro',
    KeyName='Vaibhav',
    MaxCount=1,
    MinCount=1,
)
