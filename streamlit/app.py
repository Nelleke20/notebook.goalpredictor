import streamlit as st
import pandas as pd
import numpy as np


st.title("Goal prediction")
empty_grid = pd.DataFrame(np.zeros((579, 1))).replace(0, "").astype(str)


print(type(empty_grid.columns.tolist()[0]))
empty_grid.rename(columns={0: "input_features"}, inplace=True)
df = st.data_editor(empty_grid, use_container_width=True, height=600)
