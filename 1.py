import numpy as np
import scipy.stats as stats

# open file, read into array
x, y, z = np.array(np.loadtxt("fakedata.out")).transpose()

# get means
print(f"$\\bar{{X}} = {np.mean(x):.2f}"
      f" \\bar{{Y}} = {np.mean(y):.2f},"
      f" \\bar{{Z}} = {np.mean(z):.2f}$")

# get standard deviations
print(f"$\\sigma_{{X}} = {np.std(x):.2f}"
      f" \\sigma_{{Y}} = {np.std(y):.2f},"
      f" \\sigma_{{Z}} = {np.std(z):.2f}$")

# get correlation coefficients
print(f"$C_{{X,Y}} = {np.corrcoef(x,y)[0,1]:.2f}"
      f" C_{{X,Z}} = {np.corrcoef(x,z)[0,1]:.2f},"
      f" C_{{Y,Z}} = {np.corrcoef(y,z)[0,1]:.2f}$")

# get skewness
print(f"$\\operatorname{{Skew}}(X) = {stats.skew(x):.2f}"
      f" \\operatorname{{Skew}}(Y) = {stats.skew(y):.2f},"
      f" \\operatorname{{Skew}}(Z) = {stats.skew(z):.2f}$")

