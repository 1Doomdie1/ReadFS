from typing import Union, Tuple, List, Set
from Managers.Bytes import Formater

class DataArea:
    def __init__(self, byteArray:Union[List[bytes], Tuple[bytes], Set[bytes]]) -> None:
        self.byteArray = byteArray
        self.formater = Formater()
    