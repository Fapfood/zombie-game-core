from math import sin, asin, cos, atan2, radians, degrees

"""
https://geojson.org/geojson-spec.html

multipolygon = list of polygons
polygon = list of rings (basic and holes)
ring = list of points
point = list of two coordinates

The order of elements must follow x, y, z order... longitude, latitude, altitude for coordinates

For type "Point", the "coordinates" member must be a single position.
For type "LineString", the "coordinates" member must be an array of two or more positions.
A LinearRing is closed LineString with 4 or more positions.
The first and last positions are equivalent (they represent equivalent points).
Though a LinearRing is not explicitly represented as a GeoJSON geometry type,
it is referred to in the Polygon geometry type definition.
For type "Polygon", the "coordinates" member must be an array of LinearRing coordinate arrays.
For Polygons with multiple rings, the first must be the exterior ring and any others must be interior rings or holes.
For type "MultiPolygon", the "coordinates" member must be an array of Polygon coordinate arrays.
"""


class Shape:
    base = None

    def __init__(self, coords):
        self.coords = coords

    def coordinates(self):
        return self.coords

    @classmethod
    def from_list(cls, lis):
        return cls(*(cls.base.from_list(el) for el in lis))


class Point(Shape):
    def __init__(self, long, lat):
        self.long = long
        self.lat = lat
        coords = [self.long, self.lat]
        super().__init__(coords)

    @classmethod
    def from_list(cls, lis):
        return Point(lis[0], lis[1])


class Ring(Shape):
    base = Point

    def __init__(self, *args):
        self.points = args
        coords = [p.coordinates() for p in self.points]
        super().__init__(coords)


class Polygon(Shape):
    base = Ring

    def __init__(self, *args):
        self.rings = args
        coords = [r.coordinates() for r in self.rings]
        super().__init__(coords)


class MultiPolygon(Shape):
    base = Polygon

    def __init__(self, *args):
        self.polygons = args
        coords = [p.coordinates() for p in self.polygons]
        super().__init__(coords)


def is_point_inside_path(point, path) -> bool:
    """
    EVEN-ODD EXPLAINED: http://esri.github.io/geometry-api-java/doc/Polygon.html
    WIKIPEDIA CODE: https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule
    """
    x, y = point
    res = False
    prev_el_x, prev_el_y = path[-1]
    for el in path:
        el_x, el_y = el
        if ((el_y > y) != (prev_el_y > y)) and \
                (x < el_x + (prev_el_x - el_x) * (y - el_y) / (prev_el_y - el_y)):
            res = not res
        prev_el_x, prev_el_y = el_x, el_y
    return res


def is_point_inside_multipolygon(point, multipolygon) -> bool:
    multipolygon = multipolygon.coordinates()
    res = False
    for polygon in multipolygon:
        for path in polygon:
            if is_point_inside_path(point, path):
                res = not res
    return res


def move(point, distance, bearing):
    lon, lat = point
    lat = radians(lat)
    lon = radians(lon)
    d = distance / 6371000
    b = radians(bearing)
    new_lat = asin(sin(lat) * cos(d) + cos(lat) * sin(d) * cos(b))
    new_lon = lon + atan2(sin(b) * sin(d) * cos(lat), cos(d) - sin(lat) * sin(new_lat))
    res = degrees(new_lon), degrees(new_lat)
    return res


def ring_regular(middle, radius, vertex_number, angle_offset=0):
    step = 360 / vertex_number
    res = []
    for i in range(vertex_number):
        bearing = (angle_offset + step * i) % 360
        m = move(middle, radius, bearing)
        res.append(m)
    res.append(res[0])
    ring = Ring.from_list(res)
    return ring


def ring_isosceles_triangle(vertex, side, angle_offset=0):
    res = [vertex]
    bearing = (angle_offset + 0) % 360
    m = move(vertex, side, bearing)
    res.append(m)
    bearing = (angle_offset + 90) % 360
    m = move(vertex, side, bearing)
    res.append(m)
    res.append(res[0])
    ring = Ring.from_list(res)
    return ring
