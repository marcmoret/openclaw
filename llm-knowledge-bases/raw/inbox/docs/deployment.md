# LiveKit Voice Agents Deployment Documentation

This document outlines the deployment infrastructure and CI/CD pipeline for the LiveKit Voice Agents project.

## Architecture Overview

The project uses a modern cloud-native architecture with the following components:

- **AWS ECS (Elastic Container Service)** for container orchestration
- **AWS ECR (Elastic Container Registry)** for container image storage
- **GitHub Actions** for CI/CD pipeline
- **Terraform** for Infrastructure as Code
- **AWS Secrets Manager** for secrets management
- **LiveKit** for real-time voice communication

## Infrastructure Components

### 1. Container Registry (ECR)

- Single repository with environment-specific tags:
  - `livekit-voice-agents:staging-{SHA}`
  - `livekit-voice-agents:production-{SHA}`
- Images tagged with Git commit SHA for traceability
- Immutable tags enforced

### 2. ECS Clusters

- Single cluster with environment-specific services:
  - `livekit-voice-agents-staging`
  - `livekit-voice-agents-production`
- FARGATE launch type for serverless container management
- Container insights enabled for monitoring

### 3. Task Definitions

The task definitions are managed through JSON files:
- `task-def-update.json`: Template for testing changes
- Environment-specific configurations in Terraform

Resource allocation:
- CPU: 1024 units (1 vCPU)
- Memory: 2GB
- Port mappings: 8081
- Health check: `/` endpoint

Environment variables are sourced from:
- AWS Secrets Manager for sensitive data
- Task definition for non-sensitive configuration

### 4. Services

- Environment-specific services
- Rolling deployment strategy
- Service discovery via Application Load Balancer
- Private subnets for container placement
- Public subnets for ALB

## CI/CD Pipeline

### GitHub Actions Workflow

The deployment pipeline handles:

1. **Build & Test**
   - Poetry dependency installation
   - Unit tests execution
   - Code linting and formatting
   - Container image building

2. **Security Checks**
   - Dependency scanning
   - Container image scanning
   - Code quality checks

3. **Deployment**
   - ECR image push
   - Task definition update
   - Service deployment
   - Health check verification

### Environment Selection

- `main` branch → Production deployment
- `staging` branch → Staging deployment
- Manual triggers available for specific deployments

### Security

- OIDC authentication with AWS
- Short-lived credentials
- Least privilege IAM roles
- Secrets managed in AWS Secrets Manager

## Task Definition Management

### Environment Variables

Task definitions include environment configuration and a single secret reference:

```json
{
  "environment": [
    {
      "name": "ENVIRONMENT",
      "value": "production"
    },
    {
      "name": "LOG_LEVEL",
      "value": "INFO"
    }
  ],
  "secrets": [
    {
      "name": "API_KEYS",
      "valueFrom": "arn:aws:secretsmanager:region:account:secret:livekit-voice-agents/production/api-keys"
    }
  ]
}
```

### Secret Management

All API keys and sensitive configuration are stored in a single JSON object in AWS Secrets Manager. The secret is named `livekit-voice-agents/{environment}/api-keys` and contains all necessary API keys in a structured format:

```json
{
  "livekit": {
    "url": "wss://your-livekit-server.com",
    "api_key": "your-api-key",
    "api_secret": "your-api-secret"
  },
  "openai": {
    "api_key": "your-api-key"
  },
  "deepgram": {
    "api_key": "your-api-key"
  },
  "elevenlabs": {
    "api_key": "your-api-key"
  }
}
```

The container startup script parses this single JSON secret and sets individual environment variables for each service:
- `LIVEKIT_URL`
- `LIVEKIT_API_KEY`
- `LIVEKIT_API_SECRET`
- `OPENAI_API_KEY`
- `DEEPGRAM_API_KEY`
- `ELEVENLABS_API_KEY`

This approach:
- Keeps all sensitive data in one manageable secret
- Reduces the number of secret mounts needed
- Makes secret rotation simpler
- Maintains compatibility with service SDKs that expect specific environment variables

### Testing Changes

1. **Local Testing**
```bash
# Test with development configuration
docker-compose up

# Test with production configuration
docker build -f Dockerfile.prod -t livekit-voice-agents:local .
docker run --env-file .env livekit-voice-agents:local
```

2. **Task Definition Updates**
- Update `task-def-update.json`
- Test locally with development environment
- Apply changes through Terraform

## Monitoring and Logging

### 1. Application Logs

CloudWatch Log Groups:
- `/aws/ecs/livekit-voice-agents-staging`
- `/aws/ecs/livekit-voice-agents-production`

Log Levels:
- Production: INFO
- Staging: DEBUG

### 2. Metrics

**Container Insights:**
- CPU/Memory utilization
- Container count
- Service health

**Voice Quality Metrics:**
- Speech-to-text accuracy
- Voice latency
- Call duration
- Agent transfer counts

**Application Metrics:**
- Agent success rates
- Conversation completion rates
- Error rates by type

### 3. Alerts

- Service health
- Error rate thresholds
- Resource utilization
- Voice quality degradation

## Security Considerations

### 1. Network Security

- Containers run in private subnets
- ALB in public subnets
- Security groups limit access to required ports
- VPC endpoints for AWS services

### 2. Data Security

- HIPAA compliance measures
- Encryption at rest for all data
- TLS for all communications
- Secure voice recording handling

### 3. Access Control

- OIDC authentication
- Role-based access control
- Least privilege principle
- Regular access reviews

## Troubleshooting Guide

### Common Issues

1. **Container Startup Issues**
- Check CloudWatch logs
- Verify environment variables
- Check container health check
- Validate memory/CPU allocation

2. **Voice Processing Issues**
- Check Deepgram connectivity
- Verify OpenAI API access
- Check ElevenLabs integration
- Monitor voice quality metrics

3. **Agent Issues**
- Review agent transfer logs
- Check conversation context
- Verify prompt templates
- Monitor agent success rates

### Deployment Failures

1. **Task Definition**
- Validate JSON syntax
- Check resource allocations
- Verify secret ARNs
- Validate environment variables

2. **Service Updates**
- Check deployment circuit breaker
- Verify target group health
- Monitor service events
- Check container logs

### Recovery Procedures

1. **Rollback Process**
```bash
# View previous task definitions
aws ecs list-task-definitions

# Rollback to previous version
aws ecs update-service --cluster livekit-voice-agents \
  --service livekit-voice-agents-production \
  --task-definition previous-task-def:1
```

2. **Data Recovery**
- Backup procedures for conversation logs
- State recovery for interrupted calls
- Agent context restoration

## Maintenance

### Regular Tasks

1. **Updates**
- Weekly dependency updates
- Monthly security patches
- Quarterly infrastructure review

2. **Monitoring**
- Daily log review
- Weekly metric analysis
- Monthly performance review

3. **Security**
- Regular secret rotation
- Access review
- Security patch application

### Backup and Recovery

1. **Configuration Backup**
- Task definitions
- Environment variables
- Terraform state

2. **Data Backup**
- Conversation logs
- Voice recordings
- Performance metrics

## Support and Escalation

### Support Levels

1. **L1 Support**
- Basic troubleshooting
- Log analysis
- Known issue resolution

2. **L2 Support**
- Advanced debugging
- Performance optimization
- Security incident response

### Escalation Path

1. On-call DevOps engineer
2. Platform team
3. Security team (for security incidents)
4. Management escalation
