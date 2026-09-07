# 🤖 Production Multi-Agent Systems with CrewAI

An enterprise-ready reference repository demonstrating modular, autonomous multi-agent systems using the **CrewAI** orchestration framework.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-Orchestration-FF4B4B?logo=ai&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Tools-1C3C3C?logo=chainlink&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🏛️ Multi-Agent Architecture Patterns

```
                          ┌────────────────────────┐
                          │   HIERARCHICAL CREW    │
                          └───────────┬────────────┘
                                      │
                                      ▼
                        ┌───────────────────────────┐
                        │    Manager Agent (LLM)    │
                        │ • Plans task decomposition│
                        │ • Delegates to workers    │
                        │ • Reviews output quality  │
                        └─────────────┬─────────────┘
                                      │
               ┌──────────────────────┴──────────────────────┐
               ▼                                             ▼
  ┌─────────────────────────┐                   ┌─────────────────────────┐
  │      Worker Agent 1     │                   │      Worker Agent 2     │
  │ • Role: Senior Analyst  │                   │ • Role: Lead Writer     │
  │ • Tools: Search / Scrape│                   │ • Tools: Formatter      │
  └─────────────────────────┘                   └─────────────────────────┘
```

---

## 📂 Modular Architectures & Examples

| Directory | Execution Model | Description | Key Components |
| :--- | :--- | :--- | :--- |
| **`examples/01-basic-crew`** | **Sequential** | Basic multi-agent pipeline passing context from Researcher to Writer. | `Agent`, `Task`, `Crew`, Sequential Process |
| **`examples/02-with-tools`** | **Tool-Calling** | Agents equipped with web search and custom Python functions for dynamic data retrieval. | Custom Tools, Serper API, Error Handling |
| **`examples/03-hierarchical-crew`** | **Hierarchical** | Autonomous manager agent delegates tasks to specialized workers based on capability. | Manager LLM, Dynamic Delegation, Consensus |

---

## 🚀 Quick Execution Guide

### Prerequisites
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install crewai langchain-community
```

### Running the Examples

1. **Basic Sequential Crew**:
   ```bash
   python examples/01-basic-crew/basic_crew.py
   ```

2. **Crew with Tool Calling**:
   ```bash
   python examples/02-with-tools/crew_with_tools.py
   ```

3. **Hierarchical Manager Delegation Crew**:
   ```bash
   python examples/03-hierarchical-crew/hierarchical_crew.py
   ```

---

## 🛡️ Production Best Practices

- **Role Definition**: Specific personas with distinct `role`, `goal`, and `backstory` attributes yield superior reasoning compared to general prompts.
- **Context Passing**: Explicitly declare `context=[prior_task]` on downstream tasks to ensure dependencies are accurately mapped without hallucinations.
- **Cost & Latency Management**: Use fast, cost-effective models (e.g., Nova Lite / GLM 5.3 Free) for worker nodes, and reserve high-capability reasoning models for manager oversight.
