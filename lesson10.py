#Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых 
import scipy.stats as stats
import numpy as np
#футболистов, хоккеистов и штангистов. Даны значения роста в трех группах случайно выбранных спортсменов:
#Футболисты: 173, 175, 180, 178, 177, 185, 183, 182. 
#Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180. 
#Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
football=np.array([173, 175, 180, 178, 177, 185, 183, 182])
hokkey=np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
powerlift=np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
alpha=0.05
n_football = stats.shapiro(football)
print(n_football)
n_hokkey = stats.shapiro(hokkey)
print(n_hokkey)
n_powerlift = stats.shapiro(powerlift)
print(n_powerlift)
# pvalue > alpha для всех случаев - данные распределены нормально
disp = stats.bartlett(football, hokkey, powerlift)
print(disp)
# pvalue > alpha - дисперсии равны
#H0: m1 = m2 = m3
#H1: m1 <> m2 <> m3
h = stats.f_oneway(football, hokkey, powerlift)
print(h)
# pvalue = 0.01048, а alpha = 0.05 значит отвергаем нулевую гипотезу, а следовательно рост спрортсменов различен