"use client"

import { Button } from "@/components/ui/button"
import { User, Briefcase, Code, Gamepad2, Mail } from "lucide-react"

interface QuickActionTabsProps {
  onAction: (category: string) => void
}

export function QuickActionTabs({ onAction }: QuickActionTabsProps) {
  const tabs = [
    { id: "me", label: "Me", icon: User },
    { id: "projects", label: "Projects", icon: Briefcase },
    { id: "skills", label: "Skills", icon: Code },
    { id: "fun", label: "Fun", icon: Gamepad2 },
    { id: "contact", label: "Contact", icon: Mail },
  ]

  return (
    <div className="flex flex-wrap gap-2 justify-center">
      {tabs.map((tab) => {
        const Icon = tab.icon
        return (
          <Button
            key={tab.id}
            variant="outline"
            size="sm"
            onClick={() => onAction(tab.id)}
            className="bg-slate-900/50 border-slate-800 text-slate-300 hover:bg-primary/10 hover:border-primary/30 hover:text-primary-foreground transition-all duration-200"
          >
            <Icon className="w-4 h-4 mr-2" />
            {tab.label}
          </Button>
        )
      })}
    </div>
  )
}
