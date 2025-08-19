import boto3


def create_and_attach_igw(vpc_id):
    ec2 = boto3.client('ec2', region_name='us-east-1')  # Use your region

    # 1. Create Internet Gateway
    igw_response = ec2.create_internet_gateway()
    igw_id = igw_response['InternetGateway']['InternetGatewayId']
    print(f"✅ Created Internet Gateway: {igw_id}")

    # 2. Attach Internet Gateway to your VPC
    ec2.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
    print(f"✅ Attached Internet Gateway {igw_id} to VPC {vpc_id}")

    return igw_id


if __name__ == "__main__":
    # Replace with your actual VPC ID
    my_vpc_id = 'vpxxxxxxxxxxxx'
    create_and_attach_igw(my_vpc_id)
