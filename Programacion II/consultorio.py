# Juan Esteban Arcila Espitia
# Consultorio Odontologico - Version Consola
# Universidad de Manizales
# Profesor: Jose Ubaldo Carvajal

from collections import deque

# ── Clase Cliente ────────────────────────────────────────────
class Cliente:
    def __init__(self):
        self.cedula: str = ""
        self.nombre: str = ""
        self.telefono: str = ""
        self.tipo_cliente: str = ""
        self.tipo_atencion: str = ""
        self.cantidad: int = 1
        self.prioridad: str = ""
        self.fecha_cita: str = ""
        self.valor_total: float = 0

    def __str__(self):
        return (f"  Nombre       : {self.nombre}\n"
                f"  Cedula       : {self.cedula}\n"
                f"  Telefono     : {self.telefono}\n"
                f"  Tipo cliente : {self.tipo_cliente}\n"
                f"  Atencion     : {self.tipo_atencion} x{self.cantidad}\n"
                f"  Prioridad    : {self.prioridad}\n"
                f"  Fecha cita   : {self.fecha_cita}\n"
                f"  Valor total  : ${self.valor_total:,.0f}")

# ── Estructuras de datos ─────────────────────────────────────
lista_clientes = []       # Lista general
pila_urgentes  = deque()  # Pila LIFO para urgentes
cola_agenda    = deque()  # Cola FIFO para agenda del dia

# ── Tabla de tarifas ─────────────────────────────────────────
TARIFAS = {
    "Particular": {
        "cita": 80000,
        "Limpieza":   60000,
        "Calzas":     80000,
        "Extraccion": 100000,
        "Diagnostico": 50000,
    },
    "EPS": {
        "cita": 5000,
        "Limpieza":    0,
        "Calzas":     40000,
        "Extraccion": 40000,
        "Diagnostico": 0,
    },
    "Prepagada": {
        "cita": 30000,
        "Limpieza":    0,
        "Calzas":     10000,
        "Extraccion": 10000,
        "Diagnostico": 0,
    },
}

# ── Funcion calcular valor ───────────────────────────────────
def calcular_valor(tipo_cliente, tipo_atencion, cantidad):
    cita    = TARIFAS[tipo_cliente]["cita"]
    atencion = TARIFAS[tipo_cliente][tipo_atencion]
    return cita + (atencion * cantidad)

# ── Funcion mostrar tarifas ──────────────────────────────────
def mostrar_tarifas():
    print("\n" + "="*60)
    print("           TABLA DE TARIFAS - ODONTOCLINIC")
    print("="*60)
    print(f"{'Concepto':<20} {'Particular':>12} {'EPS':>10} {'Prepagada':>12}")
    print("-"*60)
    print(f"{'Cita base':<20} {'$80.000':>12} {'$5.000':>10} {'$30.000':>12}")
    print(f"{'Limpieza':<20} {'$60.000':>12} {'$0':>10} {'$0':>12}")
    print(f"{'Calzas (c/u)':<20} {'$80.000':>12} {'$40.000':>10} {'$10.000':>12}")
    print(f"{'Extraccion (c/u)':<20} {'$100.000':>12} {'$40.000':>10} {'$10.000':>12}")
    print(f"{'Diagnostico':<20} {'$50.000':>12} {'$0':>10} {'$0':>12}")
    print("="*60)
    print("Formula: Total = Cita base + (Precio atencion x Cantidad)")
    print("Limpieza y Diagnostico tienen cantidad fija de 1.")
    print("="*60)

# ── Funcion elegir opcion numerada ───────────────────────────
def elegir_opcion(opciones, titulo="Seleccione una opcion"):
    print(f"\n{titulo}:")
    for i, op in enumerate(opciones, 1):
        print(f"  {i}. {op}")
    while True:
        try:
            sel = int(input("Opcion: "))
            if 1 <= sel <= len(opciones):
                return opciones[sel - 1]
            print(f"  Ingrese un numero entre 1 y {len(opciones)}.")
        except ValueError:
            print("  Ingrese un numero valido.")

