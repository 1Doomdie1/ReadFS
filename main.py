from typing import Union
from ReFS.bootsector import BootSector
from ReFS.superblock import Superblock
from ReFS.checkpoint import Checkpoint

def getBytes(byteRange: Union[list[bytes, int], tuple[bytes, int], set[bytes, int]], offset: Union[int, bytes] = 0) -> bytes:
    path = "samples/logical_refs2.001"
    with open(path, "rb") as file:
        file.seek(offset+ byteRange[0])
        data = file.read(abs(byteRange[0] - byteRange[1]))
    return data

def main():
    bootSector = BootSector(getBytes([0x0, 0x48]))
    pageSize = bootSector.sectorsPerCluster() * bootSector.bytesPerSector()
    sbo = bootSector.superBlockOffset()
    sb = Superblock(getBytes([0x0, pageSize], sbo))
    # print(sb.info())
    chkoff = sb.checkpointOffset()[0]
    checkpoint = Checkpoint(getBytes([0x0, pageSize], chkoff))
    # print(chkoff)
    print(checkpoint.info())

if __name__ == '__main__':
    main()
