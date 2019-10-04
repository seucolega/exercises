import unittest
import trains


class TrainsTest(unittest.TestCase):
    def test_distance_input_1(self):
        railroad = trains.Railroad()
        self.assertEqual(railroad.distance('AB'), '5')

    def test_distance_input_2(self):
        railroad = trains.Railroad()
        self.assertEqual(railroad.distance('BC'), '4')

    def test_distance_input_3(self):
        railroad = trains.Railroad()
        self.assertEqual(railroad.distance('CD'), '8')

    def test_distance_input_4(self):
        railroad = trains.Railroad()
        self.assertEqual(railroad.distance('DC'), '8')

    def test_distance_input_5(self):
        railroad = trains.Railroad()
        self.assertEqual(railroad.distance('DE'), '6')

    def test_distance_input_6(self):
        railroad = trains.Railroad()
        self.assertEqual(railroad.distance('AD'), '5')

    def test_distance_input_7(self):
        railroad = trains.Railroad()
        self.assertEqual(railroad.distance('CE'), '2')

    def test_distance_input_8(self):
        railroad = trains.Railroad()
        self.assertEqual(railroad.distance('EB'), '3')

    def test_distance_input_9(self):
        railroad = trains.Railroad()
        self.assertEqual(railroad.distance('AE'), '7')

    def test_distance_aba(self):
        """
        The distance of the route A-B-C.
        """
        railroad = trains.Railroad()
        self.assertEqual(railroad.distance('ABC'), '9')

    def test_distance_ad(self):
        """
        The distance of the route A-D.
        """
        railroad = trains.Railroad()
        self.assertEqual(railroad.distance('AD'), '5')

    def test_distance_adc(self):
        """
        The distance of the route A-D-C.
        """
        railroad = trains.Railroad()
        self.assertEqual(railroad.distance('ADC'), '13')

    def test_distance_aebcd(self):
        """
        The distance of the route A-E-B-C-D.
        """
        railroad = trains.Railroad()
        self.assertEqual(railroad.distance('AEBCD'), '22')

    def test_distance_aed(self):
        """
        The distance of the route A-E-D.
        """
        railroad = trains.Railroad()
        self.assertEqual(railroad.distance('AED'), 'NO SUCH ROUTE')

    def test_trips_starting_and_ending_with_c_by_3_stops(self):
        """
        The number of trips starting at C and ending at C with a maximum of 3 stops. In the sample data below,
        there are two such trips: C-D-C (2 stops). and C-E-B-C (3 stops).
        """
        railroad = trains.Railroad()
        self.assertEqual(sorted(railroad.find_routes('C', 'C', 3)), sorted(['CDC', 'CEBC']))

    def test_trips_starting_at_a_and_ending_at_c_by_4_stops(self):
        """
        The number of trips starting at A and ending at C with exactly 4 stops. In the sample data below,
        there are three such trips: A to C (via B,C,D); A to C (via D,C,D); and A to C (via D,E,B).
        """
        railroad = trains.Railroad()
        self.assertEqual(sorted(railroad.find_routes('A', 'C', 4, 4)), sorted(['ABCDC', 'ADCDC', 'ADEBC']))

    def test_shortest_route_from_a_to_c(self):
        """
        The length of the shortest route (in terms of distance to travel) from A to C.
        """
        railroad = trains.Railroad()
        self.assertEqual(railroad.shortest_route_distance('A', 'C'), 9)

    def test_shortest_route_from_b_to_b(self):
        """
        The length of the shortest route (in terms of distance to travel) from B to B.
        """
        railroad = trains.Railroad()
        self.assertEqual(railroad.shortest_route_distance('B', 'B'), 9)

    def test_different_routes_from_c_to_c_and_distance_less_than_30(self):
        """
        The number of different routes from C to C with a distance of less than 30. In the sample data,
        the trips are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC, CEBCEBC, CEBCEBCEBC.
        """
        railroad = trains.Railroad()
        routes = railroad.find_routes('C', 'C', 9)
        routes = railroad.filter_routes_by_distance(routes, 0, 30)
        self.assertEqual(len(routes), 7)


if __name__ == '__main__':
    unittest.main()
