import streamlit as st
import os
from langchain.chains import ConversationChain
from langchain.llms import HuggingFaceHub
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from streamlit_chat import message
from dotenv import load_dotenv

load_dotenv()
HUB_API_TOKEN = os.getenv("HUB_API_TOKEN", None)
PAGE_TITLE = "Google / Flan T5 Chatbot workshop Demo"
PAGE_HEADLINE = "I'm a TwoFarmBot"
HUGGINGFACE_REPO_ID = "google/flan-t5-small"
HUGGINGFACE_FINE_TUNING_REPO_ID = os.getenv(
    "HUGGINGFACE_FINE_TUNING_REPO_ID", "tuphamdf/flan-t5-small-alpaca-workshop-demo"
)
MAX_LENGTH_HISTORIES = 3
DEFAULT_RADIO_MODEL = "T5-Small"
DEBUG = True
IS_CLEAR_HISTORIES = True
MODEL_KWARGS = {"temperature": 0.1, "max_new_tokens": 64, "do_sample": True}

TEMPLATE = """A chat between a curious human and an artificial intelligence assistant. The AI assistant is talkative and provides lots of specific details from its context.

### PREVIOUS CONVERSATION
{history}
USER: {input}
### ASSISTANT:"""

PROMPT = PromptTemplate(input_variables=["history", "input"], template=TEMPLATE)
MEMORY = ConversationBufferMemory(human_prefix="USER", ai_prefix="### ASSISTANT")
LLM_DEFAULT = HuggingFaceHub(
    repo_id=HUGGINGFACE_REPO_ID,
    model_kwargs=MODEL_KWARGS,
    huggingfacehub_api_token=HUB_API_TOKEN,
)
LLM_TUNING = HuggingFaceHub(
    repo_id=HUGGINGFACE_FINE_TUNING_REPO_ID,
    model_kwargs=MODEL_KWARGS,
    huggingfacehub_api_token=HUB_API_TOKEN,
)


def get_llm_chain(radio):
    if "tuning" in radio:
        return ConversationChain(
            llm=LLM_TUNING, prompt=PROMPT, verbose=DEBUG, memory=MEMORY
        )
    return ConversationChain(
        llm=LLM_DEFAULT, prompt=PROMPT, verbose=DEBUG, memory=MEMORY
    )


def clear_chat_histories():
    MEMORY.chat_memory.clear()
    st.session_state["past"] = []
    st.session_state["generated"] = []


st.set_page_config(page_title=PAGE_TITLE)
st.title(PAGE_HEADLINE)
col1, col2 = st.columns(2)
with col1:
    radio = st.radio(
        "Set model 👇",
        key="Flan T5-Small",
        options=["T5-Small", "T5-Small Fine-tuning"],
        horizontal=True,
        on_change=clear_chat_histories,
    )
    do_sample = st.toggle("Activate do sample.", value=True)
    st.button("Clear Chat Histories", on_click=clear_chat_histories)

with col2:
    histories = st.radio(
        "Chat Histories (max 3 conversations) 👇",
        key="Save 3 Chat Histories",
        options=["No", "Yes"],
        horizontal=True,
    )
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.1)

user_input = st.chat_input(
    "Say something 👉",
)

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []

if "entered_prompt" not in st.session_state:
    st.session_state["entered_prompt"] = ""

if user_input:
    if histories == "Yes" and st.session_state.past and st.session_state.generated:
        for idx, conv in enumerate(
            zip(st.session_state.past[3::-1], st.session_state.generated)
        ):
            if len(conv) == 2:
                MEMORY.chat_memory.add_user_message(conv[0])
                MEMORY.chat_memory.add_ai_message(conv[1])
    else:
        MEMORY.chat_memory.clear()

    llm_chain = get_llm_chain(radio)
    llm_chain.llm_kwargs.update(
        {"do_sample": do_sample if do_sample > 0 else None, "temperature": temperature}
    )
    output = llm_chain.run(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
