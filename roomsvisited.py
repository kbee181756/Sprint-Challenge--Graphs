from collections import deque
import random

class roomsvisited():
    def __init__(self):
        self.rooms = {}
        self.room_ct = 0

    
    def __len__(self):
        return self.room_ct


    def __repr__(self):
        output = " "
        for room in self.rooms:
            room_stuff = " "
            for dir in self.rooms[room]:
                self.rooms[room][dir]
                room_stuff += f"{dir}{self.rooms[room][dir]}"
            output += f'{room}({room_stuff})'
        return output


    def add_room(self, room_id, exits):
        if not isinstance(room_id, int):
            print("Warming: room_id should be an integer")
            return
        if room_id in self.rooms:
            return

        
        dirs = {}
        for exit in exits:
            dirs[exit]= "?"

        self.rooms[room_id] = dirs
        self.room_ct += 1

    
    def get_unexlpored_exit(self, room_id):
        if not isinstance(room_id, int):
            print("Warning: room_id should be an integer")
            return
        
        if room_id not in self.rooms:
            print(f"Warning: room {room_id} not in graph")
            return

        room_vertex = self.rooms[room_id]
        unexplored_rooms = []
        for exit in room_vertex:
            if room_vertex[exit] == "?":
                unexplored_rooms.append(exit)
        if unexplored_rooms:
            return random.choice(unexplored_rooms)
        else:
            return None
        
    
    def connect_rooms(self, room1_id, exit_to, room2_id):

        if not isinstance(room1_id, int):
            print("Warning: room_id should an integer")
            return
        
        if not isinstance(room2_id, int):
            print("Warning: room_id should an integer")
            return
        
        if room1_id not in self.rooms:
            print(f"Warning: room {room1_id} not in graph")
            return
        
        if room2_id not in self.rooms:
            print(f"Warning: room {room2_id} not in graph")
            return
        
        if room1_id == room2_id:
            print(f"Warning: room ids cannot be the same")

        if exit_to not in "nesw":
            print(f"Warning: give a valid exit direction")
            return

        room1vertex = self.rooms[room1_id]
        room1vertex[exit_to] = room2_id

        room2vertex = self.rooms[room2_id]
        room2vertex[self.changeDirection(exit_to)] = room1_id

    def changeDirection(self, dir):
        if dir == "n":
            return "s"
        if dir == "s":
            return "n"
        if dir == "w":
            return "e"
        if dir == "e":
            return "w"    
