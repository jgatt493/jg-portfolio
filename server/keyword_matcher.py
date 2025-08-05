import re
from typing import Dict, List, Tuple

class KeywordMatcher:
    def __init__(self):
        self.intent_keywords = {
            "about": ["who", "yourself", "background", "bio", "introduction", "tell me about yourself"],
            "projects": ["projects", "work", "portfolio", "built", "created", "developed", "what have you made", "deepgram", "current work"],
            "past_projects": ["past projects", "previous work", "before deepgram", "earlier projects", "career history", "previous experience"],
            "skills": ["skills", "technologies", "tech", "programming", "languages", "frameworks", "tools"],
            "experience": ["experience", "career", "job", "work history", "professional", "employment"],
            "contact": ["contact", "reach", "email", "phone", "connect", "hire", "get in touch"],
            "fun": ["fun", "hobbies", "interests", "personal", "free time", "outside work"],
            "architecture": ["architecture", "tech stack", "how built", "structure", "system", "how does this work"],
            "greeting": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "what's up", "howdy", "sup"],
            "test": ["test", "testing", "check", "ping", "hello world", "does this work"],
            "ai_question": ["real ai", "artificial intelligence", "chatgpt", "gpt", "ai service", "bot", "robot", "machine learning", "are you ai", "are you real", "chatbot"],
            "fishing": ["fish", "fishing", "salmon", "angling", "catch", "rod", "reel", "lake", "river", "bass", "trout"],
            "soccer": ["soccer", "football", "fifa", "premier league", "mls", "world cup", "kick", "goal", "pitch", "madonna university"],
            "gaming": ["video games", "gaming", "xbox", "playstation", "nintendo", "pc gaming", "steam", "games", "gamer"],
            "outdoors": ["outdoors", "camping", "backpacking", "hiking", "nature", "wilderness", "tent", "trail", "mountains"],
            "family": ["wife", "daughters", "family", "kids", "children", "married", "dad", "father", "parent"],
            "location": ["michigan", "livonia", "detroit", "where do you live", "location", "from michigan", "midwest"],
            "name": ["what is your name", "who are you", "your name", "name", "introduce yourself", "tell me your name"],
            "music": ["music", "piano", "guitar", "film scoring", "composer", "musician", "instruments", "play music", "soundtrack"],
            "personal_state": ["tired", "exhausted", "sleepy", "busy", "stressed", "excited", "happy", "sad", "bored", "frustrated"],
            "project_details": ["product adia", "stripe onboarding", "voiceworks", "project flux", "river", "voice agent", "stripe voice", "adia", "flux"],
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
        
        # Special priority for project details - check first
        if scores.get("project_details", 0) > 0:
            return "project_details"
        
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
