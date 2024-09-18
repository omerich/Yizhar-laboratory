import numpy as np
import matplotlib.pyplot as plt
from pycromanager import Acquisition, multi_d_acquisition_events
from pathlib import Path
from time import sleep

# from datetime import datetime
from utils import *


def run_alloptical(mmc, savepath, config_params):
    mmc.set_config("CameraMode", "ExtTrigAllOptical")

    mmc.set_property(
        "Spectra", "Cyan_Level", str(config_params["light_intensity_cyan"])
        # "Spectra", "Green_Level", str(config_params["light_intensity_cyan"])
    )

    foldername = get_folder_name(config_params) + "all_opt"
    print(f"foldername: \n{foldername}")
    num_sweep = config_params["sweeps"]
    frames_per_sweep = config_params["frames_per_sweep"]
    num_frames = num_sweep * frames_per_sweep

    events = multi_d_acquisition_events(
        num_time_points=num_frames,
        time_interval_s=0.001,  # actually should be ~1/60 ms, don't know how this works...
        # doesn't work well with 0, also don't know why.
    )

    yellow_level_dict = get_yellow_level_dict_ao(config_params)
    new_events = update_events_yellow_dict(events, yellow_level_dict)
    # new_events = update_events_yellow_dict2(events, yellow_level_dict) # 2 funciton actually changes cyan
    # print(new_events)
    # return
    sleep(1.0)
    print("starting acquisition")

    with Acquisition(
        directory=Path(savepath).absolute().as_posix(),
        name=foldername,
        saving_queue_size=1000,
    ) as acq:
        acq.acquire(new_events)
    print("finished acquisition")


def run_alloptical_flipped(mmc, savepath, config_params):
    mmc.set_config("CameraMode", "ExtTrigAllOptical")

    mmc.set_property(
        # "Spectra", "Cyan_Level", str(config_params["light_intensity_cyan"])
        "Spectra", "Green_Level", str(config_params["light_intensity_cyan"])
    )

    foldername = get_folder_name(config_params) + "all_opt_flipped"
    print(f"foldername: \n{foldername}")
    num_sweep = config_params["sweeps"]
    frames_per_sweep = config_params["frames_per_sweep"]
    num_frames = num_sweep * frames_per_sweep

    events = multi_d_acquisition_events(
        num_time_points=num_frames,
        time_interval_s=0.001,  # actually should be ~1/60 ms, don't know how this works...
        # doesn't work well with 0, also don't know why.
    )

    yellow_level_dict = get_yellow_level_dict_ao(config_params)
    # new_events = update_events_yellow_dict(events, yellow_level_dict)
    new_events = update_events_yellow_dict2(events, yellow_level_dict) # 2 funciton actually changes cyan
    # print(new_events)
    # return
    sleep(1.0)
    print("starting acquisition")

    with Acquisition(
        directory=Path(savepath).absolute().as_posix(),
        name=foldername,
        saving_queue_size=1000,
    ) as acq:
        acq.acquire(new_events)
    print("finished acquisition")



def run_GCaMP_Exc(mmc, savepath, config_params):
    mmc.set_config("CameraMode", "ExtTrigGCaMPExc")

    mmc.set_property(
        "Spectra", "Cyan_Level", str(config_params["light_intensity_cyan"])
    )

    foldername = get_folder_name(config_params) + "GCaMP_Exc"
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

    yellow_level_dict = get_cyan_level_dict_PC(config_params)
    new_events = update_events_cyan_dict(events, yellow_level_dict)

    sleep(1.0)
    print("starting acquisition")

    with Acquisition(
        directory=Path(savepath).absolute().as_posix(),
        name=foldername,
        saving_queue_size=1000,
    ) as acq:
        acq.acquire(new_events)
    print("finished acquisition")


def run_chrimson_pc(mmc, savepath, config_params):
    mmc.set_config("CameraMode", "ExtTrigChrimsonPC")

    # mmc.set_property("Spectra","Cyan_Level",str(config_params["light_intensity_cyan"]))

    foldername = get_folder_name(config_params) + "chrim_pc"
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

    yellow_level_dict = get_yellow_level_dict_PC(config_params)
    new_events = update_events_yellow_dict(events, yellow_level_dict)

    # return new_events
    # return
    sleep(1.0)
    print("starting acquisition")

    with Acquisition(
        directory=Path(savepath).absolute().as_posix(),
        name=foldername,
        saving_queue_size=1000,
    ) as acq:
        acq.acquire(new_events)
    print("finished acquisition")


