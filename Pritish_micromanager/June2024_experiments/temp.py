#%%
import numpy as np
import matplotlib.pyplot as plt
from pycromanager import Acquisition, multi_d_acquisition_events
from pathlib import Path
# %%
from pycromanager import Core,Studio
import time

mmc =Core()
# mmStudio = Studio()
# %%
str_save_path=r"""C:\Users\oferlab\Documents\CODE\temp_acq/"""
name = "pycromanager test"
sweep_frames=600
num_sweeps=5
num_frames=sweep_frames*num_sweeps

# %%
events = multi_d_acquisition_events(
                                    num_time_points=num_frames, time_interval_s=0.001,
                                    # channel_group='camera_ex_trigger', channels=['PClamp_trig'],
                                    # z_start=0, z_end=1, z_step=0.4,
    # keep_shutter_open_between_channels =True,
    # keep_shutter_open_between_z_steps = True,
    # channel_exposures_ms=[3.0],
    # exposure= 4,

                                    # order='tcz'
                                    )
new_events=events
events[1:10]
# %%
frames=np.arange(0,num_frames,sweep_frames)
print(frames)
levels=np.logspace(np.log10(5),2,len(frames)).round().astype(int)

cyan_level_dict=dict(zip(frames,levels))
for k,v in cyan_level_dict.items():
    print(k,v)


#%%
new_events=[]
for event in events:
    print(event)
    t =event['axes']['time']
    if  t in cyan_level_dict:
        # cyan_level=str(cyan_level_dict[t])
        # mmc.set_property("Spectra","Cyan_Level",cyan_level)
        # print("cyan level",t,cyan_level)
        # print("")
        cyan_level=str(cyan_level_dict[t])
        event['properties']= [['Spectra', 'Green_Level', cyan_level],]
    sweep,f_sweep =divmod(t,sweep_frames)
    print(sweep)
    # event['min_start_time']+=sweep*(13.0-5)
        # print(event)
    # break
    new_events.append(event)
    # break
new_events
#%%
# def hook_fn(event):
#     # print(event)
#     t=event['axes']['time']
#     print(t, end =" ")
#     if  t in cyan_level_dict:
#         cyan_level=str(cyan_level_dict[t])
#         mmc.set_property("Spectra","Cyan_Level",cyan_level)
#         print("cyan level",t,cyan_level)
#         print("")
#     return event

# pass in the function as a post_hardware_hook
# with Acquisition(directory='/path/to/saving/dir', name='acquisition_name',
#                 ) as acq:



mmc.set_config("camera_ex_trigger","PClamp_trig")
time.sleep(5)

# %%
save_path = Path(str_save_path)
mmc.set_property("Spectra","Cyan_Level",str(10))
mmc.set_property("Spectra","Green_Level",str(10))

time.sleep(1.0)

with Acquisition(
    directory=save_path.absolute().as_posix(), 
    name="all_optical_60_fps"
    # post_hardware_hook_fn=hook_fn
    ) as acq:
    acq.acquire(new_events)


# save_path = Path(str_save_path)
# mmc.set_property("Spectra","Cyan_Level",str(10))
# mmc.set_property("Spectra","Green_Level",str(100))

# time.sleep(1.0)

# with Acquisition(
#     directory=save_path.absolute().as_posix(), 
#     name="all_optical_split2"
#     # post_hardware_hook_fn=hook_fn
#     ) as acq:
#     acq.acquire(new_events)

# # %%

# %%
#read data

from pycromanager import Dataset

# %%

with Acquisition(    directory=save_path.absolute().as_posix(), 
    name="all_optical_60_fps_2") as acq:

        ### send some instructions so something is acquired ######

        dataset = acq.get_dataset()
# %%

#This path is to the top level of the dataset
data_path = r'C:\Users\oferlab\Documents\CODE\temp_acq\all_optical_60_fps_2'

dataset = Dataset(data_path)
# %%
plt.plot(np.diff(et))
plt.ylim(-10,25)
# %%



