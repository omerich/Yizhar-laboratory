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
# from protocols import run_alloptical,run_GCaMP_Exc,run_chrimson_pc,run_chrimson_CT,run_chrimson_linear,run_chrimson_linear_cyan
from protocols import *
from configs import *


# %%
# Setup communication with micromanager
mmc = Core()
savepath = r"""C:\Users\oferlab\Documents\DATA_jun2024\4.06.2024\IMAGING"""



#%%
#update for every cell
cell_dict={
    "cell":5,
    "coverslip": 2, 
    "construct": "AAV366",
}
verify_cell(cell_dict)

#%%
#run above to load everything from scratch



#%%
#IV curve
# print(get_folder_name(cell_dict)+ "_IVCurve")







#%%
config_params_chrimson_pc_ct.update(cell_dict)
# %%
# Chrimson PC CT
config_params_chrimson_pc_ct.update(cell_dict)
pp.pprint(config_params_chrimson_pc_ct)
get_yellow_level_dict_PC(config_params_chrimson_pc_ct)
# get_cyan_level_dict_PC(config_params_chrimson_pc_ct)
#%%
run_chrimson_pc_ct(mmc, savepath, config_params_chrimson_pc_ct)
# sleep(60)
# print("finished 1 min")

# %%
# %%
#GCaMP Exc
config_params_gcamp_exc.update(cell_dict)
pp.pprint(config_params_gcamp_exc)
get_cyan_level_dict_PC(config_params_gcamp_exc)

# %%
run_GCaMP_Exc(mmc, savepath, config_params_gcamp_exc)

# %%


# %%
#all optical

config_params_all_optical.update(cell_dict)
pp.pprint(config_params_all_optical)
get_yellow_level_dict_ao(config_params_all_optical)
# %%
run_alloptical(mmc, savepath, config_params_all_optical)

# %%
#all optical_flipped
config_params_all_optical_flipped.update(cell_dict)
pp.pprint(config_params_all_optical_flipped)
get_yellow_level_dict_ao(config_params_all_optical_flipped)
# %%
run_alloptical_flipped(mmc, savepath, config_params_all_optical_flipped)

# %%


# %%
# Jedi
config_params_jedi.update(cell_dict)
pp.pprint(config_params_jedi)

# %%
run_JEDI_Exc(mmc, savepath, config_params_jedi)



# %%
# Chrimson PC CT
config_params_GTARC2_yellow_cyan.update(cell_dict)
pp.pprint(config_params_GTARC2_yellow_cyan)
get_yellow_level_dict_PC(config_params_GTARC2_yellow_cyan)

#%%
run_chrimson_pc_ct(mmc, savepath, config_params_GTARC2_yellow_cyan)


# %%
# Chrmine PC 
config_params_chrmine_pc.update(cell_dict)
pp.pprint(config_params_chrmine_pc)
get_teal_level_dict_PC(config_params_chrmine_pc)
# get_teal_level_dict_PC(config_params_chrmine_pc)
#%%
run_chrmine_pc(mmc, savepath, config_params_chrmine_pc)
# sleep(60)
# print("finished 1 min")









# %%
config_params_spiking_diff_hz.update(cell_dict)
pp.pprint(config_params_spiking_diff_hz)
get_teal_level_dict_PC(config_params_spiking_diff_hz)
#%%
run_spiking_diffHz_teal(mmc, savepath, config_params_spiking_diff_hz)
# %%
