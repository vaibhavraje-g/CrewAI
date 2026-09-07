# Example 3: Hierarchical Crew

## 🎯 Objective

Demonstrate hierarchical process where a manager agent delegates tasks to worker agents.

## 🏢 Structure

```
        Manager (GPT-4)
           /  |  \
          /   |   \
    Worker1 Worker2 Worker3
```

## 📚 Concepts Demonstrated

- Hierarchical process (vs sequential)
- Auto-generated manager agent
- Task delegation
- Multi-agent coordination

## 🆚 Comparison

**Sequential Process**: You define task order  
**Hierarchical Process**: Manager decides who does what!

This is unique to CrewAI - no direct equivalent in LangGraph!

## 🚀 Run

```bash
python hierarchical_crew.py
```
