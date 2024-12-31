import json
from entities.WatchState import WatchState

class WatchStateService:
    def __init__(self):
        pass

    def get_all(self)->list[WatchState]:
        with open("data/watchstates.json","r") as file:
            watch_states=json.load(file)
        return [WatchState(**watch_state) for watch_state in watch_states]
    
    def get_by_id(self,id:int)->WatchState:
        watch_states=self.get_all()
        for watch_state in watch_states:
            if watch_state.id==id:
                return watch_state
        return None