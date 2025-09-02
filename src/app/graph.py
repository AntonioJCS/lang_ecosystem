from typing import TypedDict, Dict, Any
from langgraph.graph import StateGraph, END
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from .llm_factory import make_llm

class State(TypedDict):
    consulta: str
    artefatos: Dict[str, Any]
    log: list[str]

def agent_analista_dados(state: State) -> Dict[str, Any]:
    llm = make_llm(temperature=0.1)
    prompt = ChatPromptTemplate.from_template(
        "Atue como Analista de Dados. Resuma a tarefa e proponha 3 passos práticos: {consulta}"
    )
    chain = prompt | llm | StrOutputParser()
    resposta = chain.invoke({"consulta": state["consulta"]})
    return {
        "artefatos": {"analista": resposta},
        "log": state.get("log", []) + ["analista_dados executado"]
    }

def agent_eng_process(state: State) -> Dict[str, Any]:
    llm = make_llm(temperature=0.1)
    prompt = ChatPromptTemplate.from_template(
        "Atue como Engenheiro de Processos. Sugira um fluxo enxuto (passo-a-passo) para: {consulta}"
    )
    chain = prompt | llm | StrOutputParser()
    resposta = chain.invoke({"consulta": state["consulta"]})
    return {
        "artefatos": {"eng_process": resposta},
        "log": state.get("log", []) + ["eng_process executado"]
    }

def router(state: State) -> str:
    """
    Orquestrador simples: se mencionar 'dados' -> analista; senão -> eng_process.
    """
    texto = state["consulta"].lower()
    if "dado" in texto or "dados" in texto:
        return "analista_dados"
    return "eng_process"

def build_app():
    g = StateGraph(State)
    g.add_node("analista_dados", agent_analista_dados)
    g.add_node("eng_process", agent_eng_process)
    g.set_entry_point(router)
    g.add_edge("analista_dados", END)
    g.add_edge("eng_process", END)
    return g.compile()
