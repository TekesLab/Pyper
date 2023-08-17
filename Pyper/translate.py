import pandas as pd
from pyper.viper_classes import PolhemusViper

from pyper.io.decoding_utils import extract_data_from_acceleration_frame

result = [[86, 80, 82, 67, 24, 0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 102, 10, 0, 0],
[86, 80, 82, 67, 24, 0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 103, 246, 0, 0]]


df = pd.DataFrame()
for i in range(len(result)):

    df_frame = extract_data_from_acceleration_frame(result[i], "continuous", orientation="euler_degrees", conv_factor=viper.conf['conversion_factor']['euler_degrees'])
    df = pd.concat([df, df_frame], ignore_index=True)
