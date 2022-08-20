import json
import os

def MakeDir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def GetModelConfig(json_file='./Temp/my_config.json'):
    MakeDir("./Temp")
    if os.path.exists(json_file):
        f = open("./Temp/my_config.json", "r")
        config = json.loads(f.read().strip())
        return config
    else:
        f = open("./Temp/my_config.json", "w")
        config = {}
        config["grid_size"] = 20
        config["generator_lr"] = 0.001
        config["discriminator_lr"] = 0.001
        config["pre_train_epoch"] = 1
        config["train_epoch"] = 1
        config["batch_size"] = 20
        config["mean_shift_radius"] = 25
        config["mean_shift_bandwith"] = 20
        config["strange_num"]=-200
        config["low_data_path"] = "Temp/low_data.npy"
        config["high_data_path"] = "Temp/high_data.npy"
        config["model_out_path"] = "Temp/SI-AGAN.pth"
        config["log_path"] = "Temp/SI-AGAN-log.txt"
        f.write(json.dumps(config))
        f.close()
        return config


    