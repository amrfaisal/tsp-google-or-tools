"""Linear optimization example"""
#!/usr/bin/python3

from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

# Distance callback


def create_distance_callback(dist_matrix):
    # Create a callback to calculate distances between cities.

    def distance_callback(from_node, to_node):
        return int(dist_matrix[from_node][to_node])

    return distance_callback


def main():
    # Cities
    city_names = ["New York", "Los Angeles", "Chicago", "Minneapolis", "Denver", "Dallas", "Seattle",
                  "Boston", "San Francisco", "St. Louis", "Houston", "Phoenix", "Salt Lake City"]
    # Distance matrix
    dist_matrix = [
        [0, 2451,  713, 1018, 1631, 1374, 2408,  213,
            2571,  875, 1420, 2145, 1972],  # New York
        [2451,    0, 1745, 1524,  831, 1240,  959, 2596,
         403, 1589, 1374,  357,  579],  # Los Angeles
        [713, 1745,    0,  355,  920,  803, 1737,  851,
         1858,  262,  940, 1453, 1260],  # Chicago
        [1018, 1524,  355,    0,  700,  862, 1395, 1123,
         1584,  466, 1056, 1280,  987],  # Minneapolis
        [1631,  831,  920,  700,    0,  663, 1021, 1769,
         949,  796,  879,  586,  371],  # Denver
        [1374, 1240,  803,  862,  663,    0, 1681, 1551,
         1765,  547,  225,  887,  999],  # Dallas
        [2408,  959, 1737, 1395, 1021, 1681,    0, 2493,
         678, 1724, 1891, 1114,  701],  # Seattle
        [213, 2596,  851, 1123, 1769, 1551, 2493,    0,
         2699, 1038, 1605, 2300, 2099],  # Boston
        [2571,  403, 1858, 1584,  949, 1765,  678, 2699,
         0, 1744, 1645,  653,  600],  # San Francisco
        [875, 1589,  262,  466,  796,  547, 1724, 1038,
         1744,    0,  679, 1272, 1162],  # St. Louis
        [1420, 1374,  940, 1056,  879,  225, 1891, 1605,
         1645,  679,    0, 1017, 1200],  # Houston
        [2145,  357, 1453, 1280,  586,  887, 1114, 2300,
         653, 1272, 1017,    0,  504],  # Phoenix
        [1972,  579, 1260,  987,  371,  999,  701, 2099,  600, 1162,  1200,  504,   0]]  # Salt Lake City

    tsp_size = len(city_names)
    num_routes = 1
    depot = 0

    # Create routing model
    if tsp_size > 0:
        routing = pywrapcp.RoutingModel(tsp_size, num_routes, depot)
        search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
        # Create the distance callback.
        dist_callback = create_distance_callback(dist_matrix)
        routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
        # Solve the problem.
        assignment = routing.SolveWithParameters(search_parameters)
        if assignment:
            # Solution distance.
            print("Total distance: " +
                  str(assignment.ObjectiveValue()) + " miles\n")
            # Display the solution.
            # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1
            route_number = 0
            # Index of the variable for the starting node.
            index = routing.Start(route_number)
            route = ''
            while not routing.IsEnd(index):
                # Convert variable indices to node indices in the displayed route.
                route += str(city_names[routing.IndexToNode(index)]) + ' -> '
                index = assignment.Value(routing.NextVar(index))
            route += str(city_names[routing.IndexToNode(index)])
            print("Route:\n\n" + route)
        else:
            print('No solution found.')
    else:
        print('Specify an instance greater than 0.')


if __name__ == '__main__':
    main()
