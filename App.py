# Juan Esteban Arcila Espitia
# Consultorio Odontologico - Interfaz Streamlit
# Universidad de Manizales
# Profesor: Jose Ubaldo Carvajal

import streamlit as st
from collections import deque

# ── Configuracion de pagina ──────────────────────────────────
st.set_page_config(
    page_title="OdontoClinic",
    page_icon="🦷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── CSS personalizado ────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── GENERAL ── */
.stApp { background: #f0f4f8; font-family: 'DM Sans', sans-serif; }
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* ── TEXTO OSCURO EN AREA PRINCIPAL (selectores específicos, sin tocar botones ni banners) ── */
.block-container p,
.block-container span,
.block-container label { color: #1a2a3a !important; }

.block-container h1,
.block-container h2,
.block-container h3,
.block-container h4 { color: #1a2a3a !important; }

/* inputs de texto */
.stTextInput input, .stNumberInput input {
    color: #1a2a3a !important;
    background: white !important;
    border-radius: 8px !important;
    border: 1.5px solid #d1dce8 !important;
}

/* selectbox fondo blanco */
.stSelectbox [data-baseweb="select"] { background: white !important; }
.stSelectbox [data-baseweb="select"] * { color: #1a2a3a !important; background: white !important; }
[data-baseweb="popover"] * { color: #1a2a3a !important; background: white !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #0a2342 0%, #1a3a5c 60%, #0d3b6e 100%) !important;
}
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] div,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 { color: #ffffff !important; }
[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.2) !important; }

/* ── CARDS METRICAS ── */
.metric-card {
    background: white; border-radius: 16px; padding: 1.5rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    border-left: 4px solid #1a6bd4; margin-bottom: 1rem;
}
.metric-card h3 { font-family:'Playfair Display',serif; font-size:2rem; color:#0a2342 !important; margin:0; font-weight:700; }
.metric-card p  { color:#6b7c9a !important; font-size:0.85rem; margin:0.3rem 0 0 0; font-weight:500; text-transform:uppercase; letter-spacing:1px; }

/* ── CARDS CLIENTE ── */
.cliente-card {
    background: white; border-radius: 12px; padding: 1.2rem 1.5rem;
    margin-bottom: 0.7rem; box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    border-left: 4px solid #1a6bd4;
}
.cliente-card.urgente { border-left-color: #e53e3e; }
.cliente-card.pila    { border-left-color: #e53e3e; background: linear-gradient(to right, #fff5f5, white); }
.cliente-card.cola    { border-left-color: #38a169; background: linear-gradient(to right, #f0fff4, white); }
.cliente-nombre { font-family:'Playfair Display',serif; font-size:1.1rem; color:#0a2342 !important; font-weight:600; margin:0 0 0.3rem 0; }
.cliente-info   { color:#6b7c9a !important; font-size:0.82rem; margin:0; }

/* ── BADGES ── */
.badge { display:inline-block; padding:0.2rem 0.7rem; border-radius:20px; font-size:0.72rem; font-weight:600; letter-spacing:0.5px; text-transform:uppercase; }
.badge-urgente    { background:#fed7d7; color:#c53030 !important; }
.badge-normal     { background:#bee3f8; color:#2b6cb0 !important; }
.badge-particular { background:#fefcbf; color:#744210 !important; }
.badge-eps        { background:#c6f6d5; color:#276749 !important; }
.badge-prepagada  { background:#e9d8fd; color:#553c9a !important; }

/* ── VALOR CHIP ── */
.valor-chip { background:#ebf4ff; color:#1a6bd4 !important; font-weight:700; padding:0.2rem 0.8rem; border-radius:20px; font-size:0.9rem; }

/* ── HEADERS DE SECCION ── */
.section-header { font-family:'Playfair Display',serif; font-size:1.6rem; color:#0a2342 !important; font-weight:700; margin-bottom:0.3rem; }
.section-sub    { color:#6b7c9a !important; font-size:0.88rem; margin-bottom:1.5rem; }

/* ── LINEA DECORATIVA ── */
.deco-line { height:3px; background:linear-gradient(to right,#1a6bd4,#7eb8f7,transparent); border-radius:2px; margin:1.5rem 0; }

/* ── FORMULARIO ── */
div[data-testid="stForm"] { background:white; border-radius:16px; padding:1.5rem; box-shadow:0 2px 12px rgba(0,0,0,0.06); }

/* ── BOTONES ── texto blanco siempre visible ── */
.stButton > button {
    background: linear-gradient(135deg,#1a3a5c,#1a6bd4) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 500 !important;
    box-shadow: 0 2px 8px rgba(26,107,212,0.3) !important;
}
.stButton > button * {
    color: white !important;
}
.stButton > button p,
.stButton > button span,
.stButton > button div {
    color: white !important;
}

/* ── TURNO BADGES ── */
.turno-badge      { background:#e53e3e; color:white !important; border-radius:50%; width:28px; height:28px; display:inline-flex; align-items:center; justify-content:center; font-weight:700; font-size:0.85rem; margin-right:0.7rem; }
.turno-badge-cola { background:#38a169; color:white !important; border-radius:50%; width:28px; height:28px; display:inline-flex; align-items:center; justify-content:center; font-weight:700; font-size:0.85rem; margin-right:0.7rem; }

/* ── BANNER SIGUIENTE ── texto blanco forzado ── */
.banner-siguiente p,
.banner-siguiente span,
.banner-siguiente div {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

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

# ── Estado de sesion ─────────────────────────────────────────
if "lista_clientes" not in st.session_state:
    st.session_state.lista_clientes = []
if "pila_urgentes" not in st.session_state:
    st.session_state.pila_urgentes = deque()
if "cola_agenda" not in st.session_state:
    st.session_state.cola_agenda = deque()

# ── Funcion calcular valor ───────────────────────────────────
def calcular_valor(tipo_cliente, tipo_atencion, cantidad):
    if tipo_cliente == "Particular":
        cita = 80000
        if tipo_atencion == "Limpieza":      atencion = 60000
        elif tipo_atencion == "Calzas":      atencion = 80000
        elif tipo_atencion == "Extraccion":  atencion = 100000
        else:                                atencion = 50000
    elif tipo_cliente == "EPS":
        cita = 5000
        if tipo_atencion == "Limpieza":      atencion = 0
        elif tipo_atencion == "Calzas":      atencion = 40000
        elif tipo_atencion == "Extraccion":  atencion = 40000
        else:                                atencion = 0
    else:
        cita = 30000
        if tipo_atencion == "Limpieza":      atencion = 0
        elif tipo_atencion == "Calzas":      atencion = 10000
        elif tipo_atencion == "Extraccion":  atencion = 10000
        else:                                atencion = 0
    return cita + (atencion * cantidad)

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <h1>🦷 OdontoClinic</h1>
        <p style='color:#7eb8f7 !important; font-size:0.7rem; margin:0.2rem 0 0 0; letter-spacing:2px; text-transform:uppercase;'>Sistema de gestión</p>
        <p style='color:#ffffff !important; font-size:0.85rem; margin:0.5rem 0 0 0; font-weight:600;'>Juan Esteban Arcila</p>
        <p style='color:#b8d0f0 !important; font-size:0.72rem; margin:0.1rem 0 0 0;'>Universidad de Manizales</p>
    </div>
    """, unsafe_allow_html=True)

    seccion = st.radio(
        "Navegación",
        [
            "🏠  Inicio",
            "➕  Registrar cliente",
            "📋  Lista de clientes",
            "📊  Estadísticas",
            "🚨  Pila urgentes",
            "📅  Agenda del día",
        ],
        label_visibility="collapsed"
    )

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style='text-align:center; padding: 0.5rem;'>
        <p style='font-size:0.75rem; color:#7eb8f7 !important; margin:0;'>Clientes registrados</p>
        <p style='font-size:2rem; font-weight:700; color:#ffffff !important; margin:0;'>{len(st.session_state.lista_clientes)}</p>
    </div>
    <div style='text-align:center; padding: 0.5rem;'>
        <p style='font-size:0.75rem; color:#f48fb1 !important; margin:0;'>🚨 Urgentes en pila</p>
        <p style='font-size:2rem; font-weight:700; color:#ffffff !important; margin:0;'>{len(st.session_state.pila_urgentes)}</p>
    </div>
    <div style='text-align:center; padding: 0.5rem;'>
        <p style='font-size:0.75rem; color:#a5d6a7 !important; margin:0;'>📅 En agenda hoy</p>
        <p style='font-size:2rem; font-weight:700; color:#ffffff !important; margin:0;'>{len(st.session_state.cola_agenda)}</p>
    </div>
    """, unsafe_allow_html=True)

# ── INICIO ───────────────────────────────────────────────────
if seccion == "🏠  Inicio":
    st.markdown('<p class="section-header">Bienvenido al sistema</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Consultorio Odontológico · Juan Esteban Arcila · Universidad de Manizales</p>', unsafe_allow_html=True)
    st.markdown('<div class="deco-line"></div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    lista = st.session_state.lista_clientes
    ingresos = sum(c.valor_total for c in lista)
    extracciones = sum(1 for c in lista if c.tipo_atencion == "Extraccion")
    urgentes = sum(1 for c in lista if c.prioridad == "Urgente")

    with col1:
        st.markdown(f'<div class="metric-card"><h3>{len(lista)}</h3><p>Total clientes</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><h3>${ingresos:,.0f}</h3><p>Ingresos totales</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><h3>{extracciones}</h3><p>Extracciones</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="metric-card"><h3>{urgentes}</h3><p>Urgentes</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="deco-line"></div>', unsafe_allow_html=True)
    st.markdown("### Últimos clientes registrados")
    if len(lista) == 0:
        st.info("Aún no hay clientes registrados. Ve a **Registrar cliente** para comenzar.")
    else:
        for c in reversed(lista[-5:]):
            badge_tc = f'<span class="badge badge-{c.tipo_cliente.lower()}">{c.tipo_cliente}</span>'
            badge_pr = f'<span class="badge badge-{"urgente" if c.prioridad=="Urgente" else "normal"}">{c.prioridad}</span>'
            st.markdown(f"""
            <div class="cliente-card {'urgente' if c.prioridad=='Urgente' else ''}">
                <p class="cliente-nombre">{c.nombre} &nbsp; {badge_tc} &nbsp; {badge_pr}</p>
                <p class="cliente-info">📋 {c.cedula} &nbsp;|&nbsp; 📞 {c.telefono} &nbsp;|&nbsp; 🦷 {c.tipo_atencion} &nbsp;|&nbsp; 📅 {c.fecha_cita} &nbsp;|&nbsp; <span class="valor-chip">${c.valor_total:,.0f}</span></p>
            </div>
            """, unsafe_allow_html=True)

# ── REGISTRAR CLIENTE ────────────────────────────────────────
elif seccion == "➕  Registrar cliente":
    st.markdown('<p class="section-header">Registrar nuevo cliente</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Complete los datos de la cita</p>', unsafe_allow_html=True)
    st.markdown('<div class="deco-line"></div>', unsafe_allow_html=True)

    with st.form("form_cliente", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            cedula   = st.text_input("Cédula")
            nombre   = st.text_input("Nombre completo")
            telefono = st.text_input("Teléfono")
            fecha    = st.text_input("Fecha de la cita (DD/MM/AAAA)")
        with col2:
            tipo_cliente  = st.selectbox("Tipo de cliente",  ["Particular", "EPS", "Prepagada"])
            tipo_atencion = st.selectbox("Tipo de atención", ["Limpieza", "Calzas", "Extraccion", "Diagnostico"])
            prioridad     = st.selectbox("Prioridad",        ["Normal", "Urgente"])
            if tipo_atencion in ["Limpieza", "Diagnostico"]:
                cantidad = 1
                st.info("Cantidad: 1 (fija para Limpieza y Diagnóstico)")
            else:
                cantidad = st.number_input("Cantidad", min_value=1, value=1)

        submitted = st.form_submit_button("✅ Registrar cliente")
        if submitted:
            if cedula == "" or nombre == "" or fecha == "":
                st.error("Por favor completa todos los campos obligatorios.")
            else:
                valor = calcular_valor(tipo_cliente, tipo_atencion, cantidad)
                c = Cliente()
                c.cedula        = cedula
                c.nombre        = nombre
                c.telefono      = telefono
                c.tipo_cliente  = tipo_cliente
                c.tipo_atencion = tipo_atencion
                c.cantidad      = cantidad
                c.prioridad     = prioridad
                c.fecha_cita    = fecha
                c.valor_total   = valor
                st.session_state.lista_clientes.append(c)
                st.success(f"✅ Cliente **{nombre}** registrado. Valor a pagar: **${valor:,.0f}**")

# ── LISTA DE CLIENTES ────────────────────────────────────────
elif seccion == "📋  Lista de clientes":
    st.markdown('<p class="section-header">Lista de clientes</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Ordenados de mayor a menor valor de atención</p>', unsafe_allow_html=True)
    st.markdown('<div class="deco-line"></div>', unsafe_allow_html=True)

    lista = st.session_state.lista_clientes
    if len(lista) == 0:
        st.info("No hay clientes registrados.")
    else:
        ordenados = sorted(lista, key=lambda c: c.valor_total, reverse=True)

        buscar = st.text_input("🔍 Buscar por cédula")
        if buscar:
            encontrado = None
            for c in lista:
                if c.cedula == buscar:
                    encontrado = c
            if encontrado:
                st.success(f"Cliente encontrado: **{encontrado.nombre}** | {encontrado.tipo_atencion} | ${encontrado.valor_total:,.0f}")
            else:
                st.error("No se encontró ningún cliente con esa cédula.")

        st.markdown('<div class="deco-line"></div>', unsafe_allow_html=True)

        for c in ordenados:
            badge_tc = f'<span class="badge badge-{c.tipo_cliente.lower()}">{c.tipo_cliente}</span>'
            badge_pr = f'<span class="badge badge-{"urgente" if c.prioridad=="Urgente" else "normal"}">{c.prioridad}</span>'
            st.markdown(f"""
            <div class="cliente-card {'urgente' if c.prioridad=='Urgente' else ''}">
                <p class="cliente-nombre">{c.nombre} &nbsp; {badge_tc} &nbsp; {badge_pr}</p>
                <p class="cliente-info">📋 {c.cedula} &nbsp;|&nbsp; 📞 {c.telefono} &nbsp;|&nbsp; 🦷 {c.tipo_atencion} x{c.cantidad} &nbsp;|&nbsp; 📅 {c.fecha_cita} &nbsp;|&nbsp; <span class="valor-chip">${c.valor_total:,.0f}</span></p>
            </div>
            """, unsafe_allow_html=True)

# ── ESTADISTICAS ─────────────────────────────────────────────
elif seccion == "📊  Estadísticas":
    st.markdown('<p class="section-header">Estadísticas</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Resumen general del consultorio</p>', unsafe_allow_html=True)
    st.markdown('<div class="deco-line"></div>', unsafe_allow_html=True)

    lista = st.session_state.lista_clientes
    if len(lista) == 0:
        st.info("No hay clientes registrados.")
    else:
        total        = len(lista)
        ingresos     = sum(c.valor_total for c in lista)
        extracciones = sum(1 for c in lista if c.tipo_atencion == "Extraccion")
        urgentes     = sum(1 for c in lista if c.prioridad == "Urgente")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f'<div class="metric-card"><h3>{total}</h3><p>Total clientes</p></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="metric-card"><h3>{extracciones}</h3><p>Clientes para extracción</p></div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="metric-card"><h3>${ingresos:,.0f}</h3><p>Ingresos totales</p></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="metric-card"><h3>{urgentes}</h3><p>Clientes urgentes</p></div>', unsafe_allow_html=True)

        st.markdown('<div class="deco-line"></div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Por tipo de cliente**")
            for tc in ["Particular", "EPS", "Prepagada"]:
                n = sum(1 for c in lista if c.tipo_cliente == tc)
                st.markdown(f'<span class="badge badge-{tc.lower()}">{tc}</span> &nbsp; {n} clientes', unsafe_allow_html=True)
                st.write("")
        with col2:
            st.markdown("**Por tipo de atención**")
            for ta in ["Limpieza", "Calzas", "Extraccion", "Diagnostico"]:
                n = sum(1 for c in lista if c.tipo_atencion == ta)
                st.markdown(f"🦷 **{ta}**: {n} clientes")

# ── PILA URGENTES ────────────────────────────────────────────
elif seccion == "🚨  Pila urgentes":
    st.markdown('<p class="section-header">Pila de urgentes</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Clientes de extracción con prioridad urgente · Orden LIFO por fecha</p>', unsafe_allow_html=True)
    st.markdown('<div class="deco-line"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⚡ Generar pila de urgentes"):
            lista = st.session_state.lista_clientes
            filtrados = [c for c in lista if c.tipo_atencion == "Extraccion" and c.prioridad == "Urgente"]
            if len(filtrados) == 0:
                st.warning("No hay clientes de extracción urgente.")
            else:
                filtrados_ord = sorted(filtrados, key=lambda c: c.fecha_cita)
                st.session_state.pila_urgentes = deque(filtrados_ord)
                st.success(f"Pila generada con {len(filtrados_ord)} clientes.")
    with col2:
        if st.button("🏥 Atender siguiente urgente"):
            if len(st.session_state.pila_urgentes) == 0:
                st.warning("La pila está vacía.")
            else:
                c = st.session_state.pila_urgentes.pop()
                st.success(f"✅ Atendido: **{c.nombre}** | {c.cedula} | {c.fecha_cita}")

    st.markdown('<div class="deco-line"></div>', unsafe_allow_html=True)
    st.markdown("### Informe de la pila")

    pila = st.session_state.pila_urgentes
    if len(pila) == 0:
        st.info("La pila está vacía. Genera la pila primero.")
    else:
        lista_pila = list(pila)
        for i, c in enumerate(reversed(lista_pila)):
            st.markdown(f"""
            <div class="cliente-card pila">
                <p class="cliente-nombre"><span class="turno-badge">{i+1}</span>{c.nombre}</p>
                <p class="cliente-info">📋 {c.cedula} &nbsp;|&nbsp; 📞 {c.telefono} &nbsp;|&nbsp; 📅 {c.fecha_cita} &nbsp;|&nbsp; <span class="valor-chip">${c.valor_total:,.0f}</span></p>
            </div>
            """, unsafe_allow_html=True)

# ── COLA AGENDA ──────────────────────────────────────────────
elif seccion == "📅  Agenda del día":
    st.markdown('<p class="section-header">Agenda del día</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Cola de atención · Orden FIFO · Primero en llegar, primero en ser atendido</p>', unsafe_allow_html=True)
    st.markdown('<div class="deco-line"></div>', unsafe_allow_html=True)

    lista = st.session_state.lista_clientes
    cola  = st.session_state.cola_agenda

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        cedula_agregar = st.text_input("Cédula del cliente a agregar a la agenda")
    with col2:
        st.write("")
        st.write("")
        if st.button("➕ Agregar a agenda"):
            if cedula_agregar == "":
                st.warning("Ingresa una cédula.")
            else:
                encontrado = None
                for c in lista:
                    if c.cedula == cedula_agregar:
                        encontrado = c
                if encontrado == None:
                    st.error("Cliente no encontrado.")
                else:
                    cola.append(encontrado)
                    st.success(f"**{encontrado.nombre}** agregado a la agenda.")
    with col3:
        st.write("")
        st.write("")
        if st.button("✅ Atender siguiente"):
            if len(cola) == 0:
                st.warning("No hay clientes en la agenda.")
            else:
                c = cola.popleft()
                st.success(f"Atendido: **{c.nombre}** | {c.tipo_atencion}")

    if len(cola) > 0:
        siguiente = cola[0]
        st.markdown(f"""
        <div class="banner-siguiente" style="background: linear-gradient(135deg, #0a2342, #1a6bd4); border-radius:12px; padding:1rem 1.5rem; margin:1rem 0;">
            <p style="margin:0; font-size:0.75rem; color:rgba(255,255,255,0.8) !important; text-transform:uppercase; letter-spacing:1px;">Siguiente en ser atendido</p>
            <p style="margin:0.3rem 0 0 0; font-family:'Playfair Display',serif; font-size:1.3rem; font-weight:600; color:white !important;">{siguiente.nombre}</p>
            <p style="margin:0.2rem 0 0 0; font-size:0.85rem; color:rgba(255,255,255,0.8) !important;">🦷 {siguiente.tipo_atencion} &nbsp;|&nbsp; 📅 {siguiente.fecha_cita}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="deco-line"></div>', unsafe_allow_html=True)
    st.markdown("### Agenda completa")

    if len(cola) == 0:
        st.info("No hay clientes en la agenda. Agrega clientes usando su cédula.")
    else:
        for i, c in enumerate(cola):
            badge_tc = f'<span class="badge badge-{c.tipo_cliente.lower()}">{c.tipo_cliente}</span>'
            st.markdown(f"""
            <div class="cliente-card cola">
                <p class="cliente-nombre"><span class="turno-badge-cola">{i+1}</span>{c.nombre} &nbsp; {badge_tc}</p>
                <p class="cliente-info">📋 {c.cedula} &nbsp;|&nbsp; 📞 {c.telefono} &nbsp;|&nbsp; 🦷 {c.tipo_atencion} &nbsp;|&nbsp; 📅 {c.fecha_cita} &nbsp;|&nbsp; <span class="valor-chip">${c.valor_total:,.0f}</span></p>
            </div>
            """, unsafe_allow_html=True)