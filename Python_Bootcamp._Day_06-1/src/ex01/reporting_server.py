import grpc
import random
import ship_pb2
import ship_pb2_grpc
from concurrent import futures

officers_names = ('John', 'Mary', 'David', 'Karen', 'Steven', 'Alan')
officers_surnames = ('Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Shepard')
officers_ranks = ('Captain', 'Lieutenant', 'Sergeant', 'Commander')

enemies_spaceships = ('Death Star', 'Executor', 'Star Destroyer', 'Imperial Shuttle', 'Unknown')
ally_spaceships = ('Normandy', 'X-Wing', 'Millennium Falcon')


def get_officer():
    return {
        "first_name": random.choice(officers_names),
        "last_name": random.choice(officers_surnames),
        "rank": random.choice(officers_ranks)
    }


def ship_init():
    ship = ship_pb2.SpaceShip()
    ship.alignment = random.randint(0, 1)
    if ship.alignment == 1:
        ship.name = random.choice(enemies_spaceships)
        officers_num = random.randint(0, 10)
    else:
        ship.name = random.choice(ally_spaceships)
        officers_num = random.randint(1, 10)
    ship.ship_class = random.randint(0, 5)
    ship.length = round(random.uniform(80.0, 20000.0), 1)
    ship.crew_size = random.randint(4, 500)
    ship.armed = random.randint(0, 1)
    result_value = {
        'alignment': ship.alignment,
        'name': ship.name,
        'ship_class': ship.ship_class,
        'length': ship.length,
        'crew_size': ship.crew_size,
        'armed': ship.armed,
        'officers': [get_officer() for _ in range(officers_num)]
    }
    return result_value


class Service(ship_pb2_grpc.UnaryServicer):
    def GetServerResponse(self, request, context):
        ships = [ship_pb2.SpaceShip(**ship_init()) for _ in range(random.randint(0, 10))]
        yield from ships


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    ship_pb2_grpc.add_UnaryServicer_to_server(Service(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    print('Server Started')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
