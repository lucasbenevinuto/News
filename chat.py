import streamlit as st
import os
from dotenv import load_dotenv
from langchain.chains.retrieval_qa.base import RetrievalQA
from prompt import prompts
from models import Models

# 🔹 Carregar variáveis do arquivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Configuração da página
st.set_page_config(
    page_title="Gerador de Postagens para LinkedIn",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Gerador de Postagens para LinkedIn")
st.markdown("---")

# 🔹 Sidebar para configurações
with st.sidebar:
    st.header("Configurações")
    
    # 🔹 Exibir API Key carregada (mas oculta para segurança)
    if api_key:
        st.success("🔑 API Key carregada do .env")
    else:
        st.error("⚠️ API Key não encontrada no .env! Verifique o arquivo.")

    # Seleção do tipo de conteúdo
    content_type = st.selectbox("Tipo de Geração", ["Conteudo", "Post", "Humanizar"])
    generate_image_option = st.checkbox("Gerar imagem do conteúdo com DALL-E")

# 🔹 Entrada do usuário (sempre visível)
user_prompt = st.text_area("Digite o tema da postagem:", height=150)

# 🔹 Botão de gerar postagem
if st.button("Gerar Postagem"):
    if not api_key:
        st.error("⚠️ API Key não foi encontrada! Verifique o arquivo .env.")
    elif not user_prompt.strip():
        st.warning("⚠️ Por favor, digite um tema para a postagem.")
    else:
        with st.spinner("Gerando postagem..."):
            try:
                model = Models()
                chat, vectordb = model.initialize_models(api_key)

                if not chat or not vectordb:
                    st.error("Erro ao inicializar modelos. Verifique sua OpenAI API Key.")
                else:
                    chain = RetrievalQA.from_chain_type(
                        llm=chat,
                        retriever=vectordb.as_retriever(
                            search_type='mmr',
                            search_kwargs={'k': 10, 'fetch_k': 20, 'lambda_mult': 0.7}
                        ),
                        chain_type_kwargs={'prompt': prompts[content_type]},
                        return_source_documents=True
                    )

                    response = chain.invoke({'query': user_prompt})

                    st.subheader("📄 Postagem Gerada:")
                    st.write(response['result'])

                    st.download_button(
                        label="📥 Exportar Postagem",
                        data=response['result'],
                        file_name="postagem_linkedin.txt",
                        mime="text/plain"
                    )

                    if generate_image_option:
                        with st.spinner("Gerando imagem..."):
                            try:
                                dalle_prompt = f"Uma ilustração profissional e moderna, sem texto: {response['result'][:500]}"
                                image_url = model.generate_image(dalle_prompt, api_key)
                                st.image(image_url, caption="Imagem gerada por DALL-E")
                            except Exception as e:
                                st.error(f"Erro ao gerar imagem: {str(e)}")

                    with st.expander("📚 Fontes consultadas"):
                        for i, doc in enumerate(response['source_documents'], 1):
                            st.markdown(f"**Fonte {i}:**")
                            st.text(doc.page_content[:200] + "...")

            except Exception as e:
                st.error(f"Erro ao gerar conteúdo: {str(e)}")
