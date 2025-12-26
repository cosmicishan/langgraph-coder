# LangGraph Coder 🚀

A multi-agent system built with **LangGraph** designed to automate the software development lifecycle. This project orchestrates three specialized agents—**Planner**, **Architect**, and **Coder**—to transform high-level requirements into structured, functional code.

## 🏗 System Architecture

The project follows a linear, state-based graph execution where information flows sequentially through specialized nodes:

1. **Planner Agent**: Analyzes the initial request and breaks it down into a comprehensive execution strategy.
2. **Architect Agent**: Defines the technical structure, file organization, and logic flow based on the plan.
3. **Coder Agent**: Implements the actual code and utilizes built-in **File Writing Tools** to save the output to the local filesystem.

## 📂 Project Structure

```text
├── Agents/             # Agent logic (Planner, Architect, Coder)
├── Graphs/             # LangGraph orchestration and compilation logic
├── Loggers/            # Custom logging configuration for debugging
├── Prompts/            # System prompts for each specialized agent
├── State/              # Type definitions and Schema for the Graph state
├── Tools/              # Utility functions (File writing, etc.)
├── main.py             # Entry point of the application
└── pyproject.toml      # Dependency management (using uv)

```

## 🛠 Features

* **Sequential Workflow**: Ensures logical progression from planning to execution.
* **Persistent State**: Uses a custom `CoderState` to track plans, architecture, and file changes across nodes.
* **File System Integration**: The Coder agent can autonomously create and write files using dedicated tools.
* **Deep Observability**: Structured logging via `Loggers/` to track agent decision-making in real-time.

## 🚀 Getting Started

### Prerequisites

This project uses `uv` for extremely fast Python package management.

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

```

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/cosmicishan/langgraph-coder.git
cd langgraph-coder

```


2. **Set up Environment Variables:**
Create a `.env` file in the root directory (this is ignored by git):
```env
ANTHROPIC_API_KEY=your_key_here
GROQ_API_KEY=your_key_here

```


3. **Install dependencies:**
```bash
uv sync

```



### Usage

To run the agentic workflow, execute the main script:

```bash
uv run main.py

```

## 🧠 The Graph Flow

The graph is compiled in `Graphs/compile_graph.py` and follows this path:

`START` ➔ **Planner** ➔ **Architect** ➔ **Coder** (with Tool Access) ➔ `END`

---
