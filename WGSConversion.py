import math


class WGSConversion:
    lat0 = 0
    lon0 = 0
    deltaX = 0
    deltaY = 0
    hasLinearizationPoint = False

    def setOrigin(self, latitude, longitude):
        self.lat0 = latitude
        self.lon0 = longitude

        a = 6378137.0
        f = 1.0 / 298.257223563
        b = a * (1.0 - f)
        a2 = a * a
        b2 = b * b

        sin_lat = math.sin(math.pi / 180.0 * latitude)
        cos_lat = math.cos(math.pi / 180.0 * latitude)

        tmp = math.sqrt(a2 * cos_lat * cos_lat + b2 * sin_lat * sin_lat)

        self.deltaX = (math.pi / 180.0) * (a2 / tmp) * cos_lat
        self.deltaY = (math.pi / 180.0) * (a2 * b2 / (tmp * tmp * tmp))

        self.hasLinearizationPoint = True

    def calculateENLongitude(self, longitude):
        return self.deltaX * (longitude - self.lon0)

    def calculateENLatitude(self, latitude):
        return self.deltaY * (latitude - self.lat0)

    def WGStoEN(self, latitude, longitude):
        if not self.hasLinearizationPoint:
            "Origin hasn't been set before the conversion"
        else:
            temp_latitude = self.calculateENLatitude(latitude)
            temp_longitude = self.calculateENLongitude(longitude)

            return temp_latitude, temp_longitude

