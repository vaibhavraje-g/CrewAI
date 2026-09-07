# Example 1: Basic Crew - Research & Write

## 🎯 Objective

Create a simple two-agent crew that researches a topic and writes a blog post about it.

## 🏗️ Structure

- **Agent 1**: Researcher (finds information)
- **Agent 2**: Writer (creates content)
- **Process**: Sequential (research first, then write)

## 📚 Concepts Demonstrated

- Creating agents with roles and goals
- Defining tasks
- Sequential task execution
- Basic crew setup

## 🚀 Run

```bash
python basic_crew.py
```

## 📝 Compare with LangGraph

In LangGraph, you'd manually:
1. Define state schema
2. Create nodes for each function
3. Add edges to connect nodes
4. Compile the graph

In CrewAI:
1. Define agents (auto-handle their own logic)
2. Assign tasks
3. Crew runs autonomously!
