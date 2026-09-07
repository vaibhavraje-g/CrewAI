"""
CrewAI Example: Hierarchical Process

This demonstrates one of CrewAI's most unique features:
A manager agent that automatically delegates tasks to the right workers!

NO EQUIVALENT IN LANGGRAPH - This is pure CrewAI magic! ✨
"""

from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
import os

load_dotenv()

print("=" * 60)
print("🏢 CrewAI Example: Hierarchical Crew (Manager + Workers)")
print("=" * 60)

# ============================================================================
# WORKER AGENTS (Specialists)
# ============================================================================

researcher = Agent(
    role='Market Research Specialist',
    goal='Conduct thorough market research and competitor analysis',
    backstory="""You're an experienced market researcher with a keen eye 
    for industry trends. You excel at gathering and analyzing market data.""",
    verbose=True,
    allow_delegation=False,  # Workers don't delegate
)

analyst = Agent(
    role='Business Analyst',
    goal='Analyze business opportunities and provide strategic insights',
    backstory="""You're a strategic thinker who can identify business 
    opportunities and risks. You provide data-driven recommendations.""",
    verbose=True,
    allow_delegation=False,
)

writer = Agent(
    role='Business Writer',
    goal='Create clear, professional business documents',
    backstory="""You're a professional business writer who can distill 
    complex analysis into clear, actionable reports.""",
    verbose=True,
    allow_delegation=False,
)

print("\n✅ Worker agents created:")
print(f"   - {researcher.role}")
print(f"   - {analyst.role}")
print(f"   - {writer.role}")

# ============================================================================
# TASKS (High-level objectives, manager will delegate)
# ============================================================================

task1 = Task(
    description="""Analyze the AI agent framework market:
    - Identify key players (LangChain, LangGraph, CrewAI, AutoGen, etc.)
    - Research market trends
    - Note major use cases
    
    This is a high-level task - the manager will assign it to the right agent.""",
    expected_output="Comprehensive market analysis with key findings",
    # NOTE: No agent assigned! Manager will decide who should do this
)

task2 = Task(
    description="""Based on market research, identify:
    - Business opportunities
    - Target customer segments  
    - Competitive advantages needed
    - Potential challenges
    
    Provide strategic recommendations.""",
    expected_output="Strategic business analysis with recommendations",
    # Again, no agent - manager decides
)

task3 = Task(
    description="""Create an executive summary report that includes:
    - Market overview
    - Strategic recommendations
    - Action items
    
    Keep it concise and professional (300-400 words).""",
    expected_output="Executive summary in professional format",
)

print("\n✅ Tasks defined:")
print("   - Market Analysis Task")
print("   - Strategic Analysis Task")
print("   - Executive Summary Task")
print("\n   💡 No agents assigned - manager will delegate!")

# ============================================================================
# HIERARCHICAL CREW (The magic happens here!)
# ============================================================================

crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[task1, task2, task3],
    process=Process.hierarchical,  # 🔑 This is the key!
    manager_llm='gpt-4',  # Manager uses GPT-4 for better delegation
    verbose=2,
)

print("\n✅ Hierarchical crew created!")
print("   📊 Structure:")
print("      Manager (GPT-4)")
print("      ├── Market Research Specialist")
print("      ├── Business Analyst")
print("      └── Business Writer")

# ============================================================================
# EXECUTION
# ============================================================================

print("\n" + "=" * 60)
print("🎬 Starting hierarchical crew...")
print("=" * 60)
print("\n💡 Watch the MANAGER assign tasks to workers!\n")

try:
    result = crew.kickoff()
    
    print("\n" + "=" * 60)
    print("✨ FINAL RESULT")
    print("=" * 60)
    print(result)
    
    with open('hierarchical_output.md', 'w', encoding='utf-8') as f:
        f.write(str(result))
    print("\n💾 Saved to 'hierarchical_output.md'")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nNote: Hierarchical process requires a capable LLM (like GPT-4)")

print("\n" + "=" * 60)
print("🎉 Completed!")
print("=" * 60)

# ============================================================================
# DEEP DIVE: HIERARCHICAL vs SEQUENTIAL
# ============================================================================
"""
🔑 HIERARCHICAL PROCESS - UNIQUE TO CREWAI

WHAT HAPPENS:
1. CrewAI creates an invisible "Manager Agent"
2. Manager reviews all tasks and available agents
3. Manager decides which agent should do which task
4. Manager coordinates execution and monitors progress
5. Manager can reassign tasks if needed

SEQUENTIAL PROCESS:
- You define: Task1 → Task2 → Task3
- Agents execute in order
- No flexibility

HIERARCHICAL PROCESS:
- Manager decides: "Researcher does Task1, Analyst does Task2"
- Dynamic delegation based on agent capabilities
- Can parallelize tasks
- Manager handles dependencies

COMPARISON TO LANGGRAPH:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LangGraph approach:
```python
# You manually route tasks
def routing_function(state):
    if state["task_type"] == "research":
        return "researcher_node"
    elif state["task_type"] == "analysis":
        return "analyst_node"
    # ... etc

graph.add_conditional_edges("router", routing_function)
```

CrewAI approach:
```python
# Manager agent automatically routes!
crew = Crew(
    process=Process.hierarchical,
    manager_llm='gpt-4'
)
# That's it! Manager handles everything
```

WHEN TO USE HIERARCHICAL:
✅ Complex projects with many tasks
✅ Want optimal task allocation
✅ Tasks could be parallelized
✅ Agents have overlapping skills

WHEN TO USE SEQUENTIAL:
✅ Simple, linear workflows
✅ Strict order required
✅ Each task clearly needs specific agent
✅ Simpler and more predictable
"""

# ============================================================================
# BONUS: How to influence manager decisions
# ============================================================================
"""
💡 TIPS FOR HIERARCHICAL CREWS:

1. AGENT ROLES: Be specific! Manager matches roles to tasks
   ❌ Bad: role='Worker'
   ✅ Good: role='Senior Python Developer'

2. AGENT BACKSTORY: Manager considers expertise
   ✅ Include relevant experience and skills

3. TASK DESCRIPTIONS: Clear descriptions help manager delegate
   ✅ Mention required skills or domain knowledge

4. MANAGER LLM: Use capable model (GPT-4 > GPT-3.5)
   - Better understanding of agent capabilities
   - More intelligent delegation

5. VERBOSE MODE: Set verbose=2 to see manager's thinking!
"""
