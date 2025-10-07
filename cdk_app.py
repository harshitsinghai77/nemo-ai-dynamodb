import os
import aws_cdk as cdk
from infrastructure.dynamodb_stack import NemoAIDynamoDBStack

app = cdk.App()

NemoAIDynamoDBStack(
    app,
    "NemoAIDynamoDBStack",
    env=cdk.Environment(account=os.getenv("AWS_DEFAULT_ACCOUNT"), region="us-east-1"),
)

app.synth()
print("CDK app synthesized successfully")
