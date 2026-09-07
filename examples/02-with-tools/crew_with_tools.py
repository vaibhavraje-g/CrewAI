"""
CrewAI Example: Agents with Tools

This demonstrates how agents can use tools autonomously.
Key difference from LangChain: Agents DECIDE when to use tools!
"""

from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, WebsiteSearchTool, FileReadTool
from dotenv import load_dotenv
import os

load_dotenv()

print("=" * 60)
print("🛠️  CrewAI Example: Agents with Tools")
print("=" * 60)

# ============================================================================
# TOOLS SETUP
# ============================================================================
# CrewAI tools are objects that agents can use

# Search tool - requires SERPER_API_KEY
# Get free key from: https://serper.dev/
search_tool = SerperDevTool()

# Website scraping tool
website_tool = WebsiteSearchTool()

# File reading tool
file_tool = FileReadTool()

print("\n✅ Tools initialized:")
print("   - SerperDevTool (Google search)")
print("   - WebsiteSearchTool (Web scraping)")
print("   - FileReadTool (Local files)")

# ============================================================================
# AGENTS WITH TOOLS
# ============================================================================

researcher = Agent(
    role='Tech Research Specialist',
    goal='Find the most accurate and up-to-date information on tech topics',
    backstory="""You're an expert researcher who knows how to find reliable 
    sources on the internet. You always verify information from multiple 
    sources and cite your findings.""",
    tools=[search_tool, website_tool],  # Give researcher search capabilities
    verbose=True,
    allow_delegation=False,
)

analyst = Agent(
    role='Data Analyst',
    goal='Analyze information and extract key insights',
    backstory="""You're a detail-oriented analyst who can spot patterns 
    and trends in data. You provide clear, actionable insights.""",
    tools=[file_tool],  # Analyst can read files
    verbose=True,
    allow_delegation=False,
)

writer = Agent(
    role='Technical Writer',
    goal='Create clear, engaging technical content',
    backstory="""You're a skilled writer who can explain complex topics 
    in simple terms. You craft compelling narratives from research data.""",
    verbose=True,
    allow_delegation=False,
    # Writer doesn't need tools - uses input from other agents
)

print("\n✅ Agents created with tools:")
print(f"   - {researcher.role} → [{search_tool.__class__.__name__}, {website_tool.__class__.__name__}]")
print(f"   - {analyst.role} → [{file_tool.__class__.__name__}]")
print(f"   - {writer.role} → [No tools, uses agent outputs]")

# ============================================================================
# TASKS
# ============================================================================

research_task = Task(
    description="""Search for information about 'CrewAI framework' and find:
    1. What is CrewAI?
    2. Key features
    3. Main use cases
    4. Current version and updates
    
    Use your search tools to find accurate, current information.""",
    expected_output="""A research summary with:
    - Overview of CrewAI
    - List of key features (at least 5)
    - Main use cases (at least 3)
    - Version info or recent updates
    - Sources""",
    agent=researcher,
)

analysis_task = Task(
    description="""Analyze the research findings and identify:
    1. What makes CrewAI unique?
    2. Who should use it?
    3. How it compares to alternatives
    
    Provide clear, structured insights.""",
    expected_output="""Analysis report with:
    - Unique value propositions
    - Target audience
    - Competitive positioning
    - Recommendations""",
    agent=analyst,
    context=[research_task],  # Depends on research
)

writing_task = Task(
    description="""Write a concise, informative blog post introduction 
    (2-3 paragraphs) about CrewAI based on the research and analysis.
    
    Make it engaging and highlight why readers should care.""",
    expected_output="""Blog post introduction that:
    - Hooks the reader
    - Explains what CrewAI is
    - Highlights key benefits
    - Is 150-250 words""",
    agent=writer,
    context=[research_task, analysis_task],  # Uses both previous outputs
)

print("\n✅ Tasks defined:")
print("   - Research (uses search tools)")
print("   - Analysis (processes research)")
print("   - Writing (synthesizes everything)")

# ============================================================================
# CREW EXECUTION
# ============================================================================

crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[research_task, analysis_task, writing_task],
    process=Process.sequential,
    verbose=2,
)

print("\n" + "=" * 60)
print("🎬 Starting crew with tools...")
print("=" * 60)
print("\n💡 Watch how agents AUTONOMOUSLY decide when to use tools!\n")

try:
    # Check for required API keys
    if not os.getenv("SERPER_API_KEY"):
        print("⚠️  Warning: SERPER_API_KEY not set")
        print("For full functionality, get a free key from https://serper.dev/")
        print("\nRunning in limited mode (agents will use their knowledge)...\n")
    
    result = crew.kickoff()
    
    print("\n" + "=" * 60)
    print("✨ FINAL OUTPUT")
    print("=" * 60)
    print(result)
    
    with open('output_with_tools.md', 'w', encoding='utf-8') as f:
        f.write(str(result))
    print("\n💾 Saved to 'output_with_tools.md'")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nIf you see 'SERPER_API_KEY' error:")
    print("1. Go to https://serper.dev/ and sign up (free)")
    print("2. Get your API key")
    print("3. Add to .env: SERPER_API_KEY=your_key_here")

print("\n" + "=" * 60)
print("🎉 Completed!")
print("=" * 60)

# ============================================================================
# KEY INSIGHTS: TOOLS IN CREWAI vs LANGCHAIN
# ============================================================================
"""
🔑 TOOLS: CREWAI vs LANGCHAIN

LANGCHAIN APPROACH:
```python
# You explicitly call tools in chains
chain = LLMChain(...)
search_result = search_tool.run("query")
chain_result = chain.run(search_result)
```

CREWAI APPROACH:
```python
# Agent gets tools and decides when/how to use them
agent = Agent(tools=[search_tool])
task = Task(description="Research...", agent=agent)
# Agent autonomously uses tools as needed!
```

ADVANTAGES OF CREWAI TOOLS:
1. ✅ Autonomous decision-making (agent picks right tool)
2. ✅ Multiple tool usage in one task
3. ✅ Tool chaining (agent can use tool A → tool B)
4. ✅ Error handling (agent retries with different tools)

WHEN TO USE LANGCHAIN TOOLS:
- Need precise control over tool execution order
- Tools have side effects that must be controlled
- Debugging specific tool behavior

WHEN TO USE CREWAI TOOLS:
- Want agents to work autonomously
- Multiple tools available for agent to choose from
- Complex tasks where tool selection depends on context
"""
