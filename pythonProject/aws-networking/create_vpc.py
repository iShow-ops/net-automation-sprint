import boto3


def create_vpc():
    ec2 = boto3.client('ec2')

    # Create the VPC
    vpc_response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = vpc_response['Vpc']['VpcId']
    print(f"✅ Created VPC: {vpc_id}")

    # Enable DNS support (optional but useful)
    ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsSupport={'Value': True})
    ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsHostnames={'Value': True})

    # Add a name tag to the VPC
    ec2.create_tags(Resources=[vpc_id], Tags=[{'Key': 'Name', 'Value': 'AutomationVPC'}])
    print(f"🏷️ Tagged VPC as 'AutomationVPC'")

    return vpc_id


if __name__ == "__main__":
    create_vpc()
