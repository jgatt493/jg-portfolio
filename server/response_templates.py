import random
from typing import List, Dict, Any

class ResponseTemplates:
    def get_about_response(self) -> str:
        return """Hey there! I'm Jeremy, a passionate software engineer who loves building innovative web applications and solving complex technical challenges.

I have a strong background in full-stack development with over 6 years of experience creating scalable applications. I specialize in modern web technologies like Next.js, React, Python, and cloud infrastructure.

What drives me is the opportunity to turn ideas into reality through code. I enjoy working on everything from user-facing interfaces to backend systems and DevOps automation.

When I'm not coding, you'll find me exploring new technologies, contributing to open source projects, or hiking in the mountains! 🏔️"""

    def get_projects_response(self, projects: List[Dict]) -> str:
        return """I've built some exciting projects that showcase my technical skills:

🚀 **Real-time Analytics Dashboard** - Next.js, Python, PostgreSQL
   High-performance dashboard processing millions of data points with real-time updates

📊 **Microservices E-commerce Platform** - FastAPI, Docker, Kubernetes
   Scalable architecture handling 10k+ concurrent users with 99.9% uptime

🔧 **DevOps Automation Suite** - Python, Terraform, AWS
   Infrastructure-as-code solution that reduced deployment time by 80%

💻 **Open Source CLI Tool** - Go, distributed via Homebrew
   Developer productivity tool with 2k+ GitHub stars and active community

🌐 **Portfolio Chat System** - Next.js, FastAPI, WebSockets
   The interactive system you're using right now! Built with performance in mind.

Each project taught me valuable lessons about scalability, user experience, and system design. Want to dive deeper into any of these?"""

    def get_skills_response(self, skills: Dict) -> str:
        return """I work across the full technology stack with expertise in:

**Languages & Frameworks:**
• Python (FastAPI, Django, Flask) - 6+ years
• JavaScript/TypeScript (React, Next.js, Node.js) - 5+ years  
• Go - For high-performance backend services
• SQL (PostgreSQL, MySQL) - Advanced query optimization

**Cloud & Infrastructure:**
• AWS (EC2, Lambda, RDS, S3, CloudFormation)
• Docker & Kubernetes for containerization
• Terraform for infrastructure as code
• CI/CD with GitHub Actions and Jenkins

**Databases & Caching:**
• PostgreSQL, MongoDB, Redis
• Database design and performance tuning
• Real-time data processing with Apache Kafka

**System Design:**
• Microservices architecture
• API design (REST, GraphQL, gRPC)
• Load balancing and horizontal scaling
• Monitoring with Prometheus and Grafana

I'm always learning and staying current with emerging technologies. Recently exploring Rust and WebAssembly! 🦀"""

    def get_experience_response(self, experience: List[Dict]) -> str:
        return """My professional journey has been focused on building scalable systems:

**Senior Software Engineer** @ TechScale Inc. (2021-Present)
• Lead a team of 5 engineers building cloud-native applications
• Architected microservices handling 1M+ requests/day
• Reduced system latency by 60% through performance optimization
• Mentored junior developers and established coding standards

**Full-Stack Engineer** @ DataFlow Solutions (2019-2021)
• Built real-time analytics platform from ground up
• Implemented automated testing reducing bugs by 75%
• Collaborated with product team to deliver features ahead of schedule
• Migrated legacy monolith to modern microservices architecture

**Software Developer** @ WebCraft Agency (2018-2019)
• Developed custom web applications for enterprise clients
• Worked with diverse tech stacks based on client requirements
• Gained experience in client communication and project management
• Built responsive applications serving 100k+ users

Each role has strengthened my problem-solving skills and deepened my understanding of building production-ready systems! 💼"""

    def get_contact_response(self, contact: Dict) -> str:
        return """I'd love to connect and discuss opportunities or interesting projects!

📧 **Email:** jeremy.engineer@example.com
💼 **LinkedIn:** linkedin.com/in/jeremysoftware
🐙 **GitHub:** github.com/jeremydev
🐦 **Twitter:** @jeremycodes

I'm always interested in:
• Challenging technical problems
• Open source collaboration  
• Mentoring and knowledge sharing
• Innovative startup opportunities

Feel free to reach out if you want to discuss technology, potential collaborations, or just chat about software engineering. I typically respond within a few hours during business days.

Looking forward to connecting! 🚀"""

    def get_fun_response(self) -> str:
        return """When I'm not deep in code, I enjoy:

🏔️ **Hiking & Photography** - I love exploring mountain trails and capturing landscapes. Recently hiked the Pacific Crest Trail!

🎸 **Music** - I play guitar and enjoy jamming with friends. Currently learning jazz improvisation.

📚 **Reading** - Big fan of sci-fi novels and technical books. Just finished "Designing Data-Intensive Applications" by Martin Kleppmann.

🏃‍♂️ **Running** - Training for my first marathon! Running helps me think through complex problems.

🎮 **Gaming** - I enjoy strategy games and indie titles. Currently obsessed with Factorio (the engineer's game!).

🍳 **Cooking** - I love experimenting with new recipes, especially Asian cuisine. Homemade ramen is my specialty!

☕ **Coffee** - Serious coffee enthusiast with a home espresso setup. Always happy to discuss brewing techniques!

What about you? What do you enjoy doing outside of work? 😊"""

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
        responses = [
            f"That's an interesting question about '{input_text}'! While I don't have specific information on that topic, I'd be happy to tell you about my projects, technical skills, or experience. What would you like to explore?",
            f"I'm not sure I have details about '{input_text}' specifically, but I'm here to share information about my software engineering background! Try asking about my projects, skills, or experience.",
            f"Hmm, I don't have information about '{input_text}' in my knowledge base. Would you like to know about my development experience, recent projects, or technical expertise instead?",
            f"That's a great question about '{input_text}'! While I don't have specific details on that, I can tell you all about my work as a software engineer. What aspect interests you most?",
        ]
        return random.choice(responses)
