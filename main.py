from memory_info import InformationMemory
from process_analyzer import ListDirectory
from process_scanner import analyze_process


def main():
    print("=" * 10 + " MEMORY MONITOR " + "=" * 10)
    print(InformationMemory())
    print("=" * 30, end="\n\n")

    result = ListDirectory()

    if result is None:
        print("No se pudo identificar el proceso con mayor consumo de memoria.")
        return

    description, pid = result
    print(description, end="\n\n")
    
    print(analyze_process(pid))


if __name__ == "__main__":
    main()