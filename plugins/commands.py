from src import dungeon
from src import dungeon, handler


@handler.when('hit THING')
def hit_something(thing: str) -> None:
    """"""
    the_thing = dungeon.current_room.entities.find(thing)
    if the_thing is None:
        print('wtf t con')
    else:
        dungeon.PLAYER.attack(thing)