# ── Registrar cliente ────────────────────────────────────────
def registrar_cliente():
    print("\n" + "="*60)
    print("           REGISTRAR NUEVO CLIENTE")
    print("="*60)

    c = Cliente()
    c.cedula   = input("Cedula          : ").strip()
    c.nombre   = input("Nombre completo : ").strip()
    c.telefono = input("Telefono        : ").strip()
    c.fecha_cita = input("Fecha cita (DD/MM/AAAA): ").strip()

    if not c.cedula or not c.nombre or not c.fecha_cita:
        print("\n  ERROR: Cedula, nombre y fecha son obligatorios.")
        return

    c.tipo_cliente  = elegir_opcion(["Particular", "EPS", "Prepagada"], "Tipo de cliente")
    c.tipo_atencion = elegir_opcion(["Limpieza", "Calzas", "Extraccion", "Diagnostico"], "Tipo de atencion")
    c.prioridad     = elegir_opcion(["Normal", "Urgente"], "Prioridad")

    if c.tipo_atencion in ["Limpieza", "Diagnostico"]:
        c.cantidad = 1
        print("  Cantidad: 1 (fija para Limpieza y Diagnostico)")
    else:
        while True:
            try:
                c.cantidad = int(input("Cantidad        : "))
                if c.cantidad >= 1:
                    break
                print("  La cantidad debe ser al menos 1.")
            except ValueError:
                print("  Ingrese un numero valido.")

    c.valor_total = calcular_valor(c.tipo_cliente, c.tipo_atencion, c.cantidad)
    lista_clientes.append(c)

    print(f"\n  Cliente '{c.nombre}' registrado exitosamente.")
    print(f"  Valor a pagar: ${c.valor_total:,.0f}")

# ── Listar clientes ──────────────────────────────────────────
def listar_clientes():
    print("\n" + "="*60)
    print("      LISTA DE CLIENTES (mayor a menor valor)")
    print("="*60)
    if not lista_clientes:
        print("  No hay clientes registrados.")
        return
    ordenados = sorted(lista_clientes, key=lambda c: c.valor_total, reverse=True)
    for i, c in enumerate(ordenados, 1):
        print(f"\n  [{i}]")
        print(c)
    print("="*60)

# ── Buscar cliente por cedula ────────────────────────────────
def buscar_cliente():
    print("\n" + "="*60)
    print("           BUSCAR CLIENTE POR CEDULA")
    print("="*60)
    cedula = input("Cedula a buscar : ").strip()
    encontrado = None
    for c in lista_clientes:
        if c.cedula == cedula:
            encontrado = c
            break
    if encontrado:
        print("\n  Cliente encontrado:")
        print(encontrado)
    else:
        print(f"\n  No se encontro ningun cliente con cedula '{cedula}'.")
    print("="*60)

# ── Estadisticas ─────────────────────────────────────────────
def mostrar_estadisticas():
    print("\n" + "="*60)
    print("              ESTADISTICAS")
    print("="*60)
    if not lista_clientes:
        print("  No hay clientes registrados.")
        return
    total        = len(lista_clientes)
    ingresos     = sum(c.valor_total for c in lista_clientes)
    extracciones = sum(1 for c in lista_clientes if c.tipo_atencion == "Extraccion")
    urgentes     = sum(1 for c in lista_clientes if c.prioridad == "Urgente")

    print(f"  Total clientes       : {total}")
    print(f"  Ingresos totales     : ${ingresos:,.0f}")
    print(f"  Extracciones         : {extracciones}")
    print(f"  Clientes urgentes    : {urgentes}")
    print()
    print("  Por tipo de cliente:")
    for tc in ["Particular", "EPS", "Prepagada"]:
        n = sum(1 for c in lista_clientes if c.tipo_cliente == tc)
        print(f"    {tc:<12}: {n}")
    print()
    print("  Por tipo de atencion:")
    for ta in ["Limpieza", "Calzas", "Extraccion", "Diagnostico"]:
        n = sum(1 for c in lista_clientes if c.tipo_atencion == ta)
        print(f"    {ta:<12}: {n}")
    print("="*60)

