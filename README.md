# Gerador de Postagens para LinkedIn

## 📌 Visão Geral
Esta aplicação é um gerador de postagens para o LinkedIn que utiliza inteligência artificial para criar conteúdos envolventes e informativos. Baseia-se no modelo GPT da OpenAI para produzir textos, além de um sistema de recuperação de informações baseado em vetores para enriquecer o conteúdo. Opcionalmente, a aplicação pode gerar imagens utilizando o modelo DALL-E.

## 🚀 Funcionalidades
- Geração automática de postagens para LinkedIn.
- Três modos de geração: **Conteúdo**, **Post** e **Humanizar**.
- Integração com OpenAI GPT-4 para criação de textos.
- Recuperação de informações relevantes usando **ChromaDB**.
- Geração opcional de imagens com **DALL-E**.
- Interface intuitiva desenvolvida com **Streamlit**.
- Exportação da postagem gerada em formato de texto.

---

## 🛠️ Requisitos
Para rodar esta aplicação, é necessário instalar os seguintes pacotes:

```sh
pip install -r requirements.txt
```

### 📋 Dependências principais
- **streamlit**: Interface gráfica.
- **python-dotenv**: Gerenciamento de variáveis de ambiente.
- **langchain**: Framework para IA generativa.
- **langchain-openai**: Integração com modelos da OpenAI.
- **langchain-community**: Ferramentas adicionais do Langchain.
- **requests**: Comunicação com API da OpenAI.
- **PyPDF2**: Processamento de arquivos PDF.
- **chromadb**: Banco de dados vetorial para recuperação de informações.

---

## 🔧 Configuração
### 1️⃣ Clonar o repositório
```sh
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

### 2️⃣ Criar e configurar o arquivo `.env`
Crie um arquivo `.env` na raiz do projeto e adicione sua chave da OpenAI:

```
OPENAI_API_KEY=your_openai_api_key
```

### 3️⃣ Executar a aplicação
```sh
streamlit run chat.py
```

---

## 🏗️ Estrutura do Projeto

```
├── arquivos/
│   ├── chat_retrieval_db/  # Banco de dados vetorial
│   ├── deepseek.pdf        # Documento para recuperação de informações
│
├── chat.py                 # Interface principal com Streamlit
├── models.py               # Inicialização dos modelos de IA
├── prompt.py               # Templates de prompt para geração de conteúdo
├── rag.py                  # Implementação do sistema de recuperação de informações
├── requirements.txt        # Dependências do projeto
├── .env                    # Chave da API (não incluído no repositório)
```

---

## 📜 Como Usar
1. **Acesse a interface** através do navegador após rodar o comando `streamlit run chat.py`.
2. **Escolha o tipo de postagem** no menu lateral:
   - `Conteúdo`: Postagens detalhadas e aprofundadas.
   - `Post`: Publicações curtas e diretas.
   - `Humanizar`: Versão mais natural e menos robótica do texto.
3. **Digite o tema da postagem** no campo de entrada.
4. **Clique em "Gerar Postagem"**.
5. (Opcional) **Gerar imagem** para acompanhar a postagem.
6. **Baixe o texto gerado** no formato `.txt`.

---

## 🛑 Erros Comuns e Soluções
- **Erro: "API Key não encontrada!"**
  - Certifique-se de que o arquivo `.env` contém sua chave da OpenAI e está corretamente carregado.

- **Erro: "Erro ao inicializar modelos"**
  - Verifique se sua chave da OpenAI é válida e se os pacotes necessários estão instalados.

- **Erro ao recuperar informações**
  - Certifique-se de que há documentos na pasta `arquivos/` e que o banco de vetores foi criado corretamente.

---

## 📌 Melhorias Futuras
- Melhor otimização da recuperação de informações para aumentar a relevância dos textos.
- Adição de suporte para múltiplas línguas.
- Integração com APIs externas para geração de insights baseados em tendências.

---

## 👨‍💻 Autor
Desenvolvido por [Seu Nome]. Caso tenha dúvidas ou sugestões, sinta-se à vontade para contribuir ou entrar em contato!

