from typing import List
from typing import Union
from typing import Optional
import re


class Tools:
    def __init__(self) -> None:
        pass
    
    def joinlines(self, lines: list, joiner: str = "\n") -> str:
        result = ""
        for index in range(len(lines)):
            if lines[index]:
                result += lines[index]
                if index != len(lines) - 1:
                    result += joiner
        return result

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
    
    def _remove_unecessary_spaces(self, lines: List[str]) -> List[str]:
        pattern = r"\}(\s+)\w."
        for index, line in enumerate(lines):
            matches = re.finditer(pattern, line)
            for match_num, match in enumerate(matches, start=1):
                line_ = list(line)
                line_[match.start(1):match.end(1)] = ''
                lines[index] = ''.join(line_)
        return lines
    
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
                if not line.strip():
                    line = ''
                backward_lines[index] = line
        lines = backward_lines[::-1]
        return lines

    def _final_fix(self, lines: List[str], align_position) -> List[str]:
        pattern = r"(.+?)(\s+)(\{|\}|\;)"
        for index, line in enumerate(lines):
            try:
                result = re.search(pattern, line).groups()
                num_of_missing_space = align_position - len(result[0]) - len(result[1]) - 1
                line = line.replace(result[0], result[0] + ' ' * num_of_missing_space)
                lines[index] = line
            except:
                pass
        return lines

    def format(self) -> str:
        content = self.content
        lines: list = content.splitlines()
        align_position = max(len(line) for line in lines) + 2
        lines = self._remove_unecessary_spaces(lines)
        lines = self._move_last_letter(lines, ';', align_position)
        lines = self._move_last_letter(lines, '{', align_position)
        lines = self._move_right_braces(lines, align_position)
        lines = self._final_fix(lines, align_position)
        
        return tools.joinlines(lines)
