import math
import numpy
def MillierConvertion(lon, lat):
    earth_longth = 6381372 * math.pi * 2
    W = earth_longth
    H = earth_longth / 2
    mill = 2.3
    x = lon * math.pi / 180
    y = lat * math.pi / 180
    y = 1.25 * math.log(math.tan(0.25 * math.pi + 0.4 * y))
    x = (W / 2) + (W / (2 * math.pi)) * x
    y = (H / 2) - (H / (2 * mill)) * y
    result = numpy.zeros(2)
    result[0] = x
    result[1] = y
    return result
def MillierConvertion1(x, y):
    W = 6381372 * math.pi * 2
    H = W / 2
    mill = 2.3
    lat = ((H / 2 - y) * 2 * mill) / (1.25 * H)
    lat = ((math.atan(math.exp(lat)) - 0.25 * math.pi) * 180) / (0.4 * math.pi)
    lon = (x - W / 2) * 360 / W
    result = numpy.zeros(2)
    result[0] = lon
    result[1] = lat
    return result
if __name__ == "__main__":
    lon, lat = 0, 0
    x, y = MillierConvertion(lon, lat)
    print(x, y)
    lon, lat = MillierConvertion1(x, y)
    print(lon, lat)