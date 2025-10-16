# GenAI-With-LangChain

![LangChain](https://img.shields.io/badge/LangChain-0.1.0-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)


A comprehensive collection of examples, notebooks, and tutorials demonstrating how to build applications with LangChain and various generative AI models.

## 📋 Overview

This repository contains a structured learning path for understanding and implementing various LangChain features and components. From basic language models to complex agent architectures, this collection provides practical code examples that showcase the full LangChain ecosystem.

## 🗂️ Repository Structure

The repository is organized into modules that follow a logical progression from basic to advanced LangChain concepts:

### Foundation Components
- **01Langchain_models**: Working with different language models (LLMs, Chat Models, Embedding Models)
- **02Langchain_prompts**: Prompt engineering techniques and templates
- **03langchain-structured-output**: Getting structured responses from LLMs using TypedDict, Pydantic, etc.
- **04langchain-output-parsers**: Different methods to parse and structure LLM outputs

### Core Processing Flows
- **05langchain-chains**: Building sequential, parallel, and conditional chains
- **06langchain-runnables**: Modern approach to composable LangChain workflows
- **07langchain-document-loaders**: Loading documents from various sources (text, PDF, web)
- **08langchain-text-splitters**: Different techniques for chunking documents

### Advanced Retrieval & Generation
- **09langchain-vector-stores**: Working with vector databases (Chroma)
- **10langchain-retrievers**: Implementing various retrieval strategies
- **11langchain-retrieval-augmented-generation**: Building RAG applications
- **12langchain-tools**: Using and creating tools for LLM augmentation
- **13langchain-tool-calling**: Advanced tool usage with function calling
- **14langchain-agents**: Building autonomous agents with reasoning capabilities

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Required packages listed in `requirements.txt`

### Installation

1. Clone this repository:
```bash
git clone https://github.com/prince-kumar-singh/GenAI-With-LangChain.git
cd GenAI-With-LangChain
```

2. Install dependencies:
```bash
pip install -r 01Langchain_models/requirements.txt
```

3. Set up your API keys:
Create a `.env` file in the project root and add your API keys:
```
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_key
ANTHROPIC_API_KEY=your_anthropic_key
HF_API_KEY=your_huggingface_key
```

## 📚 Learning Path

For those new to LangChain, we recommend following this learning path:

1. Start with **01Langchain_models** to understand basic model interactions
2. Move to **02Langchain_prompts** to learn prompt engineering techniques
3. Explore **05langchain-chains** and **06langchain-runnables** for composition patterns
4. Progress through document loaders and text splitters (07-08)
5. Learn about vector stores and retrievers (09-10)
6. Build a RAG application with **11langchain-retrieval-augmented-generation**
7. Finally, advance to tools and agents (12-14)

## 🌟 Key Features

- Comprehensive examples for all major LangChain components
- Practical implementations with multiple AI providers (OpenAI, Google, Anthropic, HuggingFace)
- Progressively complex examples - from simple model calls to autonomous agents
- Real-world applications like YouTube video QA chatbots and search augmentation
- Structured code with extensive comments for educational purposes

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request



## 🙏 Acknowledgments

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- All the AI model providers (OpenAI, Google, Anthropic, Hugging Face)
- The open-source community for their valuable resources and support