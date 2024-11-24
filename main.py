from fastapi import FastAPI, HTTPException
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

app = FastAPI()

# Initialize AWS Config client
try:
    config_client = boto3.client("config", region_name="ap-south-1") # Specify the region explicitly
except NoCredentialsError:
    raise HTTPException(status_code=401, detail="AWS credentials not found.")
except PartialCredentialsError:
    raise HTTPException(status_code=401, detail="Incomplete AWS credentials provided.")

@app.get("/rules/enabled")
async def get_enabled_rules():
    """
    Get all enabled AWS Config rules.
    """
    try:
        response = config_client.describe_config_rules()
        rules = [rule['ConfigRuleName'] for rule in response.get('ConfigRules', [])]
        return {"enabled_rules": rules}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/rules/compliance")
async def get_compliance_status():
    """
    Get compliance status of all AWS Config rules.
    """
    try:
        response = config_client.describe_compliance_by_config_rule()
        compliance_status = {
            rule['ConfigRuleName']: rule['Compliance']['ComplianceType']
            for rule in response.get('ComplianceByConfigRules', [])
        }
        return {"compliance_status": compliance_status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/rules/{rule_name}/compliance")
async def get_compliance_status_by_rule(rule_name: str):
    """
    Get compliance details of a specific AWS Config rule by name.
    """
    try:
        response = config_client.get_compliance_details_by_config_rule(
            ConfigRuleName=rule_name
        )
        compliance_details = response.get('EvaluationResults', [])
        return {"rule_name": rule_name, "compliance_details": compliance_details}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/resources/{resource_id}/compliance")
async def get_compliance_details_by_resource(resource_id: str):
    """
    Get compliance details of resources by resource ID.
    """
    try:
        response = config_client.get_compliance_details_by_resource(
            ResourceId=resource_id,
            ResourceType="AWS::AllSupported"  # You can specify a specific type like 'AWS::EC2::Instance'
        )
        compliance_details = response.get('EvaluationResults', [])
        return {"resource_id": resource_id, "compliance_details": compliance_details}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))