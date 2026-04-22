import random
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        random_int = random.randint(1, 10)
        encoded_int = chr(random_int)
        final_str = f"{encoded_int}#"
        for string in strs:
            encoded_str = ""
            for char in string:
                encoded_str += chr(ord(char) - random_int)
            final_str += f"{encoded_str}{chr(0)}"
        return final_str

    def decode(self, s: str) -> List[str]:
        encoded_int = s[0]
        random_int = ord(encoded_int)
        final_list = []
        decoded_text = ""
        for char in s[2:]:
            if char == chr(0):
                final_list.append(decoded_text)
                decoded_text = ""
                continue
            decoded_text += chr(ord(char) + random_int)
        return final_list
