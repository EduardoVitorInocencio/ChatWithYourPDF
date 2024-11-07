
# Chat with yout pdf.

## Introdução
Este projeto utiliza diversas bibliotecas do Python para carregar, processar e interagir com documentos PDF de maneira eficiente, usando inteligência artificial para realizar buscas e extração de informações relevantes a partir desses documentos. O projeto é estruturado para funcionar com LangChain, OpenAI, FAISS e outras bibliotecas, e tem como objetivo a criação de um sistema de recuperação de informações a partir de arquivos PDF.

A funcionalidade principal é a criação de um índice vetorial de um documento PDF, o qual pode ser consultado com perguntas. O sistema irá retornar respostas baseadas no conteúdo do documento carregado. Abaixo está a explicação detalhada de como cada biblioteca é utilizada e o funcionamento do código.

## Explicação das Bibliotecas e Pacotes Importados
• **os**: Biblioteca padrão do Python para interagir com o sistema operacional. No código, é usada para manipulação de caminhos de arquivos e variáveis de ambiente.

• **dotenv (load_dotenv, find_dotenv)**: Permite o carregamento de variáveis de ambiente a partir de um arquivo .env. Essas variáveis podem ser usadas para armazenar chaves secretas e configurações do ambiente.

• **langchain_community.document_loaders.PyPDFLoader**: Responsável por carregar documentos PDF. A classe PyPDFLoader é utilizada para extrair o conteúdo do arquivo PDF especificado.

• **langchain_text_splitters.CharacterTextSplitter**: Utilizada para dividir o texto extraído do PDF em segmentos menores (pedaços de texto), o que facilita o processamento e análise do conteúdo. O separador é definido como "\n" para dividir as seções com base nas quebras de linha.

• **langchain_openai.OpenAIEmbeddings**: Esta biblioteca gera embeddings para o texto. Embeddings são representações vetoriais de palavras ou documentos, que são usadas para calcular semelhanças entre os textos.

• **langchain_community.vectorstores.FAISS**: FAISS (Facebook AI Similarity Search) é uma biblioteca para busca e clustering eficiente de grandes conjuntos de dados vetoriais. Aqui, é usada para armazenar e consultar os embeddings gerados a partir do texto do documento.

• **openai.embeddings**: Essa importação conecta-se à API da OpenAI para utilizar embeddings de modelos de linguagem, como o GPT, para representar o texto de maneira vetorial.

• **langchain.hub**: Permite o uso de modelos e componentes disponíveis na comunidade LangChain diretamente do hub, o que facilita a integração de modelos prontos e pré-configurados.

• **langchain.chains.combine_documents.create_stuff_documents_chain**: Utilizada para combinar diferentes documentos de forma que o conteúdo seja recuperado e retornado com base na consulta.

• **langchain.chains.retrieval.create_retrieval_chain**: Esta função cria um "pipeline" de recuperação de informações. Ele conecta a base de dados de documentos indexados (FAISS) com o modelo de IA para permitir que a consulta seja processada e respondida de maneira inteligente.


## Explicação de Cada Bloco de Código

1. Carregamento de variáveis de ambiente:

```python

    load_dotenv(find_dotenv('.env'))

```
Carrega as variáveis de ambiente de um arquivo .env. Esse arquivo geralmente contém chaves secretas e configurações necessárias para o projeto, como credenciais da OpenAI.

2. Carregamento do PDF:
```python
    file_path = 'C:\\Users\\edinocencio\\ChatWithYourPDF\\2210.03629v3.pdf'
    loader = PyPDFLoader(file_path=file_path)
    documents = loader.load()
```
A variável file_path especifica o caminho do arquivo PDF. O PyPDFLoader é então usado para carregar e ler o conteúdo do PDF.

3. Divisão do texto:
```python
    text_splitter = CharacterTextSplitter(separator="\n")
    docs = text_splitter.split_documents(documents=documents)
```
Após o PDF ser carregado, o texto extraído é dividido em documentos menores usando o CharacterTextSplitter. A divisão é feita por quebras de linha (\n).

4. Geração de embeddings e criação de índice FAISS:
```python
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(docs, embeddings)
    vector_store.save_local("faiss_index_react")
```

A classe OpenAIEmbeddings é utilizada para gerar representações vetoriais do texto. Esses embeddings são armazenados em uma base de dados vetorial usando o FAISS. O índice gerado é salvo localmente para posterior uso.

5. Carregamento do índice FAISS:
```python
    new_vectorstore = FAISS.load_local(
        "faiss_index_react", 
        embeddings, 
        allow_dangerous_deserialization=True
    )
```
Carrega o índice FAISS previamente salvo para permitir consultas rápidas com embeddings.

6. Preparação do modelo de recuperação de documentos:
```python
    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    combine_docs_chain = create_stuff_documents_chain(OpenAI(), retrieval_qa_chat_prompt)
    retrieval_chain = create_retrieval_chain(new_vectorstore.as_retriever(), combine_docs_chain)
```
Esse bloco de código puxa um modelo de recuperação de perguntas e respostas (QA) do LangChain Hub. Em seguida, cria um "pipeline" para combinar documentos e recuperar a informação com base na consulta do usuário.

7. Consulta e resposta:
```python
    res = retrieval_chain.invoke({"input":"What is ReAct in 3 sentences"})
    print(res['answer'])
```
A consulta é enviada para o sistema, que retorna uma resposta baseada no conteúdo do PDF carregado. A resposta é então exibida na tela.

# Como Utilizar e Rodar o Código
## Requisitos:

Antes de rodar o código, você precisa ter as seguintes dependências instaladas:
    •  Python 3.7+
    •  Bibliotecas necessárias: os, dotenv, langchain, openai, faiss-cpu, entre outras.

### Passos:
1. Instalar as dependências: Execute o seguinte comando no terminal ou prompt de comando para instalar as bibliotecas necessárias:
```bash
    pip install python-dotenv langchain openai faiss-cpu
``` 

2. Criar um arquivo .env: No mesmo diretório do seu script, crie um arquivo .env contendo as suas credenciais da OpenAI:
```makefile
    OPENAI_API_KEY=your-api-key-here
```

3. Preparar o PDF: Certifique-se de ter um arquivo PDF para carregar. Modifique a variável file_path no código para refletir o caminho correto do seu arquivo PDF.


4. Executar o código: Depois de configurar as dependências e o arquivo .env, basta rodar o script em seu terminal:
```bash
    python script_name.py
``` 

5. Obter resposta: O código irá carregar o documento, criar o índice e fornecer uma resposta para a pergunta definida no input (no exemplo, "What is ReAct in 3 sentences").