import os


def read_status(pid: int) -> dict:
    path = f"/proc/{pid}/status"
    data = {}

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if ":" in line:
                    key, value = line.split(":", 1)
                    data[key.strip()] = value.strip()
    except (FileNotFoundError, PermissionError):
        return {}

    return data


def get_libraries(pid: int) -> list[str]:
    path = f"/proc/{pid}/maps"
    libraries = set()

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 6:
                    possible_path = parts[-1]

                    if ".so" in possible_path:
                        libraries.add(possible_path)
    except (FileNotFoundError, PermissionError):
        return []

    return sorted(libraries)


def get_open_files(pid: int) -> list[str]:
    path = f"/proc/{pid}/fd"
    open_files = set()

    try:
        for fd in os.listdir(path):
            fd_path = os.path.join(path, fd)

            try:
                target = os.readlink(fd_path)
                open_files.add(target)
            except (FileNotFoundError, PermissionError, OSError):
                continue

    except (FileNotFoundError, PermissionError):
        return []

    return sorted(open_files)


def analyze_process(pid: int) -> str:
    status = read_status(pid)
    libraries = get_libraries(pid)
    open_files = get_open_files(pid)

    result = []
    result.append("=" * 10 + " ANÁLISIS DEL PROCESO " + "=" * 10)
    result.append(f"PID analizado: {pid}")

    if status:
        result.append(f"Nombre: {status.get('Name', 'No disponible')}")
        result.append(f"Estado: {status.get('State', 'No disponible')}")
        result.append(f"VmRSS: {status.get('VmRSS', 'No disponible')}")
        result.append(f"VmSize: {status.get('VmSize', 'No disponible')}")
        result.append(f"Hilos: {status.get('Threads', 'No disponible')}")
        result.append(f"PPid: {status.get('PPid', 'No disponible')}")
    else:
        result.append("No se pudo leer /proc/<PID>/status")

    result.append("\nBibliotecas cargadas:")
    if libraries:
        for lib in libraries[:15]:
            result.append(f"- {lib}")
        if len(libraries) > 15:
            result.append(f"... y {len(libraries) - 15} más")
    else:
        result.append("- No se encontraron bibliotecas o no hubo permisos")

    result.append("\nArchivos abiertos:")
    if open_files:
        for file in open_files[:15]:
            result.append(f"- {file}")
        if len(open_files) > 15:
            result.append(f"... y {len(open_files) - 15} más")
    else:
        result.append("- No se encontraron archivos abiertos o no hubo permisos")

    return "\n".join(result)