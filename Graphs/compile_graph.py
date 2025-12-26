from Agents import *

from langgraph.graph import StateGraph, END

def graph_builder():

    graph = StateGraph(dict)

    graph.add_node("planner_agent", planner_agent)
    graph.add_node("architect_agent", architech_agent)
    graph.add_node("coder_agent", coder_agent)

    graph.set_entry_point("planner_agent")

    graph.add_edge("planner_agent", "architect_agent")
    graph.add_edge("architect_agent", "coder_agent")

    graph.add_conditional_edges(
    "coder_agent",
    lambda s: "END" if s.get("status") == "DONE" else "coder_agent",
    {"END": END, "coder_agent": "coder_agent"}
)
    compiled_graph = graph.compile()

    return compiled_graph