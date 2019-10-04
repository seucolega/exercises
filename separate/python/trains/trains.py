class NoSuchRoute(Exception):
    pass


class Route:
    def __init__(self, origin, destination, distance=None):
        self._origin = origin
        self._destination = destination
        self._distance = distance

    @property
    def origin(self) -> str:
        return self._origin

    @property
    def destination(self) -> str:
        return self._destination

    @property
    def distance(self) -> int:
        return self._distance

    def is_the_same_route(self, other_route: 'Route') -> bool:
        return self._origin == other_route._origin and self._destination == other_route._destination


class Railroad:
    def __init__(self):
        self._routes: [Route] = []

        self.add_route('AB5')
        self.add_route('BC4')
        self.add_route('CD8')
        self.add_route('DC8')
        self.add_route('DE6')
        self.add_route('AD5')
        self.add_route('CE2')
        self.add_route('EB3')
        self.add_route('AE7')

    @property
    def routes(self) -> [Route]:
        return self._routes

    def add_route(self, route: str):
        origin = route[0]
        destination = route[1]
        distance = int(route[2])
        self._routes.append(Route(origin, destination, distance))

    def distance(self, trip: str) -> str:
        try:
            distance = 0
            for route in self.trip_to_routes(trip):
                routes = [r.distance for r in self.routes if r.is_the_same_route(route)]
                if not len(routes):
                    raise NoSuchRoute
                distance += sum(routes)
            return str(distance)
        except NoSuchRoute:
            return 'NO SUCH ROUTE'

    def get_routes(self, trip):
        pass

    @staticmethod
    def trip_to_routes(trip: str) -> [Route]:
        towns = list(trip.upper())
        origins = towns[:-1]
        destinations = towns[1:]
        return [Route(origin, destination) for origin, destination in zip(origins, destinations)]

    def next_destinations(self, origin: str) -> list:
        town = origin[-1].upper()
        return [r.destination for r in self.routes if r.origin == town]

    def all_next_destinations(self, origin: str, stops: int) -> list:
        origins = [origin.upper()]
        all_destinations = []
        for _ in range(0, stops):
            next_destinations = []
            for origin in origins:
                next_destinations.extend([origin + d for d in self.next_destinations(origin)])
            origins = next_destinations
            all_destinations.extend(next_destinations)
        return list(set(all_destinations))

    def find_routes(self, origin: str, destination: str, max_stops: int, min_stops: int = 1) -> list:
        routes = self.all_next_destinations(origin, max_stops)
        return [d for d in routes if
                d[0] == origin and d[-1] == destination and min_stops <= len(d) - 1 <= max_stops]

    def filter_routes_by_distance(self, routes: list, min_distance: int, max_distance: int):
        return [d for d in routes if min_distance < int(self.distance(d)) < max_distance]

    def shortest_route_distance(self, origin: str, destination: str):
        routes = self.find_routes(origin, destination, 3)
        routes_with_distances = {int(self.distance(r)): r for r in routes}
        return sorted(routes_with_distances.keys())[0]
