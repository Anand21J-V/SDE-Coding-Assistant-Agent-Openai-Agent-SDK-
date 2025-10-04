# 💻 SDE Coding Agnet Assistant Using Gemini

A powerful AI-powered coding assistant that helps streamline your development workflow through intelligent planning, code generation, and review. Built with Google's Gemini 2.0 Flash model and Streamlit.

## 🌟 Features

- **🧠 Intelligent Planning**: Automatically breaks down complex coding problems into manageable subtasks
- **🛠️ Code Generation**: Generates clean, well-structured code with explanations
- **🔍 Code Review**: Provides suggestions, optimizations, and identifies potential issues
- **⚡ Fast & Efficient**: Powered by Gemini 2.0 Flash for quick responses
- **🎨 User-Friendly Interface**: Built with Streamlit for an intuitive web experience

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API Key
- pip (Python package installer)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Anand21J-V/SDE-Coding-Assistant-Agent-Openai-Agent-SDK-.git
cd SDE-Coding-Assistant-Agent-Openai-Agent-SDK-
```

### 2. Install Dependencies

```bash
pip install streamlit pydantic python-dotenv agents asyncio
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

**How to get your Gemini API Key:**
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key to your `.env` file

## 📦 Project Structure

```
sde-coding-assistant/
├── app.py                 # Main application file
├── .env                   # Environment variables (create this)
├── .env.example          # Example environment file
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🎯 Usage

### Starting the Application

Run the following command in your terminal:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Workflow

1. **Describe Your Problem**: Enter your coding problem or feature request in the sidebar text area
2. **Plan & Build**: Click the button to generate a structured plan with subtasks and tech stack suggestions
3. **Select a Subtask**: Choose which component you want to implement from the dropdown
4. **Generate Code**: Click to generate code with explanations for the selected subtask
5. **Review Code**: Request an AI-powered code review to get optimization suggestions

## 🔧 How It Works

The application uses a multi-agent system powered by Gemini 2.0:

### Agent Architecture

1. **Planner Agent**
   - Analyzes the problem statement
   - Breaks down requirements into subtasks
   - Suggests appropriate tech stack
   - Returns structured JSON output

2. **Code Generator Agent**
   - Takes a specific subtask as input
   - Generates production-ready code
   - Provides detailed explanations
   - Outputs filename, code, and explanation

3. **Code Reviewer Agent**
   - Reviews generated code
   - Identifies potential issues
   - Suggests optimizations
   - Provides best practice recommendations

## 🔐 Configuration

### Gemini Model Options

You can switch between different Gemini models by modifying the `GEMINI_MODEL` variable:

```python
GEMINI_MODEL = "gemini-2.0-flash"   # Fast and efficient (default)
# GEMINI_MODEL = "gemini-2.0-pro"   # More capable, slower
```

### Tracing

Tracing is disabled by default. To enable it for debugging:

```python
set_tracing_disabled(False)
```

## 📝 Example Use Cases

- **Web Application Development**: Plan and build REST APIs, front-end components
- **Data Processing Scripts**: Generate ETL pipelines, data transformation code
- **Algorithm Implementation**: Create optimized algorithms with explanations
- **Utility Tools**: Build CLI tools, automation scripts
- **Bug Fixes**: Analyze and fix code issues with AI assistance

## 🛡️ Data Models

The application uses Pydantic models for structured outputs:

### CodingPlan
```python
{
    "problem": "Description of the problem",
    "subtasks": ["Task 1", "Task 2", ...],
    "tech_stack": ["Python", "Flask", ...]
}
```

### CodeOutput
```python
{
    "filename": "example.py",
    "code": "# Your generated code",
    "explanation": "Detailed explanation"
}
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: `GEMINI_API_KEY is not set in environment variables`
- **Solution**: Ensure your `.env` file exists and contains the correct API key

**Issue**: Import errors
- **Solution**: Install all required dependencies using pip

**Issue**: Application doesn't start
- **Solution**: Check if port 8501 is available or specify a different port:
  ```bash
  streamlit run app.py --server.port 8502
  ```

**Issue**: Async errors in Streamlit
- **Solution**: The application handles async operations correctly, but ensure you're using Python 3.8+

## 🔄 Session State Management

The application maintains three key session states:
- `code_plan`: Stores the planning output
- `generated_code`: Stores the generated code and explanation
- `code_review`: Stores the review suggestions

These persist across interactions within a session.

## 🌐 API Endpoint

The application uses Google's Gemini API endpoint:
```
https://generativelanguage.googleapis.com/v1beta/openai/
```

## 📊 Performance

- **Planning**: ~2-5 seconds
- **Code Generation**: ~3-8 seconds
- **Code Review**: ~2-5 seconds

*Note: Times may vary based on complexity and API response times*

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Google Gemini](https://deepmind.google/technologies/gemini/)
- Uses the [Agents framework](https://github.com/anthropics/anthropic-sdk-python) for agent orchestration

## 📧 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review the troubleshooting section

## 🔮 Future Enhancements

- [ ] Support for multiple file generation
- [ ] Code execution and testing
- [ ] Version control integration
- [ ] Export to different formats
- [ ] Custom agent configurations
- [ ] Conversation history
- [ ] Multi-language support

---

**Built by Anand Kumar Vishwakarma*
