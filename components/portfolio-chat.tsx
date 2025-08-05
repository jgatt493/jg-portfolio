"use client"

import { useState, useRef, useEffect } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import { Send } from "lucide-react"
import { ChatMessage } from "@/components/chat-message"
import { QuickActionTabs } from "@/components/quick-action-tabs"

interface Message {
  id: string
  content: string
  isUser: boolean
  timestamp: Date
}

export function PortfolioChat() {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }

  useEffect(() => {
    scrollToBottom()
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
        <h2 className="text-6xl font-bold text-white mb-8">Software Engineer</h2>

        <Avatar className="w-32 h-32 mx-auto mb-8">
          <AvatarFallback className="bg-gradient-to-br from-emerald-400 to-blue-500 text-white text-4xl">
            👨‍💻
          </AvatarFallback>
        </Avatar>
      </div>

      {/* Chat Interface */}
      <div className="bg-slate-800/30 rounded-lg backdrop-blur-sm">
        <div className="p-4">
          {/* Messages */}
          <div className="space-y-4 mb-4 min-h-[200px] max-h-[400px] overflow-y-auto">
            {messages.length === 0 && (
              <div className="text-center text-slate-400 py-8">
                <p className="text-sm">Try asking about my projects, skills, or experience!</p>
              </div>
            )}

            {messages.map((message) => (
              <ChatMessage key={message.id} message={message} />
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

            <div ref={messagesEndRef} />
          </div>

          {/* Input */}
          <div className="flex space-x-2 mb-3">
            <Input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask me anything..."
              className="flex-1 bg-slate-700/50 border-slate-600 text-white placeholder-slate-400"
              onKeyPress={(e) => e.key === "Enter" && handleSendMessage(input)}
              disabled={isLoading}
            />
            <Button
              onClick={() => handleSendMessage(input)}
              disabled={isLoading || !input.trim()}
              className="bg-emerald-500 hover:bg-emerald-600 text-white"
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
