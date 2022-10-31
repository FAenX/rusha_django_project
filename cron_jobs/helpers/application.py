from typing import Any


class Application:
    def __init__(self, app_json):
        self.__dict__ = app_json
    
    def __setattr__(self, __name: str, __value: Any):
        super().__setattr__(__name, __value)

    def __call__(self):
        for key, value in self.__dict__.items():
            self.__setattr__(key, value)

    def __repr__(self):
        return f"Application({self.__dict__})"
    
    
    