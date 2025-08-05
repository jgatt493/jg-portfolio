import random
import time
from typing import List, Dict, Any

class ResponseTemplates:
    def __init__(self):
        # Track conversation state for more organic responses
        self.conversation_state = {
            "test_count": 0,
            "last_test_time": 0,
            "user_patterns": {},
        }
    def get_about_response(self) -> str:
        return """Hey there! I'm Jeremy, a passionate full-stack engineer who loves building innovative web applications and solving complex technical challenges at scale.

I have extensive experience creating large-scale APIs supporting global operations, with deep expertise in cloud platforms (GCP, AWS, Azure) and modern DevOps practices including Jenkins, Tekton, and Cloud Build. I'm highly proficient in Java, with heavy familiarity in Angular, React, and Spring Boot.

Throughout my career, I've worked on everything from rebuilding mainframe applications handling hundreds of millions of dollars in inventory to developing global ecommerce platforms and developer marketplaces. I specialize in taking complex business problems and turning them into scalable, modern technical solutions.

What drives me is the opportunity to turn ideas into reality through code. I enjoy working across the full stack - from user-facing interfaces to backend systems, database optimization, and DevOps automation.

When I'm not coding, I'm usually fishing Michigan's many lakes and rivers, playing piano (I'm certified in film scoring!), or camping with my wife and three daughters. Living in Livonia, Michigan gives me the perfect balance of tech opportunities and outdoor adventures! 🎣🎵"""

    def get_projects_response(self, projects: List[Dict]) -> str:
        return """I've done a lot of cool stuff throughout my career, but I think what's of most interest is my work thus far at Deepgram! Here's what I've been building:"""
    
    def get_past_projects_response(self) -> str:
        return """I've been fortunate to work on some fascinating enterprise-scale projects throughout my career:"""

    def get_skills_response(self, skills: Dict) -> str:
        return """Here's a visual breakdown of my technical expertise across different areas:"""

    def get_experience_response(self, experience: List[Dict]) -> str:
        return """This app is just a quick highlight of my projects, please contact me for a resume to see all past experience."""

    def get_contact_response(self, contact: Dict) -> str:
        return """I'd love to connect and discuss opportunities or interesting projects!

📧 **Email:** jpgatt06@yahoo.com
📱 **Cell:** 313-324-2964
💼 **LinkedIn:** (I'll get you this link tomorrow!)
🐙 **GitHub:** github.com/jeremydev

I'm always interested in:
• Challenging technical problems
• Open source collaboration  
• Mentoring and knowledge sharing
• Innovative startup opportunities

Feel free to reach out if you want to discuss technology, potential collaborations, or just chat about software engineering. I typically respond within a few hours during business days.

Looking forward to connecting! 🚀"""

    def get_fun_response(self) -> str:
        return """When I'm not deep in code, I love staying active and exploring my creative side:

🎣 **Fishing** - Especially salmon fishing in the fall! Michigan's Great Lakes tributaries are incredible for salmon runs.

⚽ **Soccer** - Played at Madonna University and still love the beautiful game. Great for staying in shape and team strategy!

🎵 **Music** - I play piano and guitar, and I'm certified in film scoring! Creating soundtracks combines my technical and artistic sides.

🏕️ **Outdoor Adventures** - Camping and backpacking are my therapy. Nothing beats disconnecting in Michigan's wilderness areas.

🎮 **Gaming** - Video games are perfect for unwinding. I appreciate the engineering that goes into great game design!

👨‍👩‍👧‍👧 **Family Time** - My wife and three daughters keep life interesting! We love exploring Michigan's parks and trails together.

🏠 **Home in Livonia** - Perfect location for both the Detroit tech scene and easy access to all of Michigan's outdoor opportunities.

The Midwest lifestyle gives me the perfect balance of career growth, creative expression, and outdoor recreation. What do you enjoy doing in your free time? 😊"""

    def get_architecture_response(self) -> str:
        return """Great question! This portfolio showcases a modern, performance-focused architecture:

**Frontend (Next.js 14):**
• App Router for optimal performance and SEO
• Tailwind CSS for responsive, utility-first styling
• TypeScript for type safety and better DX
• Real-time WebSocket connections for instant responses

**Backend (FastAPI + Python):**
• High-performance async API with <50ms response times
• Rule-based response engine (no AI models needed!)
• Modular architecture for easy feature additions
• Built-in health checks and monitoring endpoints

**Response System:**
• Pre-compiled regex patterns for lightning-fast intent classification
• Template-based responses with dynamic content injection
• Confidence scoring for response quality
• Extensible design for adding Unix tools and system commands

**Infrastructure:**
• Docker containers for consistent deployments
• Ready for Kubernetes orchestration
• Environment-based configuration
• Structured logging for observability

**Performance Optimizations:**
• Response caching for frequently asked questions
• Async processing for non-blocking operations
• Minimal dependencies for faster cold starts
• Optimized bundle sizes and lazy loading

The goal was to create something that feels intelligent and responsive while being completely deterministic and blazingly fast! ⚡"""

    def get_greeting_response(self) -> str:
        greetings = [
            "Hello! Welcome to my interactive portfolio. I'm Jeremy, and I'm excited to chat with you about my work and experience!",
            "Hey there! Thanks for visiting my portfolio. I'm Jeremy, a software engineer who loves building cool stuff. What would you like to know?",
            "Hi! Great to meet you. I'm Jeremy, and this is my interactive portfolio. Feel free to ask me anything about my projects or experience!",
            "Greetings! I'm Jeremy, and I'm passionate about software engineering. What brings you here today?",
        ]
        return random.choice(greetings)

    def get_default_response(self, input_text: str) -> str:
        """Default response for unknown topics"""
        responses = [
            "Hmm, that's not something I have specific information about in my knowledge base. I'm focused on sharing details about my software engineering background, projects, and experience. What would you like to know about my work?",
            "I don't have details about that topic, but I'd be happy to tell you about my technical skills, projects, or experience as a software engineer. What interests you most?",
            "That's outside my current knowledge base, but I can share plenty about my development work, technical expertise, or personal interests. What would you like to explore?",
            "I'm not sure about that particular topic, but I'm here to discuss my software engineering background! Feel free to ask about my projects, skills, or experience.",
        ]
        return random.choice(responses)
    
    def get_ai_question_response(self) -> str:
        """Handle questions about whether this is AI"""
        responses = [
            "Nope, not AI! This is a custom-built response system for lightning-fast, targeted interactions. Just clever pattern matching and pre-written responses so you can quickly find exactly what you want to know about me! 🤖",
            "Ha! I get this question a lot. This is actually a rule-based system I built for instant, targeted responses about my background. Smart keyword matching and response templates make it easy to get specific info quickly! 😄",
            "Not artificial intelligence - just regular intelligence! This portfolio uses pattern recognition and response templates so you can get to know me easier and ask targeted questions with lightning-fast responses.",
            "Good eye! This isn't AI - it's a deterministic response engine I coded for lightning-fast, targeted responses. Every response is crafted and triggered by keyword patterns so you can quickly learn about my background! 💻",
        ]
        return random.choice(responses)
    
    def get_fishing_response(self) -> str:
        """Handle fishing-related conversations"""
        responses = [
            "A fellow angler! I absolutely love fishing, especially salmon fishing in the fall here in Michigan. There's nothing quite like the fight of a Great Lakes salmon! 🎣",
            "Fishing is one of my favorite ways to unwind! Living in Michigan gives me amazing access to salmon runs in the fall. The tributaries coming off Lake Huron are incredible this time of year.",
            "You caught my attention with fishing! 😄 I'm passionate about salmon fishing - Michigan's fall runs are legendary. There's something meditative about being on the water at dawn.",
            "Fishing is my zen time! Michigan is a paradise for salmon fishing, especially in the fall. I love hitting the rivers when the salmon are running - it's pure magic.",
        ]
        return random.choice(responses)
    
    def get_soccer_response(self) -> str:
        """Handle soccer-related conversations"""  
        responses = [
            "Soccer! I played at Madonna University back in the day. Nothing beats the beautiful game - still follow it closely and try to get out on the pitch when I can! ⚽",
            "A soccer fan! I had some great years playing at Madonna University. The sport taught me so much about teamwork and strategy - skills I use in software development too!",
            "Soccer is such a passion of mine! Played collegiately at Madonna University and still love the game. Do you follow any particular leagues or teams?",
            "You've hit on one of my favorite topics! Soccer was a huge part of my college experience at Madonna University. The discipline and teamwork from soccer definitely shaped how I approach engineering projects.",
        ]
        return random.choice(responses)
    
    def get_gaming_response(self) -> str:
        """Handle gaming conversations"""
        responses = [
            "Gaming is a great way to unwind after coding all day! I enjoy everything from indie games to AAA titles. There's something satisfying about well-designed game mechanics - probably the engineer in me! 🎮",
            "Love video games! They're like interactive software experiences, which appeals to my developer brain. Plus, they're perfect for relaxing after a long day of problem-solving.",
            "Gaming and coding go hand in hand for me! I appreciate the artistry in game design and often find inspiration for UI/UX work. What type of games do you enjoy?",
            "Video games are one of my favorite hobbies! As a developer, I'm fascinated by game engines and the technical challenges of creating immersive experiences.",
        ]
        return random.choice(responses)
    
    def get_outdoors_response(self) -> str:
        """Handle outdoor activities"""
        responses = [
            "The outdoors is where I recharge! Camping and backpacking in Michigan's wilderness areas are some of my favorite activities. Nothing beats sleeping under the stars after a long hike! 🏕️",
            "I'm all about outdoor adventures! Backpacking and camping help me disconnect from screens and reconnect with nature. Michigan has some incredible trails and camping spots.",
            "Outdoor enthusiast here! Whether it's backpacking through state forests or camping with the family, I love being in nature. It's the perfect balance to spending time behind a computer.",
            "Nature is my therapy! Camping and backpacking adventures help clear my mind and often lead to my best problem-solving insights. Michigan's outdoor scene is fantastic!",
        ]
        return random.choice(responses)
    
    def get_family_response(self) -> str:
        """Handle family-related conversations"""
        responses = [
            "Family is everything to me! I'm blessed with an amazing wife and three beautiful daughters. They keep me grounded and remind me what's truly important in life. 👨‍👩‍👧‍👧",
            "My wife and three daughters are my world! Balancing family time with my passion for technology keeps life interesting. They're incredibly supportive of my career.",
            "Being a dad to three daughters and having an incredible wife is the best part of my life! They inspire me to work hard but also to make sure I'm present for all the important moments.",
            "Family first, always! My wife and three daughters make every day an adventure. They've taught me patience, creativity, and the importance of work-life balance.",
        ]
        return random.choice(responses)
    
    def get_location_response(self) -> str:
        """Handle location/Michigan questions"""
        responses = [
            "I'm based in Livonia, Michigan! It's a great location - close to Detroit for the tech scene, but with easy access to all the outdoor activities Michigan has to offer. 🏠",
            "Livonia, Michigan is home! I love living here - it's got that perfect Midwest feel, great schools for the kids, and I'm never far from a fishing spot or hiking trail.",
            "Home is Livonia, Michigan! Living in the Midwest gives me the best of both worlds - a growing tech community and incredible outdoor recreation opportunities.",
            "I call Livonia, Michigan home! It's been perfect for raising our family and I love the proximity to both urban opportunities and natural beauty.",
        ]
        return random.choice(responses)
    
    def get_name_response(self) -> str:
        """Handle name/identity questions"""
        responses = [
            "I'm Jeremy! Software engineer, outdoor enthusiast, and proud dad from Livonia, Michigan. Nice to meet you! 👋",
            "Hey there! I'm Jeremy - a full-stack developer who loves building cool tech, fishing Michigan's rivers, and spending time with my family. What's your name?",
            "I'm Jeremy! When I'm not coding or chasing salmon in Michigan's tributaries, I'm probably camping with my wife and three daughters. Great to connect with you!",
            "Jeremy's the name! I'm a software engineer living in Michigan who's passionate about technology, the outdoors, and family time. Thanks for asking!",
        ]
        return random.choice(responses)
    
    def get_music_response(self) -> str:
        """Handle music-related conversations"""
        responses = [
            "Music is a huge passion of mine! I play both piano and guitar, and I actually have a certificate in film scoring. There's something magical about creating soundtracks that enhance storytelling! 🎵",
            "I love music! Piano and guitar are my instruments of choice, and I've studied film scoring too. Creating music for visual media combines my technical and creative sides perfectly.",
            "Music and coding have a lot in common - both require pattern recognition and creativity! I play piano and guitar, plus I'm certified in film scoring. Do you play any instruments?",
            "You've hit on another passion! I play piano and guitar, and I have a certificate in film scoring. There's something about composing music that complements the logical thinking of programming. 🎹🎸",
        ]
        return random.choice(responses)
    
    def get_personal_state_response(self, input_text: str = "") -> str:
        """Handle personal state expressions like being tired, excited, etc."""
        input_lower = input_text.lower()
        
        if any(word in input_lower for word in ["tired", "exhausted", "sleepy"]):
            responses = [
                "Ah, I hear you on being tired! Long days can be tough. Maybe take a break and come back to chat about my projects when you're feeling more refreshed? 😴",
                "Being tired is rough! As a developer, I know those late coding sessions can wear you out. Feel free to ask me anything quick, or come back when you're more rested!",
                "I totally get being tired - between coding, family time, and outdoor adventures, I know that feeling! What would you like to know about my work?",
            ]
        elif any(word in input_lower for word in ["excited", "happy"]):
            responses = [
                "That's awesome that you're excited! I love that energy. What's got you excited? And what would you like to know about my projects?",
                "Great to hear you're in good spirits! I'm always excited to talk about technology and development work. What interests you most?",
                "Excitement is contagious! I get excited talking about coding projects and outdoor adventures. What would you like to explore?",
            ]
        elif any(word in input_lower for word in ["stressed", "frustrated"]):
            responses = [
                "Sorry to hear you're feeling stressed! Sometimes a good chat about technology or outdoor adventures can be a nice distraction. What would you like to know?",
                "Stress can be rough - I find that coding or getting outdoors helps me unwind. What can I tell you about my work or hobbies?",
                "I understand feeling frustrated! As a developer, debugging can definitely test your patience. Want to hear about some of my projects?",
            ]
        else:
            responses = [
                "I appreciate you sharing that with me! While I'm focused on discussing my software engineering background, I'm here to chat. What would you like to know about my work?",
                "Thanks for letting me know how you're feeling! I'm here to share about my development experience and projects. What interests you?",
                "I hear you! Feel free to ask me anything about my technical skills, projects, or experience. What would you like to explore?",
            ]
        
        return random.choice(responses)
    
    def get_project_details_response(self, input_text: str = "") -> str:
        """Handle specific project detail requests"""
        input_lower = input_text.lower()
        
        if "product adia" in input_lower or "adia" in input_lower:
            return """**Product Adia - TTS Demo Under Pressure** 🚀

This was a classic "I need this yesterday" scenario! The stakeholders needed a working text-to-speech demo that could handle massive amounts of text without crashing or eating up all the memory.

**The Challenge:**
• Handle up to 100,000 characters seamlessly
• Keep memory overhead minimal (no memory bloat)
• Intelligent sentence chunking for natural speech flow
• Deliver fast under tight deadline pressure

**The Solution:**
I built a smart TTS system that breaks down large text blocks into manageable chunks while maintaining natural speech patterns. The key was optimizing memory usage so it could process huge documents without performance degradation.

**Tech Stack:** Text-to-Speech APIs, Memory Optimization, Performance Tuning

**The Result:** A working demo that impressed stakeholders and proved we could handle enterprise-scale TTS requirements. Sometimes the best solutions come from deadline pressure! 💪"""

        elif "stripe" in input_lower and ("onboarding" in input_lower or "voice" in input_lower):
            return """**Stripe Onboarding Voice Agent - My Interview Project** 🎤

This was my chance to showcase what's possible with Deepgram's Voice Agent technology. The goal? Complete Stripe Connected Account onboarding without ever touching a keyboard.

**The Vision:**
• Fully voice-controlled user experience
• Handle complex financial onboarding via conversation
• Showcase DG Voice Agent capabilities
• Prove voice-first can replace traditional forms

**Technical Implementation:**
Built with Next.js frontend, Node.js/Express backend, integrated with Deepgram Voice Agent and Stripe's Connected Accounts API. The tricky part was handling all the edge cases in natural conversation flow.

**The Impact:**
Demonstrated that voice interfaces can handle complex, multi-step processes that typically require forms. This opened up discussions about voice-first experiences across financial services.

**Tech Stack:** Next.js, Node.js, Express, Deepgram Voice Agent, Stripe API

It was incredibly satisfying to see something that complex work seamlessly through voice alone! 🎯"""

        elif "voiceworks" in input_lower:
            return """**Voiceworks Contributions - Hit the Ground Running** ⚡

In my first few weeks at Deepgram, I dove straight into Voiceworks - and I'm convinced this product has massive potential for customers!

**What I Tackled:**
• **Front-end Bug Fixes:** Squashed critical UX issues that were affecting user experience
• **Auth Flow Improvements:** Streamlined the authentication process for better developer experience  
• **Debug Test Page:** Built an integrated debugging interface for easier troubleshooting
• **Debug Tap Component:** Created a reusable component for debugging workflows

**The Tech:**
Working with Rust and React - a fascinating combination that really showcases the performance benefits of Rust for backend processing while maintaining familiar React patterns on the frontend.

**Future Vision:**
I'm actively discussing with Applied Engineering about getting Voiceworks out to customers. This product deserves to be in the hands of developers - it's genuinely awesome and has major potential for voice-enabled applications.

**Tech Stack:** Rust, React

The speed at which I could contribute meaningfully shows how well-architected the Voiceworks codebase is! 🛠️"""

        elif "flux" in input_lower or "river" in input_lower:
            return """**Project Flux (River Revamp) - Making Benchmarks Actually Useful** 📊

I took an existing STT comparison demo and completely revamped it to provide real, actionable benchmarking data. The previous version had some issues with latency measurements that made it misleading.

**The Problem:**
• Four STT models needed fair comparison
• Previous demo showed inaccurate latency (services weren't properly isolated)
• Stakeholders needed real performance data, not misleading metrics

**My Solution:**
• Isolated each STT service for true latency measurements
• Added comprehensive benchmarking across multiple metrics
• Built proper testing infrastructure for fair comparisons
• Delivered accurate performance data stakeholders could trust

**The Timeline:**
This was done across 2 intense days while juggling other priorities. Time management and focus were crucial - but that's often when you do your best work!

**Tech Stack:** Speech-to-Text APIs, Benchmarking Tools, Performance Analysis

**The Result:** Stakeholders finally had reliable data to make informed decisions about STT model selection. Sometimes the most valuable work is making existing tools actually useful! 🎯"""

        else:
            return """I'd love to dive deeper into any of my Deepgram projects! Here's what I can tell you more about:

🎤 **Stripe Onboarding Voice Agent** - My interview project showcasing voice-first experiences
⚡ **Voiceworks Contributions** - Front-end fixes, auth improvements, and debug tooling  
🚀 **Product Adia** - Rapid TTS demo handling 100k+ characters under deadline pressure
📊 **Project Flux** - STT model comparison with real benchmarking data

Just ask about any of these specifically, or feel free to inquire about my other past work and experience! I love discussing the technical challenges and solutions. 🔧"""
        
        return random.choice([
            "I'd be happy to share more details about that project! What specifically would you like to know?",
            "Great question! Let me dive deeper into the technical details and challenges of that project.",
            "That's one of my favorite projects to discuss! What aspect interests you most?"
        ])
    
    def get_test_response(self, input_text: str = "") -> str:
        """Generate organic test responses based on conversation state"""
        current_time = time.time()
        self.conversation_state["test_count"] += 1
        time_since_last = current_time - self.conversation_state["last_test_time"]
        self.conversation_state["last_test_time"] = current_time
        
        count = self.conversation_state["test_count"]
        
        # Different responses based on context
        if count == 1:
            responses = [
                "I can see you're testing this chat system, and good news - it works! 🎉",
                "Testing, testing... and yes, I'm receiving you loud and clear! ✅",
                "Ah, the classic test message! Everything's working perfectly on my end.",
                "Test confirmed! The system is responsive and ready for your questions.",
            ]
        elif count == 2:
            responses = [
                "Testing again? I appreciate the thoroughness! Still working great. 😊",
                "Round two of testing! Yep, still here and still responding.",
                "Double-checking the system? Smart move - and yes, all systems go!",
                "Another test? I'm consistently here and ready to chat!",
            ]
        elif count <= 5:
            responses = [
                f"Test #{count}! You're really making sure this works, aren't you? 😄",
                f"Still testing after {count} tries? I admire your dedication to quality assurance!",
                f"Test message #{count} received! I'm not going anywhere.",
                f"This is test #{count} - I'm starting to feel like a QA environment! 🧪",
            ]
        else:
            responses = [
                "Okay, I think we've established the system works! 😅 What would you like to know about my projects or experience?",
                "You've tested this quite thoroughly! How about we chat about something more interesting?",
                "I'm definitely working - maybe we can move on to discussing my technical skills or projects?",
                "Test mode complete! Ready for some real questions about my background?",
            ]
        
        # Add time-based context
        if time_since_last < 5:  # Less than 5 seconds
            time_responses = [
                " That was quick!",
                " Lightning fast testing!",
                " You're on a roll!",
                " Rapid fire testing, I see!",
            ]
            return random.choice(responses) + random.choice(time_responses)
        elif time_since_last > 300:  # More than 5 minutes
            time_responses = [
                " Welcome back to testing!",
                " Back for another test run?",
                " Testing after a break - nice!",
                " Returning to verify I'm still here?",
            ]
            return random.choice(time_responses) + " " + random.choice(responses)
        
        return random.choice(responses)
