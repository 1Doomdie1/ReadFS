from typing import Union
from ReFS.Tables import Table

class ParentChild(Table):
    def __init__(self, byteArray:Union[list[bytes], tuple[bytes], set[bytes]]) -> None:
        super().__init__(byteArray)

    def parent(self) -> str:
        return hex(self.formater.toDecimal(self.byteArray[0x8:0xA]))

    def child(self) -> str:
        return hex(self.formater.toDecimal(self.byteArray[0x18:0x20]))

    def structure(self) -> dict:
        return {"Parent ID":f"{self.tableID(self.parent())} ({self.parent()})",
                "Child ID":self.child()}