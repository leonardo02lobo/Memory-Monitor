from memory_info import InformationMemory
from process_analyzer import ListDirectory


def main():
    print("="*10+"MEMORY MONITOR"+"="*10)
    print(InformationMemory())
    print("="*30)
    description, pid = ListDirectory()
    print(description)

if __name__ == "__main__":    main()