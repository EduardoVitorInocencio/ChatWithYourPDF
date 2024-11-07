
# Chat with yout pdf.

## Introdução
Este projeto utiliza diversas bibliotecas do Python para carregar, processar e interagir com documentos PDF de maneira eficiente, usando inteligência artificial para realizar buscas e extração de informações relevantes a partir desses documentos. O projeto é estruturado para funcionar com LangChain, OpenAI, FAISS e outras bibliotecas, e tem como objetivo a criação de um sistema de recuperação de informações a partir de arquivos PDF.

A funcionalidade principal é a criação de um índice vetorial de um documento PDF, o qual pode ser consultado com perguntas. O sistema irá retornar respostas baseadas no conteúdo do documento carregado. Abaixo está a explicação detalhada de como cada biblioteca é utilizada e o funcionamento do código.

## Explicação das Bibliotecas e Pacotes Importados
• *os*: Biblioteca padrão do Python para interagir com o sistema operacional. No código, é usada para manipulação de caminhos de arquivos e variáveis de ambiente.

• *dotenv (load_dotenv, find_dotenv)*: Permite o carregamento de variáveis de ambiente a partir de um arquivo .env. Essas variáveis podem ser usadas para armazenar chaves secretas e configurações do ambiente.

• *langchain_community.document_loaders.PyPDFLoader*: Responsável por carregar documentos PDF. A classe PyPDFLoader é utilizada para extrair o conteúdo do arquivo PDF especificado.

• *langchain_text_splitters.CharacterTextSplitter*: Utilizada para dividir o texto extraído do PDF em segmentos menores (pedaços de texto), o que facilita o processamento e análise do conteúdo. O separador é definido como "\n" para dividir as seções com base nas quebras de linha.

• *langchain_openai.OpenAIEmbeddings*: Esta biblioteca gera embeddings para o texto. Embeddings são representações vetoriais de palavras ou documentos, que são usadas para calcular semelhanças entre os textos.

• *langchain_community.vectorstores.FAISS*: FAISS (Facebook AI Similarity Search) é uma biblioteca para busca e clustering eficiente de grandes conjuntos de dados vetoriais. Aqui, é usada para armazenar e consultar os embeddings gerados a partir do texto do documento.

• *openai.embeddings*: Essa importação conecta-se à API da OpenAI para utilizar embeddings de modelos de linguagem, como o GPT, para representar o texto de maneira vetorial.

• *langchain.hub*: Permite o uso de modelos e componentes disponíveis na comunidade LangChain diretamente do hub, o que facilita a integração de modelos prontos e pré-configurados.

• *langchain.chains.combine_documents.create_stuff_documents_chain*: Utilizada para combinar diferentes documentos de forma que o conteúdo seja recuperado e retornado com base na consulta.

• *langchain.chains.retrieval.create_retrieval_chain*: Esta função cria um "pipeline" de recuperação de informações. Ele conecta a base de dados de documentos indexados (FAISS) com o modelo de IA para permitir que a consulta seja processada e respondida de maneira inteligente.


## Explicação de Cada Bloco de Código

1. Carregamento de variáveis de ambiente:

```python

    load_dotenv(find_dotenv('.env'))
    
```