import os


def ListDirectory() -> tuple[str, int] | None:
    list_directory: list[str] = os.listdir("/proc")
    pids = [pid for pid in list_directory if pid.isdigit()]
    max_vmrrs: int = 0
    max_pid: str = ""
    max_process_name: str = ""
    for pid in pids:
        status_path = os.path.join("/proc", pid, "status")
        try:
            with open(status_path, "r") as f:
                vmrrs = 0
                for line in f:
                    if line.startswith("Name:"):
                        max_process_name = line.strip().split()[1]
                    if line.startswith("VmRSS:"):
                        vmrrs = int(line.strip().split()[1])
                        if vmrrs > max_vmrrs:
                            max_vmrrs = vmrrs
                            max_pid = pid
        except FileNotFoundError:
            continue
        except PermissionError:
            continue
    return [f"El proceso con mayor VmRSS es \n Name: {max_process_name}\n PID: {max_pid}\n VmRSS: {max_vmrrs} kB", max_pid]
