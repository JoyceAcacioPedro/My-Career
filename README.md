
# 🚀 Mu Career Advisor

### 🛠️ Technologies

* **Language:** Python 3.10+
* **AI Framework:** LlamaIndex (RAG Orchestration)
* **LLM Engine:** GPT4All (Local Model Execution)
* **Model:** Llama 3.2 1B-Instruct (Quantized GGUF)
* **Embeddings:** HuggingFace `bge-small-en-v1.5`
* **Interface:** Streamlit
* **API:** Adzuna Job Search API

---

### 🌟 Features (What you can do)

* **Secure Upload:** Drag and drop your `.pdf` or `.docx` resume safely.
* **Instant Analysis:** Get a professional breakdown of your resume's strengths and weaknesses.
* **Rating System:** Receive scores on content quality, keywords, and market relevance.
* **Live Job Matching:** Automatically search for active job vacancies that match your profile.
* **Data Privacy:** Experience AI without an internet connection (except for job searching).

---

### ⌨️ Keyboard Shortcuts (Streamlit Standard)

* **`R`**: Rerun the application.
* **`C`**: Clear the cache (useful if you change the model file).
* **`Enter`**: Confirm file upload or trigger the analysis button when focused.

---

### 🏗️ The Creation Process

The development followed a **"Privacy-First"** philosophy.

1. **Environment Setup:** Created a virtual environment to manage complex AI dependencies.
2. **Model Selection:** Tested different GGUF models to find the perfect balance between speed and reasoning (Llama 3.2 1B).
3. **Bridge Building:** Developed a `CustomLLM` adapter class to connect the GPT4All local engine to the LlamaIndex framework.
4. **RAG Implementation:** Configured a vector store to index resume data for precise context retrieval.
5. **API Integration:** Connected the Adzuna service to bridge the gap between "AI analysis" and "Real-world action."

---

### 📝 What I Learned

* **LLM Adapters:** How to write custom classes to make incompatible libraries work together.
* **Resource Management:** Using `@st.cache_resource` to keep large models in RAM, preventing system lag.
* **Prompt Engineering:** How to guide small 1B models to stay focused on specific tasks without "hallucinating."
* **RAG Architecture:** The power of giving an AI a specific "memory" (the resume) rather than relying on its general knowledge.

---

### 📈 How it can be Improved

* **Cover Letter Generation:** Add a feature to draft a personalized cover letter for the found jobs.
* **Multi-language Support:** Expand the prompt templates to analyze resumes in Portuguese and Spanish.
* **Database Integration:** Allow users to save their analysis history locally using SQLite.
* **Better Models:** Testing Llama 3.2 3B or Mistral models for even deeper reasoning if hardware allows.

---

### 🚀 How to Run

1. **Clone & Enter:**
```bash
git clone https://github.com/JoyceAcacioPedro/My-Career.git

```


2. **Install Requirements:**
```bash
pip install streamlit llama-index gpt4all requests docx2txt llama-index-embeddings-huggingface

```


3. **Model Path:**
Open `My_Career.py` and ensure the `model_path` matches your local GPT4All folder.
4. **Run:**
```bash
streamlit run My_Career.py

```



---

### 📺 Demo Video

https://youtu.be/KZlMncvWR2k

> "Watch how Mu Career Advisor transforms a raw resume into a targeted career strategy in seconds."

---

**Developed with 🧠 by Joyce Pedro**

