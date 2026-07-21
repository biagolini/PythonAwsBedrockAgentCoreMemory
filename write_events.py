"""
Write Events: Simulates a customer conversation with the car dealership
agent and writes it to AgentCore Memory.
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

REGION = os.getenv("AWS_REGION", "us-east-1")
MEMORY_ID = os.getenv("MEMORY_ID")

if not MEMORY_ID:
    print("Error: MEMORY_ID not set in .env file")
    sys.exit(1)

from bedrock_agentcore.memory import MemorySessionManager
from bedrock_agentcore.memory.constants import ConversationalMessage, MessageRole

session_manager = MemorySessionManager(
    memory_id=MEMORY_ID,
    region_name=REGION
)

session = session_manager.create_memory_session(
    actor_id="customer-001",
    session_id="visit-001"
)

print("Writing conversation to memory...")

session.add_turns(
    messages=[
        ConversationalMessage(
            "Welcome to our dealership! How can I help you find your next car?",
            MessageRole.ASSISTANT
        )
    ]
)

session.add_turns(
    messages=[
        ConversationalMessage(
            "I'm looking for a reliable SUV under $25,000. I prefer something "
            "with low mileage, ideally in white or silver.",
            MessageRole.USER
        )
    ]
)

session.add_turns(
    messages=[
        ConversationalMessage(
            "Based on your budget and color preferences, I'd recommend looking at "
            "our Toyota RAV4 2022 in silver with 28,000 miles, or the Honda CR-V 2021 "
            "in white with 32,000 miles. Both are well within your budget.",
            MessageRole.ASSISTANT
        )
    ]
)

print("Conversation written to memory.")

print("\n--- Short-term Memory (last turns) ---")
turns = session.get_last_k_turns(k=5)
for turn in turns:
    for message in turn:
        role = message["role"]
        text = message["content"]["text"]
        print(f"  [{role}] {text}")
