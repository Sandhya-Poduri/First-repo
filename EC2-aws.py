import boto3
def create_ec2_instance():
   try:
        print("Creating EC2 Instance")
        resource_ec2= boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-0ca285d4c2cda3300",
            MinCount=1,
            MaxCount=1,
            KeyName="EC2-Python"
        )
   except Exception as e:
       print(e)

create_ec2_instance()
resource_ec2 = boto3.client("ec2")
print(resource_ec2.describe_instances())