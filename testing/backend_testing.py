import pytest
from backend.data_processing import analyzeEmailChain, extractKeywords
from backend.learning_algorithm import learnUserPreferences
from backend.integration import integrateEmailPlatform

def test_analyzeEmailChain():
    email_chain = "Hello, Can we have a meeting tomorrow? Regards, John"
    result = analyzeEmailChain(email_chain)
    assert isinstance(result, dict), "The result should be a dictionary"
    assert "context" in result, "The result should contain 'context'"

def test_extractKeywords():
    email_chain = "Hello, Can we have a meeting tomorrow? Regards, John"
    result = extractKeywords(email_chain)
    assert isinstance(result, list), "The result should be a list"
    assert "meeting" in result, "The result should contain 'meeting'"

def test_learnUserPreferences():
    user_preferences = {"reply_style": "formal", "sign_off": "Best", "common_phrases": ["Looking forward", "As per our discussion"]}
    feedback = {"liked": ["Looking forward"], "disliked": ["As per our discussion"]}
    result = learnUserPreferences(user_preferences, feedback)
    assert isinstance(result, dict), "The result should be a dictionary"
    assert "reply_style" in result, "The result should contain 'reply_style'"

def test_integrateEmailPlatform():
    email_platform = "Gmail"
    result = integrateEmailPlatform(email_platform)
    assert isinstance(result, bool), "The result should be a boolean"
    assert result == True, "The result should be True"

pytest.main()