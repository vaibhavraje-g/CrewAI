# CrewAI Examples

Progressive examples to learn CrewAI from basics to advanced concepts.

## 📚 Learning Path

### 1. [Basic Crew](01-basic-crew/) - **START HERE**
Simple two-agent crew (researcher + writer) with sequential process.

**Concepts**: Agents, Tasks, Crews, Sequential execution

**Runtime**: ~1-2 minutes

---

### 2. [Crew with Tools](02-with-tools/)
Agents with real tools for searching and web scraping.

**Concepts**: Tool integration, Autonomous tool usage

**Requirements**: SERPER_API_KEY (optional, free tier available)

**Runtime**: ~2-3 minutes

---

### 3. [Hierarchical Crew](03-hierarchical-crew/)
Manager agent that delegates tasks to workers.

**Concepts**: Hierarchical process, Dynamic delegation

**Unique to CrewAI**: No direct LangGraph equivalent!

**Runtime**: ~2-4 minutes

---

## 🚀 Quick Start

```bash
# 1. Set up environment
cd examples
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r ../requirements.txt

# 3. Configure environment
cp ../.env.example ../.env
# Edit .env and add your OPENAI_API_KEY

# 4. Run an example
cd 01-basic-crew
python basic_crew.py
```

## 🔑 Key Differences from LangChain/LangGraph

| Feature | LangGraph | CrewAI |
|---------|-----------|---------|
| **Abstraction** | Low-level (nodes/edges) | High-level (roles/tasks) |
| **Control** | Explicit flow control | Autonomous agents |
| **Delegation** | Manual routing | Automatic (hierarchical) |
| **Tools** | Explicit calls | Agent decides |
| **Use Case** | Custom workflows | Multi-agent teams |

## 📖 Learning Resources

- [Notes: CrewAI Basics](../notes/crewai-basics.md) - Comprehensive guide
- [Official Docs](https://docs.crewai.com/)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewAI)

## 💡 Tips

1. **Start with Example 1** - Understand core concepts
2. **Compare to LangGraph** - Note the differences
3. **Experiment** - Modify agent roles and tasks
4. **Check verbose output** - See how agents think
5. **Read the comments** - Each example has detailed explanations

---

**Next**: Check out [projects/](../projects/) for more complex multi-agent systems!
