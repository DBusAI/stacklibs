import numpy as np
from sklearn.metrics import mean_squared_error,mean_absolute_error
from matplotlib.pylab import plt

def plt_sct(y_test,preds):
    print('MSE - ',mean_squared_error(y_test,preds))
    print('MAE - ',mean_absolute_error(y_test,preds))
    plt.scatter(y_test,preds)