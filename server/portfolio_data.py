from typing import Dict, List, Any

class PortfolioData:
    def get_projects(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "Real-time Analytics Dashboard",
                "description": "High-performance dashboard processing millions of data points",
                "tech": ["Next.js", "Python", "PostgreSQL", "Redis"],
                "status": "Production",
                "users": "50k+ daily active users",
                "performance": "Sub-100ms query response times"
            },
            {
                "name": "Microservices E-commerce Platform", 
                "description": "Scalable architecture handling high concurrent load",
                "tech": ["FastAPI", "Docker", "Kubernetes", "PostgreSQL"],
                "status": "Production",
                "scale": "10k+ concurrent users",
                "uptime": "99.9% SLA"
            },
            {
                "name": "DevOps Automation Suite",
                "description": "Infrastructure-as-code solution for rapid deployments",
                "tech": ["Python", "Terraform", "AWS", "GitHub Actions"],
                "status": "Production",
                "impact": "80% reduction in deployment time",
                "coverage": "15+ microservices"
            },
            {
                "name": "Open Source CLI Tool",
                "description": "Developer productivity tool with active community",
                "tech": ["Go", "Cobra CLI", "Homebrew"],
                "status": "Open Source",
                "stars": "2k+ GitHub stars",
                "downloads": "10k+ monthly downloads"
            }
        ]

    def get_skills(self) -> Dict[str, List[str]]:
        return {
            "frontend": [
                "HTML", "CSS", "JavaScript/TypeScript", "Tailwind CSS", "Bootstrap", 
                "Next.js", "React", "Angular", "Vercel AI SDK", "Gsap"
            ],
            "backend": [
                "Java", "Python", "C#", "C++", "Spring Boot", "Python FastAPI", 
                "Node.js", "COBOL", "Git", "GitHub"
            ],
            "databases": [
                "PostgreSQL", "SQL", "DB2", "BigQuery", "Hadoop", "MongoDB"
            ],
            "cloud": [
                "GCP", "AWS", "Azure", "Docker", "Kubernetes", "Cloud Functions"
            ],
            "devops": [
                "Jenkins", "Tekton", "Cloud Build", "CI/CD", "DevOps", "Infrastructure"
            ]
        }

    def get_experience(self) -> List[Dict[str, Any]]:
        return [
            {
                "title": "Senior Software Engineer",
                "company": "TechScale Inc.",
                "period": "2021-Present",
                "description": "Lead engineering team building cloud-native applications",
                "achievements": [
                    "Architected microservices handling 1M+ requests/day",
                    "Reduced system latency by 60% through optimization",
                    "Mentored 5+ junior developers"
                ]
            },
            {
                "title": "Full-Stack Engineer", 
                "company": "DataFlow Solutions",
                "period": "2019-2021",
                "description": "Built real-time analytics platform from ground up",
                "achievements": [
                    "Implemented automated testing reducing bugs by 75%",
                    "Migrated legacy monolith to microservices",
                    "Delivered features 30% ahead of schedule"
                ]
            },
            {
                "title": "Software Developer",
                "company": "WebCraft Agency", 
                "period": "2018-2019",
                "description": "Developed custom web applications for enterprise clients",
                "achievements": [
                    "Built applications serving 100k+ users",
                    "Worked with diverse tech stacks",
                    "Maintained 98% client satisfaction rate"
                ]
            }
        ]

    def get_contact(self) -> Dict[str, str]:
        return {
            "email": "jeremy.engineer@example.com",
            "linkedin": "linkedin.com/in/jeremysoftware",
            "github": "github.com/jeremydev",
            "twitter": "@jeremycodes",
            "location": "San Francisco, CA",
            "timezone": "PST (UTC-8)"
        }
