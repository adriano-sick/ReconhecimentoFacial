# Projeto de Reconhecimento Facial

Este projeto consiste em dois scripts que implementam um sistema de reconhecimento facial. O primeiro script cria um modelo de reconhecimento facial a partir de um conjunto de imagens de rostos. O segundo script usa esse modelo para identificar rostos a partir da webcam.

## Estrutura do Projeto

O projeto contém os seguintes arquivos:

- `reconhecimentoModelo.py`: Este script cria um modelo de reconhecimento facial a partir de um conjunto de imagens de rostos.
- `reconhecimento.py`: Este script usa o modelo criado para identificar rostos a partir da webcam.
- `nomes.txt`: Este arquivo contém uma lista de nomes correspondentes aos números identificadores usados nas imagens do conjunto de dados.
- `requirements.txt`: Este arquivo lista as dependências do projeto.

## Configuração do Ambiente

1. Clone o repositório para o seu computador local.
2. Navegue até o diretório do projeto.
3. Crie um ambiente virtual com o comando `python -m venv venv`.
4. Ative o ambiente virtual. No Windows, use `venv\Scripts\activate`. No Linux/Mac, use `source venv/bin/activate`.
5. Instale as dependências do projeto com o comando `pip install -r requirements.txt`.

## Execução do Projeto

1. Com o ambiente virtual ativado, execute o script `reconhecimentoModelo.py` para criar o modelo de reconhecimento facial.
2. Em seguida, execute o script `reconhecimento.py` para iniciar o reconhecimento facial a partir da webcam.

## Conjunto de Dados

O conjunto de dados deve ser colocado na pasta `dataset`. Cada imagem do conjunto de dados deve seguir o formato `xxxx.N.jpg`, onde `xxxx` pode ser qualquer texto e `N` é um número que identifica o indivíduo na imagem. Por exemplo, todas as imagens com o número 1 serão do mesmo indivíduo.

Os nomes correspondentes aos números identificadores devem ser listados no arquivo `nomes.txt`, no formato `N,nome`, onde `N` é o número identificador e `nome` é o nome do indivíduo.

## Notas

Este projeto foi testado com Python 3.12. Certifique-se de ter a versão correta do Python instalada antes de tentar executar o projeto.
