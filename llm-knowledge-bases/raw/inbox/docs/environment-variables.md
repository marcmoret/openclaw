# Environment Variables and Configuration Management

This document outlines how environment variables and configuration are managed across different environments in the project.

## Terraform Configuration Structure

```
terraform/
├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars        # Non-sensitive, shared defaults
└── environments/
    ├── dev/
    │   └── terraform.tfvars    # Dev-specific overrides
    ├── staging/
    │   └── terraform.tfvars    # Staging-specific overrides
    └── production/
        └── terraform.tfvars    # Production-specific overrides
```

### Configuration Hierarchy (highest to lowest precedence)
1. Command line variables (`-var` or `-var-file`)
2. Environment-specific tfvars (`environments/<env>/terraform.tfvars`)
3. Shared defaults (`terraform.tfvars`)
4. Variable defaults in `variables.tf`

## Secrets Management

All sensitive values are stored in AWS Secrets Manager with the following structure:

```json
{
  "livekit": {
    "url": "wss://your-livekit-instance.cloud",
    "api_key": "your-api-key",
    "api_secret": "your-api-secret"
  },
  "openai": {
    "api_key": "your-openai-key"
  },
  "deepgram": {
    "api_key": "your-deepgram-key"
  },
  "elevenlabs": {
    "api_key": "your-elevenlabs-key"
  },
  "instaclinic": {
    "api_key": "your-instaclinic-key"
  }
}
```

The secret is stored at: `livekit-voice-agents/{environment}/api-keys`

## Local Development

Create a `.env` file in the root directory with the following structure:

```bash
# AWS Configuration
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=us-west-2
AWS_PROFILE=livekit-voice-dev

# Environment Selection
TF_WORKSPACE=dev        # or staging, production

# Optional Development Settings
DEBUG=false
NODE_ENV=development
```

## Running Terraform

1. Select workspace:
```bash
terraform workspace select dev  # or staging, production
```

2. Plan/Apply with environment overrides:
```bash
# Development
terraform plan \
  -var-file="environments/dev/terraform.tfvars"

# Production
terraform plan \
  -var-file="environments/production/terraform.tfvars"
```

## CI/CD Environment

The CI/CD pipeline uses:
1. GitHub Actions secrets for AWS authentication
2. AWS IAM roles for service permissions
3. AWS Secrets Manager for application secrets

## Security Notes

1. Never commit sensitive values to git
2. Use AWS Secrets Manager for all secrets
3. Keep different environments separate
4. Rotate keys regularly
5. Use least privilege access

## Cleanup Required

1. Remove redundant tfvars files:
   ```bash
   # Remove root level files
   rm secrets.tfvars
   
   # Move environment-specific variables
   mkdir -p terraform/environments/{dev,staging}
   mv terraform/terraform.tfvars terraform/environments/dev/
   ```

2. Move AWS credentials to proper location:
   ```bash
   rm shoukry_AWS_keys.txt .aws_credentials
   mv terraform/awskeys.txt ~/.aws/credentials
   ```

3. Move LiveKit credentials to AWS Secrets Manager:
   ```bash
   rm livekit-voice-production-credentials.txt
   ``` 