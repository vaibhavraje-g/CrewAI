"""
Basic CrewAI Example: Research & Write Team

This example demonstrates:
1. Creating agents with specific roles
2. Defining tasks for agents
3. Running a sequential crew
"""

from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Verify API key is set
if not os.getenv("OPENAI_API_KEY"):
    print("⚠️  Warning: OPENAI_API_KEY not found in environment variables")
    print("Please create a .env file with your OpenAI API key")
    exit(1)

print("=" * 60)
print("🚀 Basic CrewAI Example: Research & Write Team")
print("=" * 60)

# ============================================================================
# STEP 1: Define Agents (Team Members)
# ============================================================================
# Think of agents as team members with specific expertise

researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in AI and data science',
    backstory="""You are a seasoned research analyst with expertise in 
    technology trends. You have a knack for finding accurate, relevant 
    information and presenting it clearly.""",
    verbose=True,          # Show agent's thinking process
    allow_delegation=False,  # This agent won't delegate to others
    # In a real scenario, you'd add tools like:
    # tools=[search_tool, scrape_tool]
)

writer = Agent(
    role='Tech Content Writer',
    goal='Write compelling and informative blog posts about technology',
    backstory="""You are a talented tech writer who can take complex 
    technical topics and make them accessible and engaging for a broad 
    audience. You have a gift for clear, concise writing.""",
    verbose=True,
    allow_delegation=False,
    # Could add tools like:
    # tools=[writing_assistant_tool]
)

print("\n✅ Agents created:")
print(f"   - {researcher.role}")
print(f"   - {writer.role}")

# ============================================================================
# STEP 2: Define Tasks (What needs to be done)
# ============================================================================
# Tasks are assigned to specific agents

research_task = Task(
    description="""Research the latest trends in Large Language Models (LLMs) 
    for 2024. Focus on:
    - Major breakthroughs
    - New architectures or techniques
    - Practical applications
    - Key companies and researchers involved
    
    Provide a comprehensive summary with key findings.""",
    
    expected_output="""A detailed research report with:
    - 3-5 major trends
    - Brief description of each trend
    - Why it matters
    - Sources (even if hypothetical for this demo)""",
    
    agent=researcher,  # Assign to researcher
)

writing_task = Task(
    description="""Using the research findings, write an engaging blog post 
    about LLM trends in 2024. The post should:
    - Have a catchy title
    - Include an introduction that hooks the reader
    - Cover the main trends in an accessible way
    - End with a conclusion about the future of LLMs
    
    Keep it informative but conversational. Target: 500-700 words.""",
    
    expected_output="""A complete blog post in markdown format with:
    - Title
    - Introduction
    - Main content sections
    - Conclusion
    - Professional yet accessible tone""",
    
    agent=writer,  # Assign to writer
    context=[research_task],  # This task depends on research_task output
)

print("\n✅ Tasks defined:")
print(f"   - Research Task (assigned to {researcher.role})")
print(f"   - Writing Task (assigned to {writer.role})")

# ============================================================================
# STEP 3: Create Crew (Assemble the team)
# ============================================================================

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,  # Tasks run one after another
    verbose=2,  # 0=quiet, 1=normal, 2=detailed
)

print("\n✅ Crew assembled!")
print("   Process: Sequential (Research → Write)")

# ============================================================================
# STEP 4: Kickoff! (Start the work)
# ============================================================================

print("\n" + "=" * 60)
print("🎬 Starting crew work...")
print("=" * 60 + "\n")

try:
    result = crew.kickoff()
    
    print("\n" + "=" * 60)
    print("✨ RESULTS")
    print("=" * 60)
    print(result)
    
    # Save the output
    with open('output.md', 'w', encoding='utf-8') as f:
        f.write(str(result))
    print("\n💾 Output saved to 'output.md'")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nTroubleshooting:")
    print("1. Make sure OPENAI_API_KEY is set in your .env file")
    print("2. Check your OpenAI API credits")
    print("3. Verify internet connection")

print("\n" + "=" * 60)
print("🎉 Crew work completed!")
print("=" * 60)

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
🔑 KEY DIFFERENCES FROM LANGGRAPH:

1. AGENTS vs NODES:
   - LangGraph: Nodes are functions you define
   - CrewAI: Agents are autonomous with roles/goals

2. FLOW CONTROL:
   - LangGraph: Explicit edges and conditional routing
   - CrewAI: Task dependencies and process type

3. STATE MANAGEMENT:
   - LangGraph: Explicit state schema and updates
   - CrewAI: Implicit (output of one task → input to next)

4. ABSTRACTION LEVEL:
   - LangGraph: Low-level (you control everything)
   - CrewAI: High-level (agents decide how to do tasks)

5. COLLABORATION:
   - LangGraph: Manual (you define all interactions)
   - CrewAI: Automatic (agents can delegate, discuss)
"""
