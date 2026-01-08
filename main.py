# main.py para testar a função draw_plot localmente
from sea_level_predictor import draw_plot
import matplotlib.pyplot as plt

# Gera o gráfico e salva
ax = draw_plot()
print("sea_level_plot.png salvo.")

# plt.show() # Descomente para visualizar a janela do gráfico localmente
