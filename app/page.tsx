import { PortfolioChat } from "@/components/portfolio-chat"

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-gray-950 via-slate-950 to-gray-950">
      <div className="container mx-auto px-4 py-8">
        <PortfolioChat />
      </div>
    </main>
  )
}
