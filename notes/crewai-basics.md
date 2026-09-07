# CrewAI Basics - Coming from LangChain/LangGraph

## 🎯 What is CrewAI?

CrewAI is a **high-level orchestration framework** for building multi-agent systems. Think of it as focusing on the "organization" and "role-playing" aspects of agents, rather than low-level chain/graph construction.

## 🔄 Key Differences from LangChain/LangGraph

### LangChain
- **Focus**: Building blocks (chains, prompts, tools)
- **Level**: Low to mid-level primitives
- **You control**: Exact prompt flow, chain composition
- **Use case**: Flexible LLM application building

### LangGraph  
- **Focus**: State machines and workflow graphs
- **Level**: Mid-level orchestration
- **You control**: Graph structure, state transitions, conditional edges
- **Use case**: Complex workflows with branching logic

### CrewAI
- **Focus**: Agent roles, tasks, and collaboration
- **Level**: High-level agent orchestration
- **You control**: Roles, goals, task delegation
- **Use case**: Multi-agent systems with autonomous collaboration

## 📊 Mental Model Comparison

```
LangChain:     Components → Chains → Apps
LangGraph:     Nodes → Edges → State Graphs → Workflows
CrewAI:        Agents → Tasks → Crews → Autonomous Teams
```

## 🏗️ Core CrewAI Concepts

### 1. **Agent** (vs LangGraph "Node")
An agent is like a **team member with a role**.

```python
from crewai import Agent

researcher = Agent(
    role='Research Analyst',           # Job title
    goal='Find accurate information',   # What they're trying to achieve
    backstory='Expert researcher...',   # Context for better responses
    tools=[search_tool, scrape_tool],   # What they can use
    verbose=True,
    allow_delegation=False              # Can they ask other agents for help?
)
```

**Key differences from LangGraph:**
- Agents have **personality/context** (backstory)
- Can **delegate** to other agents automatically
- Think "job role" not "function"

### 2. **Task** (vs LangGraph "Edge/Transition")
A task is a **specific job to be done**.

```python
from crewai import Task

research_task = Task(
    description='Research the latest AI trends in 2024',
    expected_output='A detailed report with sources',
    agent=researcher,                    # Who does this?
    async_execution=False               # Sequential or parallel?
)
```

**Key differences:**
- Tasks are **assigned to agents** (not just state transitions)
- Can run **sequentially or in parallel**
- Agents can use their tools autonomously

### 3. **Crew** (vs LangGraph "CompiledGraph")
A crew is your **team executing a mission**.

```python
from crewai import Crew, Process

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,          # or Process.hierarchical
    verbose=True
)

result = crew.kickoff()  # Start the mission!
```

**Execution modes:**
- `Process.sequential`: Tasks run one after another (like a pipeline)
- `Process.hierarchical`: Manager agent delegates to workers (like a company)

## 🔧 Comparison: Same Problem, Different Approaches

### Problem: Research a topic and write a blog post

#### **LangGraph Approach** (Low-level control)
```python
# Define state
class State(TypedDict):
    topic: str
    research: str
    blog: str

# Define nodes
def research_node(state):
    # Manual chain execution
    research = research_chain.invoke(state["topic"])
    return {"research": research}

def write_node(state):
    blog = writing_chain.invoke(state["research"])
    return {"blog": blog}

# Build graph
graph = StateGraph(State)
graph.add_node("research", research_node)
graph.add_node("write", write_node)
graph.add_edge("research", "write")
graph.set_entry_point("research")
```

#### **CrewAI Approach** (High-level roles)
```python
# Define agents
researcher = Agent(
    role='Research Analyst',
    goal='Research topics thoroughly',
    tools=[search_tool]
)

writer = Agent(
    role='Content Writer',
    goal='Write engaging blog posts',
    tools=[writing_tool]
)

# Define tasks
research = Task(
    description='Research {topic}',
    agent=researcher
)

write = Task(
    description='Write blog post about the research',
    agent=writer
)

# Create crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research, write],
    process=Process.sequential
)

crew.kickoff(inputs={'topic': 'AI trends'})
```

## 🎭 When to Use What?

### Use **LangChain** when:
- Building single-agent apps
- Need fine-grained control over prompts
- Working with specific LLM features
- Building reusable components

### Use **LangGraph** when:
- Need complex conditional workflows
- State management is crucial
- Need to loop/retry specific steps
- Want full control over execution flow

### Use **CrewAI** when:
- Multiple specialized agents needed
- Agents should collaborate autonomously
- Role-based task division makes sense
- Want agents to use tools independently

## 🚀 CrewAI Unique Features

### 1. **Delegation** (Not in LangGraph)
Agents can ask other agents for help:
```python
agent = Agent(
    allow_delegation=True  # Can delegate to teammates
)
```

### 2. **Hierarchical Process** (Built-in manager)
```python
crew = Crew(
    agents=[worker1, worker2, worker3],
    tasks=[task1, task2],
    process=Process.hierarchical,
    manager_llm='gpt-4'  # Manager agent auto-created
)
```

### 3. **Memory** (Across executions)
```python
agent = Agent(
    memory=True  # Remembers past interactions
)
```

### 4. **Callbacks** (Monitor progress)
```python
crew = Crew(
    agents=[...],
    tasks=[...],
    step_callback=lambda x: print(x)
)
```

## 📝 Quick Reference

| Concept | LangGraph | CrewAI |
|---------|-----------|---------|
| Basic unit | Node (function) | Agent (role) |
| Connection | Edge | Task assignment |
| Execution | Graph.invoke() | Crew.kickoff() |
| State | Explicit StateGraph | Implicit (task context) |
| Conditional | add_conditional_edges() | Agent decision-making |
| Parallel | send() | async_execution=True |
| Control flow | Manual (edges) | Automatic (delegation) |

## 💡 Best Practices

1. **Be specific with roles**: "Senior Python Developer" > "Developer"
2. **Clear goals**: Agents optimize for their goals
3. **Good backstories**: Provides context, improves responses
4. **Right tools**: Only give tools agents actually need
5. **Task descriptions**: Be explicit about expected outputs

## 🎓 Learning Path

1. ✅ Understand Agent, Task, Crew basics
2. Create simple sequential crew (research → write)
3. Add tools to agents
4. Try hierarchical process
5. Experiment with delegation
6. Add memory and callbacks
7. Build complex multi-agent systems

---

**Next**: Let's build some examples! 🚀
