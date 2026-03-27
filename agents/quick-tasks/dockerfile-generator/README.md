# Dockerfile Generator

> **Quick Task Agent - Instant Results**

## Overview
Generate optimized Dockerfiles for any language/framework. Best practices built-in.

## Capabilities
- Language-specific Dockerfiles
- Multi-stage builds
- Security best practices
- Size optimization
- Docker Compose generation
- Kubernetes deployment files

## Input
```json
{
  "language": "node|python|go|rust|java",
  "framework": "express|fastapi|nextjs|react",
  "options": {
    "multi_stage": true,
    "alpine": true,
    "port": 3000
  }
}
```

## Output
```json
{
  "dockerfile": "FROM node:18-alpine...",
  "dockerignore": "node_modules\n.git...",
  "docker_compose": "version: '3'...",
  "size_estimate": "150MB"
}
```

## Pricing
- **Free**: 10 Dockerfiles/day
- **Pro**: $3.99/mo unlimited

## Revenue Potential
$200-600/month

---

*Quick Task Agent - Containerization helper*
