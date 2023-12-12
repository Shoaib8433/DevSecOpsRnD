import boto3
import json

def create_iam_user(user_name, policy_arns):
    iam_client = boto3.client('iam')

    # Create IAM user
    response = iam_client.create_user(UserName=user_name)
    user_arn = response['User']['Arn']

    # Attach policies to the user
    for policy_arn in policy_arns:
        iam_client.attach_user_policy(UserName=user_name, PolicyArn=policy_arn)

    print(f"IAM User '{user_name}' created with policies: {policy_arns}")
    print(f"User ARN: {user_arn}")

def main():
    # Read IAM configuration from JSON file
    with open('iam_config.json') as f:
        iam_config = json.load(f)

    for user_data in iam_config.get('users', []):
        username = user_data.get('username')
        policies = user_data.get('policies', [])

        if username and policies:
            create_iam_user(username, policies)
        else:
            print(f"Skipping user creation for {username}. Missing username or policies.")

if __name__ == "__main__":
    main()
