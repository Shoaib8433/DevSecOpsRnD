import boto3

aws_access_key_id = ''
aws_secret_access_key = ''
region_name = 'us-east-1'

print("=== Instances without terminate protection ==============")

try:
    ec2_client = boto3.client('ec2', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    instances = ec2_client.describe_instances()['Reservations']

    for reservation in instances:
        for instance in reservation['Instances']:
            if not instance.get('InstanceLifecycle') and not instance.get('InstanceInitiatedShutdownBehavior') == 'terminate':
                if instance['State']['Name'] == 'running':
                    print(f"Instance Name: {instance.get('Tags', [{}])[0].get('Value', 'N/A')}")
                    print(f"Instance ID: {instance['InstanceId']}")
                    print("Termination Protection: Disabled")
                    print("===================================")

except Exception as e:
    print("An error occurred:")
    print(e)
    traceback.print_exc()

print("=====================================================")
