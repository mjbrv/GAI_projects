# Generative AI Projects

A hands-on learning repository covering fundamental to advanced concepts in building AI applications with Large Language Models (LLMs), from simple Q&A systems to sophisticated stateful agents with reasoning capabilities.

## 📚 Projects Overview

This repository contains three progressive projects that build upon each other, starting with basic LLM interactions and advancing to complex agent architectures.

### 1️⃣ Simple Question Answering Application
**Focus**: Introduction to LLMs and basic query-response systems

Build your first LLM-powered applications using multiple providers (OpenAI, HuggingFace, Google Gemini). Learn the fundamentals of prompt engineering and API integration through interactive notebooks and a fully functional Streamlit web app.

**Key Topics**:
- Working with different LLM providers (OpenAI, HuggingFace, Gemini)
- LangChain fundamentals and API wrappers
- Building a simple Streamlit Q&A interface
- Environment setup and API key management

**Tech Stack**: `langchain`, `streamlit`, `openai`, `huggingface`, `google-genai`

📂 [View Detailed Documentation](1_Simple_QA_App/README.md)

---

### 2️⃣ Conversational Chat Application
**Focus**: Multi-turn conversations with context and memory

Evolve from stateless Q&A to context-aware chatbots that maintain conversation history. Learn about chat models, message types, and session management to create natural dialogue experiences.

**Key Topics**:
- Chat Models vs Completion Models
- Message types (SystemMessage, HumanMessage, AIMessage)
- Session state management with Streamlit
- Building context-aware conversational interfaces
- Customizing AI personality and behavior

**Tech Stack**: `langchain`, `streamlit`, `langchain-openai`, `streamlit-chat`

📂 [View Detailed Documentation](2_Conversational_Chat_App/README.md)

---

### 3️⃣ LangGraph - AI Agents with Reasoning & Tools
**Focus**: Building stateful agents with decision-making capabilities

Master LangGraph to create sophisticated AI agents that can reason, use tools, and maintain persistent memory. Build graph-based workflows with conditional routing and multi-step reasoning.

**Key Topics**:
- Graph-based agent architectures (nodes, edges, state)
- ReAct pattern (Reasoning + Acting)
- Tool binding and automatic tool selection
- Conditional routing and decision logic
- Persistent memory with checkpointing
- Multi-turn conversations with context retention

**Tech Stack**: `langgraph`, `langchain-openai`, `python-dotenv`

📂 [View Detailed Documentation](3_LangGraph/README.md)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager
- API keys for LLM providers (OpenAI, HuggingFace, or Google Gemini)

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd GAI_projects
```

2. **Choose a project and navigate to it**
```bash
cd 1_Simple_QA_App
# or
cd 2_Conversational_Chat_App
# or
cd 3_LangGraph
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up API keys**
```bash
# Create a .env file or export environment variables
export OPENAI_API_KEY="your_key_here"
export HUGGINGFACEHUB_API_TOKEN="your_token_here"
export GOOGLE_API_KEY="your_key_here"
```

5. **Run the application or notebook**
```bash
# For Streamlit apps
streamlit run app.py

# For Jupyter notebooks
jupyter notebook

# For Python scripts
python script_name.py
```

---

## 📖 Learning Path

### Recommended Order:

**Level 1: Foundations** → Start with `1_Simple_QA_App`
- Learn LLM basics and API integration
- Understand prompt engineering fundamentals
- Build your first AI-powered web app

**Level 2: Conversations** → Move to `2_Conversational_Chat_App`
- Understand stateful vs stateless interactions
- Master conversation flow and context management
- Implement session-based chatbots

**Level 3: Agents** → Advance to `3_LangGraph`
- Build sophisticated reasoning agents
- Implement tool use and function calling
- Create complex workflows with conditional logic
- Add persistent memory to agents

---

## 🎯 What You'll Build

| Project | Application Type | Complexity | Key Feature |
|---------|-----------------|------------|-------------|
| **Simple Q&A** | Basic query-response | ⭐ Beginner | Single-turn interactions |
| **Conversational Chat** | Context-aware chatbot | ⭐⭐ Intermediate | Multi-turn with memory |
| **LangGraph Agents** | Reasoning agents | ⭐⭐⭐ Advanced | Tools + Memory + Logic |

---

## 🔑 API Keys Setup

