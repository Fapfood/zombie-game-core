from .shape_helper import Point, Ring, Polygon, MultiPolygon


class ShapeService:
    def __init__(self, pointDao, ringDao, polygonDao, multipolygonDao):
        self.pointDao = pointDao
        self.ringDao = ringDao
        self.polygonDao = polygonDao
        self.multipolygonDao = multipolygonDao

    def create_multipolygon(self, multipolygon):
        multipolygon_record = self.multipolygonDao.create()
        for i, polygon in enumerate(multipolygon.polygons):
            polygon_record = self.polygonDao.create(order=i, multipolygon_id=multipolygon_record.id)
            for j, ring in enumerate(polygon.rings):
                ring_record = self.ringDao.create(order=j, polygon_id=polygon_record.id)
                for k, point in enumerate(ring.points):
                    self.pointDao.create(order=k, long=point.long, lat=point.lat, ring_id=ring_record.id)
        return multipolygon_record

    def read_multipolygon(self, id):
        multipolygon_record = self.multipolygonDao.read_by_id(id)
        polygons = []
        for polygon_record in multipolygon_record.polygons:
            rings = []
            for ring_record in polygon_record.rings:
                points = []
                for point_record in ring_record.points:
                    point = Point(point_record.long, point_record.lat)
                    points.append(point)
                ring = Ring(*points)
                rings.append(ring)
            polygon = Polygon(*rings)
            polygons.append(polygon)
        multipolygon = MultiPolygon(*polygons)
        return multipolygon
