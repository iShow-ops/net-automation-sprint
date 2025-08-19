import boto3


def setup_public_route_table(vpc_id, public_subnet_id, igw_id):
    ec2 = boto3.client('ec2', region_name='us-east-1')

    # 1. Create a route table in the VPC
    route_table_response = ec2.create_route_table(VpcId=vpc_id)
    route_table_id = route_table_response['RouteTable']['RouteTableId']
    print(f"✅ Created Route Table: {route_table_id}")

    # 2. Create a route that directs all outbound traffic to the Internet Gateway
    ec2.create_route(
        RouteTableId=route_table_id,
        DestinationCidrBlock='0.0.0.0/0',
        GatewayId=igw_id
    )
    print(f"✅ Created route to IGW {igw_id} in route table {route_table_id}")

    # 3. Associate the route table with the public subnet
    ec2.associate_route_table(RouteTableId=route_table_id, SubnetId=public_subnet_id)
    print(f"✅ Associated Route Table {route_table_id} with Public Subnet {public_subnet_id}")

    return route_table_id


if __name__ == "__main__":
    vpc_id = 'vxxxxxxxxxxxxxx'  # Replace with your VPC ID
    public_subnet_id = 'sxxxxxxxxxxxx'  # Replace with your Public Subnet ID
    igw_id = 'ixxxxxxxxxxxxxx'  # Replace with your Internet Gateway ID

    setup_public_route_table(vpc_id, public_subnet_id, igw_id)
