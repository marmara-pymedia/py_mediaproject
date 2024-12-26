import json
from entities.WatchState import WatchState

class WatchStateService:
    def __init__(self):
        pass

    def get_all(self)->list[WatchState]:
        with open("data/watchstates.json","r") as file:
            watch_states=json.load(file)
        return [WatchState(**watch_state) for watch_state in watch_states]