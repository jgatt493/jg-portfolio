"use client"

import { Badge } from "@/components/ui/badge"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Code, Database, Cloud, Wrench, Palette, Server } from "lucide-react"

interface SkillsSectionProps {
  skills?: {
    frontend?: string[]
    backend?: string[]
    databases?: string[]
    cloud?: string[]
    devops?: string[]
  }
}

const defaultSkills = {
  frontend: [
    "HTML", "CSS", "JavaScript/TypeScript", "Tailwind CSS", "Bootstrap", 
    "Next.js", "React", "Angular", "Vercel AI SDK", "Gsap"
  ],
  backend: [
    "Java", "Python", "C#", "C++", "Spring Boot", "Python FastAPI", 
    "Node.js", "COBOL", "Git", "GitHub"
  ],
  databases: [
    "PostgreSQL", "SQL", "DB2", "BigQuery", "Hadoop", "MongoDB"
  ],
  cloud: [
    "GCP", "AWS", "Azure", "Docker", "Kubernetes", "Cloud Functions"
  ],
  devops: [
    "Jenkins", "Tekton", "Cloud Build", "CI/CD", "DevOps", "Infrastructure"
  ]
}

const skillIcons = {
  frontend: Code,
  backend: Server,
  databases: Database,
  cloud: Cloud,
  devops: Wrench
}

const skillTitles = {
  frontend: "Frontend Development",
  backend: "Backend & Languages",
  databases: "Databases & Data",
  cloud: "Cloud Platforms",
  devops: "DevOps & CI/CD"
}

export function SkillsSection({ skills }: SkillsSectionProps) {
  const skillsData = skills || defaultSkills

  return (
    <div className="space-y-8">
      <div className="text-center">
        <h2 className="text-3xl font-bold text-white mb-2">Skills & Expertise</h2>
      </div>
      
      {Object.entries(skillsData).map(([category, items]) => {
        const Icon = skillIcons[category as keyof typeof skillIcons] || Code
        const title = skillTitles[category as keyof typeof skillTitles] || category
        
        return (
          <div key={category} className="space-y-4">
            <div className="flex items-center space-x-2 text-white">
              <Icon className="w-5 h-5 text-emerald-400" />
              <h3 className="text-xl font-semibold">{title}</h3>
            </div>
            
            <div className="flex flex-wrap gap-3">
              {items.map((skill, index) => (
                <Badge
                  key={index}
                  variant="secondary"
                  className="px-4 py-2 text-sm font-medium bg-slate-800/80 border-slate-700 text-slate-200 hover:bg-slate-700/80 hover:text-white transition-colors duration-200"
                >
                  {skill}
                </Badge>
              ))}
            </div>
          </div>
        )
      })}
    </div>
  )
}