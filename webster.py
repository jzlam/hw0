def join_names(name_list: list[str]) -> str:
    result = ",".join(name_list) 
    return result 

def check_name(name: str) -> None:
    if not name.isalpha():
        raise ValueError("Name must contain only alphabetic characters.")
    if len(name) < 2 or len(name) > 11:
        raise ValueError("Name must be between 2 and 11 characters long.")
    vowels = {"a", "e", "i", "o", "u"}
    if not any(c.lower() in vowels for c in name):
        raise ValueError("Name must contain at least one vowel (a, e, i, o, u)")
    
def split_names(names: str) -> list[str]: 
    names = names.strip() 
    name_list = names.split(",")
    for name in name_list:
        check_name(name)
    return name_list

def my_function_test(f, arg) -> str:
    try: 
        result = f(arg)
        return f"Success: returned value was {result}"
    except Exception as e:
        return f"{type(e).__name__}: {e}"
    
def my_function_test_2(f, *args, **kwargs) -> str:
    try: 
        result = f(*args, **kwargs)
        return f"Success: returned value was {result}"
    except Exception as e:
        return f"{type(e).__name__}: {e}"
    
def describe_letters_in_name(name: str) -> list[dict]: 
    check_name(name)
    vowels = {"a", "e", "i", "o", "u"}
    result = []

    position = 1
    for char in name:
        if char.isspace():
            continue  
        result.append({
            "position": position,
            "letter": char,
            "is_vowel": char.lower() in vowels
        })
        position += 1

    return result


class HotelError(Exception):
    """Custom exception for hotel-specific errors."""
    pass


class Hotel: 
    def __init__(self, floors: int, rooms_per_floor: int):
        if floors < 1:
            raise ValueError("floors must be at least 1")
        if rooms_per_floor < 1:
            raise ValueError("rooms_per_floor must be at least 1")
        self.floors = floors
        self.rooms_per_floor = rooms_per_floor
        self._matrix = []
        for f in range(floors):
            row = []
            for r in range(rooms_per_floor):
                row.append({
                    "suite": f * 100 + r,
                    "friend": None,
                    "catch": 0
                })
            self._matrix.append(row)

    def get_hotel_matrix(self) -> list[list[dict]]: 
        return [[room.copy() for room in row] for row in self.matrix]
    
    def check_in(self, suite_number: int, name: str) -> None:
        check_name(name)
        floor = suite_number // 100
        room = suite_number % 100
        if floor < 0 or floor >= self.floors or room < 0 or room >= self.rooms_per_floor:
            raise ValueError("Invalid suite number.")
        if self._matrix[floor][room]["friend"] is not None:
            raise HotelError(f"Suite {suite_number} is already occupied")
        self._matrix[floor][room]["friend"] = name

    def catch(self, suite_number: int) -> None:
        floor = suite_number // 100
        room = suite_number % 100
        if floor < 0 or floor >= self.floors or room < 0 or room >= self.rooms_per_floor:
            raise ValueError("Invalid suite number.")
        if room["friend"] is None:
            raise HotelError(f"Suite {suite_number} is vacant")
        self._matrix[floor][room]["catch"] += 1

    def check_out(self, suite_number: int) -> None:
        floor = suite_number // 100
        room = suite_number % 100
        if floor < 0 or floor >= self.floors or room < 0 or room >= self.rooms_per_floor:
            raise ValueError("Invalid suite number.")
        if self._matrix[floor][room]["friend"] is None:
            raise HotelError(f"Suite {suite_number} is vacant")
        self._matrix[floor][room]["friend"] = None
        self._matrix[floor][room]["catch"] = 0

    def get_room_info(self, suite_number: int) -> dict:
        floor = suite_number // 100
        room = suite_number % 100
        if floor < 0 or floor >= self.floors or room < 0 or room >= self.rooms_per_floor:
            raise ValueError("Invalid suite number.")
        return self._matrix[floor][room].copy() 
    
    def get_top_rooms(self, k : int) -> list[dict]:
        all_rooms = []
        for row in self._matrix:
            for room in row:
                all_rooms.append(room)
        all_rooms.sort(key=lambda x: x["catch"], reverse=True)
        return all_rooms[:k]
    



