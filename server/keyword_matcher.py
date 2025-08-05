import re
from typing import Dict, List, Tuple

class KeywordMatcher:
    def __init__(self):
        self.intent_keywords = {
            "about": ["about", "who", "yourself", "background", "bio", "introduction", "tell me about"],
            "projects": ["projects", "work", "portfolio", "built", "created", "developed", "what have you made"],
            "skills": ["skills", "technologies", "tech", "programming", "languages", "frameworks", "tools"],
            "experience": ["experience", "career", "job", "work history", "professional", "employment"],
            "contact": ["contact", "reach", "email", "phone", "connect", "hire", "get in touch"],
            "fun": ["fun", "hobbies", "interests", "personal", "free time", "outside work"],
            "architecture": ["architecture", "tech stack", "how built", "structure", "system", "how does this work"],
            "greeting": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "what's up"],
        }
        
        # Compile regex patterns for faster matching
        self.compiled_patterns = {}
        for intent, keywords in self.intent_keywords.items():
            pattern = r'\b(' + '|'.join(re.escape(keyword) for keyword in keywords) + r')\b'
            self.compiled_patterns[intent] = re.compile(pattern, re.IGNORECASE)
    
    def classify_intent(self, input_text: str) -> str:
        """Fast intent classification using pre-compiled regex patterns"""
        scores = {}
        
        for intent, pattern in self.compiled_patterns.items():
            matches = pattern.findall(input_text)
            scores[intent] = len(matches)
        
        # Find the intent with the highest score
        best_intent = max(scores.items(), key=lambda x: x[1])
        
        return best_intent[0] if best_intent[1] > 0 else "default"
    
    def get_confidence_score(self, input_text: str, intent: str) -> float:
        """Calculate confidence score for the classified intent"""
        if intent == "default":
            return 0.0
        
        if intent in self.compiled_patterns:
            matches = self.compiled_patterns[intent].findall(input_text)
            word_count = len(input_text.split())
            return min(len(matches) / max(word_count, 1), 1.0)
        
        return 0.0
