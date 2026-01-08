import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # 1. Lê os dados do arquivo CSV
    df = pd.read_csv('epa-sea-level.csv')

    # Configura a figura e eixos do Matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 2. Cria o gráfico de dispersão (scatter plot)
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # 3. Primeira linha de melhor ajuste (usando todos os dados)
    # Usa linregress para obter slope e intercept de todos os dados
    lin_reg_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope_all = lin_reg_all.slope
    intercept_all = lin_reg_all.intercept

    # Define o range de anos para a linha (1880 até 2050)
    years_future = np.arange(1880, 2051)
    # Calcula os valores y previstos (y = mx + b)
    predicted_sea_level_all = slope_all * years_future + intercept_all
    
    # Plota a primeira linha de regressão
    ax.plot(years_future, predicted_sea_level_all, 'r', label='Linha de ajuste (1880 em diante)')

    # 4. Segunda linha de melhor ajuste (usando dados a partir do ano 2000)
    # Filtra o DataFrame para incluir apenas anos >= 2000
    df_recent = df[df['Year'] >= 2000]
    lin_reg_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    slope_recent = lin_reg_recent.slope
    intercept_recent = lin_reg_recent.intercept

    # Define o range de anos para a segunda linha (2000 até 2050)
    years_future_recent = np.arange(2000, 2051)
    # Calcula os valores y previstos para a segunda linha
    predicted_sea_level_recent = slope_recent * years_future_recent + intercept_recent

    # Plota a segunda linha de regressão
    ax.plot(years_future_recent, predicted_sea_level_recent, 'g', label='Linha de ajuste (2000 em diante)')
    
    # 5. Adiciona rótulos e título
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    # 6. Salva o plot (conforme instruções para o freeCodeCamp)
    plt.savefig('sea_level_plot.png')
    
    # Retorna o objeto ax para testes automatizados
    return ax