def run_chrimson_linear(mmc, savepath, config_params):
    mmc.set_config("CameraMode", "ExtTrigChrimsonPC")

    # mmc.set_property("Spectra","Cyan_Level",str(config_params["light_intensity_cyan"]))

    foldername = get_folder_name(config_params) + "green_light_curve"
    print(f"foldername: {foldername}")
    num_sweep = config_params["sweeps"]
    frames_per_sweep = config_params["frames_per_sweep"]
    num_runs = config_params["runs"]
    num_frames = num_sweep * frames_per_sweep * num_runs

    events = multi_d_acquisition_events(
        num_time_points=num_frames,
        time_interval_s=0.1,  # actually should be ~1/60 ms, don't know how this works...
        # doesn't work well with 0, also don't know why.
    )

    yellow_level_dict = get_yellow_level_dict_linear(config_params)
    new_events = update_events_yellow_dict(events, yellow_level_dict)

    # return new_events
    # return
    sleep(1.0)
    print("starting acquisition")

    with Acquisition(
        directory=Path(savepath).absolute().as_posix(),
        name=foldername,
        saving_queue_size=1000,
    ) as acq:
        acq.acquire(new_events)
    print("finished acquisition")




def run_chrimson_CT(mmc, savepath, config_params):
    mmc.set_config("CameraMode", "ExtTrigChrimsonPC")

    # mmc.set_property("Spectra","Cyan_Level",str(config_params["light_intensity_cyan"]))

    foldername = get_folder_name(config_params) + "chrim_CT"
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

    yellow_level_dict = get_cyan_level_dict_PC(config_params)
    new_events = update_events_cyan_dict(events, yellow_level_dict)

    # return new_events
    # return
    sleep(1.0)
    print("starting acquisition")

    with Acquisition(
        directory=Path(savepath).absolute().as_posix(),
        name=foldername,
        saving_queue_size=1000,
    ) as acq:
        acq.acquire(new_events)
    print("finished acquisition")

def run_chrimson_linear_cyan(mmc, savepath, config_params):
    mmc.set_config("CameraMode", "ExtTrigChrimsonPC")

    # mmc.set_property("Spectra","Cyan_Level",str(config_params["light_intensity_cyan"]))

    foldername = get_folder_name(config_params) + "cyan_light_curve"
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

    yellow_level_dict = get_yellow_level_dict_linear(config_params)
    new_events = update_events_cyan_dict(events, yellow_level_dict)

    # return new_events
    # return
    sleep(1.0)
    print("starting acquisition")

    with Acquisition(
        directory=Path(savepath).absolute().as_posix(),
        name=foldername,
        saving_queue_size=1000,
    ) as acq:
        acq.acquire(new_events)
    print("finished acquisition")



def run_chrimson_pc_ct(mmc, savepath, config_params):
    mmc.set_config("CameraMode", "ExtTrigChrimsonPC")

    # mmc.set_property("Spectra","Cyan_Level",str(config_params["light_intensity_cyan"]))

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

    yellow_level_dict = get_yellow_level_dict_PC(config_params)
    cyan_level_dict = get_cyan_level_dict_PC(config_params)
    
    cyan_level_dict = {k+1:v for k,v in cyan_level_dict.items()} 
    #offset by 1 so that updates are not done in the same frame
    
    new_events = update_events_yellow_and_cyan_dict(events, cyan_level_dict,yellow_level_dict)
    print(new_events)
    # new_events = update_events_yellow_dict(events, yellow_level_dict)
    # new_events = update_events_cyan_dict(new_events, cyan_level_dict)

    # return new_events
    # return
    sleep(1.0)
    print("starting acquisition")

    with Acquisition(
        directory=Path(savepath).absolute().as_posix(),
        name=foldername,
        saving_queue_size=1000,
    ) as acq:
        acq.acquire(new_events)
    print("finished acquisition")



