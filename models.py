"""
Pydantic Models for Request/Response Validation

These models provide:
1. Automatic request validation
2. Response serialization
3. OpenAPI schema generation for Joule Action import
"""

from pydantic import BaseModel, Field


class ClassifyRequest(BaseModel):
    """Request model for the classification endpoint."""

    query: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="The user query to classify",
        json_schema_extra={"example": "How do I submit my annual performance review?"},
    )


class LinkInfo(BaseModel):
    """Information about a help resource link."""

    title: str = Field(..., description="Title of the help resource")
    url: str = Field(..., description="URL to the SAP Help Portal page")
    description: str = Field(..., description="Brief description of the resource")


class ClassifyResponse(BaseModel):
    """Response model for the classification endpoint."""

    is_talent_management: bool = Field(
        ..., description="Whether the query relates to Talent Management"
    )
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Confidence score of the classification (0.0 to 1.0)",
    )
    topic: str | None = Field(
        None, description="The identified topic key (e.g., 'performance_management')"
    )
    topic_display_name: str | None = Field(
        None, description="Human-readable topic name (e.g., 'Performance Management')"
    )
    links: list[LinkInfo] = Field(
        default_factory=list, description="Relevant SAP Help Portal links"
    )
    summary: str = Field(
        ..., description="A brief summary message about the classification result"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "is_talent_management": True,
                    "confidence": 0.95,
                    "topic": "performance_management",
                    "topic_display_name": "Performance Management",
                    "links": [
                        {
                            "title": "Performance & Goals Administration",
                            "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_PERFORMANCE_GOALS",
                            "description": "Complete guide to Performance Management in SuccessFactors",
                        }
                    ],
                    "summary": "Your question is about Performance Management. Here are helpful resources.",
                },
                {
                    "is_talent_management": False,
                    "confidence": 0.92,
                    "topic": None,
                    "topic_display_name": None,
                    "links": [],
                    "summary": "This query doesn't appear to be related to Talent Management.",
                },
            ]
        }
    }


class HealthResponse(BaseModel):
    """Response model for health check endpoint."""

    status: str = Field(..., description="Health status of the service")
    service: str = Field(..., description="Name of the service")
    version: str = Field(..., description="API version")
