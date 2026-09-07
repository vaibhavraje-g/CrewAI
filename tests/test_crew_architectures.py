"""
Unit and architecture tests for CrewAI implementations
"""
import pytest
import os
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool
from crewai_common import resolve_llm, has_valid_api_key


@pytest.fixture
def mock_llm():
    return LLM(model="gpt-4o-mini", api_key="mock-key-for-testing")


def test_agent_initialization(mock_llm):
    """Ensures Agent roles, goals, and backstories initialize accurately"""
    researcher = Agent(
        role='Principal AI Researcher',
        goal='Analyze autonomous agent architectures',
        backstory='Expert researcher in multi-agent orchestration systems.',
        verbose=False,
        allow_delegation=False,
        llm=mock_llm
    )
    assert researcher.role == 'Principal AI Researcher'
    assert 'autonomous agent' in researcher.goal
    assert researcher.allow_delegation is False


def test_task_configuration(mock_llm):
    """Validates Task structure, descriptions, and expected output schemas"""
    writer = Agent(
        role='Tech Editor',
        goal='Polish documentation',
        backstory='Veteran editor specializing in developer documentation.',
        llm=mock_llm
    )
    task = Task(
        description='Review the architecture diagram and write a 2-page brief.',
        expected_output='Markdown technical brief with 3 sections.',
        agent=writer
    )
    assert task.agent == writer
    assert 'Markdown technical brief' in task.expected_output
    assert 'architecture diagram' in task.description


def test_sequential_crew_assembly(mock_llm):
    """Validates full Sequential Crew pipeline construction"""
    agent1 = Agent(role='Researcher', goal='Gather info', backstory='Collector', llm=mock_llm)
    agent2 = Agent(role='Writer', goal='Compose report', backstory='Writer', llm=mock_llm)

    task1 = Task(description='Gather 3 data points', expected_output='3 points', agent=agent1)
    task2 = Task(description='Summarize into report', expected_output='Summary', agent=agent2)

    crew = Crew(
        agents=[agent1, agent2],
        tasks=[task1, task2],
        process=Process.sequential,
        verbose=False
    )
    assert len(crew.agents) == 2
    assert len(crew.tasks) == 2
    assert crew.process == Process.sequential


def test_hierarchical_crew_assembly(mock_llm):
    """Validates Hierarchical Crew configuration and manager delegation"""
    worker1 = Agent(role='Frontend Engineer', goal='Build UI', backstory='UI dev', llm=mock_llm)
    worker2 = Agent(role='Backend Engineer', goal='Build API', backstory='API dev', llm=mock_llm)

    task1 = Task(description='Design responsive interface', expected_output='UI Mockup')
    task2 = Task(description='Create REST endpoints', expected_output='API endpoints')

    crew = Crew(
        agents=[worker1, worker2],
        tasks=[task1, task2],
        process=Process.hierarchical,
        manager_llm=mock_llm,
        verbose=False
    )
    assert crew.process == Process.hierarchical
    assert len(crew.agents) == 2
    assert crew.manager_llm is not None


def test_custom_tool_registration(mock_llm):
    """Ensures custom tools can be authored and assigned to agents cleanly"""
    @tool("Metric Calculator")
    def calculate_efficiency(score_a: float, score_b: float) -> float:
        """Calculates harmonic mean efficiency between two benchmark scores."""
        if score_a <= 0 or score_b <= 0:
            return 0.0
        return 2 * (score_a * score_b) / (score_a + score_b)

    tool_agent = Agent(
        role='Evaluator',
        goal='Calculate benchmark rankings',
        backstory='Quantitative benchmark specialist',
        tools=[calculate_efficiency],
        llm=mock_llm
    )
    assert len(tool_agent.tools) == 1
    # Verify tool execution directly
    res = calculate_efficiency.run(score_a=80.0, score_b=120.0)
    assert float(res) == pytest.approx(96.0)


def test_llm_resolver_custom_base_url():
    """Verifies that resolve_llm dynamically binds base_url when provided"""
    os.environ["OPENAI_BASE_URL"] = "https://api.tokenrouter.com/v1"
    os.environ["TOKENROUTER_API_KEY"] = "sk-test-token"
    
    llm = resolve_llm("z-ai/glm-5.3-free")
    assert llm.model == "z-ai/glm-5.3-free"
    assert llm.base_url == "https://api.tokenrouter.com/v1"
