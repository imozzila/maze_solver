from dataclasses import dataclass 

MAGIC_NUMBER: bytes = b"MAZE"

@dataclass(frozen=True)
class FileHeader:
    format_version: int
    width: int 
    height: int 
