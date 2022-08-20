from distutils.command.config import config
import numpy as np
import math
from scipy.interpolate import griddata
# import utils
import ConfigReader
import FileUtils

config = ConfigReader.GetModelConfig("./Temp/my_config.json")

low_data_path = config["low_data_path"]
high_data_path = config["high_data_path"]
grid_size = config["grid_size"] # 20
ms_radius = config["mean_shift_radius"] # 25
ms_bandwith = config["mean_shift_bandwith"] # 20
log_path = config["log_path"]
strange_num = config["strange_num"] # -200

# x=lon y=lat
def GetGridMap(x, y, size, region, min_lon, max_lon, min_lat, max_lat):
    min_p = [min_lon, min_lat]
    max_p = [max_lon, max_lat]
    for r in region:
        if r[0] <= min_p[0]:
            min_p[0] = r[0]
        if r[1] <= min_p[1]:
            min_p[1] = r[1]
        if r[0] >= max_p[0]:
            max_p[0] = r[0]
        if r[1] >= max_p[1]:
            max_p[1] = r[1]

    x = math.ceil((size - 1) * (x - min_p[0]) / (max_p[0] - min_p[0]))
    y = math.ceil((size - 1) * (y - min_p[1]) / (max_p[1] - min_p[1]))

    return x, y

#numpy X: (size, 4)  [time, longitude, latitude, value]
def GenerateLowHighPair(X, min_lon, max_lon, min_lat, max_lat, use_interpolation_scipy=False,generate_X=None,use_interpolation_lgb=False):
    """
    parameter:
        X: numpy (size, 4),  [time, longitude, latitude, value]
        generate_X: numpy (size, 4),  [time, longitude, latitude, value]
        min_lon: float, min value of longitude
        max_lon: float, max value of longitude
        min_lat: float, min value of latitude
        max_lat: float, max value of latitude
        use_interpolation_lgb: bool, 
            True : use lightgbm predict value to interpolation
            False : do not use lightgbm predict value to interpolation
     
    """
    low_quality_data = []
    high_quality_data = []

    # Generate Low and High
    for idx, t in enumerate(np.unique(X[:, 0])):
        FileUtils.WriteFile("Pair,{}\n".format((idx + 1) /len(np.unique(X[:, 0]))), log_path, "a")
        low_z = np.full((grid_size, grid_size), strange_num)
        high_z = np.full((grid_size, grid_size), strange_num)

        # Pad with real value by grid
        site_values = X[np.where(X[:, 0] == t), 1:][0]
        val = {}
        for site in site_values:
            dense_region = site_values[:,:2]
            i, j = GetGridMap(site[0], site[1], grid_size, dense_region, min_lon, max_lon, min_lat, max_lat)
            k = "%d,%d" % (i, j)
            if k in val:
                val[k].append(float(site[2]))
            else:
                val[k] = [float(site[2])]

        for k in val.keys():
            i, j = map(int, k.split(","))
            high_z[i][j] = np.mean(val[k])

        # Random Sample
        low_points = ""
        candidates = list(val.keys())
        already = []
        low_point_num = 60 # int(len(candidates) / 4)
        low_point_num = low_point_num if low_point_num<len(candidates) else len(candidates)-1
        for iter in range(low_point_num):
            flag = True
            k = ""
            while flag:
                k = candidates[np.random.randint(0, len(candidates) - 1)]
                if k not in already:
                    flag = False
            i, j = map(int, k.split(","))
            low_z[i][j] = high_z[i][j]
            high_z[i][j] = strange_num
            low_points += "{},{}\n".format(i, j)

        # print('generate data -------------------------')
        def interpolation_with_lgb(data):
            generate_site_values = generate_X[np.where(generate_X[:, 0] == t), 1:][0]
            generate_val = {}

            for site in generate_site_values:
                dense_region = generate_site_values[:,:2]
                i, j = GetGridMap(site[0], site[1], grid_size, dense_region, min_lon, max_lon, min_lat, max_lat)
                k = "%d,%d" % (i, j)
                if k in generate_val:
                    generate_val[k].append(float(site[2]))
                else:
                    generate_val[k] = [float(site[2])]

            for k in generate_val.keys():
                i, j = map(int, k.split(","))
                if data[i][j] == strange_num:
                    data[i][j] = np.mean(generate_val[k])
            return data

        # Cubic Interpolation
        def interpolation(data):
            points, values, grid = [], [], []
            for i in range(grid_size):
                for j in range(grid_size):
                    grid.append([i, j])
                    if data[i][j] != strange_num:
                        points.append([i, j])
                        values.append(data[i][j])
            points = np.array(points)
            values = np.array(values)
            grid = np.array(grid)

            z = griddata(points, values, grid, method='nearest')
            return z.reshape((grid_size, grid_size))

        try:
            if use_interpolation_scipy:
                if use_interpolation_lgb:
                    low_z = interpolation_with_lgb(low_z)
                    high_z = interpolation_with_lgb(high_z)
                low_z = interpolation(low_z)
                high_z = interpolation(high_z)
            else:
                if use_interpolation_lgb:
                    low_z = interpolation_with_lgb(low_z)
                    high_z = interpolation_with_lgb(high_z)

        except Exception as e:
            continue

        low_quality_data.append(low_z)
        high_quality_data.append(high_z)

    FileUtils.WriteFile("Pair,Fin\n", log_path, "a")
    low_quality_data = np.array(low_quality_data)
    high_quality_data = np.array(high_quality_data)
    np.save(low_data_path, low_quality_data)
    np.save(high_data_path, high_quality_data)



