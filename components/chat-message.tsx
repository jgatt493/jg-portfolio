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
    <div className={`flex ${message.isUser ? "justify-end" : "justify-start"} mb-4`}>
      <div className={`flex ${message.isUser ? "flex-row-reverse" : "flex-row"} items-start space-x-3 max-w-[80%]`}>
        <Avatar className="w-8 h-8 flex-shrink-0">
          <AvatarFallback className={message.isUser ? "bg-blue-500 text-white" : "bg-emerald-500 text-white"}>
            {message.isUser ? "👤" : "🤖"}
          </AvatarFallback>
        </Avatar>

        <Card
          className={`p-3 ${
            message.isUser ? "bg-blue-500/20 border-blue-500/30 ml-3" : "bg-slate-700/50 border-slate-600 mr-3"
          }`}
        >
          <p className="text-white text-sm leading-relaxed whitespace-pre-wrap">{message.content}</p>
          <p className="text-xs text-slate-400 mt-2">{message.timestamp.toLocaleTimeString()}</p>
        </Card>
      </div>
    </div>
  )
}
