![Código Certo Coders](![alt text](image.png))

# 📚 Trilha Final Ciência de Dados Jr



## Cientista de Dados
Análise de Feedback da Comunidade
Este repositório contém a análise de feedback da comunidade, utilizando técnicas de machine learning, análise de sentimentos e visualização de dados. O objetivo é identificar padrões, clusters e tendências de satisfação entre os membros da comunidade.

### Estrutura do Repositório
data/: Contém o arquivo CSV com os dados de feedback da comunidade.
notebooks/: Contém os notebooks Jupyter usados na análise.
results/: Contém as visualizações e relatórios gerados durante a análise.
README.md: Este arquivo, explicando o repositório e como usá-lo.

## Pré-requisitos
Para executar os scripts e notebooks deste repositório, você precisará ter o Python instalado em seu sistema. É recomendável usar um ambiente virtual para gerenciar as dependências. Siga os passos abaixo para configurar seu ambiente:

## 1. Instalação do Python
Certifique-se de ter o Python instalado. Você pode baixá-lo em python.org.


## 2. Instalação do Jupyter Notebook
Você pode instalar o Jupyter Notebook com o seguinte comando:

``` pip install notebook```

bash
Copiar código
pip install notebook

## 3. Instalação das Dependências
Clone o repositório e navegue até o diretório do projeto. Então, instale as dependências necessárias com o seguinte comando:

```git clone https://github.com/seu-usuario/seu-repositorio.git```
```cd seu-repositorio```
```pip install -r requirements.txt```

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
pip install -r requirements.txt
O arquivo requirements.txt deve conter todas as bibliotecas necessárias. Caso não exista, você pode criar um arquivo com o seguinte conteúdo baseado nas bibliotecas usadas no projeto:

```plaintext, pandas, matplotlib, seaborn ,scikit-learn ,textblob , wordcloud``


## 4. Execução dos Notebooks
Para iniciar o Jupyter Notebook, execute o seguinte comando no diretório raiz do projeto:

```jupyter notebook```

bash
Copiar código
jupyter notebook
Isso abrirá uma nova aba no seu navegador com o painel do Jupyter Notebook. Navegue até o diretório notebooks/ e abra o notebook desejado para visualizar a análise.

- Sobre o Dataset
O dataset **feedback_junho2024.csv** , **feedback_julho2024.csv** .  contém informações sobre a satisfação dos membros da comunidade. As principais colunas do dataset são:

-comentario_adicional: Comentários adicionais fornecidos pelos membros.
-horas_semanais_dedicadas: Número de horas dedicadas semanalmente pelos membros.
-satisfacao_geral_comunidade: Avaliação geral da satisfação dos membros com a comunidade.
-reunioes_do_time: Frequência das reuniões do time.
-colaboracao_entre_membros: Nível de colaboração entre os membros.
-ambiente_de_aprendizagem: Qualidade do ambiente de aprendizagem.
-comunicacao_entre_membros: Qualidade da comunicação entre os membros.


## Análise Realizada
- Pré-processamento dos Dados: Inclui a limpeza e preparação dos dados para análise.
- Análise Exploratória: Realizada para entender a distribuição e os padrões dos dados.
- Análise de Sentimentos: Utilizando técnicas de NLP (Natural Language Processing) para classificar os comentários como positivos, negativos ou neutros.
Clustering: Aplicação de algoritmos de clustering como K-Means e DBSCAN para identificar grupos semelhantes de membros.
- PCA (Análise de Componentes Principais): Redução de dimensionalidade para visualização dos clusters.
- Modelos Preditivos: Criação e avaliação de modelos preditivos para prever a satisfação com base em diferentes variáveis.
Resultados
- Os resultados incluem gráficos, tabelas e relatórios gerados a partir das análises. Os principais insights são:

## Distribuição dos Sentimentos: A maioria dos comentários é positiva.
Clusters Identificados: Identificação de grupos distintos de membros com base em horas dedicadas e satisfação geral.
PCA: Visualização dos clusters em um espaço reduzido de duas dimensões.

Modelos Preditivos: Avaliação do modelo de regressão linear e Random Forest para prever a satisfação dos membros.
Contribuições. 

---

🔗 **Mantenha-se Conectado:**
  
- [LinkedIn](https://www.linkedin.com/in/marcelo-ishida-takeya-a8213897/)
  
🌐 **Contato:**

- Email: marcelo.ishida@yahoo.com.br
