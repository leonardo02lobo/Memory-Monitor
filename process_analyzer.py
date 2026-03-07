import os


def ListDirectory() -> tuple[str, int] | None:
    list_directory: list[str] = os.listdir("/proc")
    pids = [pid for pid in list_directory if pid.isdigit()]

    max_vmrss: int = -1
    max_pid: str = ""
    max_process_name: str = ""

    for pid in pids:
        status_path = os.path.join("/proc", pid, "status")

        try:
            with open(status_path, "r", encoding="utf-8") as f:
                process_name = ""
                vmrss = 0

                for line in f:
                    if line.startswith("Name:"):
                        process_name = line.split(":", 1)[1].strip()

                    elif line.startswith("VmRSS:"):
                        vmrss = int(line.split()[1])

                if vmrss > max_vmrss:
                    max_vmrss = vmrss
                    max_pid = pid
                    max_process_name = process_name

        except (FileNotFoundError, PermissionError, ProcessLookupError):
            continue

    if not max_pid:
        return None

    description = (
        f"El proceso con mayor VmRSS es:\n"
        f"Name: {max_process_name}\n"
        f"PID: {max_pid}\n"
        f"VmRSS: {max_vmrss} kB"
    )

    return description, int(max_pid)