from datetime import datetime
import numpy as np


def get_folder_name(config_params):
    dt = datetime.now().strftime("%Y%m%d-%H%M%S")
    foldername = f"""{dt}_{config_params["construct"]}_CS_{config_params["coverslip"]}_cell_{config_params["cell"]}"""
    return foldername


def get_yellow_level_dict_ao(config_params):
    num_sweep = config_params["sweeps"]
    frames_per_sweep = config_params["frames_per_sweep"]
    num_frames = num_sweep * frames_per_sweep
    frames = np.arange(0, num_frames, frames_per_sweep)
    # print(frames)
    levels = (
        np.logspace(
            np.log10(config_params["min_yellow_light"]),
            np.log10(config_params["max_yellow_light"]),
            len(frames),
        )
        .round()
        .astype(int)
    )

    yellow_level_dict = dict(zip(frames, levels))
    return yellow_level_dict


def update_events_yellow_dict(events, yellow_level_dict):
    new_events = []
    for event in events:
        # print(event)
        t = event["axes"]["time"]
        if t in yellow_level_dict:
            yellow_level = str(yellow_level_dict[t])
            event["properties"] = [
                ["Spectra", "Green_Level", yellow_level],
            ]
        new_events.append(event)
    return new_events


def get_yellow_level_dict_PC(config_params):
    num_sweep = config_params["sweeps"]
    num_runs = config_params["runs"]
    frames_per_sweep = config_params["frames_per_sweep"]
    num_frames = num_sweep * frames_per_sweep * num_runs
    frames = np.arange(0, num_frames, frames_per_sweep * num_sweep)
    # print(frames)
    levels = (
        np.logspace(
            np.log10(config_params["min_yellow_light"]),
            np.log10(config_params["max_yellow_light"]),
            len(frames),
        )
        .round()
        .astype(int)
    )

    yellow_level_dict = dict(zip(frames, levels))
    return yellow_level_dict

def get_yellow_level_dict_linear(config_params):
    num_sweep = config_params["sweeps"]
    num_runs = config_params["runs"]
    frames_per_sweep = config_params["frames_per_sweep"]
    num_frames = num_sweep * frames_per_sweep * num_runs
    frames = np.arange(0, num_frames, frames_per_sweep * num_sweep)
    # print(frames)
    levels = (
        np.linspace(
            config_params["min_yellow_light"],
            config_params["max_yellow_light"],
            len(frames),
        )
        .round()
        .astype(int)
    )

    yellow_level_dict = dict(zip(frames, levels))
    return yellow_level_dict



def get_level_dict_linear(config_params):
    num_sweep = config_params["sweeps"]
    num_runs = config_params["runs"]
    frames_per_sweep = config_params["frames_per_sweep"]
    num_frames = num_sweep * frames_per_sweep * num_runs
    frames = np.arange(0, num_frames, frames_per_sweep * num_sweep)
    # print(frames)
    levels = (
        np.linspace(
            config_params["min_light"],
            config_params["max_light"],
            len(frames),
        )
        .round()
        .astype(int)
    )

    light_level_dict = dict(zip(frames, levels))
    return light_level_dict



def update_events_yellow_dict2(events, yellow_level_dict):
    new_events = []
    for event in events:
        # print(event)
        t = event["axes"]["time"]
        if t in yellow_level_dict:
            yellow_level = str(yellow_level_dict[t])
            event["properties"] = [
                ["Spectra", "Cyan_Level", yellow_level],
            ]
        new_events.append(event)
    return new_events



def get_cyan_level_dict_PC(config_params):
    num_sweep = config_params["sweeps"]
    num_runs = config_params["runs"]
    frames_per_sweep = config_params["frames_per_sweep"]
    num_frames = num_sweep * frames_per_sweep * num_runs
    frames = np.arange(0, num_frames, frames_per_sweep * num_sweep)
    # print(frames)
    levels = (
        np.logspace(
            np.log10(config_params["min_cyan_light"]),
            np.log10(config_params["max_cyan_light"]),
            len(frames),
        )
        .round()
        .astype(int)
    )

    cyan_level_dict = dict(zip(frames, levels))
    return cyan_level_dict



def update_events_cyan_dict(events, cyan_level_dict):
    new_events = []
    for event in events:
        # print(event)
        t = event["axes"]["time"]
        if t in cyan_level_dict:
            cyan_level = str(cyan_level_dict[t])
            event["properties"] = [
                ["Spectra", "Cyan_Level", cyan_level],
            ]
            
        new_events.append(event)
    return new_events


def update_events_yellow_and_cyan_dict(events, cyan_level_dict,yellow_level_dict):
    new_events = []
    for event in events:
        # print(event)
        t = event["axes"]["time"]
        if t in cyan_level_dict:
            cyan_level = str(cyan_level_dict[t])
            event["properties"] = [
                ["Spectra", "Cyan_Level", cyan_level],
            ]
        if t in yellow_level_dict:
            yellow_level = str(yellow_level_dict[t])
            event["properties"] = [
                ["Spectra", "Green_Level", yellow_level],
            ]            
        new_events.append(event)
    return new_events


def update_events_curve_dict(events, level_dict,color):
    new_events = []
    level_name = f"{color}_Level"
    for event in events:
        # print(event)
        t = event["axes"]["time"]
        if t in level_dict:
            light_level = str(level_dict[t])
            event["properties"] = [
                ["Spectra",level_name, light_level],
            ]
        new_events.append(event)
    return new_events



def verify_cell(cell_dict):
    valid_construct=['D910', 'D850', 'D871', 'D911', 'D839', 'D907', 'AAV349-1', 'AAV350-1', 'AAV358-1', 'D830', 'AAV359-1','AAV361-1', 'D830', 'D832', 'AAV357-1','D918','D919','Add12Con','AAV223','AAV362','AAV363', 'AAV366','AAV83','AAV367'
                     ]
    
    assert(cell_dict["construct"] in valid_construct)

    print("all good!")
# %%
def get_teal_level_dict_PC(config_params):
    num_sweep = config_params["sweeps"]
    num_runs = config_params["runs"]
    frames_per_sweep = config_params["frames_per_sweep"]
    num_frames = num_sweep * frames_per_sweep * num_runs
    frames = np.arange(0, num_frames, frames_per_sweep * num_sweep)
    # print(frames)
    levels = (
        np.logspace(
            np.log10(config_params["min_teal_light"]),
            np.log10(config_params["max_teal_light"]),
            len(frames),
        )
        .round()
        .astype(int)
    )

    teal_level_dict = dict(zip(frames, levels))
    return teal_level_dict


def update_events_yellow_and_cyan_dict_TEAL(events, cyan_level_dict,yellow_level_dict):
    new_events = []
    for event in events:
        # print(event)
        t = event["axes"]["time"]
        if t in cyan_level_dict:
            cyan_level = str(cyan_level_dict[t])
            event["properties"] = [
                ["Spectra", "Cyan_Level", cyan_level],
            ]
        if t in yellow_level_dict:
            yellow_level = str(yellow_level_dict[t])
            event["properties"] = [
                ["Spectra", "Teal_Level", yellow_level],
            ]            
        new_events.append(event)
    return new_events