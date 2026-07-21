"""
Create Memory: Creates an AgentCore Memory resource with the semantic
strategy for the car dealership agent.
"""

import os
import sys
import time
import boto3
from dotenv import load_dotenv

load_dotenv()

REGION = os.getenv("AWS_REGION", "us-east-1")

control_client = boto3.client("bedrock-agentcore-control", region_name=REGION)

print("Creating memory resource...")
response = control_client.create_memory(
    name="MyCarDealerMemory",
    description="Memory for the car dealership agent to remember customer preferences.",
    eventExpiryDuration=7,
    memoryStrategies=[
        {
            "semanticMemoryStrategy": {
                "name": "CustomerFacts",
                "namespaceTemplates": ["/facts/{actorId}/"]
            }
        }
    ]
)

memory_id = response["memory"]["id"]
print(f"Memory ID: {memory_id}")

print("Waiting for memory to become ACTIVE (this takes 2-3 minutes)...")
while True:
    status_response = control_client.get_memory(memoryId=memory_id)
    status = status_response["memory"]["status"]
    print(f"  Status: {status}")
    if status == "ACTIVE":
        break
    time.sleep(15)

print(f"\nMemory is ready! ID: {memory_id}")
print("Add this ID to your .env file as MEMORY_ID")
