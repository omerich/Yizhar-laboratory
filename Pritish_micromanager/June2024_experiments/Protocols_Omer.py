import numpy as np
import matplotlib.pyplot as plt
from pycromanager import Acquisition, multi_d_acquisition_events
from pathlib import Path
from time import sleep 
from utils import *

def run_yellow_cyan_control(mmc, savepath, config_params):
    mmc.set_config("CameraMode", "ExtTrigChrimsonPC")

    foldername = get_folder_name(config_params) + "chrim_pc_ct"
    print(f"foldername: {foldername}")
    num_sweep = config_params["sweeps"]
    frames_per_sweep = config_params["frames_per_sweep"]
    num_runs = config_params["runs"]
    num_frames = num_sweep * frames_per_sweep * num_runs

    events = multi_d_acquisition_events(
        num_time_points=num_frames,
        time_interval_s=0.001)

    yellow_level_dict = get_yellow_level_dict_PC(config_params)
    cyan_level_dict = get_cyan_level_dict_PC(config_params)
    
    cyan_level_dict = {k+1:v for k,v in cyan_level_dict.items()} 
    #offset by 1 so that updates are not done in the same frame
    
    new_events = update_events_yellow_and_cyan_dict(events, cyan_level_dict,yellow_level_dict)
    print(new_events)
    sleep(1.0)
    print("starting acquisition")

    with Acquisition(
        directory=Path(savepath).absolute().as_posix(),
        name=foldername,
        saving_queue_size=1000,
    ) as acq:
        acq.acquire(new_events)
    print("finished acquisition")


def run_teal_cyan_control(mmc, savepath, config_params):
    mmc.set_config("CameraMode", "ExtTrigChrimsonPC")


    foldername = get_folder_name(config_params) + "chrim_pc_ct"
    print(f"foldername: {foldername}")
    num_sweep = config_params["sweeps"]
    frames_per_sweep = config_params["frames_per_sweep"]
    num_runs = config_params["runs"]
    num_frames = num_sweep * frames_per_sweep * num_runs

    events = multi_d_acquisition_events(
        num_time_points=num_frames,
        time_interval_s=0.001,  # actually should be ~1/60 ms, don't know how this works...
        # doesn't work well with 0, also don't know why.
    )

    teal_level_dict = get_teal_level_dict_PC(config_params)
    cyan_level_dict = get_cyan_level_dict_PC(config_params)
    
    cyan_level_dict = {k+1:v for k,v in cyan_level_dict.items()} 
    #offset by 1 so that updates are not done in the same frame
    
    new_events = update_events_yellow_and_cyan_dict_TEAL(events, cyan_level_dict,teal_level_dict)
    print(new_events)
    sleep(1.0)
    print("starting acquisition")

    with Acquisition(
        directory=Path(savepath).absolute().as_posix(),
        name=foldername,
        saving_queue_size=1000,
    ) as acq:
        acq.acquire(new_events)
    print("finished acquisition")
