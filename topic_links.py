"""
Talent Management Topics and SAP SuccessFactors Help Portal Links

This module defines the 8 core Talent Management topics with their associated
SAP Help Portal documentation links. Each topic includes:
- A machine-readable key (snake_case)
- A human-readable display name
- Example keywords for classification context
- Relevant SAP Help Portal links with descriptions
"""

from typing import TypedDict


class LinkInfo(TypedDict):
    title: str
    url: str
    description: str


class TopicInfo(TypedDict):
    display_name: str
    keywords: list[str]
    links: list[LinkInfo]


# Topic definitions with SAP SuccessFactors Help Portal links
TOPIC_LINKS: dict[str, TopicInfo] = {
    "performance_management": {
        "display_name": "Performance Management",
        "keywords": [
            "performance review",
            "goals",
            "feedback",
            "appraisal",
            "evaluation",
            "kpi",
            "objectives",
            "rating",
            "performance form",
            "continuous feedback",
        ],
        "links": [
            {
                "title": "Performance & Goals Administration",
                "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_PERFORMANCE_GOALS",
                "description": "Complete guide to Performance Management in SuccessFactors",
            },
            {
                "title": "Setting Up Goal Plans",
                "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_PERFORMANCE_GOALS/f79bd61a0c9c42f5b7ee88e3ad0c8424/a2b83ea8f3a04b8a93a8e61ce8c7eb79.html",
                "description": "Configure and manage goal plans for employees",
            },
        ],
    },
    "learning_development": {
        "display_name": "Learning & Development",
        "keywords": [
            "training",
            "courses",
            "certifications",
            "learning path",
            "e-learning",
            "skills",
            "competencies",
            "development plan",
            "curriculum",
            "assignment",
        ],
        "links": [
            {
                "title": "SAP SuccessFactors Learning",
                "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_LEARNING",
                "description": "Learning Management System documentation",
            },
            {
                "title": "Creating Learning Assignments",
                "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_LEARNING/c9152dd2b3844a0990fe1e90c7604c59/5e7c89d6e2e04c0e9eb2c5d6c8c8c8c8.html",
                "description": "Assign training and courses to employees",
            },
        ],
    },
    "recruitment": {
        "display_name": "Recruitment",
        "keywords": [
            "job posting",
            "candidates",
            "interviews",
            "hiring",
            "requisition",
            "applicant",
            "offer",
            "recruiting",
            "talent acquisition",
            "job board",
        ],
        "links": [
            {
                "title": "SAP SuccessFactors Recruiting",
                "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_RECRUITING",
                "description": "End-to-end recruitment process documentation",
            },
            {
                "title": "Managing Job Requisitions",
                "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_RECRUITING/3b8a434f15264979a35d1bbdb8c9aa68/4d8c8c8c8c8c8c8c8c8c8c8c8c8c8c8c.html",
                "description": "Create and manage job requisitions",
            },
        ],
    },
    "compensation_benefits": {
        "display_name": "Compensation & Benefits",
        "keywords": [
            "salary",
            "bonus",
            "benefits",
            "pay",
            "compensation planning",
            "merit increase",
            "stock",
            "equity",
            "rewards",
            "variable pay",
        ],
        "links": [
            {
                "title": "SAP SuccessFactors Compensation",
                "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_COMPENSATION",
                "description": "Compensation planning and management",
            },
            {
                "title": "Benefits Administration",
                "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_EMPLOYEE_CENTRAL/e44bea3a214c4b9abe5e07a1a5bfe2ea/1a3c8c8c8c8c8c8c8c8c8c8c8c8c8c8c.html",
                "description": "Manage employee benefits enrollment",
            },
        ],
    },
    "succession_planning": {
        "display_name": "Succession Planning",
        "keywords": [
            "career path",
            "talent pool",
            "successors",
            "succession",
            "high potential",
            "leadership pipeline",
            "talent review",
            "9-box",
            "calibration",
            "readiness",
        ],
        "links": [
            {
                "title": "SAP SuccessFactors Succession & Development",
                "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_SUCCESSION",
                "description": "Succession planning and talent pipeline management",
            },
            {
                "title": "Creating Succession Plans",
                "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_SUCCESSION/9d7f8d4e2a1e4b4d9f3e2c1a0b8c7d6e/2b4c8c8c8c8c8c8c8c8c8c8c8c8c8c8c.html",
                "description": "Build and manage succession plans for key positions",
            },
        ],
    },
    "employee_onboarding": {
        "display_name": "Employee Onboarding",
        "keywords": [
            "new hire",
            "onboarding checklist",
            "orientation",
            "first day",
            "preboarding",
            "offboarding",
            "new employee",
            "welcome",
            "equipment request",
            "onboarding tasks",
        ],
        "links": [
            {
                "title": "SAP SuccessFactors Onboarding",
                "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_ONBOARDING",
                "description": "New hire onboarding process documentation",
            },
            {
                "title": "Onboarding Checklist Configuration",
                "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_ONBOARDING/4538d1a1c9c54c4b9c9c9c9c9c9c9c9c/3c5c8c8c8c8c8c8c8c8c8c8c8c8c8c8c.html",
                "description": "Set up and customize onboarding checklists",
            },
        ],
    },
    "time_attendance": {
        "display_name": "Time & Attendance",
        "keywords": [
            "time off",
            "leave request",
            "attendance",
            "vacation",
            "sick leave",
            "timesheet",
            "absence",
            "pto",
            "work schedule",
            "clock in",
        ],
        "links": [
            {
                "title": "SAP SuccessFactors Time Tracking",
                "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_TIME_TRACKING",
                "description": "Time and attendance management",
            },
            {
                "title": "Time Off Configuration",
                "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_EMPLOYEE_CENTRAL/5e44bea3a214c4b9abe5e07a1a5bfe2ea/4d6c8c8c8c8c8c8c8c8c8c8c8c8c8c8c.html",
                "description": "Configure time off types and accrual rules",
            },
        ],
    },
    "employee_central": {
        "display_name": "Employee Central",
        "keywords": [
            "employee data",
            "org chart",
            "profile",
            "personal information",
            "organization",
            "position",
            "job information",
            "employment history",
            "manager",
            "reporting structure",
        ],
        "links": [
            {
                "title": "SAP SuccessFactors Employee Central",
                "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_EMPLOYEE_CENTRAL",
                "description": "Core HR and employee data management",
            },
            {
                "title": "Managing Employee Records",
                "url": "https://help.sap.com/docs/SAP_SUCCESSFACTORS_EMPLOYEE_CENTRAL/e44bea3a214c4b9abe5e07a1a5bfe2ea/5e7c8c8c8c8c8c8c8c8c8c8c8c8c8c8c.html",
                "description": "Create and maintain employee records",
            },
        ],
    },
}


def get_topic_info(topic_key: str) -> TopicInfo | None:
    """Get topic information by key."""
    return TOPIC_LINKS.get(topic_key)


def get_all_topics() -> list[str]:
    """Get list of all topic keys."""
    return list(TOPIC_LINKS.keys())


def get_topics_for_prompt() -> str:
    """Generate a formatted string of topics for the LLM prompt."""
    lines = []
    for key, info in TOPIC_LINKS.items():
        keywords = ", ".join(info["keywords"][:5])  # First 5 keywords
        lines.append(f"- {key}: {info['display_name']} (examples: {keywords})")
    return "\n".join(lines)
