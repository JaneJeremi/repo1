from sklearn. model_selection import train_test_split
from sklearn. model_selection import KFold
from sklearn. model_selection import cross_val_score
from sklearn. linear_model import LinearRegression
from numpy import mean
from numpy import absolute
from numpy import sqrt
import pandas as pd

scores = cross_val_score(model, X, y, scoring='neg_mean_squared_error', cv=cv, n_jobs=-1)