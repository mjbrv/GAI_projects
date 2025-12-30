# Conversational Chat Application

This project demonstrates how to build conversational chatbot applications using LangChain's Chat Models. Unlike simple Q&A systems, this project implements stateful conversations with context retention, allowing for natural multi-turn dialogues.

## 📁 Project Structure

```
2_Conversational_Chat_App/
├── Chat Model Practical Implementation/
│   └── Chat Model Intro.ipynb                # Introduction to Chat Models & Message Types
└── Simple Conversational Application/
    ├── app.py                                # Streamlit chatbot application
    ├── requirements.txt
    ├── env-sample.txt
    └── README.md
```

## 🎯 What You'll Learn

### 1. Chat Models vs LLMs
- Difference between completion models and chat-optimized models
- Understanding the chat message structure (System, Human, AI)
- Building multi-turn conversations with context
- Managing conversation state and history

### 2. LangChain Message Types
- **SystemMessage**: Sets the AI's behavior and personality
- **HumanMessage**: Represents user input
- **AIMessage**: Represents AI responses (for context passing)

### 3. Session Management
- Maintaining conversation history across interactions
- Using Streamlit's session state for persistence
- Building context-aware chatbots

## 📓 Jupyter Notebook

### Chat Model Intro.ipynb

This notebook covers the fundamentals of chat models:

#### Key Concepts:

**1. Basic Chat Model Setup:**
```python
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

chat = ChatOpenAI(temperature=0.7, model='gpt-3.5-turbo')
```

**2. Simple Chat Interaction:**
```python
chat.invoke([
    SystemMessage(content="You are a sarcastic AI assistant"),
    HumanMessage(content="Please answer in 30 words: How can I learn driving a car")
])
```

**3. Multi-Turn Conversation:**
```python
ourConversation = chat.invoke([
    SystemMessage(content="You are a 3 years old girl who answers very cutely and in a funny way"),
    HumanMessage(content="How can I learn driving a car"),
    AIMessage(content="I can't drive yet! But I have a driver, my dad..."),
    HumanMessage(content="Can you teach me driving?")
])
```

#### What Makes This Different?
- The model maintains context across multiple exchanges
- System messages define the AI's personality and behavior
- Previous AI responses can be included for continuity
- Temperature parameter (0.7) allows for creative, varied responses

## 🚀 Streamlit Conversational Application

The `Simple Conversational Application` implements a fully functional chatbot with persistent conversation history.

### Features
- ✅ **Persistent Memory**: Maintains full conversation history in session
- ✅ **Context-Aware**: Each response considers previous messages
- ✅ **Real-Time Interaction**: Instant responses in a clean UI
- ✅ **System Prompt**: Pre-configured helpful assistant behavior
- ✅ **Session Management**: Automatic conversation state handling

### How It Works

1. **Session Initialization**: Creates a session with a system message
   ```python
   if "sessionMessages" not in st.session_state:
       st.session_state.sessionMessages = [
           SystemMessage(content="You are a helpful assistant.")
       ]
   ```

2. **Message Handling**: Appends user questions and AI responses to history
   ```python
   def load_answer(question):
       st.session_state.sessionMessages.append(HumanMessage(content=question))
       assistant_answer = chat.invoke(st.session_state.sessionMessages)
       st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))
       return assistant_answer.content
   ```

3. **Context Retention**: Every interaction includes the full conversation history

## 🛠️ Setup Instructions

### 1. Navigate to the Application Directory
```bash
cd "Simple Conversational Application"
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Required packages:
- `streamlit==1.36.0` - Web framework
- `langchain==0.2.5` - LangChain core
- `langchain-openai==0.1.9` - OpenAI integration
- `openai==1.35.3` - OpenAI API client
- `streamlit-chat==0.1.1` - Chat UI components
- `python-dotenv==1.0.1` - Environment variable management

### 3. Configure API Key

**Option A: Environment Variable**
```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

**Option B: .env File**
Create a `.env` file in the application directory:
```
OPENAI_API_KEY=your_openai_api_key_here
```

**Option C: Direct in Code (Not Recommended for Production)**
Uncomment and update lines 7-8 in `app.py`:
```python
import os
os.environ["OPENAI_API_KEY"] = "your_key_here"
```

### 4. Run the Application
```bash
streamlit run app.py
```

### 5. Access the Chatbot
Open your browser and navigate to `http://localhost:8501`

## 💬 Using the Application

1. **Start a Conversation**: Type your message in the "You:" input field
2. **Submit**: Click the "Generate" button
3. **View Response**: The AI's answer appears below
4. **Continue Chatting**: Ask follow-up questions - the bot remembers the context!
5. **Refresh to Reset**: Reload the page to start a new conversation

### Example Conversation Flow:
```
You: What's the capital of France?
AI: The capital of France is Paris.

You: What's the population there?
AI: Paris has a population of approximately 2.2 million people...
```
*(Note: The AI knows "there" refers to Paris from the previous context)*

## 🎨 Customization Options

### 1. Change AI Personality
Modify the system message in `app.py` (line 25):
```python
st.session_state.sessionMessages = [
    SystemMessage(content="You are a friendly and enthusiastic teacher.")
]
```

### 2. Adjust Temperature
Change the creativity level (line 46):
```python
chat = ChatOpenAI(temperature=0.7)  # 0 = deterministic, 1 = creative
```

### 3. Switch Models
Use different OpenAI models:
```python
chat = ChatOpenAI(temperature=0, model='gpt-4')  # More capable
chat = ChatOpenAI(temperature=0, model='gpt-3.5-turbo')  # Faster, cheaper
```

