import streamlit as st
import os
import tempfile
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader, PromptTemplate
from llama_index.core.llms import CustomLLM, CompletionResponse, LLMMetadata
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from gpt4all import GPT4All as NativeGPT4All
from Tools import fetch_jobs_api

# --- CLASSE DE ADAPTAÇÃO (PARA PULAR O ERRO DE INSTALAÇÃO) ---
class LocalLLM(CustomLLM):
    model_instance: any = None

    def __init__(self, model_instance):
        super().__init__()
        self.model_instance = model_instance

    @property
    def metadata(self) -> LLMMetadata:
        return LLMMetadata()

    def complete(self, prompt: str, **kwargs) -> CompletionResponse:
        # O modelo local gera a resposta aqui
        response = self.model_instance.generate(prompt, max_tokens=500)
        return CompletionResponse(text=response)

    def stream_complete(self, prompt: str, **kwargs):
        return self.complete(prompt, **kwargs)


# --- CONFIGURAÇÃO DOS MODELOS ---
st.set_page_config(page_title="Mu Career Advisor", layout="centered")
st.title("My Career - AI Job Advisor")


@st.cache_resource
def init_models():
    model_name = "Llama-3.2-1B-Instruct-Q4_0.gguf"
    model_path = r"C:\Users\administrator\AppData\Local\nomic.ai\GPT4All"
    
    # Carrega o modelo nativo que você já tem
    native_model = NativeGPT4All(model_name=model_name, model_path=model_path, allow_download=False)
    
    # Configura o LlamaIndex usando nossa adaptação manual
    Settings.llm = LocalLLM(model_instance=native_model)
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    return True
try:
    init_models()
except Exception as e:
    st.error(f"Erro ao carregar modelos: {e}")




uploaded_file = st.file_uploader("Upload your resume (PDF/DOCX)", type=['pdf', 'docx'], key="v_final")

if uploaded_file:
    with st.spinner("Processing your resume..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_path = tmp.name
        
        try:
            reader = SimpleDirectoryReader(input_files=[tmp_path])
            documents = reader.load_data()
            index = VectorStoreIndex.from_documents(documents)
            os.remove(tmp_path)
            
            st.success("Resume loaded!")
            
            task = st.radio(  "Select the service you need:",
            ["Analyze Resume", 
            "Skills to Develop", 
            "Find Matching Jobs"]
    )
            
            if st.button("Run Analysis"):
                query_engine = index.as_query_engine()
                
                if task == "Analyze Resume":
                    res = query_engine.query("Analyze the quality of this resume.")
                    st.subheader("Analysis Results:")
                    st.write(str(res))

                        
                elif task == "Skills to Develop":
                    res = query_engine.query("Suggest skills for professional growth.")
                    st.subheader("Skills Roadmap")
                    st.write(str(res))
                
                elif task == "Find Matching Jobs":
                    with st.spinner("Searching Adzuna API..."):
                        results = fetch_jobs_api(query_engine)
                        st.markdown(results)
                        
        except Exception as e:
            st.error(f"Error: {e}")
            if "docx2txt" in str(e):
                st.warning("Please run: pip install docx2txt")