#numpy X: (size, 4)  [time, longitude, latitude, value]
def GenerateLowHighPair2(X, min_lon, max_lon, min_lat, max_lat, use_interpolation_scipy=False,generate_X=None,use_interpolation_lgb=False):
    """
    parameter:
        X: numpy (size, 4),  [time, longitude, latitude, value]
        generate_X: numpy (size, 4),  [time, longitude, latitude, value]
        min_lon: float, min value of longitude
        max_lon: float, max value of longitude
        min_lat: float, min value of latitude
        max_lat: float, max value of latitude
        use_interpolation_lgb: bool, 
            True : use lightgbm predict value to interpolation
            False : do not use lightgbm predict value to interpolation
     
    """
    # low_quality_data = []
    high_quality_data = []

    # Generate Low and High
    for idx, t in enumerate(np.unique(X[:, 0])):
        FileUtils.WriteFile("Pair,{}\n".format((idx + 1) /len(np.unique(X[:, 0]))), log_path, "a")
        # low_z = np.full((grid_size, grid_size), strange_num)
        high_z = np.full((grid_size, grid_size), strange_num)

        # Pad with real value by grid
        site_values = X[np.where(X[:, 0] == t), 1:][0]
        val = {}
        for site in site_values:
            dense_region = site_values[:,:2]
            i, j = GetGridMap(site[0], site[1], grid_size, dense_region, min_lon, max_lon, min_lat, max_lat)
            k = "%d,%d" % (i, j)
            if k in val:
                val[k].append(float(site[2]))
            else:
                val[k] = [float(site[2])]

        for k in val.keys():
            i, j = map(int, k.split(","))
            high_z[i][j] = np.mean(val[k])

        # # Random Sample
        # low_points = ""
        # candidates = list(val.keys())
        # already = []
        # low_point_num = 60 # int(len(candidates) / 4)
        # low_point_num = low_point_num if low_point_num<len(candidates) else len(candidates)-1
        # for iter in range(low_point_num):
        #     flag = True
        #     k = ""
        #     while flag:
        #         k = candidates[np.random.randint(0, len(candidates) - 1)]
        #         if k not in already:
        #             flag = False
        #     i, j = map(int, k.split(","))
        #     low_z[i][j] = high_z[i][j]
        #     high_z[i][j] = strange_num
        #     low_points += "{},{}\n".format(i, j)

        # print('generate data -------------------------')
        def interpolation_with_lgb(data):
            generate_site_values = generate_X[np.where(generate_X[:, 0] == t), 1:][0]
            generate_val = {}

            for site in generate_site_values:
                dense_region = generate_site_values[:,:2]
                i, j = GetGridMap(site[0], site[1], grid_size, dense_region, min_lon, max_lon, min_lat, max_lat)
                k = "%d,%d" % (i, j)
                if k in generate_val:
                    generate_val[k].append(float(site[2]))
                else:
                    generate_val[k] = [float(site[2])]

            for k in generate_val.keys():
                i, j = map(int, k.split(","))
                if data[i][j] == strange_num:
                    data[i][j] = np.mean(generate_val[k])
            return data

        # Cubic Interpolation
        def interpolation(data):
            points, values, grid = [], [], []
            for i in range(grid_size):
                for j in range(grid_size):
                    grid.append([i, j])
                    if data[i][j] != strange_num:
                        points.append([i, j])
                        values.append(data[i][j])
            points = np.array(points)
            values = np.array(values)
            grid = np.array(grid)

            # z = griddata(points, values, grid, method='nearest')
            z = griddata(points, values, grid, method='cubic')
            return z.reshape((grid_size, grid_size))

        try:
            if use_interpolation_scipy:
                if use_interpolation_lgb:
                    # low_z = interpolation_with_lgb(low_z)
                    high_z = interpolation_with_lgb(high_z)
                # low_z = interpolation(low_z)
                high_z = interpolation(high_z)
            else:
                if use_interpolation_lgb:
                    # low_z = interpolation_with_lgb(low_z)
                    high_z = interpolation_with_lgb(high_z)

        except Exception as e:
            continue

        # low_quality_data.append(low_z)
        high_quality_data.append(high_z)

    FileUtils.WriteFile("Pair,Fin\n", log_path, "a")
    # low_quality_data = np.array(low_quality_data)
    high_quality_data = np.array(high_quality_data)
    # np.save(low_data_path, low_quality_data)
    # np.save(high_data_path, high_quality_data)

    if use_interpolation_scipy:
        np.save(high_data_path, high_quality_data)
    else:
        np.save(low_data_path, high_quality_data)
