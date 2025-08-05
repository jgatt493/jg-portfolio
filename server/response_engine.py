import asyncio
import re
from typing import Dict, Any
from keyword_matcher import KeywordMatcher
from response_templates import ResponseTemplates
from portfolio_data import PortfolioData

class ResponseEngine:
    def __init__(self):
        self.portfolio_data = PortfolioData()
        self.keyword_matcher = KeywordMatcher()
        self.response_templates = ResponseTemplates()
        
    async def generate_response(self, input_text: str) -> Dict[str, Any]:
        """Generate a response based on user input with minimal latency"""
        normalized_input = input_text.lower().strip()
        
        # Fast intent classification
        intent = self.keyword_matcher.classify_intent(normalized_input)
        
        # Generate response based on intent
        response = await self._get_response_for_intent(intent, normalized_input)
        
        return {
            "response": response,
            "intent": intent,
            "confidence": self.keyword_matcher.get_confidence_score(normalized_input, intent)
        }
    
    async def _get_response_for_intent(self, intent: str, input_text: str) -> str:
        """Get response for specific intent - optimized for speed"""
        
        response_map = {
            "about": self.response_templates.get_about_response,
            "projects": lambda: self.response_templates.get_projects_response(self.portfolio_data.get_projects()),
            "skills": lambda: self.response_templates.get_skills_response(self.portfolio_data.get_skills()),
            "experience": lambda: self.response_templates.get_experience_response(self.portfolio_data.get_experience()),
            "contact": lambda: self.response_templates.get_contact_response(self.portfolio_data.get_contact()),
            "fun": self.response_templates.get_fun_response,
            "architecture": self.response_templates.get_architecture_response,
            "greeting": self.response_templates.get_greeting_response,
        }
        
        if intent in response_map:
            return response_map[intent]()
        else:
            return self.response_templates.get_default_response(input_text)
