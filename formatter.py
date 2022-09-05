from itertools import count
from typing import List
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
    
    def _move_last_letter(self, lines: List[str], letter, align_position) -> List[str]:
        for index, line in enumerate(lines):
            if line.endswith(letter):
                line = line[:-1]
                line = line.ljust(align_position - 1) + letter
                lines[index] = line
        return lines
    
    def _move_right_braces(self, lines: List[str], align_position) -> List[str]:
        backward_lines = lines[::-1]
        for index, line in enumerate(backward_lines):
            if ('}' in line) and (line.index('}') < align_position):
                count_of_right_braces = line.count('}')
                line = line.replace('}', '')
                backward_lines[index+1] += '}' * count_of_right_braces
                # if nothing left in line, remove it
                if not line.strip():
                    line = ''
                backward_lines[index] = line
        lines = backward_lines[::-1]
        return lines

    def format(self) -> str:
        content = self.content
        lines: list = content.splitlines()
        align_position = max(len(line) for line in lines) + 2
        lines = self._move_last_letter(lines, ';', align_position)
        lines = self._move_last_letter(lines, '{', align_position)
        lines = self._move_right_braces(lines, align_position)
        
        return tools.joinlines(lines)
