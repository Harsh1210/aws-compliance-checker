
# AWS Config Compliance API

This FastAPI project provides endpoints to fetch information from AWS Config, such as enabled rules, compliance statuses, and compliance details by rule or resource.

## Features

- Get all enabled AWS Config rules.
- Fetch compliance status for all rules.
- Retrieve compliance details for a specific rule.
- Get compliance details for a specific resource.

---

## Prerequisites

### 1. AWS Account
- Ensure you have an AWS account with AWS Config enabled and rules configured.
- Attach the necessary IAM permissions to your user or EC2 instance role:
  - `config:DescribeConfigRules`
  - `config:DescribeComplianceByConfigRule`
  - `config:GetComplianceDetailsByConfigRule`
  - `config:GetComplianceDetailsByResource`

### 2. Python Environment
- Python 3.10 or above is recommended.
- Install `pip` for managing Python dependencies.

### 3. Required Libraries
Install the following libraries using `pip`:
- `boto3`: For interacting with AWS services.
- `fastapi`: For building the API.
- `uvicorn`: For running the API server.

---

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-repo/aws-config-compliance-api.git
cd aws-config-compliance-api
```

### Step 2: Set Up the Environment
1. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation:**
   ```bash
   pip list
   ```

### Step 3: Configure AWS Credentials
**Option 1: Using AWS CLI**
- Configure credentials using the AWS CLI:
  ```bash
  aws configure
  ```
  Provide:
  - AWS Access Key ID
  - AWS Secret Access Key
  - Default region name (e.g., `us-east-1`)

**Option 2: Using Environment Variables**
- Set environment variables:
  ```bash
  export AWS_ACCESS_KEY_ID="your-access-key"
  export AWS_SECRET_ACCESS_KEY="your-secret-key"
  export AWS_DEFAULT_REGION="your-region"
  ```

**Option 3: Use IAM Role (for EC2)**
- Ensure your EC2 instance has an attached IAM role with the required permissions.

---

## Running the Application

1. Start the FastAPI application using `uvicorn`:
   ```bash
   uvicorn main:app --reload
   ```
   - Default server runs at `http://127.0.0.1:8000`.

2. Access the Swagger UI for testing:
   - Open your browser and navigate to `http://127.0.0.1:8000/docs`.

3. Test Endpoints:
   - **Get all enabled rules**: `GET /rules/enabled`
   - **Get compliance status for all rules**: `GET /rules/compliance`
   - **Get compliance details by rule**: `GET /rules/{rule_name}/compliance`
   - **Get compliance details by resource**: `GET /resources/{resource_id}/compliance`

---

## Example Responses

### 1. Get Enabled Rules
**Request:**
```bash
curl http://127.0.0.1:8000/rules/enabled
```

**Response:**
```json
{
    "enabled_rules": ["rule1", "rule2", "rule3"]
}
```

### 2. Get Compliance Status
**Request:**
```bash
curl http://127.0.0.1:8000/rules/compliance
```

**Response:**
```json
{
    "compliance_status": {
        "rule1": "COMPLIANT",
        "rule2": "NON_COMPLIANT",
        "rule3": "INSUFFICIENT_DATA"
    }
}
```

### 3. Get Compliance Details by Rule
**Request:**
```bash
curl http://127.0.0.1:8000/rules/rule1/compliance
```

**Response:**
```json
{
    "rule_name": "rule1",
    "compliance_details": [
        {
            "EvaluationResultIdentifier": {
                "EvaluationResultQualifier": {
                    "ConfigRuleName": "rule1",
                    "ResourceType": "AWS::S3::Bucket",
                    "ResourceId": "bucket-id"
                }
            },
            "ComplianceType": "COMPLIANT",
            "Annotation": "Rule passed validation.",
            "ResultRecordedTime": "2024-11-23T10:12:34Z",
            "ConfigRuleInvokedTime": "2024-11-23T10:11:12Z"
        }
    ]
}
```

---

## Deployment (Optional)

1. **Containerize the Application**:
   - Use Docker to build and deploy the application.
   - Create a `Dockerfile` for the FastAPI app.

2. **Deploy to AWS**:
   - Host on AWS ECS, EKS, or Lambda (with API Gateway).

3. **Secure the API**:
   - Use API authentication mechanisms such as AWS SigV4 or API keys.

---

## Troubleshooting

1. **NoRegionError**:
   - Ensure you specify a region in the AWS CLI, environment variables, or the code.

2. **Empty Response for Compliance Details**:
   - Verify the rule name or resource ID exists and has compliance data in AWS Config.
   - Re-evaluate the rule in the AWS Management Console if necessary.

3. **ModuleNotFoundError**:
   - Ensure all dependencies are installed correctly.
   - Use `pip install -r requirements.txt`.

---

## License

This project is licensed under the Apache License 2.0..