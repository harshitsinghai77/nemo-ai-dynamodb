# NemoAI DynamoDB Infrastructure

A CDK-based infrastructure project for deploying DynamoDB resources to support Jira webhook event processing.

## Architecture

This project uses AWS CDK (Cloud Development Kit) to define and deploy cloud infrastructure as code. The main component is a DynamoDB table designed to store Jira webhook events.

### Components

- **DynamoDB Table**: `JiraWebhookEvents` table with pay-per-request billing
- **Partition Key**: `jira_id` (String) for efficient data distribution
- **Billing Mode**: Pay-per-request for cost optimization

## Directory Structure

```
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD pipeline for automatic deployment
├── infrastructure/
│   └── dynamodb_stack.py       # DynamoDB stack definition
├── cdk_app.py                  # CDK application entry point
├── cdk.json                    # CDK configuration
└── requirements.txt            # Python dependencies
```

## Features

- **Infrastructure as Code**: Complete infrastructure defined using AWS CDK
- **Automated Deployment**: GitHub Actions workflow for CI/CD
- **Cost Optimized**: Pay-per-request billing mode for DynamoDB
- **Development Ready**: Removal policy set to DESTROY for easy cleanup

## Prerequisites

- Python 3.12+
- Node.js 22+
- AWS CLI configured
- AWS CDK CLI installed

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
npm install -g aws-cdk
```

2. Configure AWS credentials:
```bash
aws configure
```

3. Set environment variable:
```bash
export AWS_DEFAULT_ACCOUNT=your-account-id
```

## Deployment

### Manual Deployment
```bash
cdk deploy
```

### Automatic Deployment
Push to `main` branch triggers automatic deployment via GitHub Actions.

## GitHub Actions

The CI/CD pipeline automatically:
- Sets up Python 3.12 and Node.js 22
- Installs CDK CLI and dependencies
- Configures AWS credentials
- Deploys the stack to `us-east-1` region

### Required Secrets
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_ACCOUNT`

## Use Cases

- Store and manage Jira webhook events
- Event-driven processing of Jira notifications
- Audit trail for Jira integrations
- Scalable event storage with DynamoDB

## Configuration

The stack deploys to `us-east-1` region by default. Modify `cdk_app.py` to change the target region or add additional configuration.