import boto3
from diagrams import Diagram
from diagrams.aws.network import VPC, InternetGateway, NATGateway, ALB, NLB
from diagrams.generic.network import Subnet

# Connect to AWS
session = boto3.Session(profile_name="default")
ec2_client = session.client("ec2")
elb_client = session.client("elbv2")  # Load Balancer API

# Get the list of all VPCs
vpcs = ec2_client.describe_vpcs()["Vpcs"]
vpc_ids = {str(index + 1): vpc["VpcId"] for index, vpc in enumerate(vpcs)}

# Display available VPCs
print("\n🔍 Available VPCs:")
for index, vpc in enumerate(vpcs, start=1):
    print(f"{index}. {vpc['VpcId']}")

# User selects a VPC
selected_vpc_key = None
while selected_vpc_key not in vpc_ids:
    selected_vpc_key = input("\n👉 Enter the number of the VPC you want to visualize (or type 'q' to quit): ").strip()
    if selected_vpc_key.lower() == 'q':
        print("👋 Exiting the program. Goodbye!")
        exit()
    if selected_vpc_key not in vpc_ids:
        print("❌ Invalid selection. Please enter a valid number from the list or 'q' to quit.")

selected_vpc_id = vpc_ids[selected_vpc_key]
print(f"✅ Selected VPC: {selected_vpc_id}")

# Fetch VPC-related resources
subnets = ec2_client.describe_subnets(Filters=[{"Name": "vpc-id", "Values": [selected_vpc_id]}])["Subnets"]
internet_gateways = ec2_client.describe_internet_gateways(Filters=[{"Name": "attachment.vpc-id", "Values": [selected_vpc_id]}])["InternetGateways"]
nat_gateways = ec2_client.describe_nat_gateways(Filters=[{"Name": "vpc-id", "Values": [selected_vpc_id]}])["NatGateways"]
load_balancers = elb_client.describe_load_balancers()["LoadBalancers"]

# Filter Load Balancers in this VPC
lb_nodes = []
for lb in load_balancers:
    if lb["VpcId"] == selected_vpc_id:
        if lb["Type"] == "application":
            lb_nodes.append(ALB(lb["LoadBalancerName"]))
        elif lb["Type"] == "network":
            lb_nodes.append(NLB(lb["LoadBalancerName"]))

# Create the diagram
with Diagram(f"AWS VPC - {selected_vpc_id}", show=True, filename=f"vpc_{selected_vpc_id}"):
    vpc_diagram = VPC(selected_vpc_id)

    # Add Internet Gateways
    igw_nodes = [InternetGateway(igw["InternetGatewayId"]) for igw in internet_gateways]

    # Add NAT Gateways
    nat_nodes = [NATGateway(nat["NatGatewayId"]) for nat in nat_gateways]

    # Add Subnets
    subnet_nodes = [Subnet(subnet["SubnetId"]) for subnet in subnets]

    # Connect resources
    for igw in igw_nodes:
        igw >> vpc_diagram

    for nat in nat_nodes:
        nat >> vpc_diagram

    for subnet in subnet_nodes:
        vpc_diagram >> subnet

    for lb in lb_nodes:
        lb >> vpc_diagram  # Connect Load Balancers to VPC

print(f"\n📊 Diagram saved as vpc_{selected_vpc_id}.png")
