import streamlit as st
import random

st.markdown('<h1 style="color:blue">Prepared by Devan Das Mehrani AI Student</h1>', unsafe_allow_html=True)

class PythonQuizApp:
    def __init__(self):
        # Initialize quiz variables in session state
        if 'questions' not in st.session_state:
            st.session_state.questions = self.load_questions()
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 0
        if 'score' not in st.session_state:
            st.session_state.score = 0
        if 'user_answers' not in st.session_state:
            st.session_state.user_answers = []
        if 'shuffled_indices' not in st.session_state:
            st.session_state.shuffled_indices = list(range(len(st.session_state.questions)))
            random.shuffle(st.session_state.shuffled_indices)
        if 'selected_option' not in st.session_state:
            st.session_state.selected_option = None
        if 'current_section' not in st.session_state:
            st.session_state.current_section = 0
        
        # Show welcome screen if not started
        if 'quiz_started' not in st.session_state:
            st.session_state.quiz_started = False
            self.create_welcome_screen()
        elif not st.session_state.quiz_started:
            self.create_welcome_screen()
        else:
            self.show_question()
    
    def load_questions(self):
        questions = [
            # Topic 1: Prompt Engineering
            {"question": "Q1. Which parameter controls randomness in model responses?", "options": ["A) Top-k", "B) Temperature", "C) Top-p", "D) Max tokens"], "answer": "b", "explanation": "Temperature is a parameter that controls the randomness of the output. A higher temperature results in more diverse and creative text, while a lower temperature makes the output more deterministic."},
            {"question": "Q2. Setting temperature=0 makes responses:", "options": ["A) Random", "B) Deterministic", "C) Unsafe", "D) Incomplete"], "answer": "b", "explanation": "Setting the temperature to 0 makes the model's responses deterministic, as it will always choose the token with the highest probability."},
            {"question": "Q3. Top-k sampling chooses tokens from:", "options": ["A) All candidates", "B) Top k probable tokens", "C) Random tokens", "D) System instructions"], "answer": "b", "explanation": "Top-k sampling limits the token generation to the 'k' most probable tokens at each step, making the output more focused."},
            {"question": "Q4. Top-p (nucleus sampling) works by:", "options": ["A) Selecting until cumulative probability ≥ p", "B) Limiting length", "C) Reducing cost", "D) Ignoring rare tokens"], "answer": "a", "explanation": "Top-p, or nucleus sampling, selects tokens from the smallest possible set whose cumulative probability exceeds a given threshold 'p'."},
            {"question": "Q5. Higher temperature + higher top-p gives:", "options": ["A) More diverse outputs", "B) Deterministic outputs", "C) Shorter tokens", "D) Lower latency"], "answer": "a", "explanation": "A combination of higher temperature and higher top-p allows for greater randomness and diversity in the model's generated text."},
            {"question": "Q6. Best practice for sensitive data in prompts:", "options": ["A) Store secrets inside system prompt", "B) Mask/redact fields", "C) Log everything", "D) Ignore risks"], "answer": "b", "explanation": "To ensure security and privacy, sensitive data should always be masked or redacted before being sent to an LLM."},
            {"question": "Q7. Purpose of system messages:", "options": ["A) Lower latency", "B) Provide high-level rules", "C) Add random tokens", "D) Hide errors"], "answer": "b", "explanation": "System messages are used to provide high-level instructions and context to the model, guiding its overall behavior and persona."},
            {"question": "Q8. Chain of Thought prompting means:", "options": ["A) Linear step-by-step reasoning", "B) Multiple branches", "C) No reasoning", "D) Masking output"], "answer": "a", "explanation": "Chain of Thought (CoT) prompting encourages the model to generate a linear, step-by-step reasoning process before providing the final answer."},
            {"question": "Q9. Tree of Thoughts prompting means:", "options": ["A) Exploring multiple reasoning paths", "B) Always deterministic", "C) Faster computation", "D) Using only 1 example"], "answer": "a", "explanation": "Tree of Thoughts (ToT) is an advanced prompting technique that explores multiple reasoning paths and evaluates them, similar to a tree-based search."},
            {"question": "Q10. Asking “Think step by step” is:", "options": ["A) Chain of Thought", "B) Tree of Thoughts", "C) Guardrails", "D) Few-shot"], "answer": "a", "explanation": "The phrase “Think step by step” is a common way to invoke Chain of Thought prompting, which encourages the model to show its reasoning."},
            {"question": "Q11. Weakness of Chain of Thought:", "options": ["A) Consumes more tokens", "B) Works only for code", "C) Not reproducible", "D) Requires fine-tuning"], "answer": "a", "explanation": "Generating the intermediate reasoning steps in Chain of Thought prompting can significantly increase the number of tokens used, leading to higher costs and latency."},
            {"question": "Q12. Tree of Thoughts is useful for:", "options": ["A) Complex multi-solution tasks", "B) Simple binary outputs", "C) Sentiment classification", "D) Token pruning"], "answer": "a", "explanation": "Tree of Thoughts is particularly effective for complex tasks that may have multiple possible solutions or require extensive reasoning, such as creative problem-solving or game-playing."},
            {"question": "Q13. Prompt leakage is when:", "options": ["A) Model reveals system prompts", "B) Top-p is high", "C) Temperature is 0", "D) Chain of Thought is used"], "answer": "a", "explanation": "Prompt leakage occurs when a user's input tricks the model into revealing its internal system instructions or other hidden information."},
            {"question": "Q14. Safe system messages use:", "options": ["A) Role-based instructions", "B) Credentials inside prompt", "C) Unclear wording", "D) Random tokens"], "answer": "a", "explanation": "Using clear, role-based instructions in system messages helps prevent prompt injection and ensures the model adheres to its intended purpose."},
            {"question": "Q15. Few-shot prompting means:", "options": ["A) Provide several examples", "B) Provide zero examples", "C) Provide random instructions", "D) Provide guardrails"], "answer": "a", "explanation": "Few-shot prompting involves providing a few examples of input-output pairs to guide the model's behavior for a specific task."},
            {"question": "Q16. Zero-shot prompting is best when:", "options": ["A) Clear task with no examples", "B) Many examples", "C) Fine-tuned model", "D) Context hidden"], "answer": "a", "explanation": "Zero-shot prompting is used when the model is given a task without any examples, relying on its pre-trained knowledge to understand and complete the request."},
            {"question": "Q17. Most deterministic setup:", "options": ["A) Temp=0, Top-k=1", "B) Temp=1, Top-k=10", "C) Temp=2, Top-p=1", "D) Temp high, Top-k=5"], "answer": "a", "explanation": "The most deterministic setup is a temperature of 0 and a top-k of 1, which forces the model to always choose the single most probable token."},
            {"question": "Q18. “Let’s break this down” is:", "options": ["A) Chain of Thought", "B) Tree of Thoughts", "C) Few-shot", "D) Guardrails"], "answer": "a", "explanation": "Similar to “Think step by step,” the phrase “Let’s break this down” is a common prompt to trigger a Chain of Thought reasoning process."},
            {"question": "Q19. Preventing harmful completions:", "options": ["A) Guardrails", "B) High temperature", "C) Random prompts", "D) Top-p=1"], "answer": "a", "explanation": "Guardrails are a set of rules and mechanisms used to prevent a model from generating harmful, unsafe, or undesirable content."},
            {"question": "Q20. Tree of Thoughts can be improved by:", "options": ["A) Branching and pruning", "B) Limiting reasoning", "C) Setting Top-k=1", "D) Avoiding randomness"], "answer": "a", "explanation": "Tree of Thoughts is improved by allowing the model to explore multiple branching paths and then 'pruning' or discarding less promising ones to find the optimal solution."},

            # Topic 2: Markdown
            {"question": "Q21. Which syntax makes a clickable image with tooltip?", "options": ["A) [![alt](img 'tip')](link)", "B) ![alt](img)", "C) <img src='img'>", "D) [alt](img 'tip')"], "answer": "a", "explanation": "The syntax combines a standard image tag `![alt](img 'tip')` inside a link tag `[...](link)`, creating a clickable image with a tooltip."},
            {"question": "Q22. To create a numbered list:", "options": ["A) 1. Item", "B) - Item", "C) * Item", "D) # Item"], "answer": "a", "explanation": "Numbered lists in Markdown are created by starting each line with a number followed by a period and a space."},
            {"question": "Q23. For bullets, you use:", "options": ["A) - or *", "B) #", "C) >", "D) ---"], "answer": "a", "explanation": "Unordered lists (bullet points) can be created using a hyphen (`-`) or an asterisk (`*`) at the beginning of each line."},
            {"question": "Q24. Markdown for bold text:", "options": ["A) **bold**", "B) _bold_", "C) ~~bold~~", "D) [bold]"], "answer": "a", "explanation": "Bold text is created by wrapping the text in two asterisks on each side, like `**bold**`."},
            {"question": "Q25. Markdown for italic text:", "options": ["A) *italic*", "B) **italic**", "C) ~~italic~~", "D) ==italic=="], "answer": "a", "explanation": "Italic text is created by wrapping the text in a single asterisk on each side, like `*italic*`."},
            {"question": "Q26. Code block syntax:", "options": ["A) ```python ... ```", "B) <code> ... </code>", "C) (code)", "D) [[code]]"], "answer": "a", "explanation": "Code blocks are created using three backticks (```) followed by the language name, and ending with three backticks on a new line."},
            {"question": "Q27. Inline code uses:", "options": ["A) `code`", "B) [code]", "C) (code)", "D) *code*"], "answer": "a", "explanation": "Inline code is created by wrapping the code snippet in a single backtick (`code`)."},
            {"question": "Q28. Headings use:", "options": ["A) #", "B) *", "C) >", "D) --"], "answer": "a", "explanation": "Headings are created by using one to six hash symbols (`#`) at the beginning of a line."},
            {"question": "Q29. Blockquotes use:", "options": ["A) >", "B) #", "C) *", "D) ~"], "answer": "a", "explanation": "Blockquotes are created by placing a greater-than sign (`>`) at the beginning of a line."},
            {"question": "Q30. Horizontal rule is made with:", "options": ["A) ---", "B) ***", "C) ===", "D) ..."], "answer": "a", "explanation": "Horizontal rules can be created using three or more hyphens (`---`) or asterisks (`***`). Both A and B are correct, but `---` is the most common."},
            {"question": "Q31. Image without link:", "options": ["A) ![alt](url)", "B) [alt](url)", "C) <url>", "D) img(url)"], "answer": "a", "explanation": "The syntax for an image is an exclamation mark, followed by alt text in brackets, and the image URL in parentheses."},
            {"question": "Q32. Link syntax:", "options": ["A) [text](url)", "B) !(url)", "C) <link>", "D) {text}(url)"], "answer": "a", "explanation": "Links are created with the link text in brackets and the URL in parentheses."},
            {"question": "Q33. Nested list requires:", "options": ["A) Indentation", "B) Blockquotes", "C) Multiple #", "D) ~"], "answer": "a", "explanation": "Nested lists are created by indenting the list item with four spaces or a tab."},
            {"question": "Q34. Table alignment is set with:", "options": ["A) :---:", "B) -><-", "C) ^^", "D) //"], "answer": "a", "explanation": "Table column alignment is set in the header row's separator line using colons. `| :--- |` for left, `| ---: |` for right, and `| :---: |` for center."},
            {"question": "Q35. Strikethrough syntax:", "options": ["A) ~~text~~", "B) --text--", "C) __text__", "D) ==text=="], "answer": "a", "explanation": "Strikethrough text is created by wrapping the text in two tildes on each side, like `~~text~~`."},
            {"question": "Q36. Task list checkbox:", "options": ["A) - [ ]", "B) * [ ]", "C) # [ ]", "D) + [ ]"], "answer": "a", "explanation": "Task lists are created using a list item marker followed by a space, then square brackets, which can contain a space for an unchecked box or 'x' for a checked one."},
            {"question": "Q37. Footnotes use:", "options": ["A) [^1]", "B) [1]", "C) (1)", "D) [[1]]"], "answer": "a", "explanation": "Footnotes are created by a caret and an identifier in brackets, like `[^1]`, and the footnote definition is placed elsewhere in the document."},
            {"question": "Q38. Escaping a special character:", "options": ["A) \\*word\\*", "B) **word**", "C) [word]", "D) /word/"], "answer": "a", "explanation": "To display a special Markdown character as a literal character, you can use a backslash (`\\`) before it to escape it."},
            {"question": "Q39. Definition list in extended Markdown:", "options": ["A) Term : Definition", "B) Term = Definition", "C) Term -> Definition", "D) Term [Definition]"], "answer": "a", "explanation": "In some extended Markdown flavors, a definition list can be created with the term on one line and the definition indented on the next, with a colon (`:`)."},
            {"question": "Q40. HTML inside Markdown:", "options": ["A) Allowed", "B) Forbidden", "C) Causes errors", "D) Converts to code"], "answer": "a", "explanation": "Markdown is designed to be a superset of HTML, meaning you can embed raw HTML tags directly within a Markdown document."},

            # Topic 3: Pydantic
            {"question": "Q41. BaseModel provides:", "options": ["A) Type validation", "B) No schema support", "C) Only serialization", "D) Faster than dataclass"], "answer": "a", "explanation": "Pydantic's `BaseModel` uses Python type hints to enforce data validation at runtime, ensuring that the data conforms to the defined schema."},
            {"question": "Q42. Python built-in dataclasses lack:", "options": ["A) Validation", "B) Type hints", "C) Fields", "D) Default values"], "answer": "a", "explanation": "While Python's built-in dataclasses use type hints, they do not perform runtime validation. Pydantic adds this crucial feature."},
            {"question": "Q43. @pydantic.dataclasses.dataclass adds:", "options": ["A) Validation to dataclasses", "B) Nothing new", "C) Serialization only", "D) Faster runtime"], "answer": "a", "explanation": "The `@pydantic.dataclasses.dataclass` decorator adds Pydantic's validation capabilities to a standard Python dataclass."},
            {"question": "Q44. Which can be output_type in agents?", "options": ["A) BaseModel", "B) Pydantic dataclass", "C) Plain dict", "D) List"], "answer": "a", "explanation": "In the context of agent frameworks, Pydantic's `BaseModel` is the preferred `output_type` because it provides strict schema validation and error handling for the model's output."},
            {"question": "Q45. Advantage of BaseModel:", "options": ["A) Schema generation", "B) Ignores types", "C) No validation", "D) Simpler"], "answer": "a", "explanation": "Pydantic can automatically generate a JSON Schema from a `BaseModel` class, which is useful for API documentation and data validation."},
            {"question": "Q46. Pydantic validates against:", "options": ["A) Type hints", "B) JSON only", "C) Tokens", "D) Schema-less data"], "answer": "a", "explanation": "Pydantic uses Python's standard type hints to define the data schema and validates input data against these hints."},
            {"question": "Q47. Wrong data type in BaseModel causes:", "options": ["A) ValidationError", "B) Ignore", "C) Crash silently", "D) Return None"], "answer": "a", "explanation": "If the input data does not match the type hints defined in the `BaseModel`, Pydantic will raise a `ValidationError`."},
            {"question": "Q48. For strict schema enforcement:", "options": ["A) Use output_type=BaseModel", "B) Use plain dataclass", "C) Use dicts", "D) No schema"], "answer": "a", "explanation": "Using `output_type=BaseModel` in an agent or function call ensures that the model's output is strictly validated against the defined Pydantic schema."},
            {"question": "Q49. Converting BaseModel to dict:", "options": ["A) .dict()", "B) .to_json()", "C) .convert()", "D) .to_dict()"], "answer": "a", "explanation": "The `.dict()` method on a Pydantic `BaseModel` instance converts the model and its data into a standard Python dictionary."},
            {"question": "Q50. For JSON output:", "options": ["A) .json()", "B) .dict()", "C) .export()", "D) .dump()"], "answer": "a", "explanation": "The `.json()` method serializes the `BaseModel` instance into a JSON string."},
            {"question": "Q51. Nested models in Pydantic are:", "options": ["A) Supported", "B) Forbidden", "C) Require plugins", "D) Convert to strings"], "answer": "a", "explanation": "Pydantic fully supports nested models, allowing you to define complex data structures by embedding one `BaseModel` within another."},
            {"question": "Q52. Fields with defaults declared using:", "options": ["A) = value", "B) .default()", "C) field=value", "D) declare()"], "answer": "a", "explanation": "Default values for a field are simply assigned using the equals sign, e.g., `name: str = 'John'`."},
            {"question": "Q53. Field metadata in Pydantic:", "options": ["A) Field()", "B) Meta()", "C) Info()", "D) Config()"], "answer": "a", "explanation": "The `Field()` function is used to add extra metadata and validation constraints to a field, such as `min_length` or `alias`."},
            {"question": "Q54. To enforce string length:", "options": ["A) Field(min_length=3)", "B) Validate()", "C) Limit()", "D) Meta()"], "answer": "a", "explanation": "You can use `Field()` with `min_length` and `max_length` to enforce specific string length constraints."},
            {"question": "Q55. Alias in schema:", "options": ["A) Field(..., alias='name')", "B) Rename()", "C) Meta()", "D) Alt()"], "answer": "a", "explanation": "The `alias` parameter in `Field()` allows you to map a field name in the schema to a different variable name in the Python class."},
            {"question": "Q56. Pydantic dataclasses differ from Python’s by:", "options": ["A) Adding runtime validation", "B) Using fewer imports", "C) Ignoring defaults", "D) No schema"], "answer": "a", "explanation": "Pydantic's dataclasses extend Python's built-in dataclasses by adding runtime data validation."},
            {"question": "Q57. Schema export format:", "options": ["A) JSON", "B) YAML only", "C) HTML", "D) CSV"], "answer": "a", "explanation": "Pydantic models can be easily converted into a JSON Schema using the `.schema()` or `.model_json_schema()` method."},
            {"question": "Q58. Pydantic’s strict mode ensures:", "options": ["A) No type coercion", "B) Faster performance", "C) Skips validation", "D) Converts to strings"], "answer": "a", "explanation": "In strict mode, Pydantic will not perform type coercion (e.g., converting a string '1' to an integer 1) and will raise a `ValidationError`."},
            {"question": "Q59. Config class in BaseModel controls:", "options": ["A) Model behavior", "B) Token usage", "C) Agents SDK hooks", "D) Markdown rendering"], "answer": "a", "explanation": "A nested `Config` class within a `BaseModel` is used to configure the model's behavior, such as ignoring extra fields or setting strict mode."},
            {"question": "Q60. Validation occurs:", "options": ["A) At instantiation", "B) After execution", "C) Before imports", "D) Never"], "answer": "a", "explanation": "Validation happens automatically when you create a new instance of a `BaseModel`, ensuring the data is correct from the start."},

            # Topic 4: OpenAI Agents SDK
            {"question": "Q61. Agents SDK default:", "options": ["A) Handles dynamic context", "B) Requires handoff", "C) Runs only sync", "D) No tool support"], "answer": "a", "explanation": "The OpenAI Agents SDK is designed to handle dynamic context and conversation flows, making it a powerful framework for building conversational agents."},
            {"question": "Q62. Handoff means:", "options": ["A) Passing to another agent", "B) Dropping tools", "C) Stopping run", "D) Restarting"], "answer": "a", "explanation": "Handoff is the process of transferring control of a conversation from one agent to another, often based on a change in user intent or task."},
            {"question": "Q63. Handoff parameters include:", "options": ["A) Target agent", "B) Error logs", "C) Token limit", "D) Prompt cache"], "answer": "a", "explanation": "When performing a handoff, you must specify the `target_agent` to which the conversation will be passed."},
            {"question": "Q64. Guardrails prevent:", "options": ["A) Unsafe outputs", "B) Token overflow", "C) Latency", "D) Tracing errors"], "answer": "a", "explanation": "Guardrails are a key feature of the Agents SDK used to prevent the model from generating unsafe or inappropriate content, ensuring compliance with safety policies."},
            {"question": "Q65. Guardrail tripwires trigger:", "options": ["A) Pre/post execution", "B) Tokenization", "C) Logging", "D) Schema"], "answer": "a", "explanation": "Guardrail tripwires are conditions or events that can be set to trigger actions both before and after a model's execution, allowing for real-time safety checks."},
            {"question": "Q66. Traces represent:", "options": ["A) Full run", "B) One span", "C) Error only", "D) Tool call"], "answer": "a", "explanation": "A trace in the Agents SDK is a complete record of a single run, including all the steps, tool calls, and model outputs."},
            {"question": "Q67. Span represents:", "options": ["A) Substep of trace", "B) Whole run", "C) Context object", "D) Guardrail"], "answer": "a", "explanation": "A span is a smaller, individual substep within a larger trace, such as a single tool call or a model generation step."},
            {"question": "Q68. Hooks modify:", "options": ["A) Behavior during execution", "B) Tracing schema", "C) Temperature", "D) Markdown"], "answer": "a", "explanation": "Hooks are custom functions that can be registered to modify an agent's behavior at specific points during its execution, such as before or after a tool call."},
            {"question": "Q69. RunHooks apply to:", "options": ["A) Individual run", "B) Global agent", "C) All sessions", "D) Tools only"], "answer": "a", "explanation": "RunHooks are temporary and apply only to a single execution of an agent."},
            {"question": "Q70. AgentHooks apply to:", "options": ["A) Whole agent lifecycle", "B) Only one run", "C) Markdown rendering", "D) Guardrails"], "answer": "a", "explanation": "AgentHooks are persistent and are registered to apply to an agent's entire lifecycle, affecting all future runs."},
            {"question": "Q71. MaxTurnsExceeded error:", "options": ["A) Too many conversation turns", "B) Guardrail failed", "C) Schema error", "D) Tool timeout"], "answer": "a", "explanation": "The `MaxTurnsExceeded` error is raised when a conversation or agent run exceeds the predefined maximum number of turns, preventing infinite loops."},
            {"question": "Q72. ModelBehaviorError is raised when:", "options": ["A) Model deviates unexpectedly", "B) Tokens exceed", "C) Runner stops", "D) Hooks fail"], "answer": "a", "explanation": "A `ModelBehaviorError` is an exception raised when the model's response deviates from the expected behavior, such as not following instructions or providing an invalid format."},
            {"question": "Q73. To run in streaming mode:", "options": ["A) run_streamed()", "B) run()", "C) run_sync()", "D) run_async()"], "answer": "a", "explanation": "The `run_streamed()` method is used to run an agent in a streaming fashion, providing real-time output as the model generates it."},
            {"question": "Q74. run_sync() is used for:", "options": ["A) Blocking synchronous runs", "B) Streaming", "C) Multi-agent runs", "D) Tracing"], "answer": "a", "explanation": "The `run_sync()` method provides a blocking, synchronous execution of an agent, which is useful for simpler scripts and debugging."},
            {"question": "Q75. run() is used for:", "options": ["A) Async execution", "B) Always sync", "C) Guardrails", "D) Tracing only"], "answer": "a", "explanation": "The standard `run()` method is an asynchronous function that should be used with `await` for non-blocking execution in an async environment."},
            {"question": "Q76. ModelSettings resolve() does:", "options": ["A) Resolve model config", "B) Debug runs", "C) Handle tool calls", "D) Apply hooks"], "answer": "a", "explanation": "The `resolve()` method on `ModelSettings` is used to finalize and resolve the model's configuration before a run, including any overrides."},
            {"question": "Q77. If output violates schema:", "options": ["A) ValidationError", "B) Silent fail", "C) Auto-correct", "D) Retry infinitely"], "answer": "a", "explanation": "If an agent's output does not conform to the specified `output_type` schema (e.g., a Pydantic `BaseModel`), a `ValidationError` will be raised."},
            {"question": "Q78. Best practice for tool call errors:", "options": ["A) Handle via callbacks", "B) Ignore", "C) Restart", "D) Fail run"], "answer": "a", "explanation": "The best practice is to handle tool call errors using callbacks or hooks that can intercept the error and provide a graceful response or recovery mechanism."},
            {"question": "Q79. Context object provides:", "options": ["A) Dynamic info for runs", "B) Temperature config", "C) Markdown tables", "D) Guardrail tracing"], "answer": "a", "explanation": "The `Context` object provides dynamic, run-specific information that can be accessed by tools and hooks during the execution of an agent."},
            {"question": "Q80. Multi-run tracing helps:", "options": ["A) Tracking related runs together", "B) Reducing latency", "C) Preventing schema errors", "D) Handling hooks"], "answer": "a", "explanation": "Multi-run tracing allows developers to track and analyze a series of related agent runs as a single logical unit, which is useful for complex workflows and debugging."}
        ]
        return questions

    def create_welcome_screen(self):
        st.title("Welcome to the AI & Python Quiz! 🤖🐍")
        st.markdown(
            """
            This quiz covers key concepts in **Prompt Engineering**, **Markdown**, 
            **Pydantic**, and the **OpenAI Agents SDK**.
            
            **Instructions:**
            1.  The quiz has 4 sections of 20 questions each, for a total of 80 questions.
            2.  Click on the correct option for each question.
            3.  You can navigate between questions within each section.
            4.  Your progress and score will be tracked as you go.
            5.  Good luck! ✨
            """
        )
        if st.button("Start Quiz"):
            st.session_state.quiz_started = True
            st.session_state.current_section = 0
            st.rerun()
    
    def show_question(self):
        # Determine current section (0=1-20, 1=21-40, etc.)
        section_start = st.session_state.current_section * 20
        section_end = section_start + 19
        
        # Get current question data
        question_idx = st.session_state.shuffled_indices[st.session_state.current_question]
        question_data = st.session_state.questions[question_idx]
        
        st.title(f"Section {st.session_state.current_section + 1}: Questions {section_start + 1}-{section_end + 1}")
        st.subheader(f"Question {st.session_state.current_question + 1} of {len(st.session_state.questions)}")
        st.markdown(f"**{question_data['question']}**")
        
        # Display options as radio buttons
        selected = st.radio(
            "Select your answer:",
            question_data["options"],
            index=None,
            key=f"question_{st.session_state.current_question}"
        )
        
        st.session_state.selected_option = selected
        
        col1, col2, col3 = st.columns([1,1,1])
        
        # Navigation buttons
        if st.session_state.current_question > section_start:
            if col1.button("Previous"):
                self.prev_question()
        
        if st.session_state.current_question < section_end:
            if col2.button("Next"):
                self.next_question()
        else:
            if col2.button("Submit Section"):
                self.next_question()
        
        if col3.button("Quit"):
            st.session_state.quiz_started = False
            st.rerun()
    
    def prev_question(self):
        if st.session_state.current_question > 0:
            st.session_state.current_question -= 1
            st.rerun()
    
    def next_question(self):
        if st.session_state.selected_option is None:
            st.warning("Please select an answer!")
            return
        
        # Get the selected option letter (a, b, c, etc.)
        selected_answer = None
        question_data = st.session_state.questions[
            st.session_state.shuffled_indices[st.session_state.current_question]
        ]
        
        for opt in question_data["options"]:
            if st.session_state.selected_option == opt:
                selected_answer = opt[0].lower()
                break
        
        # Check answer and store result
        is_correct = (selected_answer == question_data["answer"])
        st.session_state.user_answers.append({
            "question": question_data["question"],
            "user_answer": selected_answer,
            "correct_answer": question_data["answer"],
            "is_correct": is_correct,
            "explanation": question_data["explanation"]
        })
        
        if is_correct:
            st.session_state.score += 1
        
        # Move to next question or show results
        section_end = (st.session_state.current_section * 20) + 19
        if st.session_state.current_question < section_end:
            st.session_state.current_question += 1
            st.session_state.selected_option = None
            st.rerun()
        else:
            self.show_section_results()
    
    def show_section_results(self):
        st.title(f"Section {st.session_state.current_section + 1} Results")
        
        # Calculate section score
        section_start = st.session_state.current_section * 20
        section_end = section_start + 19
        section_answers = st.session_state.user_answers[section_start:section_end + 1]
        section_score = sum(1 for ans in section_answers if ans["is_correct"])
        
        st.subheader(f"Your score: {section_score}/20 ({section_score * 5}%)")
        
        # Detailed feedback
        st.subheader("Detailed Feedback:")
        
        for i, answer in enumerate(section_answers, start=section_start + 1):
            with st.expander(f"Question {i}: {answer['question']}"):
                if answer['is_correct']:
                    st.success("✅ Your answer: CORRECT")
                else:
                    st.error("❌ Your answer: INCORRECT")
                    st.write(f"You selected: {answer['user_answer'].upper()}")
                    st.write(f"Correct answer: {answer['correct_answer'].upper()}")
                
                st.write(f"**Explanation:** {answer['explanation']}")
        
        # Move to next section or final results
        if st.session_state.current_section < 3:  # 4 sections (0-3)
            if st.button("Continue to Next Section"):
                st.session_state.current_section += 1
                st.session_state.current_question = st.session_state.current_section * 20
                st.session_state.selected_option = None
                st.rerun()
        else:
            self.show_final_results()
    
    def show_final_results(self):
        st.title("Quiz Completed! 🎉")
        
        # Calculate final score
        final_score = st.session_state.score
        total_questions = len(st.session_state.questions)
        score_percent = (final_score / total_questions) * 100
        
        st.subheader(f"Final Score: {final_score}/{total_questions} ({score_percent:.1f}%)")
        
        # Section breakdown
        st.subheader("Section Performance:")
        cols = st.columns(4)
        for i in range(4):
            section_start = i * 20
            section_end = section_start + 19
            section_answers = st.session_state.user_answers[section_start:section_end + 1]
            section_score = sum(1 for ans in section_answers if ans["is_correct"])
            
            cols[i].metric(
                label=f"Section {i+1}",
                value=f"{section_score}/20",
                delta=f"{section_score / 20 * 100:.1f}%"
            )
        
        # Restart or quit buttons
        col1, col2 = st.columns([1,1])
        
        if col1.button("Restart Quiz"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.user_answers = []
            st.session_state.selected_option = None
            st.session_state.current_section = 0
            random.shuffle(st.session_state.shuffled_indices)
            st.rerun()
        
        if col2.button("Quit"):
            st.session_state.quiz_started = False
            st.rerun()

# Run the app
if __name__ == "__main__":
    app = PythonQuizApp()