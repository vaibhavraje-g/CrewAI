# Example 2: Crew with Tools

## 🎯 Objective

Add real tools to agents so they can perform actual searches and web scraping.

## 🛠️ Tools Used

- **SerperDevTool**: Google search capability
- **WebsiteSearchTool**: Scrape and search websites
- **FileReadTool**: Read local files

## 📚 Concepts Demonstrated

- Adding tools to agents
- Tools vs manual prompting
- Autonomous tool usage by agents

## 🚀 Run

```bash
# You'll need a Serper API key (free tier available)
# Add to .env: SERPER_API_KEY=your_key

python crew_with_tools.py
```

## 🔑 Key Insight

Unlike LangChain where you explicitly call tools in chains, CrewAI agents **decide when and how to use tools** based on their task!
