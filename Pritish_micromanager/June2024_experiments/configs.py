config_params_all_optical = {
    "sweeps" : 5,
    "frames_per_sweep":600,
    "min_yellow_light":4, 
    "max_yellow_light":50, 
    "light_intensity_cyan":30 
    }



config_params_jedi = {
    "sweeps" : 14,
    "frames_per_sweep":60,
    "light_intensity_cyan":30 
    }


config_params_all_optical_flipped = {
    "sweeps" : 5,
    "frames_per_sweep":600,
    "min_yellow_light":5, #actually cyan
    "max_yellow_light":50, #actually cyan
    "light_intensity_cyan":15 #actually yellow
    }


config_params_gcamp_exc = {
    "sweeps" : 1,
    "runs" : 3,
    "frames_per_sweep":1020,
    # "frames_per_sweep":360, #for cell attached
    "min_cyan_light":5,
    "max_cyan_light":5,
    "light_intensity_cyan":5
    }

config_params_chrimson_pc = {
    "sweeps" : 10,
    "runs" : 5,
    "frames_per_sweep":2,
    "min_yellow_light":3,
    "max_yellow_light":20,
    }


config_params_chrimson_CT = {
    "sweeps" : 2,
    "runs" : 9,
    "frames_per_sweep":2,
    "min_cyan_light":2,
    "max_cyan_light":20,
    }


config_params_chrimson_linear = {
    "sweeps" : 100,
    "runs" : 1,
    "frames_per_sweep":4,
    "min_yellow_light":1,
    "max_yellow_light":100,
    }


config_params_chrimson_linear_cyan = {
    "sweeps" : 100,
    "runs" : 1,
    "frames_per_sweep":4,
    "min_yellow_light":1,
    "max_yellow_light":100,
    }


config_params_chrimson_pc_ct = {
    "runs":6,
    "sweeps" : 1,
    "frames_per_sweep":20,
    "min_yellow_light":2,
    "max_yellow_light":100,
    "min_cyan_light":1,
    "max_cyan_light":100,

    }

config_params_GTARC2_yellow_cyan = {
    "runs":6,
    "sweeps" : 1,
    "frames_per_sweep":5,
    "min_yellow_light":2,
    "max_yellow_light":22,
    "min_cyan_light":1,
    "max_cyan_light":4,

    }

config_params_chrmine_pc = {
    "runs":4,
    "sweeps" : 1,
    "frames_per_sweep":20,
    "min_teal_light":1,
    "max_teal_light":100,
    "min_cyan_light":1,
    "max_cyan_light":1,

    }

config_params_spiking_diff_hz = {
    "runs":1,
    "sweeps" : 1,
    "frames_per_sweep":5,
    "min_teal_light":30,
    "max_teal_light":30,
    "min_cyan_light":12,
    "max_cyan_light":12,

    }