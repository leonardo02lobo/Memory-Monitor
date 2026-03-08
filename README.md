# Memory Monitor

Proyecto en Python para monitorear la memoria del sistema en Linux y analizar el proceso que más memoria RAM consume usando el sistema de archivos virtual `/proc`.

## Características

- Muestra información básica de la memoria del sistema.
- Identifica el proceso con mayor consumo de memoria (`VmRSS`).
- Analiza el proceso seleccionado.
- Lista bibliotecas cargadas en memoria.
- Lista archivos abiertos por el proceso.

## Requisitos

- Python 3
- Linux

## Estructura del proyecto

```bash
Memory-Monitor/
├── main.py
├── memory_info.py
├── process_analyzer.py
└── process_scanner.py
```

# Ejecucion 
```bash
python3 main.py
```

# Salida esperada

El programa muestra:

- Memoria total

- Memoria libre

- Buffers

- Caché

- Memoria usada

- Proceso con mayor VmRSS

- Información del proceso

-Bibliotecas cargadas

- Archivos abiertos

# Tecnologías

- Python

- Linux

- /proc