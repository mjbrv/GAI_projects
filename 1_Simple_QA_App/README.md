# Simple Question Answering Application

This project demonstrates how to build simple question-answering applications using Large Language Models (LLMs) with LangChain. It includes introductory notebooks and a fully functional Streamlit web application.

## 📁 Project Structure

```
1_Simple_QA_App/
├── 1_LLM_Intro.ipynb                          # Introduction to LLMs with HuggingFace & OpenAI
├── 2_LLM_Intro+Google_Gemini_Pro.ipynb        # Introduction to Google Gemini Pro
└── Simple Question Answering Application/      # Streamlit web application
    ├── app.py
    ├── requirements.txt
    ├── env-sample.txt
    └── README.md
```

## 🎯 What You'll Learn

### 1. LLM Fundamentals
- How to interact with different LLM providers (HuggingFace, OpenAI, Google Gemini)
- Using LangChain wrappers to simplify API interactions
- Basic prompt engineering and query handling
- Understanding model responses and completions

### 2. Supported LLM Providers

#### HuggingFace Hub
- **Model Used**: Mistral-7B-Instruct-v0.3
- Access to open-source models hosted on HuggingFace
- Free tier available with API token

#### OpenAI
- **Model Used**: GPT-4
- Proprietary models with advanced capabilities
- Requires OpenAI API key

#### Google Gemini Pro
- **Model Used**: gemini-pro
- Google's multimodal AI model
- Requires Google API key

## 📓 Jupyter Notebooks

### 1_LLM_Intro.ipynb
This notebook covers:
- Setting up environment variables for API keys
- Installing and importing LangChain packages
- Using HuggingFace models via `HuggingFaceEndpoint`
- Using OpenAI models via `ChatOpenAI`
- Making simple queries and processing responses

**Example Usage:**
```python
from langchain_huggingface import HuggingFaceEndpoint

llm = HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.1")
query = "What is the currency of India?"
response = llm.invoke(query)
print(response)
```

### 2_LLM_Intro+Google_Gemini_Pro.ipynb
This notebook demonstrates:
- Setting up Google Gemini Pro API
- Using `ChatGoogleGenerativeAI` class from LangChain
- Making queries to Google's Gemini model
- Processing and displaying responses

**Example Usage:**
```python
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")
query = "What is the currency of India?"
result = llm.invoke(query)
print(result.content)
```

## 🚀 Streamlit Web Application

The `Simple Question Answering Application` folder contains a user-friendly web interface built with Streamlit.

### Features
- Interactive text input for user queries
- Real-time response generation using LLMs
- Simple and clean user interface
- Support for both HuggingFace and OpenAI models

### Setup Instructions

1. **Navigate to the application directory:**
   ```bash
   cd "Simple Question Answering Application"
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys:**
   
   Create a `.env` file or set environment variables:
   ```bash
   # For HuggingFace
   export HUGGINGFACEHUB_API_TOKEN="your_huggingface_token"
   
   # For OpenAI (optional)
   export OPENAI_API_KEY="your_openai_key"
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. **Access the app:**
   Open your browser and navigate to `http://localhost:8501`

### Using the Application

1. Type your question in the text input field
2. Click the "Generate" button
3. View the AI-generated response below

## 📦 Dependencies

```
langchain==0.3.0
langchain-openai==0.2.0
langchain-huggingface==0.1.0
langchain-google-genai==2.0.0
streamlit
openai
```

## 🔑 Getting API Keys

### HuggingFace API Token
1. Sign up at [HuggingFace](https://huggingface.co/)
2. Go to Settings → Access Tokens
3. Create a new token with read permissions

### OpenAI API Key
1. Sign up at [OpenAI Platform](https://platform.openai.com/)
2. Navigate to API Keys section
3. Create a new API key

### Google Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create or select a project
3. Generate an API key

## 🎓 Learning Path

1. **Start with notebooks**: Run through `1_LLM_Intro.ipynb` to understand the basics
2. **Explore Gemini**: Check out `2_LLM_Intro+Google_Gemini_Pro.ipynb` for Google's offering
3. **Build the app**: Modify and run the Streamlit application
4. **Experiment**: Try different models, prompts, and configurations

## 🌐 Deployment

The application is configured for deployment on HuggingFace Spaces:
- The `README.md` in the application folder contains HuggingFace Spaces configuration
- Set API keys using the "Variables & Secrets" settings in HuggingFace Spaces
- The app will automatically deploy when pushed to a HuggingFace Space

## 💡 Tips & Best Practices

- **API Keys**: Never commit API keys to version control
- **Model Selection**: Choose models based on your use case and budget
  - HuggingFace: Free tier, good for experimentation
  - OpenAI: More powerful but paid
  - Gemini: Balance between capability and cost
- **Rate Limits**: Be aware of API rate limits for each provider
- **Temperature Settings**: Adjust temperature parameter (default=0) for more creative vs. deterministic responses

## 🤝 Contributing

Feel free to experiment with:
- Different LLM models and providers
- Enhanced UI/UX for the Streamlit app
- Additional features like conversation history
- Error handling and validation

## 📝 Notes

- The current app.py uses HuggingFace's Mistral model by default
- To switch to OpenAI, uncomment the OpenAI lines and comment out HuggingFace lines
- Temperature is set to 0 for deterministic responses (when using OpenAI)

## 🔗 Useful Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [HuggingFace Hub](https://huggingface.co/models)
- [OpenAI API Reference](https://platform.openai.com/docs)
- [Google Gemini Documentation](https://ai.google.dev/)

---

**Happy Learning! 🚀**

