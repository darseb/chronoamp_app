# ChronoAmp — Sistema de Control y Análisis Cronoamperométrico

**ChronoAmp** es una aplicación de escritorio para instrumentación electroquímica diseñada para operar potenciostatos portátiles (PalmSens / EmStat), ejecutar ensayos de cronoamperometría en tiempo real y automatizar el análisis cuantitativo de biosensores y sensores químicos.

---

## 🔬 Características Principales

- **Adquisición en Tiempo Real:** Visualización continua de corriente vs. tiempo ($I$ vs. $t$) a alta frecuencia ($>30\text{ FPS}$) sin bloquear la interfaz de usuario.
- **Modo Simulación (Mock):** Permite ejecutar y probar la aplicación sin necesidad de hardware físico conectado, emulando la física electroquímica (Ecuación de Cottrell y doble capa).
- **Interpretación Analítica Automatizada:**
  - Filtros digitales (Savitzky-Golay, media móvil).
  - Ajuste de curvas de calibración (lineal y no lineal 4PL) con cálculo de $R^2$ e intervalos de confianza.
  - Determinación de límites de detección (LOD) y cuantificación (LOQ) según directrices IUPAC ($3.3 \cdot s / S$ y $10 \cdot s / S$).
  - Emisión de veredictos diagnósticos en tiempo real.
- **Persistencia y Exportación:** Guardado de métodos de ensayo en formato JSON y exportación completa a **CSV** y **Microsoft Excel (.xlsx)**.
- **Interfaz Ergonómica Científica:** Diseño en tema claro tipo PSTrace/PalmSens optimizado para legibilidad en entornos de laboratorio.

---

## 📁 Estructura del Proyecto

```text
chronoamp_app/
├── core/             # Control de hardware, DeviceManager y AcquisitionThread (y Mock)
├── interpretation/   # Motores de filtrado, calibración, LOD/LOQ y veredictos
├── data/             # Persistencia de sesiones, métodos y exportadores (CSV/Excel)
├── ui/               # Interfaz gráfica en PySide6 (Qt) y graficado pglive/pyqtgraph
├── methods/          # Métodos de ensayo preconfigurados (.json)
├── tests/            # Batería de 14 suites de pruebas automatizadas con pytest
├── scripts/          # Scripts auxiliares (generador de informe PDF, etc.)
└── Informe_Realizacion_ChronoAmp.pdf # Informe técnico de ingeniería de software
```

---

## 🚀 Requisitos e Instalación

### 1. Prerrequisitos
- Python 3.10 o superior instalado en el sistema.

### 2. Clonar el repositorio
```bash
git clone https://github.com/TU_USUARIO/chronoamp_app.git
cd chronoamp_app
```

### 3. Crear y activar entorno virtual (Recomendado)
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/macOS:
source venv/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## 💻 Ejecución

Para iniciar la aplicación:
```bash
python main.py
```

*Nota:* Si no hay un potenciostato PalmSens conectado por USB/Bluetooth, la aplicación puede operar en modo simulado para pruebas y demostraciones.

---

## 🧪 Pruebas Automatizadas

Para ejecutar la batería completa de pruebas unitarias e integración:
```bash
pytest
```

---

## 📄 Informe Técnico de Ingeniería

El proyecto incluye el informe formal de ingeniería de software en formato PDF:
- [Informe_Realizacion_ChronoAmp.pdf](./Informe_Realizacion_ChronoAmp.pdf)

---

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
