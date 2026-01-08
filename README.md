# Sea Level Predictor (Preditor do Nível do Mar) 


## Sobre
Este é um projeto desenvolvido como parte do curso "Data Analysis with Python" da [freeCodeCamp](www.freecodecamp.org).

O objetivo é analisar dados históricos do nível do mar usando regressão linear para prever as tendências futuras, especificamente até o ano 2050.

## Estrutura

*   **Análise de Dados:** Utiliza Pandas para importar e manipular dados do nível do mar de 1880 a 2014.
*   **Visualização:** Cria um gráfico de dispersão com Matplotlib.
*   **Regressão Linear:** Usa `scipy.stats.linregress` para ajustar duas linhas de melhor ajuste: uma para todos os dados e outra para dados pós-2000.
*   **Previsão:** Estende as linhas de regressão até o ano 2050 para prever o nível do mar.

 ## Instrução

1.  Clone este repositório (e certifique-se de ter o arquivo `epa-sea-level.csv` no mesmo diretório):
    ```bash
    git clone github.com
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd sea-level-predictor
    ```
3.  Instale as bibliotecas necessárias: pandas, matplotlib, seaborn, numpy e scipy:
    ```bash
    pip install pandas matplotlib seaborn numpy scipy
    ```
4.  Execute o arquivo `main.py` para rodar a análise e gerar o gráfico:
    ```bash
    python3 main.py
    ```


## Arquivos no Projeto

*   `sea_level_predictor.py`: Contém a função principal de plotagem e análise (`draw_plot()`).
*   `main.py`: Arquivo de exemplo para testar a função e salvar a imagem gerada.
*   `epa-sea-level.csv`: O conjunto de dados utilizado na análise.


## Licença e Créditos

Licença MIT. Disponível para modificação e distribuição livre, desde que atribua os créditos ao autor original.

## Autor
- **GitHub:** [trsilva23]
- **E-mail:** [trsilva23.contato@gmail.com] 

