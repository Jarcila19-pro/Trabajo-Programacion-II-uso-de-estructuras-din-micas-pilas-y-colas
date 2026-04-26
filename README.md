# 🦷 OdontoClinic — Sistema de Gestión Odontológica

**Juan Esteban Arcila Espitia**  
Universidad de Manizales · Profesor: Jose Ubaldo Carvajal

---

## 📋 Descripción

Sistema de gestión para un consultorio odontológico desarrollado en Python. Permite registrar clientes, calcular valores de atención, gestionar urgencias mediante una **pila (LIFO)** y organizar la agenda del día mediante una **cola (FIFO)**.

El proyecto cuenta con **dos versiones**:

| Versión | Archivo | Requisitos |
|---|---|---|
| Interfaz gráfica | `App.py` | Python + Streamlit |
| Consola (simple) | `consultorio.py` | Solo Python |

---

## 🗂️ Estructuras de datos utilizadas

- **Lista** — almacena todos los clientes registrados
- **Pila (LIFO)** — gestiona los pacientes urgentes de extracción (`deque` + `pop()`)
- **Cola (FIFO)** — gestiona la agenda del día (`deque` + `popleft()`)

---

## 💰 Tabla de tarifas

| Concepto | Particular | EPS | Prepagada |
|---|---|---|---|
| Cita base | $80.000 | $5.000 | $30.000 |
| Limpieza | +$60.000 | Incluida | Incluida |
| Calzas (c/u) | +$80.000 | +$40.000 | +$10.000 |
| Extracción (c/u) | +$100.000 | +$40.000 | +$10.000 |
| Diagnóstico | +$50.000 | Incluido | Incluido |

> **Fórmula:** Total = Cita base + (Precio atención × Cantidad)  
> Limpieza y Diagnóstico tienen cantidad fija de 1.

---

## 🖥️ Versión consola — `consultorio_odontologico.py`

### Requisitos
- Python 3.7 o superior
- No requiere instalar ninguna librería adicional

### Cómo ejecutar

```
python consultorio.py
```

### Funcionalidades del menú

```
1. Registrar cliente
2. Listar clientes         → ordenados de mayor a menor valor
3. Buscar cliente          → búsqueda por cédula
4. Estadísticas            → totales, ingresos, por tipo
5. Tabla de tarifas        → precios por tipo de cliente
6. Pila de urgentes        → LIFO: extracción + urgente
7. Agenda del día          → FIFO: cola de atención
8. Salir
```

---

## 🎨 Versión con interfaz — `consultorio_streamlit.py`

### Requisitos

- Python 3.7 o superior
- Streamlit

### Instalación de dependencias

```
pip install streamlit
```

### Cómo ejecutar

```
streamlit run App.py
```

Esto abrirá automáticamente el navegador en `http://localhost:tu_ruta`

### Secciones de la interfaz

- **🏠 Inicio** — métricas generales y últimos clientes registrados
- **➕ Registrar cliente** — formulario completo con cálculo automático del valor
- **📋 Lista de clientes** — ordenada por valor, con búsqueda por cédula
- **📊 Estadísticas** — resumen por tipo de cliente y tipo de atención
- **💰 Tarifas** — tabla de precios con ejemplos de cobro
- **🚨 Pila urgentes** — gestión LIFO de pacientes de extracción urgente
- **📅 Agenda del día** — gestión FIFO de la cola de atención

---

## 📁 Estructura del proyecto

```
OdontoClinic/
├── consultorio_odontologico.py   ← versión consola (sin dependencias)
├── consultorio_streamlit.py      ← versión con interfaz gráfica
└── README.md
```

---

## ▶️ Ejemplo de uso (consola)

```
ODONTOCLINIC - SISTEMA DE GESTION
Juan Esteban Arcila · Univ. Manizales

Clientes: 0  |  Pila urgentes: 0  |  Agenda: 0

1. Registrar cliente
2. Listar clientes
...

Seleccione una opcion: 1

REGISTRAR NUEVO CLIENTE
Cedula          : 123456
Nombre completo : Maria Lopez
Telefono        : 300 111 2233
Fecha cita      : 30/04/2026

Tipo de cliente:
  1. Particular
  2. EPS
  3. Prepagada
Opcion: 2

  Cliente 'Maria Lopez' registrado exitosamente.
  Valor a pagar: $45.000
```