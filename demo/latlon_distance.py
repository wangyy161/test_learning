import math
import numpy as np
from math import tan, atan, radians, cos, sin, asin, sqrt, pi, log, acos

print(360000 * tan(60 * pi / 180))
print(8100000000* pi)
aa = (8100000000 * pi) ** 0.5
90000/(2**0.5)
print(aa)
def MillierConvertion(lon, lat):
    W = 6381372 * pi * 2
    H = W / 2
    mill = 2.3
    x = lon * pi / 180
    y = lat * pi / 180
    y = 1.25 * log(tan(0.25 * pi + 0.4 * y))
    x = (W / 2) + (W / (2 * pi)) * x
    y = (H / 2) - (H / (2 * mill)) * y
    return x, y
def CalculateCos(x, y):
    if len(x) != len(y):
        print("error input x and y is not in the same sapce ")
    result1 = 0.0
    result2 = 0.0
    result3 = 0.0
    for i in range(len(x)):
        result1 += x[i] * y[i]
        result2 += x[i] ** 2
        result3 += y[i] ** 2

    costheta = result1 / ((result2 * result3) ** 0.5)
    theta = acos(costheta)
    return theta

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r * 1000
if __name__ == '__main__':
    # BaseLocationLat = 120.35954044358253
    # BaseLocationLon = 27.71087962254251
    # AirPositionLat = 123.43796418514975
    # AirPositionLon = 26.34512910292743
    # TargetPositionLat = 120.54712087675536
    # TargetPositionLon = 27.772205076389456

    BaseLocationLon = 120.3704182659909
    BaseLocationLat = 27.50420099678358
    AirPositionLon = 120.53587493389284
    AirPositionLat = 27.575921476594814
    TargetPositionLon = 122.77985592944368
    TargetPositionLat = 26.30764053186346

    bas_x, bas_y = MillierConvertion(BaseLocationLon, BaseLocationLat)
    print("基地坐标为：(%f, %f) \n" %(bas_x ,bas_y))
    tar_x, tar_y = MillierConvertion(TargetPositionLon, TargetPositionLat)
    print("目标坐标为：(%f, %f) \n" % (tar_x, tar_y))
    air_x, air_y = MillierConvertion(AirPositionLon, AirPositionLat)
    print("飞机坐标为：(%f, %f) \n" % (air_x, air_y))
    tar_to_air = [air_x - tar_x, air_y - tar_y]
    tar_to_bas = [bas_x - tar_x, bas_y - tar_y]
    air_to_bas = [bas_x - air_x, bas_y - air_y]

    theta = CalculateCos(tar_to_air, tar_to_bas)

    t2a_vecmo = np.linalg.norm(tar_to_air)
    print("米勒公式---飞机到目标的距离为：%f \n" % t2a_vecmo)
    t2b_vecmo = np.linalg.norm(tar_to_bas)
    print("米勒公式---基地到目标的距离为：%f \n" % t2b_vecmo)
    a2b_vecmo = np.linalg.norm(air_to_bas)
    print("米勒公式---飞机到基地的距离为：%f \n" % a2b_vecmo)
    t2a_dis = haversine(TargetPositionLon, TargetPositionLat, AirPositionLon, AirPositionLat)
    print("经纬度求解---飞机到目标的距离为：%f \n" % t2a_dis)
    t2b_dis = haversine(TargetPositionLon, TargetPositionLat, BaseLocationLon, BaseLocationLat)
    print("经纬度求解---基地到目标的距离为：%f \n" % t2b_dis)
    a2b_dis = haversine(AirPositionLon, AirPositionLat, BaseLocationLon, BaseLocationLat)
    print("经纬度求解---飞机到基地的距离为：%f \n" % a2b_dis)
    if theta > pi / 3:
        print(False)
    elif t2a_vecmo > t2b_vecmo:
        print(False)
    elif t2a_dis > t2b_dis:
        print('########### dis #####')
    else:
        print(True)
tan((45/180) * pi )