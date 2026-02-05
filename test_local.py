#!/usr/bin/env python3
"""
Local test script for the intent classifier.

Run this to validate the mock classification logic works before
setting up the full GenAI Hub integration.
"""

import sys
sys.path.insert(0, ".")

from topic_links import get_topics_for_prompt, TOPIC_LINKS


def test_topic_links():
    """Test that topic links are properly defined."""
    print("=== Testing Topic Links ===\n")

    assert len(TOPIC_LINKS) == 8, f"Expected 8 topics, got {len(TOPIC_LINKS)}"
    print(f"✓ Found {len(TOPIC_LINKS)} topics")

    for key, info in TOPIC_LINKS.items():
        assert "display_name" in info, f"Missing display_name for {key}"
        assert "keywords" in info, f"Missing keywords for {key}"
        assert "links" in info, f"Missing links for {key}"
        assert len(info["links"]) >= 1, f"No links for {key}"
        print(f"  ✓ {key}: {info['display_name']} ({len(info['links'])} links)")

    print("\n✓ All topic links validated\n")


def test_prompt_generation():
    """Test prompt generation for topics."""
    print("=== Testing Prompt Generation ===\n")

    prompt = get_topics_for_prompt()
    assert len(prompt) > 0, "Prompt should not be empty"

    for topic in TOPIC_LINKS.keys():
        assert topic in prompt, f"Topic {topic} missing from prompt"

    print("Generated prompt for LLM:\n")
    print(prompt)
    print("\n✓ Prompt generation works\n")


def test_mock_classification():
    """Test the mock classification without GenAI Hub."""
    print("=== Testing Mock Classification ===\n")

    # Import here to avoid issues if dependencies aren't installed
    from intent_classifier import IntentClassifier

    classifier = IntentClassifier()

    # Test cases: (query, expected_topic, expected_is_tm)
    test_cases = [
        ("How do I submit my annual performance review?", "performance_management", True),
        ("I need to request time off for next week", "time_attendance", True),
        ("Where can I find training courses?", "learning_development", True),
        ("How do I post a job opening?", "recruitment", True),
        ("What is my current salary?", "compensation_benefits", True),
        ("Who is next in line for the VP role?", "succession_planning", True),
        ("New hire onboarding checklist", "employee_onboarding", True),
        ("Update my profile picture", "employee_central", True),
        ("What is the weather today?", None, False),
        ("How do I reset my laptop password?", None, False),
    ]

    passed = 0
    failed = 0

    for query, expected_topic, expected_is_tm in test_cases:
        result = classifier.classify(query)

        is_tm_match = result["is_talent_management"] == expected_is_tm
        topic_match = result["topic"] == expected_topic

        if is_tm_match and (not expected_is_tm or topic_match):
            print(f"  ✓ '{query[:40]}...'")
            print(f"    → {result['topic_display_name'] or 'Not TM'} (confidence: {result['confidence']})")
            passed += 1
        else:
            print(f"  ✗ '{query[:40]}...'")
            print(f"    Expected: {expected_topic}, Got: {result['topic']}")
            failed += 1

    print(f"\n{'✓' if failed == 0 else '✗'} {passed}/{len(test_cases)} tests passed\n")
    return failed == 0


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Talent Management Intent Classifier - Local Tests")
    print("=" * 60 + "\n")

    test_topic_links()
    test_prompt_generation()
    success = test_mock_classification()

    print("=" * 60)
    print("TEST SUMMARY: " + ("ALL PASSED ✓" if success else "SOME FAILED ✗"))
    print("=" * 60 + "\n")

    sys.exit(0 if success else 1)
