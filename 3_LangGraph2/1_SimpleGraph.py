from typing_extensions import TypedDict
import random
from typing import Literal
from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END
from IPython.display import Image


class state(TypedDict):
    graph_state: str
    
def node_1(state):
    print("---Node 1---")
    return {"graph_state": state["graph_state"] + ": 1"}

def node_2(state):
    print("---Node 2---")
    return {"graph_state": state["graph_state"] + ": 2"}

def node_3(state):
    print("---Node 3---")
    return {"graph_state": state["graph_state"] + ": 3"}


def decide_next(state) -> Literal["node_2","node_3"]:
    print("---Decide Next---") 

    user_input = state['graph_state']

    if random.random() < 0.5:
        return "node_2"
    
    return "node_3"

# Build graph
builder = StateGraph(state)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

# Logic
builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_next)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

# Add
graph = builder.compile()

# View

mermaid_image = Image(graph.get_graph().draw_mermaid_png())

# Save the image to a file
with open("mermaid_image.png", "wb") as f:
    f.write(mermaid_image.data)

tempgraph = graph.invoke({"graph_state" : "Please show a number -"})
print(tempgraph)