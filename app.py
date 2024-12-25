import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import Tool , initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler

#  Set up the Streamlit app
st.set_page_config(page_title="Langchain Math Problem Solver", page_icon="🧠", layout="wide")

st.title("The Math Problem Solver using Gemma 2")

groq_api_key = st.sidebar.text_input("Enter your GROQ API key", type="password")

if groq_api_key:
    llm = ChatGroq(groq_api_key=groq_api_key,model="Gemma2-9b-It")

    # Initialize the tools
    wikipedia_wrapper= WikipediaAPIWrapper()
    wikipedia_tool = Tool(
        name="WikipediaAPI",
        func=wikipedia_wrapper.run,
        description = "A tool that allows you to search for information on Wikipedia"
    )

    # Initialize the Math tool
    math_chain = LLMMathChain(llm=llm)
    calculator = Tool(
        name = "Calculator",
        func = math_chain.run,
        description = "A tool that allows you to perform mathematical calculations"
    )

    prompt = """
    You are an agent tasked with solving users' mathematical problems .Logically arrive at the solution and provide a detailed
    explanation of the steps you took to arrive at the solution
    Question:{question}
    Answer:
    """

    prompt_template = PromptTemplate(input_variables=["questions"],template=prompt)

    chain = LLMChain(llm=llm,prompt=prompt_template)

    reasoning_tool = Tool(
        name = "Reasoning",
        func = chain.run,
        description = "A tool that allows you to solve logical mathematical problems in a descriptive manner"
    )

    # Initialize the agent
    assistant_agent = initialize_agent(
        tools=[wikipedia_tool,calculator,reasoning_tool],
        llm = llm,
        agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose = False,
            handle_procession_errors= True
        )
    

    if "message" not in st.session_state:
        st.session_state.message = [{
            "role":"assistant","content":"Hello! I am an AI assistant that can help you solve mathematical problems. How can I help you today?"
        }]
    
    for msg in st.session_state.message:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Let's start the interaction
    question=st.text_input("Enter your question","I've 5 bananas and I ate 2. How many bananas do I have left?")

    if st.button("Find my answer"):
        if question :
            with st.spinner("Thinking..."):
                try:
                    st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
                    response = assistant_agent.run(input=question, callbacks=[st_cb])

                    st.session_state.message.append({"role":"assistant","content":question})
                    st.session_state.message.append({"role":"user","content":response})

                    st.write("### Response:")

                    st.success(response)

                except ValueError as e:
                    st.error(f"An error has occured {str(e)}")
        else:
            st.warning("Please enter a question")
else:
    st.warning("Please enter your GROQ API key")