import os

from dotenv import load_dotenv
import aws_cdk as cdk
from infrastructure.dynamodb_stack import NemoAIDynamoDBStack

load_dotenv()

app = cdk.App()

NemoAIDynamoDBStack(
    app,
    "NemoAIDynamoDBStack",
    env=cdk.Environment(account=os.getenv("CDK_DEFAULT_ACCOUNT"), region="us-east-1"),
)

app.synth()
print("CDK app synthesized successfully")
