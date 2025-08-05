"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Briefcase, Zap, Cpu, Wrench, Rocket, Users } from "lucide-react"

interface Project {
  title: string
  description: string
  details: string[]
  techStack: string[]
  category: 'current' | 'contribution' | 'demo' | 'future'
  icon?: any
}

interface ProjectsSectionProps {
  projects?: Project[]
}

const defaultProjects: Project[] = [
  {
    title: "Stripe Onboarding Voice Agent",
    description: "My interview project - proving voice-first experiences can replace traditional forms entirely",
    details: [
      "Complete Stripe onboarding flow via voice only",
      "Natural conversation handling edge cases",
      "Zero keyboard interaction required",
      "Built to showcase DG Voice Agent capabilities"
    ],
    techStack: ["Next.js", "Node.js", "Express", "Deepgram Voice Agent"],
    category: 'current',
    icon: Briefcase
  },
  {
    title: "Voiceworks Contributions",
    description: "Hit the ground running - meaningful contributions to this awesome product in my first few weeks",
    details: [
      "Squashed critical front-end bugs affecting UX",
      "Streamlined auth flow for better developer experience",
      "Built integrated Debug test page for easier troubleshooting",
      "Created reusable Debug tap component"
    ],
    techStack: ["Rust", "React"],
    category: 'contribution',
    icon: Wrench
  },
  {
    title: "Product Adia",
    description: "Classic 'I need this yesterday' request - delivered a working TTS demo under tight deadline pressure",
    details: [
      "Handles up to 100,000 characters seamlessly",
      "Smart memory management - no major overhead",
      "Intelligent sentence chunking for natural flow",
      "Rapid delivery when stakeholders needed proof of concept"
    ],
    techStack: ["Text-to-Speech", "Memory Optimization", "Performance Tuning"],
    category: 'demo',
    icon: Zap
  },
  {
    title: "Project Flux (River Revamp)",
    description: "Took an existing concept and made it actually useful - real benchmarking across 2 intense days",
    details: [
      "Four STT models in head-to-head comparison",
      "Added proper benchmarking (previous demo was misleading)",
      "Isolated each service for true latency measurements",
      "Delivered while juggling other priorities - time management FTW"
    ],
    techStack: ["Speech-to-Text", "Benchmarking", "Performance Analysis"],
    category: 'demo',
    icon: Cpu
  },
  {
    title: "Future DG Initiatives",
    description: "Always thinking ahead - collaborating on what's next for Deepgram's developer experience",
    details: [
      "Partnering with Applied Engineering on Voiceworks rollout",
      "Building DG Labs DevOps kit for experienced developers",
      "Creating battle-tested React hooks and services library",
      "Plus whatever Dan tells me to do (that one's self-explanatory 😄)"
    ],
    techStack: ["Strategy", "DevOps", "Component Libraries", "Developer Experience"],
    category: 'future',
    icon: Rocket
  }
]

const categoryConfig = {
  current: { label: "Current Projects", color: "bg-emerald-500/10 text-emerald-400 border-emerald-500/20" },
  contribution: { label: "Contributions", color: "bg-blue-500/10 text-blue-400 border-blue-500/20" },
  demo: { label: "Rapid Demos", color: "bg-purple-500/10 text-purple-400 border-purple-500/20" },
  future: { label: "Future Initiatives", color: "bg-orange-500/10 text-orange-400 border-orange-500/20" }
}

export function ProjectsSection({ projects }: ProjectsSectionProps) {
  const projectsData = projects || defaultProjects

  return (
    <div className="space-y-6">
      <div className="text-center mb-6">
        <h2 className="text-2xl font-bold text-white mb-2">Recent Deepgram Work</h2>
        <p className="text-slate-400 text-sm">Building the future of voice AI, one project at a time</p>
      </div>
      
      <div className="grid gap-4">
        {projectsData.map((project, index) => {
          const Icon = project.icon || Briefcase
          const categoryStyle = categoryConfig[project.category]
          
          return (
            <Card key={index} className="bg-card/80 border-border hover:bg-card/90 transition-colors duration-200">
              <CardHeader className="pb-3">
                <div className="flex items-start justify-between">
                  <div className="flex items-center space-x-3">
                    <div className="p-2 rounded-lg bg-primary/10">
                      <Icon className="w-5 h-5 text-primary" />
                    </div>
                    <div>
                      <CardTitle className="text-lg text-white">{project.title}</CardTitle>
                      <Badge variant="outline" className={`mt-1 text-xs ${categoryStyle.color}`}>
                        {categoryStyle.label}
                      </Badge>
                    </div>
                  </div>
                </div>
                <CardDescription className="text-slate-300 mt-2">
                  {project.description}
                </CardDescription>
              </CardHeader>
              
              <CardContent className="pt-0">
                <div className="space-y-4">
                  <div>
                    <h4 className="text-sm font-medium text-slate-300 mb-2">Key Highlights:</h4>
                    <ul className="space-y-1">
                      {project.details.map((detail, idx) => (
                        <li key={idx} className="text-sm text-slate-400 flex items-start">
                          <span className="w-1.5 h-1.5 rounded-full bg-primary/60 mt-2 mr-2 flex-shrink-0"></span>
                          {detail}
                        </li>
                      ))}
                    </ul>
                  </div>
                  
                  <div>
                    <h4 className="text-sm font-medium text-slate-300 mb-2">Tech Stack:</h4>
                    <div className="flex flex-wrap gap-2">
                      {project.techStack.map((tech, idx) => (
                        <Badge
                          key={idx}
                          variant="secondary"
                          className="text-xs bg-slate-800/60 text-slate-300 border-slate-700"
                        >
                          {tech}
                        </Badge>
                      ))}
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          )
        })}
      </div>
      
      <div className="text-center pt-6">
        <div className="bg-card/60 border border-border rounded-lg p-4">
          <p className="text-slate-300 text-sm mb-2">
            <span className="font-medium">Interested in learning more?</span>
          </p>
          <p className="text-slate-400 text-sm">
            Feel free to ask about any of these projects in detail, or inquire about my other past work and experience! I love diving deep into the technical challenges and solutions. 🚀
          </p>
        </div>
      </div>
    </div>
  )
}