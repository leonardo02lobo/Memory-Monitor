import pathlib


def InformationMemory() -> str | None:
    information: str = pathlib.Path("/proc/meminfo").read_text()
    mem_free: int = 0
    mem_total: int = 0
    buffers: int = 0
    cached: int = 0

    if not information:
        return None
    
    information: list[str] = information.strip().splitlines()
    for info in information:
        if (not info .startswith("MemTotal:") and 
            not info.startswith("MemFree:") and
            not info.startswith("Buffers:") and 
            not info.startswith("Cached:")):
            continue

        if info.startswith("MemTotal:"):
            mem_total: int = int(info.split()[1])
        elif info.startswith("MemFree:"):
            mem_free: int = int(info.split()[1])
        elif info.startswith("Buffers:"):
            buffers: int = int(info.split()[1])
        elif info.startswith("Cached:"):
            cached: int = int(info.split()[1])
    mem_used: int = mem_total - mem_free - buffers - cached
    
    return f"Memoria Total: {mem_total} kB\nMemoria Libre: {mem_free} kB\nBuffers: {buffers} kB\nCached: {cached} kB\nMemoria Usada: {mem_used} kB"