### 4. Add Conversation History Display
Enhance the UI to show the full conversation thread:
```python
for message in st.session_state.sessionMessages:
    if isinstance(message, HumanMessage):
        st.write(f"You: {message.content}")
    elif isinstance(message, AIMessage):
        st.write(f"AI: {message.content}")
```

## 🔑 Getting OpenAI API Key

1. Sign up at [OpenAI Platform](https://platform.openai.com/)
2. Navigate to **API Keys** section
3. Click **"Create new secret key"**
4. Copy the key immediately (you won't see it again!)
5. Add billing information to use the API

### API Costs
- GPT-3.5-Turbo: ~$0.002 per 1K tokens
- GPT-4: ~$0.03 per 1K tokens (input)
- Monitor usage at [platform.openai.com/usage](https://platform.openai.com/usage)

## 📊 Key Differences from Simple Q&A

| Feature | Simple Q&A | Conversational Chat |
|---------|------------|---------------------|
| **Context** | No memory | Full conversation history |
| **Messages** | Single query | SystemMessage + HumanMessage + AIMessage |
| **Use Case** | One-off questions | Multi-turn dialogues |
| **State** | Stateless | Stateful (session storage) |
| **Personality** | Generic | Customizable via SystemMessage |

## 🌐 Deployment

### HuggingFace Spaces
The application is ready for HuggingFace Spaces deployment:

1. Create a new Space on [HuggingFace](https://huggingface.co/spaces)
2. Select **Streamlit** as the SDK
3. Upload your files
4. Set `OPENAI_API_KEY` in **Settings → Repository secrets**
5. The app will auto-deploy!

### Other Platforms
- **Streamlit Cloud**: Native deployment platform for Streamlit apps
- **Heroku**: Use a Procfile with streamlit run command
- **AWS/GCP**: Deploy as a containerized application
- **Azure**: Use Azure App Service with Python runtime

## 💡 Advanced Features to Implement

### 1. Conversation Export
```python
# Add a button to download chat history
if st.button("Export Conversation"):
    conversation_text = "\n".join([f"{msg.type}: {msg.content}" 
                                   for msg in st.session_state.sessionMessages])
    st.download_button("Download", conversation_text, "conversation.txt")
```

### 2. Clear Chat History
```python
if st.button("Clear Chat"):
    st.session_state.sessionMessages = [
        SystemMessage(content="You are a helpful assistant.")
    ]
    st.experimental_rerun()
```

### 3. Token Counting
```python
from langchain.callbacks import get_openai_callback

with get_openai_callback() as cb:
    response = chat.invoke(st.session_state.sessionMessages)
    st.write(f"Tokens used: {cb.total_tokens}")
```

### 4. Multiple Chat Sessions
Store different conversations with unique session IDs for multi-user support.

### 5. Response Streaming
Enable real-time streaming for longer responses:
```python
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

chat = ChatOpenAI(
    temperature=0,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)
```

## 🎓 Learning Path

1. **Start with the Notebook**: 
   - Understand message types (System, Human, AI)
   - Experiment with different system prompts
   - Test multi-turn conversations

2. **Run the Application**:
   - Deploy locally and test various conversations
   - Observe how context is maintained
   - Try asking follow-up questions

3. **Customize & Extend**:
   - Create different AI personalities
   - Add conversation export functionality
   - Implement conversation history display
   - Add token usage tracking

4. **Production Considerations**:
   - Implement rate limiting
   - Add error handling
   - Secure API key management
   - Monitor costs and usage

## 🐛 Troubleshooting

### Issue: "API Key Not Found"
**Solution**: Ensure your `OPENAI_API_KEY` environment variable is set correctly.

### Issue: "Rate Limit Exceeded"
**Solution**: You've hit OpenAI's rate limit. Wait a minute or upgrade your plan.

### Issue: Session State Not Persisting
**Solution**: Streamlit resets state on page refresh. This is expected behavior.

### Issue: Long Response Times
**Solution**: 
- Use GPT-3.5-turbo instead of GPT-4 for faster responses
- Consider implementing streaming responses

## 🔒 Security Best Practices

1. **Never commit API keys** to version control
2. **Use environment variables** or secret management tools
3. **Implement rate limiting** to prevent abuse
4. **Validate user input** before sending to the API
5. **Set spending limits** in your OpenAI account
6. **Monitor usage regularly** to detect anomalies

## 🤝 Contributing

Ideas for enhancement:
- Add voice input/output capabilities
- Implement conversation summarization
- Add multi-language support
- Create pre-defined conversation templates
- Build conversation analytics dashboard
- Add image generation capabilities

## 📚 Additional Resources

- [LangChain Chat Models Documentation](https://python.langchain.com/docs/modules/model_io/chat/)
- [OpenAI Chat Completions Guide](https://platform.openai.com/docs/guides/chat)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Session State Guide](https://docs.streamlit.io/library/api-reference/session-state)
- [Building Conversational AI Best Practices](https://www.langchain.com/docs)

## 🎯 Next Steps

After mastering this conversational chat app, explore:
- **RAG (Retrieval-Augmented Generation)**: Add document search to your chatbot
- **LangGraph**: Build more complex conversation flows with branching logic
- **Memory Systems**: Implement long-term memory across sessions
- **Multi-Agent Systems**: Create specialized agents for different tasks

---

**Happy Chatting! 🤖💬**

