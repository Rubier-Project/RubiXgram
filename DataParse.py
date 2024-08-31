"""
Rubika Asynchronous/Synchronous Client Library 

Github: https://github.com/Rubier-Project/RubiXgram
Rubika Channel: @RubixGram1
Dev: @StreamX
Supporters: @Off_coder - @StreamX
"""

import os
import rich

os.system("")

class Parse(object):
    def __init__(self) -> None:
        pass
    
    def jsonify(self, data: str) -> None:
        rich.print_json(data)

    def stringify(self, data: dict):
        rich.print(data)