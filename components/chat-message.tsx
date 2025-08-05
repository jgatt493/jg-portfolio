import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import { Card } from "@/components/ui/card"

interface Message {
  id: string
  content: string
  isUser: boolean
  timestamp: Date
}

interface ChatMessageProps {
  message: Message
}

export function ChatMessage({ message }: ChatMessageProps) {
  return (
    <div className={`flex ${message.isUser ? "justify-end" : "justify-start"} mb-8`}>
      <div className={`flex ${message.isUser ? "flex-row-reverse" : "flex-row"} items-end max-w-[85%] ${message.isUser ? "mr-4" : ""}`}>
        <Avatar className={`w-8 h-8 flex-shrink-0 mb-1 ${message.isUser ? "ml-3" : "mr-3"}`}>
          <AvatarFallback className={message.isUser ? "bg-accent text-white" : "bg-primary text-white"}>
            {message.isUser ? "👤" : "🤖"}
          </AvatarFallback>
        </Avatar>

        <Card
          className={`p-4 border-0 shadow-sm ${
            message.isUser 
              ? "bg-accent/20 rounded-2xl rounded-br-md" 
              : "bg-card rounded-2xl rounded-bl-md"
          }`}
        >
          <p className="text-white text-sm leading-relaxed whitespace-pre-wrap">{message.content}</p>
          <p className="text-xs text-slate-400 mt-3 opacity-70">{message.timestamp.toLocaleTimeString()}</p>
        </Card>
      </div>
    </div>
  )
}