# ── Pila de urgentes ─────────────────────────────────────────
def menu_pila():
    while True:
        print("\n" + "="*60)
        print("           PILA DE URGENTES (LIFO)")
        print("="*60)
        print(f"  Urgentes en pila: {len(pila_urgentes)}")
        print()
        print("  1. Generar pila de urgentes")
        print("  2. Atender siguiente urgente (pop)")
        print("  3. Ver informe de la pila")
        print("  4. Volver al menu principal")
        op = input("Opcion: ").strip()

        if op == "1":
            filtrados = [c for c in lista_clientes
                         if c.tipo_atencion == "Extraccion" and c.prioridad == "Urgente"]
            if not filtrados:
                print("\n  No hay clientes de extraccion urgente.")
            else:
                filtrados_ord = sorted(filtrados, key=lambda c: c.fecha_cita)
                pila_urgentes.clear()
                pila_urgentes.extend(filtrados_ord)
                print(f"\n  Pila generada con {len(pila_urgentes)} clientes.")

        elif op == "2":
            if not pila_urgentes:
                print("\n  La pila esta vacia.")
            else:
                c = pila_urgentes.pop()
                print(f"\n  Atendido (tope de la pila):")
                print(c)

        elif op == "3":
            if not pila_urgentes:
                print("\n  La pila esta vacia. Genera la pila primero.")
            else:
                print("\n  Informe de la pila (orden de atencion, 1 = siguiente):")
                for i, c in enumerate(reversed(list(pila_urgentes)), 1):
                    print(f"\n  [{i}] {c.nombre} | {c.cedula} | {c.fecha_cita} | ${c.valor_total:,.0f}")

        elif op == "4":
            break
        else:
            print("  Opcion no valida.")

# ── Cola agenda del dia ──────────────────────────────────────
def menu_agenda():
    while True:
        print("\n" + "="*60)
        print("           AGENDA DEL DIA (FIFO)")
        print("="*60)
        print(f"  Clientes en agenda: {len(cola_agenda)}")
        if cola_agenda:
            print(f"  Siguiente        : {cola_agenda[0].nombre} | {cola_agenda[0].tipo_atencion}")
        print()
        print("  1. Agregar cliente a la agenda (por cedula)")
        print("  2. Atender siguiente cliente (popleft)")
        print("  3. Ver agenda completa")
        print("  4. Volver al menu principal")
        op = input("Opcion: ").strip()

        if op == "1":
            cedula = input("Cedula del cliente: ").strip()
            encontrado = None
            for c in lista_clientes:
                if c.cedula == cedula:
                    encontrado = c
                    break
            if not encontrado:
                print(f"\n  Cliente con cedula '{cedula}' no encontrado.")
            else:
                cola_agenda.append(encontrado)
                print(f"\n  '{encontrado.nombre}' agregado a la agenda.")

        elif op == "2":
            if not cola_agenda:
                print("\n  No hay clientes en la agenda.")
            else:
                c = cola_agenda.popleft()
                print(f"\n  Atendido:")
                print(c)

        elif op == "3":
            if not cola_agenda:
                print("\n  La agenda esta vacia.")
            else:
                print("\n  Agenda completa (orden de atencion):")
                for i, c in enumerate(cola_agenda, 1):
                    print(f"\n  [{i}] {c.nombre} | {c.tipo_atencion} | {c.fecha_cita} | ${c.valor_total:,.0f}")

        elif op == "4":
            break
        else:
            print("  Opcion no valida.")

# ── Menu principal ───────────────────────────────────────────
def menu_principal():
    print("\n" + "="*60)
    print("         ODONTOCLINIC - SISTEMA DE GESTION")
    print("       Juan Esteban Arcila · Univ. Manizales")
    print("="*60)

    while True:
        print(f"\n  Clientes: {len(lista_clientes)}  |  "
              f"Pila urgentes: {len(pila_urgentes)}  |  "
              f"Agenda: {len(cola_agenda)}")
        print()
        print("  1. Registrar cliente")
        print("  2. Listar clientes")
        print("  3. Buscar cliente por cedula")
        print("  4. Estadisticas")
        print("  5. Tabla de tarifas")
        print("  6. Pila de urgentes")
        print("  7. Agenda del dia")
        print("  8. Salir")
        print()
        op = input("Seleccione una opcion: ").strip()

        if   op == "1": registrar_cliente()
        elif op == "2": listar_clientes()
        elif op == "3": buscar_cliente()
        elif op == "4": mostrar_estadisticas()
        elif op == "5": mostrar_tarifas()
        elif op == "6": menu_pila()
        elif op == "7": menu_agenda()
        elif op == "8":
            print("\n  Hasta luego.\n")
            break
        else:
            print("  Opcion no valida. Intente de nuevo.")

# ── Punto de entrada ─────────────────────────────────────────
if __name__ == "__main__":
    menu_principal()