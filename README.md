# AWS Bedrock AgentCore Memory

**Author:** Carlos Biagolini-Jr.

**LinkedIn:** [https://www.linkedin.com/in/biagolini/](https://www.linkedin.com/in/biagolini/)

**Medium:** [https://medium.com/@biagolini](https://medium.com/@biagolini)

## Overview

This project demonstrates how to use [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) to store conversation history and extract long-term semantic memories for AI agents.

The scripts show how to create a memory resource, write conversation events, and retrieve automatically extracted insights using semantic search.

## Prerequisites

- AWS account with credentials configured
- Python 3.12 installed
- IAM user or role with permissions to use Amazon Bedrock AgentCore Memory
- AWS Region where AgentCore is available (us-east-1, us-west-2, ap-southeast-2, or eu-central-1)

## Setup

1. Clone this repository:

```bash
git clone https://github.com/biagolini/PythonAwsBedrockAgentCoreMemory.git
cd PythonAwsBedrockAgentCoreMemory
```

2. Create and activate a virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Copy the example environment file and edit with your values:

```bash
cp .env.example .env
```

## Usage

### Step 1: Create a Memory Resource via Console

Navigate to **Amazon Bedrock AgentCore > Memory** in the AWS Console and create a memory resource with the Semantic strategy. Copy the Memory ID and add it to your `.env` file.

### Step 2: Write Conversation Events

```bash
python write_events.py
```

This simulates a customer conversation and writes it to memory. It also demonstrates retrieving short-term memory (last turns).

### Step 3: Retrieve Long-term Memory

```bash
python retrieve_memory.py
```

This waits for long-term memory extraction and then demonstrates listing records and performing semantic search.

## Project Structure

```
.
├── .env.example          # Template for environment variables
├── .gitignore
├── requirements.txt      # Python dependencies
├── write_events.py       # Writes conversation events to memory
├── retrieve_memory.py    # Retrieves long-term memory records
├── LICENSE
└── README.md
```

## Cleanup

After testing, delete the memory resource:

```bash
aws bedrock-agentcore-control delete-memory \
  --memory-id "<your-memory-id>" \
  --region us-east-1
```

## Contributing

Feel free to submit issues and pull requests.

## License

This project is open source and available under the [MIT License](LICENSE).
