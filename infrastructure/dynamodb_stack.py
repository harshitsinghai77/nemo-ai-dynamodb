from aws_cdk import Stack, RemovalPolicy, aws_dynamodb as dynamodb, CfnOutput

from constructs import Construct


class NemoAIDynamoDBStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        jira_webhooks_table = dynamodb.Table(
            self,
            "JiraWebhookEvents",
            partition_key=dynamodb.Attribute(name="jira_id", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,  # DESTROY for dev only. Use RETAIN in prod
            table_name="JiraWebhookEvents",
        )

        CfnOutput(self, "JiraWebhookEventsTableName", value=jira_webhooks_table.table_name)
