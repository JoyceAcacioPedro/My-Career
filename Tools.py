import requests
import streamlit as st

def fetch_jobs_api(engine):
    # 1. Forçamos a IA a dar um título curto (máximo 3 palavras)
    extraction_prompt = (
        "Based on the resume, what is the professional job title for this candidate? "
        "Answer with ONLY the title, max 3 words. Example: 'Python Developer'"
    )
    
    try:
        response = engine.query(extraction_prompt)
        job_title = str(response).strip().split('\n')[0].replace(".", "")
        
        # Mostra para o usuário o que está sendo buscado
        st.info(f"Searching vacancies for: **{job_title}**")
        
        APP_ID = "3afe35e1"
        APP_KEY = "53cfffd63a972fe2832510e524ccfec5"
        
        # Usamos 'us' ou 'gb' para mais resultados, e limitamos a busca
        url = f"https://api.adzuna.com/v1/api/jobs/us/search/1"
        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "what": job_title,
            "results_per_page": 5,
            "content-type": "application/json"
        }
        
        api_res = requests.get(url, params=params)
        data = api_res.json()
        jobs = data.get('results', [])
        
        if not jobs:
            return "⚠️ No specific jobs found for this title. Try a more general role."
        
        job_list = ""
        for job in jobs:
            # Formatando como cards bonitos em Markdown
            job_list += f"### {job['title']}\n"
            job_list += f"**Company:** {job['company']['display_name']} | **Location:** {job['location']['display_name']}\n\n"
            job_list += f"[View Vacancy]({job['redirect_url']})\n\n---\n"
            
        return job_list

    except Exception as e:
        return f"Error connecting to API: {e}"