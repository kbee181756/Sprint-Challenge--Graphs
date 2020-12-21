from room import Room
from player import Player
from world import World
from roomsvisited import roomsvisited

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

rooms_checked = roomsvisited()
homeward_path = []

# stating room
curr = world.starting_room
rooms_checked.add_room(curr.id, curr.get_exits())

while len(rooms_checked) < len(room_graph):
    #get new direction
    new_dir = rooms_checked.get_unexlpored_exit(curr.id)
    if new_dir is not None:
        homeward_path.append(rooms_checked.changeDirection(new_dir)) # the trace back
    else:
        new_dir = homeward_path.pop()  # WALK BACK

    prev = curr
    curr = curr.get_room_in_direction(new_dir)
    rooms_checked.add_room(curr.id, curr.get_exits())
    rooms_checked.connect_rooms(prev.id, new_dir, curr.id)

    traversal_path.append(new_dir)

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
