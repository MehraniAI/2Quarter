import streamlit as st
import random
import time

st.markdown('<h1 style="color:blue">🤖Prepared by Devan Das Mehrani AI Student</h1>', unsafe_allow_html=True)

class OpenAIQuizApp:
    def __init__(self):
        self.questions = self.load_questions()
        if 'quiz_started' not in st.session_state:
            self.initialize_session_state()

    def initialize_session_state(self):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.user_answers = {}
        self.questions_keys = list(self.questions.keys())
        random.shuffle(self.questions_keys)
        st.session_state.shuffled_question_keys = self.questions_keys
        st.session_state.quiz_started = False
        st.session_state.quiz_completed = False
        st.session_state.time_per_question = 60
        st.session_state.start_time = time.time()
        st.session_state.submitted = False

    def load_questions(self):
        questions = {
            "101": {"question": "Which feature of the SDK helps display partial outputs while the agent is still working?", "options": ["a) Handoffs", "b) Streaming", "c) Tracing", "d) Orchestration"], "answer": "b"},
            "102": {"question": "What does tracing mainly capture?", "options": ["a) Network latency", "b) The agent’s reasoning and tool calls", "c) User typing speed", "d) Token embeddings"], "answer": "b"},
            "103": {"question": "A tool in the Agents SDK can be best described as:", "options": ["a) An agent replacement", "b) An external capability the agent can call", "c) A memory cache", "d) A streaming buffer"], "answer": "b"},
            "104": {"question": "When should handoffs be used?", "options": ["a) When one agent needs another to handle a task better", "b) When streaming fails", "c) When tokens exceed the limit", "d) When tracing is disabled"], "answer": "a"},
            "105": {"question": "Multi-agent orchestration reduces what risk?", "options": ["a) One agent handling tasks outside its specialization", "b) Token count", "c) Streaming lag", "d) GitHub syncing errors"], "answer": "a"},
            "106": {"question": "Streaming improves the user experience by:", "options": ["a) Delivering partial results in real-time", "b) Lowering API quota", "c) Storing logs", "d) Running multiple agents"], "answer": "a"},
            "107": {"question": "Which of the following is NOT part of tracing?", "options": ["a) Monitoring tool calls", "b) Inspecting agent steps", "c) Debugging errors", "d) Token streaming speed"], "answer": "d"},
            "108": {"question": "A weather-check API would be an example of:", "options": ["a) A handoff", "b) A tool", "c) A tracer", "d) A stream"], "answer": "b"},
            "109": {"question": "Which agent feature passes control to another agent?", "options": ["a) Streaming", "b) Handoffs", "c) Tracing", "d) Tooling"], "answer": "b"},
            "110": {"question": "Multi-agent orchestration is required when:", "options": ["a) Tasks require collaboration between specialized agents", "b) Only one agent is running", "c) Tools are unavailable", "d) Streaming is disabled"], "answer": "a"},
            "111": {"question": "Which SDK docs cover streaming?", "options": ["a) /tools/", "b) /handoffs/", "c) /multi_agent/", "d) /streaming/"], "answer": "d"},
            "112": {"question": "Which SDK docs cover tracing?", "options": ["a) /tracing/", "b) /tools/", "c) /handoffs/", "d) /multi_agent/"], "answer": "a"},
            "113": {"question": "Which SDK docs cover tools?", "options": ["a) /tools/", "b) /streaming/", "c) /handoffs/", "d) /tracing/"], "answer": "a"},
            "114": {"question": "Which SDK docs cover handoffs?", "options": ["a) /handoffs/", "b) /tools/", "c) /multi_agent/", "d) /streaming/"], "answer": "a"},
            "115": {"question": "Which SDK docs cover multi-agent orchestration?", "options": ["a) /multi_agent/", "b) /tracing/", "c) /handoffs/", "d) /tools/"], "answer": "a"},
            "116": {"question": "Streaming is especially helpful in:", "options": ["a) Real-time conversations and chats", "b) Offline debugging", "c) Batch processing", "d) Static file storage"], "answer": "a"},
            "117": {"question": "Tracing helps detect:", "options": ["a) Hidden errors in reasoning or tool calls", "b) Token streaming delays", "c) API quota resets", "d) Data corruption"], "answer": "a"},
            "118": {"question": "Which feature lets agents “borrow skills” from external resources?", "options": ["a) Tools", "b) Handoffs", "c) Streaming", "d) Tracing"], "answer": "a"},
            "119": {"question": "Handoffs prevent:", "options": ["a) Overloading one agent with all tasks", "b) Streaming delays", "c) Tracing failures", "d) Token price increases"], "answer": "a"},
            "120": {"question": "Multi-agent orchestration is most similar to:", "options": ["a) A team project with role-based collaboration", "b) A single student writing an essay", "c) A static website", "d) A file download"], "answer": "a"},
            "121": {"question": "The main focus of streaming events is:", "options": ["a) Live, incremental delivery", "b) Debugging only", "c) Tool chaining", "d) Multi-agent delegation"], "answer": "a"},
            "122": {"question": "Tracing is usually turned on by:", "options": ["a) Developers for monitoring and debugging", "b) Users for speed", "c) Hardware vendors", "d) Token accountants"], "answer": "a"},
            "123": {"question": "A calculator function connected to an agent is a:", "options": ["a) Tool", "b) Handoff", "c) Tracer", "d) Stream"], "answer": "a"},
            "124": {"question": "A helpdesk chatbot handing off to a billing chatbot is an example of:", "options": ["a) Handoffs", "b) Streaming", "c) Tracing", "d) Tools"], "answer": "a"},
            "125": {"question": "Multi-agent orchestration works by:", "options": ["a) Coordinating multiple specialized agents together", "b) Making one agent run faster", "c) Replacing tools", "d) Extending memory"], "answer": "a"},
            "126": {"question": "Which GitHub resource explains tracing?", "options": ["a) 14_tracing", "b) 08_tools", "c) 11_handoffs", "d) 07_streaming"], "answer": "a"},
            "127": {"question": "Which GitHub resource explains streaming?", "options": ["a) 07_streaming", "b) 14_tracing", "c) 08_tools", "d) 11_handoffs"], "answer": "a"},
            "128": {"question": "Which GitHub resource explains tools?", "options": ["a) 08_tools", "b) 07_streaming", "c) 11_handoffs", "d) 14_tracing"], "answer": "a"},
            "129": {"question": "Which GitHub resource explains handoffs?", "options": ["a) 11_handoffs", "b) 08_tools", "c) 07_streaming", "d) 14_tracing"], "answer": "a"},
            "130": {"question": "Orchestration GitHub resource is found in:", "options": ["a) multi_agent folder", "b) handoffs folder", "c) tracing folder", "d) streaming folder"], "answer": "a"},
            "131": {"question": "Streaming gives users the feeling of:", "options": ["a) Real-time conversation", "b) Batch reports", "c) Static documents", "d) Delayed replies"], "answer": "a"},
            "132": {"question": "Which feature allows deeper insight into what went wrong in an agent?", "options": ["a) Tracing", "b) Streaming", "c) Handoffs", "d) Orchestration"], "answer": "a"},
            "133": {"question": "Tools are usually built for:", "options": ["a) Domain-specific tasks like math, APIs, or databases", "b) Storing logs", "c) Generating embeddings", "d) Saving prompts"], "answer": "a"},
            "134": {"question": "Handoffs improve:", "options": ["a) Specialization of agents", "b) Token compression", "c) API quota expansion", "d) Database storage"], "answer": "a"},
            "135": {"question": "Orchestration enables:", "options": ["a) Division of labor among agents", "b) Streaming speed boosts", "c) Token count reduction", "d) Debugging"], "answer": "a"},
            "136": {"question": "Streaming reduces the waiting time for:", "options": ["a) Final outputs in long responses", "b) Tool execution", "c) Token billing", "d) Debug tracing"], "answer": "a"},
            "137": {"question": "Tracing outputs are mostly used by:", "options": ["a) Developers", "b) End-users", "c) Database admins", "d) API vendors"], "answer": "a"},
            "138": {"question": "Tools make agents more:", "options": ["a) Actionable and capable", "b) Expensive", "c) Slower", "d) Dependent"], "answer": "a"},
            "139": {"question": "Handoffs often require:", "options": ["a) Context transfer", "b) API key resets", "c) Model fine-tuning", "d) Hardware upgrade"], "answer": "a"},
            "140": {"question": "Multi-agent orchestration can involve:", "options": ["a) Planning, execution, and delegation", "b) Token counting only", "c) Tool storage", "d) Prompt replacement"], "answer": "a"},
            "141": {"question": "Streaming’s biggest advantage for long outputs is:", "options": ["a) Users see answers as they are generated", "b) Debug logs are stored", "c) Multi-agent syncs faster", "d) Tokens are cheaper"], "answer": "a"},
            "142": {"question": "Tracing is best for:", "options": ["a) Improving agent reliability", "b) Reducing latency", "c) Managing handoffs", "d) Enabling offline use"], "answer": "a"},
            "143": {"question": "Tools extend the agent’s:", "options": ["a) Functionality", "b) Token count", "c) Context window", "d) Prompt history"], "answer": "a"},
            "144": {"question": "Handoffs are like:", "options": ["a) Passing a baton in a relay race", "b) Typing faster", "c) Debugging a program", "d) Copy-pasting text"], "answer": "a"},
            "145": {"question": "Multi-agent orchestration mirrors:", "options": ["a) Human teamwork in solving tasks", "b) Token optimization only", "c) Hardware parallelism", "d) Static analysis"], "answer": "a"},
            "146": {"question": "Streaming is tied to which UX principle?", "options": ["a) Responsiveness", "b) Persistence", "c) Security", "d) Memory"], "answer": "a"},
            "147": {"question": "Tracing is tied to which developer principle?", "options": ["a) Observability", "b) Responsiveness", "c) Security", "d) Speed"], "answer": "a"},
            "148": {"question": "Tools are tied to which software design principle?", "options": ["a) Extensibility", "b) Redundancy", "c) Security", "d) Compression"], "answer": "a"},
            "149": {"question": "Handoffs are tied to which workflow principle?", "options": ["a) Delegation", "b) Persistence", "c) Latency", "d) Storage"], "answer": "a"},
            "150": {"question": "Multi-agent orchestration is tied to which systems principle?", "options": ["a) Collaboration and coordination", "b) Memory persistence", "c) Security and authentication", "d) Compression"], "answer": "a"},
            "151": {"question": "In OpenAI Agents SDK, what does event streaming provide developers?", "options": ["a) Token counts only", "b) Continuous updates during execution", "c) Cheaper models", "d) Faster tracing"], "answer": "b"},
            "152": {"question": "Which is an example use-case of tracing?", "options": ["a) Debugging why a tool call failed", "b) Making agents stream faster", "c) Creating multi-agent teams", "d) Reducing internet bandwidth"], "answer": "a"},
            "153": {"question": "Which of the following is NOT typically considered a tool in the SDK?", "options": ["a) A weather API", "b) A database query function", "c) A math calculation helper", "d) A tracing dashboard"], "answer": "d"},
            "154": {"question": "What happens during a handoff?", "options": ["a) The user prompt is deleted", "b) The current agent assigns a task to another agent", "c) Streaming restarts", "d) The session ends"], "answer": "b"},
            "155": {"question": "Multi-agent orchestration is most useful when tasks are:", "options": ["a) Simple and linear", "b) Large and multi-disciplinary", "c) Already solved by one agent", "d) Only about tracing"], "answer": "b"},
            "156": {"question": "A benefit of streaming events is:", "options": ["a) Immediate feedback loop for user interactions", "b) Permanent storage of agent outputs", "c) Cheaper server hosting", "d) Offline capability"], "answer": "a"},
            "157": {"question": "Tracing in the SDK provides visibility into:", "options": ["a) Agent memory leaks", "b) Step-by-step decision making and tool calls", "c) Token price per month", "d) GitHub repository syncing"], "answer": "b"},
            "158": {"question": "Tools can be designed to:", "options": ["a) Fetch external data", "b) Perform calculations", "c) Interact with APIs", "d) All of the above"], "answer": "d"},
            "159": {"question": "Which SDK concept ensures smooth collaboration among agents?", "options": ["a) Tools", "b) Handoffs", "c) Streaming", "d) Tracing"], "answer": "b"},
            "160": {"question": "Orchestrating multiple agents is like:", "options": ["a) Assigning workers in a project team", "b) A single computer running faster", "c) Restarting a failed stream", "d) Debugging a program"], "answer": "a"},
            "161": {"question": "Streaming is particularly valuable when:", "options": ["a) Users need real-time updates in chat UIs", "b) Agents must call many tools", "c) Tracing logs are missing", "d) Orchestration fails"], "answer": "a"},
            "162": {"question": "Which component ensures developers can audit agent workflows?", "options": ["a) Streaming", "b) Handoffs", "c) Tracing", "d) Tools"], "answer": "c"},
            "163": {"question": "Handoffs reduce which problem in multi-agent setups?", "options": ["a) Duplication of effort", "b) Token cost", "c) Streaming lag", "d) API rate limits"], "answer": "a"},
            "164": {"question": "Multi-agent orchestration often combines:", "options": ["a) Generalist agents with specialist agents", "b) Streaming with tracing", "c) Tools with databases only", "d) API rate limits with queues"], "answer": "a"},
            "165": {"question": "Which assignment from the notes was related to streaming events?", "options": ["a) Explore tracing in SDK", "b) Explore tools in SDK", "c) Explore streaming in SDK", "d) Explore handoffs in SDK"], "answer": "c"},
            "166": {"question": "In tracing, developers can observe:", "options": ["a) Logs of function calls and responses", "b) Weather updates", "c) Memory cache only", "d) Token embeddings"], "answer": "a"},
            "167": {"question": "Tools allow agents to:", "options": ["a) Extend their capabilities beyond language reasoning", "b) Replace the LLM entirely", "c) Only manage handoffs", "d) Debug tracing events"], "answer": "a"},
            "168": {"question": "Which OpenAI Agents SDK feature enables division of labor between agents?", "options": ["a) Tools", "b) Streaming", "c) Handoffs", "d) Tracing"], "answer": "c"},
            "169": {"question": "Multi-agent orchestration is closely aligned with which real-world concept?", "options": ["a) Distributed teamwork", "b) Single-thread processing", "c) Batch tokenization", "d) Static programming"], "answer": "a"},
            "170": {"question": "Which GitHub resource would you use to learn handoffs?", "options": ["a) 07_streaming", "b) 11_handoffs", "c) 08_tools", "d) 14_tracing"], "answer": "b"},
            "171": {"question": "What is the main purpose of streaming in the OpenAI Agents SDK?", "options": ["a) To process events in real-time as they happen", "b) To speed up API rate limits", "c) To store agent logs permanently", "d) To create multiple agents automatically"], "answer": "a"},
            "172": {"question": "Which OpenAI Agents SDK feature helps in debugging and analyzing agent runs?", "options": ["a) Handoffs", "b) Tools", "c) Tracing", "d) Orchestration"], "answer": "c"},
            "173": {"question": "In the context of OpenAI Agents, a Tool is best described as:", "options": ["a) A new model", "b) A function or external resource an agent can call", "c) A visualization system", "d) A way to hand off tasks between agents"], "answer": "b"},
            "174": {"question": "Which SDK feature allows seamless transfer of tasks between agents?", "options": ["a) Tracing", "b) Handoffs", "c) Streaming", "d) Multi-agent orchestration"], "answer": "b"},
            "175": {"question": "Multi-agent orchestration in OpenAI SDK is mainly used for:", "options": ["a) Splitting memory storage", "b) Coordinating multiple agents to solve complex tasks", "c) Speeding up a single agent", "d) Replacing tools entirely"], "answer": "b"},
            "176": {"question": "What does streaming events mainly improve for users?", "options": ["a) Faster feedback and responsiveness", "b) Lower costs", "c) Larger context windows", "d) Permanent storage of results"], "answer": "a"},
            "177": {"question": "In tracing, which of the following is captured?", "options": ["a) Token usage only", "b) Internal agent steps and tool calls", "c) Only user prompts", "d) Only streaming output"], "answer": "b"},
            "178": {"question": "A handoff typically occurs when:", "options": ["a) One agent delegates a task to another agent", "b) A tool is loaded into memory", "c) Tracing starts running", "d) The streaming API fails"], "answer": "a"},
            "179": {"question": "Tools in OpenAI Agents SDK can include:", "options": ["a) APIs, functions, or databases", "b) Only local files", "c) Only model weights", "d) Only GitHub repositories"], "answer": "a"},
            "180": {"question": "Which official OpenAI SDK documentation would you check to study multi-agent orchestration?", "options": ["a) /streaming/", "b) /handoffs/", "c) /multi_agent/", "d) /tracing/"], "answer": "c"}
        }
        return questions

    def display_timer(self):
        remaining_time = max(0, st.session_state.time_per_question - int(time.time() - st.session_state.start_time))
        mins, secs = divmod(remaining_time, 60)
        st.markdown(f"⏱️ **Time remaining**: {mins:02d}:{secs:02d}")
        
        if remaining_time <= 0:
            st.session_state.timer_expired = True
            st.rerun()
        return remaining_time
    
    def show_welcome_screen(self):
        st.title("OpenAI Agents SDK Quiz")
        st.write("This quiz contains questions about the OpenAI Agents SDK features like Streaming, Tracing, Tools, Handoffs, and Multi-agent Orchestration.")
        if st.button("Start Quiz"):
            self.initialize_session_state()
            st.session_state.quiz_started = True
            st.rerun()

    def show_question(self):
        st.title("OpenAI Agents SDK Quiz")
        
        if "timer_expired" in st.session_state and st.session_state.timer_expired:
            self.handle_time_expired()
            return
            
        remaining_time = self.display_timer()
        
        q_index = st.session_state.current_question
        
        if q_index >= len(st.session_state.shuffled_question_keys):
            st.session_state.quiz_completed = True
            st.rerun()
            return
            
        question_key = st.session_state.shuffled_question_keys[q_index]
        question_data = self.questions[question_key]
        
        st.subheader(f"Question {q_index + 1} of {len(st.session_state.shuffled_question_keys)}")
        st.write(question_data["question"])
        
        user_choice = st.radio("Select your answer:", question_data["options"], key=f"user_choice_{question_key}")
        
        col1, col2 = st.columns(2)
        
        if col1.button("Next Question"):
            if user_choice:
                self.record_answer(question_data, user_choice)
                st.session_state.current_question += 1
                st.session_state.start_time = time.time()
                st.rerun()
            else:
                st.warning("Please select an answer to proceed.")

        if col2.button("Submit Quiz"):
            if user_choice:
                self.record_answer(question_data, user_choice)
                st.session_state.quiz_completed = True
                st.rerun()
            else:
                st.warning("Please select an answer before submitting.")

    def handle_time_expired(self):
        q_index = st.session_state.current_question
        if q_index < len(st.session_state.shuffled_question_keys):
            question_key = st.session_state.shuffled_question_keys[q_index]
            question_data = self.questions[question_key]
            self.record_answer(question_data, None)
            st.session_state.current_question += 1
        
        st.session_state.start_time = time.time()
        st.session_state.timer_expired = False
        st.rerun()

    def record_answer(self, question_data, user_choice):
        correct_answer_char = question_data["answer"]
        user_answer_char = user_choice.split(')')[0].lower() if user_choice else None
        
        is_correct = user_answer_char == correct_answer_char
        
        st.session_state.user_answers[question_data["question"]] = {
            "user_answer": user_choice,
            "is_correct": is_correct,
            "correct_answer": [opt for opt in question_data["options"] if opt.startswith(correct_answer_char)][0]
        }
        
        if is_correct:
            st.session_state.score += 1

    def show_results(self):
        st.title("Quiz Results")
        
        score_percent = (st.session_state.score / len(self.questions)) * 100
        st.subheader(f"Your score: {st.session_state.score}/{len(self.questions)} ({score_percent:.1f}%)")
        
        st.subheader("Detailed Review:")
        
        for question_text, details in st.session_state.user_answers.items():
            is_correct = details["is_correct"]
            correct_answer = details["correct_answer"]
            user_answer = details["user_answer"] if details["user_answer"] else "No answer"

            status_emoji = "✅" if is_correct else "❌"

            with st.expander(f"{status_emoji} Question: {question_text}"):
                st.markdown(f"**Your Answer:** {user_answer}")
                st.markdown(f"**Correct Answer:** {correct_answer}")
                if not is_correct:
                    st.warning("Your answer was incorrect.")
        
        if st.button("Restart Quiz"):
            self.initialize_session_state()
            st.rerun()

    def run(self):
        if not st.session_state.get('quiz_started', False):
            self.show_welcome_screen()
        elif st.session_state.get('quiz_completed', False):
            self.show_results()
        else:
            self.show_question()

# This is the entry point for the Streamlit app
if __name__ == "__main__":
    app = OpenAIQuizApp()
    app.run()