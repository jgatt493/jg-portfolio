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
        
        result = {
            "response": response,
            "intent": intent,
            "confidence": self.keyword_matcher.get_confidence_score(normalized_input, intent)
        }
        
        # Add structured data for specific intents
        if intent == "skills":
            result["skills_data"] = self.portfolio_data.get_skills()
        elif intent == "projects":
            result["projects_data"] = self.portfolio_data.get_projects()
        elif intent == "past_projects":
            result["past_projects_data"] = self.portfolio_data.get_projects()  # Will use default data from component
            
        return result
    
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
            "test": lambda: self.response_templates.get_test_response(input_text),
            "ai_question": self.response_templates.get_ai_question_response,
            "fishing": self.response_templates.get_fishing_response,
            "soccer": self.response_templates.get_soccer_response,
            "gaming": self.response_templates.get_gaming_response,
            "outdoors": self.response_templates.get_outdoors_response,
            "family": self.response_templates.get_family_response,
            "location": self.response_templates.get_location_response,
            "name": self.response_templates.get_name_response,
            "music": self.response_templates.get_music_response,
            "personal_state": lambda: self.response_templates.get_personal_state_response(input_text),
            "past_projects": self.response_templates.get_past_projects_response,
            "project_details": lambda: self.response_templates.get_project_details_response(input_text),
        }
        
        if intent in response_map:
            return response_map[intent]()
        else:
            return self.response_templates.get_default_response(input_text)