def run_JEDI_Exc(mmc, savepath, config_params):
    mmc.set_config("CameraMode", "ExtTrigJEDI2p")

    mmc.set_property(
        "Spectra", "Cyan_Level", str(config_params["light_intensity_cyan"])
    )

    foldername = get_folder_name(config_params) + "JEDI_Exc"
    print(f"foldername: \n{foldername}")
    num_sweep = config_params["sweeps"]
    frames_per_sweep = config_params["frames_per_sweep"]
    num_runs = 1
    num_frames = num_sweep * frames_per_sweep * num_runs

    events = multi_d_acquisition_events(
        num_time_points=num_frames,
        time_interval_s=0.045,  # actually should be ~1/60 ms, don't know how this works...
        # doesn't work well with 0, also don't know why.
    )
    # yellow_level_dict = get_cyan_level_dict_PC(config_params)
    # new_events = update_events_cyan_dict(events, yellow_level_dict)
    new_events = events

    sleep(1.0)
    print("starting acquisition")

    with Acquisition(
        directory=Path(savepath).absolute().as_posix(),
        name=foldername,
        saving_queue_size=1000,
    ) as acq:
        acq.acquire(new_events)
    print("finished acquisition")





def run_chrimson_linear(mmc, savepath, config_params):
    mmc.set_config("CameraMode", "ExtTrigChrimsonPC")

    # mmc.set_property("Spectra","Cyan_Level",str(config_params["light_intensity_cyan"]))

    foldername = get_folder_name(config_params) + "green_light_curve"
    print(f"foldername: {foldername}")
    num_sweep = config_params["sweeps"]
    frames_per_sweep = config_params["frames_per_sweep"]
    num_runs = config_params["runs"]
    num_frames = num_sweep * frames_per_sweep * num_runs

    events = multi_d_acquisition_events(
        num_time_points=num_frames,
        time_interval_s=0.1,  # actually should be ~1/60 ms, don't know how this works...
        # doesn't work well with 0, also don't know why.
    )

    yellow_level_dict = get_yellow_level_dict_linear(config_params)
    new_events = update_events_yellow_dict(events, yellow_level_dict)

    # return new_events
    # return
    sleep(1.0)
    print("starting acquisition")

    with Acquisition(
        directory=Path(savepath).absolute().as_posix(),
        name=foldername,
        saving_queue_size=1000,
    ) as acq:
        acq.acquire(new_events)
    print("finished acquisition")




def run_light_curve_linear(mmc, savepath, config_params):
    mmc.set_config("CameraMode", "ExtTrigChrimsonPC")

    # mmc.set_property("Spectra","Cyan_Level",str(config_params["light_intensity_cyan"]))

    foldername = get_folder_name(config_params) + config_params["light_color"]
    print(f"foldername: {foldername}")
    num_sweep = config_params["sweeps"]
    frames_per_sweep = config_params["frames_per_sweep"]
    num_runs = config_params["runs"]
    num_frames = num_sweep * frames_per_sweep * num_runs

    events = multi_d_acquisition_events(
        num_time_points=num_frames,
        time_interval_s=0.1,  # actually should be ~1/60 ms, don't know how this works...
        # doesn't work well with 0, also don't know why.
    )

    level_dict = get_level_dict_linear(config_params)
    new_events = update_events_curve_dict(events, level_dict,color=config_params["light_color"])

    # return new_events
    # return
    sleep(1.0)
    print("starting acquisition")

    with Acquisition(
        directory=Path(savepath).absolute().as_posix(),
        name=foldername,
        saving_queue_size=1000,
    ) as acq:
        acq.acquire(new_events)
    print("finished acquisition")


def run_chrmine_pc(mmc, savepath, config_params):
    mmc.set_config("CameraMode", "ExtTrigChrimsonPC")

    # mmc.set_property("Spectra","Cyan_Level",str(config_params["light_intensity_cyan"]))

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
    # new_events = update_events_yellow_dict(events, yellow_level_dict)
    # new_events = update_events_cyan_dict(new_events, cyan_level_dict)

    # return new_events
    # return
    sleep(1.0)
    print("starting acquisition")

    with Acquisition(
        directory=Path(savepath).absolute().as_posix(),
        name=foldername,
        saving_queue_size=1000,
    ) as acq:
        acq.acquire(new_events)
    print("finished acquisition")


def run_spiking_diffHz(mmc, savepath, config_params):
    mmc.set_config("CameraMode", "ExtTrigChrimsonPC")
    foldername = get_folder_name(config_params) + "spiking_diff_hz"
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