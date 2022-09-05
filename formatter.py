from typing import Union
from typing import Optional


class Tools:
    def __init__(self) -> None:
        pass
    
    def joinlines(self, lines: list, joiner: str = "\n") -> str:
        return joiner.join(lines)

tools = Tools()
    
class Formatter:
    def __init__(self, file) -> None:
        self.content = self.read(file)
    
    def read(self, file: Union[str, bytes, bytearray]) -> str:
        if isinstance(file, str):
            return file
        elif isinstance(file, (bytes, bytearray)):
            return file.decode()
        else:
            raise TypeError(f'Unsupported type: {type(file)}')
    
    def move_semicolons(self, align_position) -> str:
        lines = self._lines
        for index, line in enumerate(lines):
            if line.endswith(';'):
                line = line[:-1]
                line = line.ljust(align_position-1) + ';'
                lines[index] = line
        return lines
    
    def format(self) -> str:
        content = self.content
        lines: list = content.splitlines()
        self._lines = lines
        align_position = max(len(line) for line in lines) + 2
        lines = self.move_semicolons(align_position)
        
        return tools.joinlines(lines)


'''
e.g.

    foo(123);
            ^
            len(line)
    foo(123)     ;
                 ^
                 align_position
            |<->|
            align_position - len(line)
'''