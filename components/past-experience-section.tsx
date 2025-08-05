"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Building2, ShoppingCart, Code2, BarChart3, Wrench } from "lucide-react"

interface PastProject {
  title: string
  description: string
  details: string[]
  techStack: string[]
  category: 'enterprise' | 'ecommerce' | 'analytics' | 'modernization'
  icon?: any
}

interface PastExperienceSectionProps {
  projects?: PastProject[]
}

const defaultPastProjects: PastProject[] = [
  {
    title: "UVIS - Used Vehicle Information System",
    description: "Rebuilt a mainframe application handling hundreds of millions of dollars in inventory annually",
    details: [
      "Modernized legacy mainframe system to current tech stack",
      "Handled hundreds of millions of dollars in vehicle inventory",
      "Seamless migration from COBOL to modern architecture",
      "Zero downtime deployment for critical business operations"
    ],
    techStack: ["Angular", "Spring", "Python", "COBOL", "SQL"],
    category: 'modernization',
    icon: Wrench
  },
  {
    title: "Ford Developer Marketplace",
    description: "Built a comprehensive marketplace enabling consumers to interact with Ford's APIs",
    details: [
      "Created developer-friendly API marketplace",
      "Enabled consumer interaction with Ford's ecosystem",
      "Streamlined API discovery and integration",
      "Enterprise-grade authentication and authorization"
    ],
    techStack: ["Angular", "Java"],
    category: 'enterprise',
    icon: Building2
  },
  {
    title: "Global Ecommerce Platform (Project EMP)",
    description: "Served as org 'anchor' managing dealer-side ecommerce development globally",
    details: [
      "Led global ecommerce initiative as organizational anchor",
      "Managed dealer-side platform development worldwide",
      "Coordinated cross-functional teams across time zones",
      "Scalable architecture supporting international operations"
    ],
    techStack: ["React", "Spring", "Cloud Functions", "BigQuery"],
    category: 'ecommerce',
    icon: ShoppingCart
  },
  {
    title: "Audience Builder",
    description: "Campaign analysis tool running historical data to predict performance outcomes",
    details: [
      "Built query generation interface for campaign analysis",
      "Processed historical campaign data at scale",
      "Predictive insights for campaign performance",
      "Big data processing with Hadoop infrastructure"
    ],
    techStack: ["Angular", "Java", "Python", "Hadoop"],
    category: 'analytics',
    icon: BarChart3
  }
]

const categoryConfig = {
  modernization: { label: "Legacy Modernization", color: "bg-green-500/10 text-green-400 border-green-500/20" },
  enterprise: { label: "Enterprise Systems", color: "bg-blue-500/10 text-blue-400 border-blue-500/20" },
  ecommerce: { label: "Global Ecommerce", color: "bg-purple-500/10 text-purple-400 border-purple-500/20" },
  analytics: { label: "Data & Analytics", color: "bg-orange-500/10 text-orange-400 border-orange-500/20" }
}

export function PastExperienceSection({ projects }: PastExperienceSectionProps) {
  const projectsData = projects || defaultPastProjects

  return (
    <div className="space-y-6">
      <div className="text-center mb-6">
        <h2 className="text-2xl font-bold text-white mb-2">Enterprise Experience</h2>
        <p className="text-slate-400 text-sm">Large-scale systems that moved the needle for major organizations</p>
      </div>
      
      <div className="grid gap-4">
        {projectsData.map((project, index) => {
          const Icon = project.icon || Building2
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
                    <h4 className="text-sm font-medium text-slate-300 mb-2">Key Achievements:</h4>
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
            <span className="font-medium">Want to know more?</span>
          </p>
          <p className="text-slate-400 text-sm">
            I love discussing the technical challenges of enterprise-scale development, legacy modernization, and building systems that handle real business impact. Feel free to ask about any of these projects in detail! 🚀
          </p>
        </div>
      </div>
    </div>
  )
}