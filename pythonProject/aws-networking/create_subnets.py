import boto3

def create_subnets(vpc_id):
    ec2 = boto3.client('ec2', region_name='us-east-1')  # Update to your region

    # Create a Public Subnet
    public_subnet = ec2.create_subnet(
        VpcId=vpc_id,
        CidrBlock='10.0.1.0/24',
        AvailabilityZone='us-east-1a'
    )
    public_subnet_id = public_subnet['Subnet']['SubnetId']
    print(f"✅ Created Public Subnet: {public_subnet_id}")

    ec2.create_tags(Resources=[public_subnet_id], Tags=[{'Key': 'Name', 'Value': 'PublicSubnet'}])

    # Create a Private Subnet
    private_subnet = ec2.create_subnet(
        VpcId=vpc_id,
        CidrBlock='10.0.2.0/24',
        AvailabilityZone='us-east-1a'
    )
    private_subnet_id = private_subnet['Subnet']['SubnetId']
    print(f"✅ Created Private Subnet: {private_subnet_id}")

    ec2.create_tags(Resources=[private_subnet_id], Tags=[{'Key': 'Name', 'Value': 'PrivateSubnet'}])

    return public_subnet_id, private_subnet_id

if __name__ == "__main__":
    # Option 1: Hardcode your VPC ID for testing
    vpc_id = 'vxxxxxxxxx'  # Replace with actual VPC ID
    create_subnets(vpc_id)