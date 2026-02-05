# Talent Management Intent Classifier API

A FastAPI service that classifies user queries related to SAP SuccessFactors Talent Management and returns relevant help portal links. Designed for integration with SAP Joule.

## Features

- Classifies queries into 8 Talent Management topics
- Returns relevant SAP Help Portal documentation links
- Uses GPT-4 via SAP GenAI Hub SDK
- Auto-generated OpenAPI spec for Joule Action import
- Mock classification fallback for local development

## Supported Topics

| Topic | Example Queries |
|-------|-----------------|
| Performance Management | performance review, goals, feedback |
| Learning & Development | training, courses, certifications |
| Recruitment | job posting, candidates, interviews |
| Compensation & Benefits | salary, bonus, benefits |
| Succession Planning | career path, talent pool, successors |
| Employee Onboarding | new hire, onboarding checklist |
| Time & Attendance | time off, leave request, vacation |
| Employee Central | employee data, org chart, profile |

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally (uses mock classification)
uvicorn app:app --reload

# Run tests
python test_local.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/classify` | Classify a user query |
| GET | `/health` | Health check |
| GET | `/docs` | Swagger UI |
| GET | `/openapi.json` | OpenAPI spec |

## Example Request

```bash
curl -X POST http://localhost:8000/api/v1/classify \
  -H "Content-Type: application/json" \
  -d '{"query": "How do I submit my performance review?"}'
```

## Example Response

```json
{
  "is_talent_management": true,
  "confidence": 0.95,
  "topic": "performance_management",
  "topic_display_name": "Performance Management",
  "links": [
    {
      "title": "Performance & Goals Administration",
      "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_PERFORMANCE_GOALS",
      "description": "Complete guide to Performance Management in SuccessFactors"
    }
  ],
  "summary": "Your question is about Performance Management. Here are helpful resources."
}
```

## Deployment

### Cloud Foundry

```bash
cf push
```

The app binds to an AI Core service instance configured in `manifest.yml`.

### Environment Variables

For local development with GenAI Hub, set these variables (see `.env.example`):

- `AICORE_AUTH_URL`
- `AICORE_CLIENT_ID`
- `AICORE_CLIENT_SECRET`
- `AICORE_BASE_URL`
- `AICORE_RESOURCE_GROUP`

## Joule Integration

1. Deploy the app to Cloud Foundry
2. Create a BTP Destination pointing to the app URL
3. Import `/openapi.json` as an Action in SAP Build Process Automation
4. Create a Joule Skill that calls the classification action
