# 🚀 My Career - AI Job Advisor

**Mu Career** is a smart, **100% private** career assistant that uses Local AI to analyze resumes and find job openings in real-time. Unlike other solutions, this project does not send your data to the cloud (like OpenAI); everything is processed directly on your CPU.

## 🛠️ Tech Stack

* **Python 3.10+**: Core language.
* **Streamlit**: Fast and intuitive web interface.
* **LlamaIndex**: Framework for data orchestration and **RAG (Retrieval-Augmented Generation)**.
* **GPT4All**: Engine to run the **Llama 3.2 1B-Instruct** model locally.
* **HuggingFace Embeddings**: `bge-small-en-v1.5` model to transform text into mathematical vectors.
* **Adzuna API**: Integration with external services for real-time job searching.

## 🌟 Key Features

1. **Resume Parsing**: Support for `.pdf` and `.docx` files.
2. **Critical Analysis**: Llama 3.2 evaluates resume quality, keywords, and industry relevance.
3. **Live Job Search**: Automatic extraction of the ideal job title followed by a real-time search via the Adzuna API.
4. **Total Privacy**: Processing is strictly local. Your data never leaves your machine.

## 🏗️ Project Architecture

The project implements the **RAG (Retrieval-Augmented Generation)** technique. The workflow is as follows:

1. The document is loaded and split into chunks.
2. These chunks are converted into vectors (numbers) and stored in a local index.
3. When a user asks a question, the system retrieves the most relevant parts of the resume and feeds them to the Llama 3.2 model to generate an accurate response.

## 🚀 How to Run the Project

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/mu-career-advisor.git
cd mu-career-advisor

```


2. **Create a virtual environment and install dependencies:**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate  
# On macOS/Linux:
source venv/bin/activate

pip install streamlit llama-index gpt4all requests docx2txt llama-index-embeddings-huggingface

```


3. **Model Configuration:**
* Ensure the `Llama-3.2-1B-Instruct-Q4_0.gguf` file is located in your GPT4All local path.


4. **Launch the application:**
```bash
streamlit run My_Career.py

```



## 📝 Lessons Learned

This project was a technical challenge that involved:

* **Solving Incompatibilities**: Implementing a `CustomLLM` class to integrate GPT4All with LlamaIndex, bypassing unstable external packages.
* **Performance Optimization**: Using `@st.cache_resource` to manage heavy models in RAM efficiently.
* **Prompt Engineering**: Refining instructions for small language models (1B parameters) to ensure high-quality output.