### OpenAI
1. Sign up at [platform.openai.com](https://platform.openai.com/)
2. Navigate to API Keys section
3. Create a new secret key
4. Add billing information

### HuggingFace
1. Create account at [huggingface.co](https://huggingface.co/)
2. Go to Settings → Access Tokens
3. Generate new token with read permissions

### Google Gemini
1. Visit [makersuite.google.com](https://makersuite.google.com/app/apikey)
2. Create or select a project
3. Generate API key

---

## 📁 Repository Structure

```
GAI_projects/
├── 1_Simple_QA_App/
│   ├── 1_LLM_Intro.ipynb
│   ├── 2_LLM_Intro+Google_Gemini_Pro.ipynb
│   ├── Simple Question Answering Application/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── README.md
│   └── README.md
│
├── 2_Conversational_Chat_App/
│   ├── Chat Model Practical Implementation/
│   │   └── Chat Model Intro.ipynb
│   ├── Simple Conversational Application/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── README.md
│   └── README.md
│
├── 3_LangGraph/
│   ├── 1_SimpleGraph.ipynb
│   ├── 1_SimpleGraph.py
│   ├── 2_SimpleGraph_with_Reasoning_&_Tools.ipynb
│   ├── 2_SimpleGraph_with_Reasoning_&_Tools.py
│   ├── 3_SimpleGraph_with_Reasoning_&_Tools_&_Memory.ipynb
│   ├── 3_SimpleGraph_with_Reasoning_&_Tools_&_Memory.py
│   ├── images/
│   ├── requirements.txt
│   └── README.md
│
└── README.md (this file)
```

---

## 🛠️ Tech Stack

### Core Frameworks
- **LangChain** - Framework for building LLM applications
- **LangGraph** - Graph-based agent orchestration
- **Streamlit** - Web UI framework

### LLM Providers
- **OpenAI** - GPT-3.5, GPT-4
- **HuggingFace** - Open-source models (Mistral, etc.)
- **Google Gemini** - Multimodal AI models

### Additional Tools
- **Python-dotenv** - Environment variable management
- **Jupyter** - Interactive notebooks
- **IPython** - Enhanced Python shell

---

## 💡 Key Concepts Covered

### LangChain Fundamentals
- LLM wrappers and abstractions
- Prompt templates and chains
- Message types and schemas
- Tool integration and function calling

### State Management
- Session state in Streamlit
- Conversation history tracking
- Checkpointing and persistence
- Thread-based memory management

### Agent Architecture
- Graph-based workflows (LangGraph)
- Conditional routing and decision logic
- Tool binding and execution
- ReAct pattern (Reasoning + Acting)

### Production Considerations
- API key security
- Error handling
- Rate limiting
- Cost optimization
- Deployment strategies

---

## 🎓 Prerequisites & Skills

### Before Starting
- Basic Python programming
- Understanding of REST APIs
- Familiarity with environment variables
- Command line basics

### By the End You'll Know
- How to integrate multiple LLM providers
- Building stateful vs stateless applications
- Creating conversational AI interfaces
- Designing agent workflows with tools
- Managing conversation memory and context
- Deploying AI applications

---

## 🌐 Deployment Options

All applications can be deployed to various platforms:

- **Streamlit Cloud** - Native Streamlit hosting (free tier available)
- **HuggingFace Spaces** - Free hosting for ML demos
- **Heroku** - Container-based deployment
- **AWS/GCP/Azure** - Enterprise cloud platforms
- **Local** - Run on your own machine

Detailed deployment instructions are available in each project's README.

---

## 🐛 Common Issues & Solutions

### "API Key Not Found"
Ensure environment variables are set correctly. Check `.env` file or use `echo $OPENAI_API_KEY`.

### "Module Not Found"
Install requirements: `pip install -r requirements.txt`

### "Rate Limit Exceeded"
Wait a minute or check your API plan limits at the provider's dashboard.

### "Streamlit Port Already in Use"
Specify a different port: `streamlit run app.py --server.port 8502`

---

## 📊 Project Comparison

| Feature | Simple Q&A | Conversational | LangGraph |
|---------|-----------|----------------|-----------|
| State Management | ❌ None | ✅ Session | ✅ Persistent |
| Context Retention | ❌ | ✅ | ✅ |
| Tool Use | ❌ | ❌ | ✅ |
| Reasoning | ❌ | ❌ | ✅ |
| Conditional Logic | ❌ | ❌ | ✅ |
| Complexity | Low | Medium | High |
| Use Case | One-off queries | Chatbots | AI Agents |

---

## 🤝 Contributing

Suggestions for enhancements:
- Add more LLM providers (Anthropic Claude, Cohere, etc.)
- Implement RAG (Retrieval-Augmented Generation)
- Add voice input/output capabilities
- Create more complex agent workflows
- Add testing and CI/CD pipelines
- Implement monitoring and logging

---

## 📚 Additional Resources

### Documentation
- [LangChain Docs](https://python.langchain.com/)
- [LangGraph Guide](https://langchain-ai.github.io/langgraph/)
- [Streamlit Docs](https://docs.streamlit.io/)

### Learning Materials
- [OpenAI API Reference](https://platform.openai.com/docs)
- [HuggingFace Hub](https://huggingface.co/docs/hub)
- [Google AI Studio](https://ai.google.dev/)

### Research Papers
- [ReAct: Reasoning and Acting](https://arxiv.org/abs/2210.03629)
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)

---

## 📝 License

This project is for educational purposes. Please check individual LLM provider licenses and terms of service.

---

## 🎯 Next Steps After Completion

### Advanced Topics to Explore
1. **RAG Systems** - Combine retrieval with generation
2. **Multi-Agent Systems** - Coordinate multiple specialized agents
3. **Fine-Tuning** - Customize models for specific tasks
4. **Vector Databases** - Semantic search and memory
5. **Production APIs** - Build and deploy LLM-powered APIs
6. **Evaluation** - Measure and improve agent performance

### Real-World Applications
- Customer support automation
- Research assistants
- Code generation and review
- Data analysis and reporting
- Content creation pipelines
- Document processing systems

---

**Happy Learning! Start with Project 1 and build your way up to sophisticated AI agents! 🚀🤖**
