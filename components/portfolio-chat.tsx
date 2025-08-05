"use client"

import { useState, useRef, useEffect } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import { Send } from "lucide-react"
import { ChatMessage } from "@/components/chat-message"
import { QuickActionTabs } from "@/components/quick-action-tabs"
import { SkillsSection } from "@/components/skills-section"
import { ProjectsSection } from "@/components/projects-section"
import { PastExperienceSection } from "@/components/past-experience-section"

interface Message {
  id: string
  content: string
  isUser: boolean
  timestamp: Date
  type?: 'text' | 'skills' | 'projects' | 'past_projects'
  data?: any
}

export function PortfolioChat() {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToNewMessage = () => {
    // Small delay to ensure the new message is rendered
    setTimeout(() => {
      if (messages.length > 0) {
        // Scroll to show the last message with some padding above it
        const lastMessageElement = document.querySelector(`[data-message-id="${messages[messages.length - 1].id}"]`)
        if (lastMessageElement) {
          lastMessageElement.scrollIntoView({ 
            behavior: "smooth",
            block: "start" // Show the top of the message
          })
        }
      }
    }, 100)
  }

  useEffect(() => {
    scrollToNewMessage()
  }, [messages])

  const handleSendMessage = async (message: string) => {
    if (!message.trim()) return

    const userMessage: Message = {
      id: Date.now().toString(),
      content: message,
      isUser: true,
      timestamp: new Date(),
    }

    setMessages((prev) => [...prev, userMessage])
    setInput("")
    setIsLoading(true)

    try {
      const response = await fetch("http://localhost:8000/api/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message }),
      })

      if (!response.ok) {
        throw new Error("Failed to get response")
      }

      const data = await response.json()

      const botMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: data.response,
        isUser: false,
        timestamp: new Date(),
        type: data.intent === 'skills' ? 'skills' : data.intent === 'projects' ? 'projects' : data.intent === 'past_projects' ? 'past_projects' : 'text',
        data: data.intent === 'skills' ? data.skills_data : data.intent === 'projects' ? data.projects_data : data.intent === 'past_projects' ? data.past_projects_data : undefined,
      }

      setMessages((prev) => [...prev, botMessage])
    } catch (error) {
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: "Sorry, I'm having trouble connecting to my backend. Please try again!",
        isUser: false,
        timestamp: new Date(),
      }
      setMessages((prev) => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  const handleQuickAction = (category: string) => {
    const quickPrompts = {
      me: "Tell me about yourself",
      projects: "What projects have you worked on?",
      skills: "What are your technical skills?",
      fun: "What do you do for fun?",
      contact: "How can I get in touch with you?",
    }

    const prompt = quickPrompts[category as keyof typeof quickPrompts] || `Tell me about ${category}`
    handleSendMessage(prompt)
  }

  return (
    <div className="max-w-4xl mx-auto">
      {/* Header */}
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold text-white mb-2">Hey, I'm Jeremy 👋</h1>
        <h2 className="text-6xl font-bold text-white mb-8">AI Portfolio</h2>

        <Avatar className="w-32 h-32 mx-auto mb-8">
          <AvatarFallback className="bg-gradient-to-br from-emerald-400 to-blue-500 text-white text-4xl">
            👨‍💻
          </AvatarFallback>
        </Avatar>
      </div>

      {/* Chat Interface */}
      <div className="bg-card/50 border border-border rounded-xl backdrop-blur-sm">
        <div className="p-6">
          {/* Messages */}
          <div className="space-y-1 mb-6 min-h-[100px] max-h-[400px] overflow-y-auto px-2">
            {messages.length === 0 && (
              <div className="text-center text-slate-400 py-12">
                <p className="text-sm">Try asking about my projects, skills, or experience!</p>
              </div>
            )}

            {messages.map((message) => (
              <div key={message.id} data-message-id={message.id}>
                <ChatMessage message={message} />
                {message.type === 'skills' && !message.isUser && (
                  <div className="mt-6 mb-8 px-2">
                    <SkillsSection skills={message.data} />
                  </div>
                )}
                {message.type === 'projects' && !message.isUser && (
                  <div className="mt-6 mb-8 px-2">
                    <ProjectsSection projects={message.data} />
                  </div>
                )}
                {message.type === 'past_projects' && !message.isUser && (
                  <div className="mt-6 mb-8 px-2">
                    <PastExperienceSection projects={message.data} />
                  </div>
                )}
              </div>
            ))}

            {isLoading && (
              <div className="flex items-center space-x-2 text-slate-400">
                <div className="flex space-x-1">
                  <div className="w-2 h-2 bg-emerald-400 rounded-full animate-bounce"></div>
                  <div
                    className="w-2 h-2 bg-emerald-400 rounded-full animate-bounce"
                    style={{ animationDelay: "0.1s" }}
                  ></div>
                  <div
                    className="w-2 h-2 bg-emerald-400 rounded-full animate-bounce"
                    style={{ animationDelay: "0.2s" }}
                  ></div>
                </div>
                <span className="text-sm">Thinking...</span>
              </div>
            )}

            <div ref={messagesEndRef} className="h-4" />
          </div>

          {/* Input */}
          <div className="flex space-x-3 mb-4">
            <Input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask me anything..."
              className="flex-1 bg-input border-border text-foreground placeholder-muted-foreground rounded-xl px-4 py-3 focus:ring-2 focus:ring-primary/20 focus:border-primary/50"
              onKeyPress={(e) => e.key === "Enter" && handleSendMessage(input)}
              disabled={isLoading}
            />
            <Button
              onClick={() => handleSendMessage(input)}
              disabled={isLoading || !input.trim()}
              className="bg-primary hover:bg-primary/90 text-primary-foreground rounded-xl px-4 py-3"
            >
              <Send className="w-4 h-4" />
            </Button>
          </div>

          {/* Quick Action Tabs */}
          <QuickActionTabs onAction={handleQuickAction} />
        </div>
      </div>
    </div>
  )
}
