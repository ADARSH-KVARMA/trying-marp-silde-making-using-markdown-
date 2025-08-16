# 24f1000922@ds.study.iitm.ac.in
# analysis.py

# %% [markdown]
# # Interactive Relationship Exploration
# 
# *(Marimo Notebook – Demonstrating variable dependency, interaction & documentation)*  
# 
# <!-- 24f1000922@ds.study.iitm.ac.in -->

# %% 
# Import libraries and sample dataset
import marimo
import numpy as np
import pandas as pd

# We generate a toy dataset for demonstration
np.random.seed(42)
df = pd.DataFrame({
    "x": np.linspace(0, 10, 100),
    "noise": np.random.normal(0, 1, 100)
})
df["y"] = 2.5 * df["x"] + df["noise"]  # y depends on x
df.head()

# %% 
# Interactive Widget Cell
# Slider will control the slope multiplier
import marimo as mo

slope_slider = mo.ui.slider(start=1, stop=5, value=2, step=0.1)
slope_slider

# %%
# Dependency cell: compute adjusted y = slider value * x
# This cell reacts to changes in slope_slider automatically.
slope = slope_slider.value

# Documenting flow: 'slope' comes from previous cell,
# and is used to generate a new dependent column.
df["adjusted_y"] = slope * df["x"]

df.head()

# %% [markdown]
# ## 📊 Dynamic Summary
# 
# Below is a dynamic update based on the slider widget ⬆️  
# Move the slider to see how the *adjusted relationship* changes!

# %%
# Dynamic markdown output based on slider state
mo.md(f"### Current slope (multiplier): **{slope}**")

# %%
# Optional visualization to understand interaction
import matplotlib.pyplot as plt

plt.scatter(df["x"], df["y"], label="Original y", alpha=0.6)
plt.plot(df["x"], df["adjusted_y"], color="red", label="Adjusted y (interactive)")
plt.title("Original vs Adjusted Trend")
plt.legend()
plt.show()
