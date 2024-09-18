#%%
%load_ext autoreload
%autoreload 2

# %%
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4)
# %%
from pycromanager import Core, Studio
from time import sleep

#%%
from utils import *
from protocols import run_alloptical,run_GCaMP_Exc,run_chrimson_pc,run_chrimson_CT,run_chrimson_linear,run_chrimson_linear_cyan,run_light_curve_linear
from configs import *


# %%
# Setup communication with micromanager
mmc = Core()
savepath = r"""C:\Users\oferlab\Documents\DATA_Apr2024\07.04.2024\IMAGING"""








#%%
#update for every cell
cell_dict={
    "cell": 1,
    "coverslip": 1, 
    "construct": "D910",
}
verify_cell(cell_dict)






# %%




light_area = 0.726 #mm^2
yl_intensitiy = 3.670  #mW
# %%

#measure yellow light
# # Chrimson yellow linear

config_params_chrimson_linear = {
    "sweeps" : 1,
    "runs" : 100,
    "frames_per_sweep":2,
    "min_yellow_light":1,
    "max_yellow_light":100,
    }

config_params_chrimson_linear.update(cell_dict)
pp.pprint(config_params_chrimson_linear)
get_yellow_level_dict_linear(config_params_chrimson_linear)
#%%
run_chrimson_linear(mmc, savepath, config_params_chrimson_linear)

# %%
# measure cyan light

config_params_chrimson_linear = {
    "sweeps" : 1,
    "runs" : 100,
    "frames_per_sweep":2,
    "min_yellow_light":1,
    "max_yellow_light":100,
    }

config_params_chrimson_linear.update(cell_dict)
pp.pprint(config_params_chrimson_linear)
get_yellow_level_dict_linear(config_params_chrimson_linear)

#%%
run_chrimson_linear_cyan(mmc, savepath, config_params_chrimson_linear)

# # %%

# %%
config_params_light_measurement = {
    "sweeps" : 1,
    "runs" : 100,
    "frames_per_sweep":2,
    "min_light":1,
    "max_light":100,
    "light_color": "Blue"
    }

config_params_light_measurement.update(cell_dict)
pp.pprint(config_params_light_measurement)
get_level_dict_linear(config_params_light_measurement)

# %%
run_light_curve_linear(mmc, savepath, config_params_light_measurement)
# %%
