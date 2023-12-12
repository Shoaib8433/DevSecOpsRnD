import boto3
import json

def get_aws_security_groups(aws_access_key_id, aws_secret_access_key, region_name):
    ec2 = boto3.client("ec2", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

    # Retrieve all security groups
    response = ec2.describe_security_groups()
    return response["SecurityGroups"]

def load_rules_config():
    with open("rules.json") as f:
        return json.load(f)

def check_specific_rules(ip_permissions, rules_config):
    specific_rules_warnings = set()

    # Check for specific rules (Modify as needed)
    for permission in ip_permissions:
        if "FromPort" in permission and "IpRanges" in permission:
            for ip_range in permission["IpRanges"]:
                port = permission["FromPort"]
                cidr_ip = ip_range["CidrIp"]

                for rule in rules_config:
                    if rule["Port"] == port and rule["CidrIp"] == cidr_ip:
                        specific_rules_warnings.add(rule["Description"])

    return specific_rules_warnings

def analyze_security_groups(account, region, security_groups, rules_config):
    print(f"\nAnalyzing Security Groups for Account: {account}, Region: {region}")

    for sg in security_groups:
        print(f"\n- Security Group: {sg['GroupId']}")

        # Check for specific rules (e.g., SSH open to the world)
        specific_rules_warnings = check_specific_rules(sg["IpPermissions"], rules_config)

        if specific_rules_warnings:
            print(f"Warning: Specific rules exposed to the internet:")
            for rule_warning in specific_rules_warnings:
                print(f"  - {rule_warning}")
        else:
            print("No specific rules exposed to the internet in this security group.")

def load_credentials(account_name):
    # Load AWS credentials from a configuration file
    with open("aws_credentials.json") as f:
        credentials = json.load(f)

    return credentials.get(account_name)

def main():
    # Define AWS accounts and regions to audit
    accounts_regions = {
        "ProductionAccount": ["us-east-1", "us-west-2"],
        # "DevelopmentAccount": ["eu-west-1", "ap-southeast-1"],
        # "TestingAccount": ["us-west-2", "eu-central-1"],
        # "StagingAccount": ["ap-southeast-2", "sa-east-1"],
    }

    rules_config = load_rules_config()

    for account, regions in accounts_regions.items():
        # Load AWS credentials for the current account
        credentials = load_credentials(account)

        # Use credentials to analyze security groups for each region
        aws_access_key_id = credentials.get("aws_access_key_id")
        aws_secret_access_key = credentials.get("aws_secret_access_key")

        if aws_access_key_id and aws_secret_access_key:
            for region in regions:
                # Get and analyze security groups for the current account and region
                security_groups = get_aws_security_groups(aws_access_key_id, aws_secret_access_key, region)
                analyze_security_groups(account, region, security_groups, rules_config)
        else:
            print(f"Missing credentials for {account}")

if __name__ == "__main__":
    main()
