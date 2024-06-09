import numpy as np
import pandas as pd

from pathlib import Path
import re
import os


target_dataframes = []

in_path = os.getenv('PATH_TO_TEST')
path_parts = in_path.split('/')
path_parts = path_parts[:-1] + ['numerical_solution']
out_path = '/'.join(path_parts)


files_path = Path(in_path).glob('*.csv')

time = 0.00
for file in files_path:

    df_item = pd.read_csv(file, sep = ',')
    df_item['t'] = time

    time += 0.05

    target_dataframes.append(df_item)

df = pd.concat(target_dataframes, ignore_index = True)

print(*df.columns)

# Space + time
x, y, z, t = (
              df['Points_0'].values,
              df['Points_1'].values,
              df['Points_2'].values,
              df['t'].values
             )

# Exact solution
T, Ux, Uy, Uz, p = (
                    df['T'].values,
                    df['U_0'].values,
                    df['U_1'].values,
                    df['U_2'].values,
                    df['p'].values
                   )
usol = np.array([T, Ux, Uy, Uz, p])


os.mkdir(path = path.split('/')
np.savez('solution.npz',
         x = x,
         y = y,
         z = z,
         t = t,
         usol = usol)
