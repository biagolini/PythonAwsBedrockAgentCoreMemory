"""
Retrieve Memory: Retrieves long-term memory records and performs
semantic search to find relevant customer information.
"""

import os
import sys
import time
from dotenv import load_dotenv

load_dotenv()

REGION = os.getenv("AWS_REGION", "us-east-1")
MEMORY_ID = os.getenv("MEMORY_ID")

if not MEMORY_ID:
    print("Error: MEMORY_ID not set in .env file")
    sys.exit(1)

from bedrock_agentcore.memory import MemorySessionManager

session_manager = MemorySessionManager(
    memory_id=MEMORY_ID,
    region_name=REGION
)

session = session_manager.create_memory_session(
    actor_id="customer-001",
    session_id="visit-001"
)

print("Waiting for long-term memory extraction (about 30 seconds)...")
time.sleep(30)

print("\n--- Long-term Memory Records ---")
memory_records = session.list_long_term_memory_records(
    namespace_path="/"
)

for i, record in enumerate(memory_records, 1):
    text = record["content"]["text"]
    print(f"  {i}. {text}")

print("\n--- Semantic Search: 'budget' ---")
search_results = session.search_long_term_memories(
    query="budget",
    namespace_path="/",
    top_k=3
)

for i, result in enumerate(search_results, 1):
    text = result["content"]["text"]
    score = result.get("score", 0)
    print(f"  {i}. [score: {score:.2f}] {text}")
