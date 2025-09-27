import random
import time
# CRITICAL CORRECTION: Added Streamlit import
import streamlit as st

st.markdown('<h1 style="color:blue">Prepared by Devan Das Mehrani AI Student</h1>', unsafe_allow_html=True)

class PythonQuizApp:
    def __init__(self):
        self.questions = self.load_questions()
        if 'current_question' not in st.session_state:
            self.initialize_session_state()
        
    def initialize_session_state(self):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.user_answers = []
        st.session_state.shuffled_indices = list(range(len(self.questions)))
        random.shuffle(st.session_state.shuffled_indices)
        st.session_state.time_per_question = 60  # 1 minute per question
        st.session_state.start_time = time.time()
        # CORRECTION: Set timer_expired to False upon initialization
        st.session_state.timer_expired = False

    def load_questions(self):
        """Loads all questions and flattens the nested dictionary structure."""
        # Using the original, detailed question set provided by the user
        nested_questions = {
            "Basics & Overview": [
                {
                    "question": "What is the main purpose of the OpenAI Agents SDK?",
                    "options": {
                        "a": "To replace Python entirely",
                        "b": "To build agentic AI apps with lightweight abstractions",
                        "c": "To create databases for LLMs",
                        "d": "To only fine-tune models",
                    },
                    "answer": "b",
                    "rationale": "The Agents SDK is designed to simplify the development of AI applications that use agents by providing lightweight, easy-to-use abstractions."
                },
                {
                    "question": "Which previous experimentation project was the Agents SDK built upon?",
                    "options": {
                        "a": "Guardrails",
                        "b": "Swarm",
                        "c": "Tracing",
                        "d": "Agent Loop",
                    },
                    "answer": "b",
                    "rationale": "The Agents SDK is a production-ready evolution of the previous experimental project called 'Swarm'."
                },
                {
                    "question": "Which of the following is NOT a primitive of the OpenAI Agents SDK?",
                    "options": {
                        "a": "Agents",
                        "b": "Handoffs",
                        "c": "Guardrails",
                        "d": "Pipelines",
                    },
                    "answer": "d",
                    "rationale": "The core primitives of the SDK are Agents, Handoffs, Guardrails, and Sessions. Pipelines are not a formal primitive."
                },
                {
                    "question": "In the Agents SDK, what are Agents?",
                    "options": {
                        "a": "Databases for storing results",
                        "b": "LLMs equipped with instructions and tools",
                        "c": "Pre-built workflows",
                        "d": "Only tracing functions",
                    },
                    "answer": "b",
                    "rationale": "An Agent is an LLM that is configured with a specific set of instructions and a library of tools it can use."
                },
                {
                    "question": "What is the function of Handoffs in the SDK?",
                    "options": {
                        "a": "To reset the conversation",
                        "b": "To delegate tasks between agents",
                        "c": "To install dependencies",
                        "d": "To optimize model training",
                    },
                    "answer": "b",
                    "rationale": "Handoffs are a primitive that enables agents to delegate tasks to other agents, facilitating complex workflows."
                },
                {
                    "question": "Which primitive ensures validation of agent inputs and outputs?",
                    "options": {
                        "a": "Sessions",
                        "b": "Guardrails",
                        "c": "Tracing",
                        "d": "Agent loop",
                    },
                    "answer": "b",
                    "rationale": "Guardrails are functions that are run on agent inputs and outputs to ensure safety and correctness, breaking early if checks fail."
                },
                {
                    "question": "What do Sessions automatically maintain?",
                    "options": {
                        "a": "Input validation",
                        "b": "Tracing graphs",
                        "c": "Conversation history across agent runs",
                        "d": "API key handling",
                    },
                    "answer": "c",
                    "rationale": "Sessions are designed to automatically handle the conversation history, eliminating the need for developers to manage this state manually."
                },
                {
                    "question": "What is a major advantage of the Agents SDK design?",
                    "options": {
                        "a": "It requires learning many abstractions",
                        "b": "It is highly customizable but hard to learn",
                        "c": "It has few primitives and is quick to learn",
                        "d": "It only works with tracing",
                    },
                    "answer": "c",
                    "rationale": "The SDK's design philosophy is to provide a minimal set of powerful primitives that are easy to learn and use."
                },
                {
                    "question": "Which feature handles calling tools, sending results, and looping until completion?",
                    "options": {
                        "a": "Guardrails",
                        "b": "Agent loop",
                        "c": "Function tools",
                        "d": "Sessions",
                    },
                    "answer": "b",
                    "rationale": "The built-in agent loop handles the iterative process of calling tools and processing results until the LLM decides the task is complete."
                },
                {
                    "question": "What is the SDK's approach to programming languages?",
                    "options": {
                        "a": "Java-first",
                        "b": "C++ integration",
                        "c": "Python-first",
                        "d": "No language support",
                    },
                    "answer": "c",
                    "rationale": "The SDK is built to be 'Python-first,' with a core focus on providing a seamless experience for Python developers."
                },
                {
                    "question": "What do Function tools in the SDK allow?",
                    "options": {
                        "a": "Turning Python functions into tools with validation",
                        "b": "Running SQL queries automatically",
                        "c": "Connecting with Java methods",
                        "d": "Handling tracing logs",
                    },
                    "answer": "a",
                    "rationale": "Function tools are a feature that automatically converts any Python function into a callable tool with built-in schema generation and validation."
                },
                {
                    "question": "Which library is used for schema validation in function tools?",
                    "options": {
                        "a": "NumPy",
                        "b": "Pydantic",
                        "c": "Pandas",
                        "d": "FastAPI",
                    },
                    "answer": "b",
                    "rationale": "Function tools leverage the Pydantic library for automatic schema generation and validation of function inputs and outputs."
                },
                {
                    "question": "Which feature lets developers visualize, debug, and monitor agent workflows?",
                    "options": {
                        "a": "Sessions",
                        "b": "Guardrails",
                        "c": "Tracing",
                        "d": "Handoffs",
                    },
                    "answer": "c",
                    "rationale": "Tracing provides a comprehensive view of the agent's workflow, making it easier to visualize, debug, and monitor its actions."
                },
                {
                    "question": "What additional benefits does tracing provide?",
                    "options": {
                        "a": "API key management",
                        "b": "Model evaluation, fine-tuning, and distillation",
                        "c": "Faster installation",
                        "d": "Auto-generating datasets",
                    },
                    "answer": "b",
                    "rationale": "Beyond debugging, tracing data can be used to evaluate models, fine-tune them, or perform distillation to create smaller, more efficient models."
                },
                {
                    "question": "Which command installs the OpenAI Agents SDK?",
                    "options": {
                        "a": "pip install openai-sdk",
                        "b": "pip install openai-agents",
                        "c": "pip install agents-openai",
                        "d": "pip install openai-tools",
                    },
                    "answer": "b",
                    "rationale": "The correct `pip` command to install the SDK is `pip install openai-agents`."
                },
                {
                    "question": "In the 'Hello World' example, which class initializes the agent?",
                    "options": {
                        "a": "Runner",
                        "b": "Agent",
                        "c": "Guardrail",
                        "d": "Tool",
                    },
                    "answer": "b",
                    "rationale": "The `Agent` class is used to initialize a new agent instance."
                },
                {
                    "question": "What environment variable must be set to run the example code?",
                    "options": {
                        "a": "OPENAI_ENV",
                        "b": "OPENAI_API_KEY",
                        "c": "OPENAI_AGENT",
                        "d": "API_SECRET_KEY",
                    },
                    "answer": "b",
                    "rationale": "To authenticate with the OpenAI API, the `OPENAI_API_KEY` environment variable must be set."
                },
                {
                    "question": "Which method runs the agent synchronously in the Hello World example?",
                    "options": {
                        "a": "Agent.run()",
                        "b": "Runner.run_sync()",
                        "c": "Agent.start()",
                        "d": "Runner.execute()",
                    },
                    "answer": "b",
                    "rationale": "The `Runner.run_sync()` method is used to run the agent in a synchronous manner."
                },
                {
                    "question": "What is printed as the output in the Hello World example?",
                    "options": {
                        "a": "A JSON object",
                        "b": "An error message",
                        "c": "The agent's final output",
                        "d": "Only the tracing logs",
                    },
                    "answer": "c",
                    "rationale": "The example prints the final output of the agent after it has completed its task."
                },
                {
                    "question": "What is the best description of the Agents SDK overall?",
                    "options": {
                        "a": "A complex framework with many abstractions",
                        "b": "A lightweight, Python-first toolkit for building AI agents",
                        "c": "A library only for tracing and debugging",
                        "d": "A replacement for machine learning frameworks",
                    },
                    "answer": "b",
                    "rationale": "The SDK is best described as a lightweight and Python-first toolkit that simplifies the development of AI agents."
                },
            ],
            "Section 1: Basics & Overview (1-10)": [
                {
                    "question": "The OpenAI Agents SDK is primarily designed for:",
                    "options": {
                        "a": "Building operating systems",
                        "b": "Building agentic AI apps with minimal abstractions",
                        "c": "Replacing Python interpreters",
                        "d": "Managing databases",
                    },
                    "answer": "b",
                    "rationale": "The SDK's main purpose is to build agentic AI apps, focusing on simplicity and minimal abstractions to speed up development."
                },
                {
                    "question": "The OpenAI Agents SDK is a production-ready upgrade of:",
                    "options": {
                        "a": "LangChain",
                        "b": "Guardrails",
                        "c": "Swarm",
                        "d": "Function tools",
                    },
                    "answer": "c",
                    "rationale": "The Agents SDK is a direct evolution and production-ready version of the earlier experimentation project known as 'Swarm'."
                },
                {
                    "question": "Which programming language is the SDK primarily built for?",
                    "options": {
                        "a": "Java",
                        "b": "Python",
                        "c": "C++",
                        "d": "Rust",
                    },
                    "answer": "b",
                    "rationale": "The SDK is explicitly described as a 'Python-first' toolkit, with a design tailored for Python developers."
                },
                {
                    "question": "The Agents SDK emphasizes:",
                    "options": {
                        "a": "Maximum abstractions",
                        "b": "Lightweight and easy-to-use design",
                        "c": "GPU optimization only",
                        "d": "High-level complexity",
                    },
                    "answer": "b",
                    "rationale": "The core philosophy behind the SDK is to offer a lightweight and user-friendly design with minimal, powerful primitives."
                },
                {
                    "question": "Which of the following is NOT mentioned as a primitive?",
                    "options": {
                        "a": "Agents",
                        "b": "Handoffs",
                        "c": "Guardrails",
                        "d": "Plugins",
                    },
                    "answer": "d",
                    "rationale": "The key primitives mentioned are Agents, Handoffs, Guardrails, and Sessions. Plugins are a broader concept, not a core primitive of the SDK."
                },
                {
                    "question": "The SDK is powerful enough to:",
                    "options": {
                        "a": "Express complex relationships between tools and agents",
                        "b": "Only run basic prompts",
                        "c": "Replace APIs",
                        "d": "Automatically build GUIs",
                    },
                    "answer": "a",
                    "rationale": "The SDK's abstractions are designed to be composable, allowing developers to create and express complex relationships and workflows between different agents and tools."
                },
                {
                    "question": "The SDK provides built-in:",
                    "options": {
                        "a": "Data encryption",
                        "b": "Tracing for visualization and debugging",
                        "c": "Operating system integration",
                        "d": "Browser plugins",
                    },
                    "answer": "b",
                    "rationale": "One of the key features of the SDK is its built-in tracing capability, which is essential for visualizing and debugging agent workflows."
                },
                {
                    "question": "Which statement best reflects the SDK's design principle?",
                    "options": {
                        "a": "Many abstractions and difficult learning",
                        "b": "Few primitives and quick to learn",
                        "c": "No customization",
                        "d": "Must learn a new programming language",
                    },
                    "answer": "b",
                    "rationale": "The SDK is designed to be quick to learn and use by providing a small, focused set of powerful primitives."
                },
                {
                    "question": "What does 'works great out of the box' mean?",
                    "options": {
                        "a": "SDK has no defaults",
                        "b": "It runs immediately with minimal setup",
                        "c": "Requires complex setup",
                        "d": "Only supports testing",
                    },
                    "answer": "b",
                    "rationale": "The phrase 'works great out of the box' implies that the SDK has sensible defaults and requires very little setup to start building and running applications."
                },
                {
                    "question": "Developers can:",
                    "options": {
                        "a": "Only use default settings",
                        "b": "Customize exactly what happens in the agent workflow",
                        "c": "Never modify primitives",
                        "d": "Run without Python",
                    },
                    "answer": "b",
                    "rationale": "While providing solid defaults, the SDK is also designed to be highly customizable, giving developers control over every aspect of their agent workflows."
                },
            ],
            "Section 2: Primitives (11-25)": [
                {
                    "question": "Agents are:",
                    "options": {
                        "a": "LLMs equipped with instructions and tools",
                        "b": "SQL servers",
                        "c": "Guard functions",
                        "d": "Tracing visualizers",
                    },
                    "answer": "a",
                    "rationale": "Agents in the SDK are large language models (LLMs) that have been configured with specific instructions and the ability to use a set of tools."
                },
                {
                    "question": "Handoffs allow:",
                    "options": {
                        "a": "Task delegation between agents",
                        "b": "Resetting conversations",
                        "c": "Saving agent outputs to files",
                        "d": "Encryptions messages",
                    },
                    "answer": "a",
                    "rationale": "The Handoff primitive is specifically for passing control and tasks from one agent to another within a workflow."
                },
                {
                    "question": "Guardrails provide:",
                    "options": {
                        "a": "Visualization",
                        "b": "Validation of inputs and outputs",
                        "c": "Conversation storage",
                        "d": "Agent orchestration",
                    },
                    "answer": "b",
                    "rationale": "Guardrails are used to validate and check both the inputs and outputs of agents to ensure they are safe and correct."
                },
                {
                    "question": "Sessions maintain:",
                    "options": {
                        "a": "Input validation",
                        "b": "History across agent runs",
                        "c": "Tracing logs",
                        "d": "Pydantic schemas",
                    },
                    "answer": "b",
                    "rationale": "A session is a primitive that automatically maintains the state and history of a conversation or agent run, making it a state management tool."
                },
                {
                    "question": "Which primitive helps in delegating work between multiple agents?",
                    "options": {
                        "a": "Sessions",
                        "b": "Handoffs",
                        "c": "Tracing",
                        "d": "Function tools",
                    },
                    "answer": "b",
                    "rationale": "Handoffs are the primitive specifically designed to allow for the delegation of work between different agents in a multi-agent system."
                },
                {
                    "question": "Which primitive ensures safety and correctness of input/output?",
                    "options": {
                        "a": "Tracing",
                        "b": "Guardrails",
                        "c": "Agents",
                        "d": "Sessions",
                    },
                    "answer": "b",
                    "rationale": "Guardrails are the mechanism in the SDK for ensuring the safety, correctness, and validity of an agent's inputs and outputs."
                },
                {
                    "question": "If you want to track past conversations, you should use:",
                    "options": {
                        "a": "Guardrails",
                        "b": "Sessions",
                        "c": "Handoffs",
                        "d": "Agent loop",
                    },
                    "answer": "b",
                    "rationale": "Sessions are the primitive that automatically maintains and manages the conversation history, making them the right choice for tracking past conversations."
                },
                {
                    "question": "Guardrails can:",
                    "options": {
                        "a": "Break early if checks fail",
                        "b": "Continue even after failure",
                        "c": "Only validate outputs",
                        "d": "Ignore schema validation",
                    },
                    "answer": "a",
                    "rationale": "A key feature of Guardrails is their ability to 'break early' in the workflow if the validation checks fail, preventing unsafe or incorrect execution."
                },
                {
                    "question": "Which primitive is responsible for state management?",
                    "options": {
                        "a": "Sessions",
                        "b": "Guardrails",
                        "c": "Handoffs",
                        "d": "Agents",
                    },
                    "answer": "a",
                    "rationale": "Sessions are the state management primitive that automatically handles the conversation history and other stateful data across agent runs."
                },
                {
                    "question": "Which primitive is closest to debugging support?",
                    "options": {
                        "a": "Guardrails",
                        "b": "Tracing",
                        "c": "Sessions",
                        "d": "Handoffs",
                    },
                    "answer": "b",
                    "rationale": "Tracing provides a visual and detailed log of the agent's workflow, making it the primary tool for debugging and monitoring."
                },
                {
                    "question": "In a workflow where one agent writes a draft and another reviews it, which primitive is used?",
                    "options": {
                        "a": "Sessions",
                        "b": "Guardrails",
                        "c": "Handoffs",
                        "d": "Tracing",
                    },
                    "answer": "c",
                    "rationale": "This type of multi-agent workflow, where a task is passed from one agent to another, is facilitated by the Handoff primitive."
                },
                {
                    "question": "Agents can be combined with tools to:",
                    "options": {
                        "a": "Make them follow structured instructions",
                        "b": "Encrypt API keys",
                        "c": "Track execution time only",
                        "d": "Replace Python modules",
                    },
                    "answer": "a",
                    "rationale": "By equipping an agent with a set of tools, you can provide it with specific capabilities and a structured way to execute tasks and follow instructions."
                },
                {
                    "question": "What happens if Guardrail checks fail?",
                    "options": {
                        "a": "SDK continues with warnings",
                        "b": "SDK breaks early",
                        "c": "SDK ignores the error",
                        "d": "SDK reruns the agent automatically",
                    },
                    "answer": "b",
                    "rationale": "Guardrails are designed to break the agent's execution early if a validation check fails, preventing incorrect or unsafe outputs."
                },
                {
                    "question": "Which primitive would you choose for workflow validation?",
                    "options": {
                        "a": "Handoffs",
                        "b": "Guardrails",
                        "c": "Sessions",
                        "d": "Agents",
                    },
                    "answer": "b",
                    "rationale": "Guardrails are the primitive in the SDK responsible for validating inputs and outputs to a workflow to ensure correctness and safety."
                },
                {
                    "question": "Which primitive ties everything together in agentic workflows?",
                    "options": {
                        "a": "Sessions",
                        "b": "Agents",
                        "c": "Guardrails",
                        "d": "Pipelines",
                    },
                    "answer": "b",
                    "rationale": "Agents are the central component of the SDK, bringing together instructions, tools, and the agent loop to perform tasks."
                },
            ],
            "Section 3: Features (26-50)": [
                {
                    "question": "The SDK has a built-in:",
                    "options": {
                        "a": "SQL connector",
                        "b": "Agent loop",
                        "c": "GPU optimizer",
                        "d": "Database layer",
                    },
                    "answer": "b",
                    "rationale": "The SDK includes a built-in agent loop that handles the iterative process of an agent deciding on an action, calling a tool, and processing the results."
                },
                {
                    "question": "The agent loop handles:",
                    "options": {
                        "a": "Tool calls and iteration until completion",
                        "b": "Only validating inputs",
                        "c": "Resetting sessions",
                        "d": "Running SQL queries",
                    },
                    "answer": "a",
                    "rationale": "The agent loop is a core feature that manages the entire process of tool orchestration, including making tool calls and iterating until the task is complete."
                },
                {
                    "question": "The SDK is described as:",
                    "options": {
                        "a": "Python-first",
                        "b": "Java-first",
                        "c": "C-first",
                        "d": "Multi-language only",
                    },
                    "answer": "a",
                    "rationale": "The SDK's design is heavily focused on the Python ecosystem and is described as 'Python-first' due to its seamless integration with Python tools and libraries."
                },
                {
                    "question": "Which feature eliminates manual state handling?",
                    "options": {
                        "a": "Guardrails",
                        "b": "Sessions",
                        "c": "Handoffs",
                        "d": "Agent loop",
                    },
                    "answer": "b",
                    "rationale": "Sessions are the primitive that simplifies state management by automatically maintaining conversation history across multiple agent runs."
                },
                {
                    "question": "Function tools allow:",
                    "options": {
                        "a": "Any Python function to be converted into a tool",
                        "b": "Only SQL-based functions to run",
                        "c": "Only async functions to run",
                        "d": "Built-in C++ integration",
                    },
                    "answer": "a",
                    "rationale": "The Function tools feature is designed to easily wrap any existing Python function, turning it into a tool that an agent can call."
                },
                {
                    "question": "Function tools use:",
                    "options": {
                        "a": "NumPy",
                        "b": "Pydantic for validation",
                        "c": "Pandas",
                        "d": "TensorFlow",
                    },
                    "answer": "b",
                    "rationale": "Function tools automatically use Pydantic to generate schemas for function parameters, which enables robust input validation."
                },
                {
                    "question": "Which feature helps with debugging workflows visually?",
                    "options": {
                        "a": "Sessions",
                        "b": "Guardrails",
                        "c": "Tracing",
                        "d": "Handoffs",
                    },
                    "answer": "c",
                    "rationale": "Tracing provides a visual representation of the agent's thought process and actions, which is invaluable for debugging complex workflows."
                },
                {
                    "question": "Which feature supports evaluation and fine-tuning of models?",
                    "options": {
                        "a": "Guardrails",
                        "b": "Tracing",
                        "c": "Sessions",
                        "d": "Agent loop",
                    },
                    "answer": "b",
                    "rationale": "The data collected through tracing can be exported and used with OpenAI's tools for model evaluation, fine-tuning, and distillation."
                },
                {
                    "question": "Agent loop continues until:",
                    "options": {
                        "a": "LLM decides the task is complete",
                        "b": "Timer expires",
                        "c": "Max tokens are reached",
                        "d": "A Guardrail fails",
                    },
                    "answer": "a",
                    "rationale": "The agent loop is designed to iterate, calling tools as needed, until the underlying LLM determines that the task has been completed and a final answer can be provided."
                },
                {
                    "question": "Which statement is true about the SDK's design?",
                    "options": {
                        "a": "It avoids using Pydantic",
                        "b": "It is built to be modular and composable",
                        "c": "It is not extensible",
                        "d": "It requires manual state management",
                    },
                    "answer": "b",
                    "rationale": "The SDK is designed with a small set of composable primitives that allow developers to build complex, modular agentic workflows."
                },
                {
                    "question": "Which command is used to install the Agents SDK?",
                    "options": {
                        "a": "pip install openai-tools",
                        "b": "pip install openai-agents",
                        "c": "pip install agents-sdk",
                        "d": "pip install agentic",
                    },
                    "answer": "b",
                    "rationale": "The correct installation command is `pip install openai-agents`."
                },
                {
                    "question": "What is the key benefit of Function tools?",
                    "options": {
                        "a": "They only work with async code",
                        "b": "They automate schema generation and validation for functions",
                        "c": "They replace the need for LLMs",
                        "d": "They manage cloud deployment",
                    },
                    "answer": "b",
                    "rationale": "The main benefit is the automatic conversion of Python functions into callable tools with schema generation (using Pydantic) and validation."
                },
                {
                    "question": "Tracing helps in optimization by enabling:",
                    "options": {
                        "a": "Deployment to a local server",
                        "b": "Evaluation and distillation of models",
                        "c": "Automatic code generation",
                        "d": "Resetting the agent's memory",
                    },
                    "answer": "b",
                    "rationale": "The tracing data provides the necessary information for model evaluation, fine-tuning, and distillation, which are all methods of optimization."
                },
                {
                    "question": "Which part of the Agent's configuration determines its personality and goals?",
                    "options": {
                        "a": "The tools library",
                        "b": "The Guardrails",
                        "c": "The instructions (system prompt)",
                        "d": "The Session history",
                    },
                    "answer": "c",
                    "rationale": "The instructions, typically provided in a system prompt, are what define an Agent's role, personality, and overall goals."
                },
                {
                    "question": "The Agents SDK provides a smooth bridge between LLM execution and:",
                    "options": {
                        "a": "External APIs and Python code",
                        "b": "Web development frameworks",
                        "c": "SQL database management",
                        "d": "Machine learning training loops",
                    },
                    "answer": "a",
                    "rationale": "The SDK, particularly with Function tools and the agent loop, is designed to seamlessly integrate LLM reasoning with actual code execution against APIs and Python functions."
                },
                {
                    "question": "Which part of the agent is responsible for deciding *when* to use a tool?",
                    "options": {
                        "a": "The Guardrail",
                        "b": "The Session",
                        "c": "The Agent Loop",
                        "d": "The LLM within the Agent",
                    },
                    "answer": "d",
                    "rationale": "The underlying LLM, based on the provided instructions and tools, is responsible for deciding whether to call a tool and what arguments to use."
                },
                {
                    "question": "What is the primary role of the `Runner` class in simple examples?",
                    "options": {
                        "a": "To define the Agent's instructions",
                        "b": "To execute the Agent's logic synchronously or asynchronously",
                        "c": "To manage the Guardrails",
                        "d": "To reset the Session state",
                    },
                    "answer": "b",
                    "rationale": "The `Runner` class (or similar concepts in the SDK) provides the execution environment, allowing you to run the agent's process in a simple, synchronous, or complex, asynchronous manner."
                },
                {
                    "question": "What is the key benefit of Guardrails in a multi-agent system?",
                    "options": {
                        "a": "Optimized memory usage",
                        "b": "Ensuring one agent's output meets the next agent's input requirements",
                        "c": "Generating Pydantic schemas",
                        "d": "Visualizing handoffs",
                    },
                    "answer": "b",
                    "rationale": "In multi-agent systems, Guardrails are crucial for validating the output of one agent before it becomes the input to another, guaranteeing a robust and correct pipeline."
                },
                {
                    "question": "The Python-first approach allows for deep integration with:",
                    "options": {
                        "a": "Java Virtual Machines",
                        "b": "Existing Python tools and libraries (e.g., NumPy, Pandas)",
                        "c": "Proprietary database formats",
                        "d": "Assembly language",
                    },
                    "answer": "b",
                    "rationale": "The Python-first design ensures that the SDK integrates smoothly with the vast and rich ecosystem of existing Python libraries for data science, web development, and more."
                },
                {
                    "question": "The Agents SDK is characterized by being:",
                    "options": {
                        "a": "A heavy, monolithic framework",
                        "b": "Lightweight and composable",
                        "c": "API-only, no local execution",
                        "d": "Exclusively for research purposes",
                    },
                    "answer": "b",
                    "rationale": "The SDK is explicitly described as lightweight and built from composable primitives, making it flexible and easy to use."
                },
            ],
        }
        
        # Flatten the nested structure into a single list of questions
        flattened_questions = []
        for category in nested_questions.values():
            flattened_questions.extend(category)
        
        return flattened_questions
    
    def get_current_question(self):
        """Returns the current question based on shuffled indices and current index."""
        if st.session_state.current_question < len(self.questions):
            shuffled_index = st.session_state.shuffled_indices[st.session_state.current_question]
            return self.questions[shuffled_index]
        return None

    def display_quiz_ui(self):
        """Renders the current question and handles user input via Streamlit."""
        
        current_q_index = st.session_state.current_question
        total_questions = len(self.questions)

        if current_q_index >= total_questions:
            self.display_results()
            return

        question_data = self.get_current_question()
        
        # Calculate time remaining
        elapsed_time = time.time() - st.session_state.start_time
        time_left = st.session_state.time_per_question - int(elapsed_time)

        if time_left <= 0:
            st.session_state.timer_expired = True
            # Automatically save a skipped/incorrect answer
            st.session_state.user_answers.append({
                "question": question_data["question"],
                "user_answer": "Timeout",
                "correct_answer": question_data["answer"],
                "is_correct": False,
                "rationale": question_data["rationale"]
            })
            self.next_question()
            st.rerun() # Rerun to display the next question/results
            return

        # Display timer
        st.info(f"⏰ **Time Left:** {time_left} seconds | **Question {current_q_index + 1}/{total_questions}** | **Score:** {st.session_state.score}")

        st.markdown(f"### {question_data['question']}")

        # Handle user selection
        options = question_data['options']
        # Create a unique key for the radio buttons to ensure they reset on question change
        radio_key = f"q_{current_q_index}"
        
        user_choice = st.radio("Select your answer:", options.keys(), format_func=lambda k: f"**{k.upper()}**: {options[k]}", key=radio_key)

        # Submit button
        if st.button("Next", key="submit_btn"):
            self.process_answer(user_choice, question_data)
            self.next_question()
            # Force a rerun to update the UI immediately with the next question
            st.rerun()

    def process_answer(self, user_choice, question_data):
        """Checks the answer and updates the score and user_answers list."""
        correct_answer = question_data['answer']
        is_correct = user_choice == correct_answer

        if is_correct:
            st.session_state.score += 1
            st.success("Correct Answer! 🎉✅")
        else:
            st.error(f"Incorrect. The correct answer was **{correct_answer.upper()}**: {question_data['options'][correct_answer]}")

        # Store the answer data
        st.session_state.user_answers.append({
            "question": question_data["question"],
            "user_answer": user_choice,
            "correct_answer": correct_answer,
            "is_correct": is_correct,
            "rationale": question_data["rationale"]
        })

    def next_question(self):
        """Moves to the next question and resets the timer."""
        st.session_state.current_question += 1
        st.session_state.start_time = time.time()
        st.session_state.timer_expired = False


    def display_results(self):
        """Displays the final score and review of all questions."""
        st.header("Quiz Complete! 🏆")
        final_score = st.session_state.score
        total_questions = len(self.questions)
        st.balloons()
        
        st.markdown(f"## Your Final Score: **{final_score}/{total_questions}**")
        
        if final_score == total_questions:
            st.success("Perfect score! Excellent work! 🧠")
        elif final_score >= total_questions * 0.7:
            st.info("Great job! You have a strong understanding of the topic. 👍")
        else:
            st.warning("Keep practicing! Review the rationales below to improve. 📚")

        st.subheader("Review Your Answers")
        
        # Use a single flag to ensure all questions are iterated
        # The list comprehension is used to force a full iteration for display
        # No actual list is needed here, but the code is simplified to demonstrate the review.
        for i, review in enumerate(st.session_state.user_answers):
            q_num = i + 1
            icon = "✅" if review['is_correct'] else "❌"
            
            st.markdown(f"---")
            st.markdown(f"**{icon} Question {q_num}:** {review['question']}")
            
            if review['is_correct']:
                st.markdown(f"**Your Answer:** {review['user_answer'].upper()}: {self.questions[st.session_state.shuffled_indices[i]]['options'][review['user_answer']]}")
                st.markdown(f"**Result:** Correct")
            else:
                user_option_text = self.questions[st.session_state.shuffled_indices[i]]['options'].get(review['user_answer'], "N/A (Timeout or Error)")
                correct_option_text = self.questions[st.session_state.shuffled_indices[i]]['options'][review['correct_answer']]
                st.markdown(f"**Your Answer:** {review['user_answer'].upper()}: {user_option_text} (Incorrect)")
                st.markdown(f"**Correct Answer:** {review['correct_answer'].upper()}: {correct_option_text}")

            st.markdown(f"**Rationale:** *{review['rationale']}*")
        
        st.markdown("---")
        
        if st.button("Start Over", key="restart_btn"):
            self.initialize_session_state()
            st.rerun()

    def run(self):
        """The main Streamlit execution loop for the quiz."""
        self.display_quiz_ui()

# --- Main application entry point ---
def main():
    # Instantiate the quiz application
    app = PythonQuizApp()
    # Run the main Streamlit display logic
    app.run()

if __name__ == "__main__":
    main()