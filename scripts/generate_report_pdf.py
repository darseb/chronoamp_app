import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas to dynamically compute and print total page count in footers.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(40, 11 * inch - 30, "ChronoAmp — Informe de Realización de Software")
            self.drawRightString(8.5 * inch - 40, 11 * inch - 30, "Ingeniería de Software & Arquitectura")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(40, 11 * inch - 34, 8.5 * inch - 40, 11 * inch - 34)
            
        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(40, 36, 8.5 * inch - 40, 36)
        
        self.drawString(40, 24, "Documento de Ingeniería de Software — ChronoAmp v1.0 (Laboratorio de Electroquímica)")
        page_str = f"Página {self._pageNumber} de {total_pages}"
        self.drawRightString(8.5 * inch - 40, 24, page_str)
        self.restoreState()


def build_pdf(output_path):
    # Usamos márgenes compactos de 40pt para aprovechar al máximo el espacio de 2 páginas
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=36,
        bottomMargin=46
    )

    styles = getSampleStyleSheet()

    # Tipografía limpia y profesional
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=17,
        leading=21,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=2
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#0369A1")
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=colors.HexColor("#1E3A8A"),
        spaceBefore=7,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.6,
        leading=12.2,
        textColor=colors.HexColor("#334155"),
        spaceAfter=4
    )

    callout_style = ParagraphStyle(
        'Callout_Text',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11.5,
        textColor=colors.HexColor("#1E293B")
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor("#1E293B")
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor("#0F172A")
    )

    story = []

    # ========================== PÁGINA 1 ==========================
    # Encabezado institucional
    meta_table_data = [
        [
            Paragraph("<b>INFORME DE REALIZACIÓN DE SOFTWARE</b>", title_style),
            Paragraph("<b>VERSIÓN:</b> 1.0 (Producción)<br/><b>FECHA:</b> Octubre 2026", ParagraphStyle('MetaRight', parent=body_style, fontSize=7.8, leading=10.5, alignment=2, textColor=colors.HexColor("#64748B")))
        ],
        [
            Paragraph("<b>ChronoAmp:</b> Plataforma de Control Electroquímico, Adquisición en Tiempo Real y Diagnóstico Cuantitativo", subtitle_style),
            Paragraph("<b>DISCIPLINA:</b> Ingeniería de Software", ParagraphStyle('MetaRight2', parent=body_style, fontSize=7.8, leading=10.5, alignment=2, textColor=colors.HexColor("#0284C7")))
        ]
    ]
    meta_table = Table(meta_table_data, colWidths=[392, 140])
    meta_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(meta_table)
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1E3A8A"), spaceBefore=6, spaceAfter=8))

    # 1. Resumen Ejecutivo
    story.append(Paragraph("1. Resumen Ejecutivo y Propósito", h1_style))
    story.append(Paragraph(
        "<b>ChronoAmp</b> es un software científico de escritorio diseñado para operar potenciostatos portátiles (hardware PalmSens / EmStat), "
        "ejecutar mediciones cronoamperométricas de precisión y automatizar el procesamiento analítico de biosensores y sensores químicos. "
        "El producto resuelve la brecha operativa entre la adquisición de datos brutos y la interpretación clínica o química, integrando "
        "en una sola suite la adquisición en tiempo real, calibraciones automáticas, cálculo de límites de detección y veredictos diagnósticos.",
        body_style
    ))

    # Recuadro de objetivos clave
    box_data = [
        [
            Paragraph(
                "<b>Objetivo General de Ingeniería:</b> Proporcionar una solución modular y robusta con arquitectura desacoplada, "
                "que garantice visualización gráfica continua a más de 30 FPS sin bloquear la interfaz, soporte de simulación completa "
                "(Mock) para desarrollo sin hardware conectado, y una experiencia de usuario (UX) ergonómica con tema claro científico tipo PSTrace.",
                callout_style
            )
        ]
    ]
    box_table = Table(box_data, colWidths=[532])
    box_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0F9FF")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#BAE6FD")),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(box_table)
    story.append(Spacer(1, 6))

    # 2. Fases de Realización del Software
    story.append(Paragraph("2. Proceso de Ingeniería y Fases de Realización (SDLC)", h1_style))
    story.append(Paragraph(
        "El desarrollo siguió un ciclo de vida iterativo por fases de ingeniería, con énfasis en modularidad y calidad continua:",
        body_style
    ))

    phases_table_data = [
        [
            Paragraph("Fase", table_header_style),
            Paragraph("Actividades Clave de Ingeniería", table_header_style),
            Paragraph("Entregable / Resultado", table_header_style)
        ],
        [
            Paragraph("<b>1. Análisis de Requisitos</b>", table_cell_bold),
            Paragraph("• Definición de especificaciones con especialistas en electroquímica.<br/>• Requisitos funcionales: adquisición en tiempo real, calibraciones, veredictos.<br/>• Requisito no funcional: UI clara tipo instrumento de laboratorio (evitar tema oscuro).", table_cell_style),
            Paragraph("Matriz de requerimientos y documento de especificación formal (<code>redesign_spec.md</code>).", table_cell_style)
        ],
        [
            Paragraph("<b>2. Diseño de Arquitectura</b>", table_cell_bold),
            Paragraph("• Arquitectura en 4 capas desacopladas (Hardware, Lógica, Datos, UI).<br/>• Patrón <i>Adapter/Bridge</i> para aislar el SDK del instrumento (<code>pypalmsens</code>).<br/>• Diseño del hilo de adquisición asíncrono y esquemas de datos JSON.", table_cell_style),
            Paragraph("Diagrama de paquetes, contratos de interfaz y esquemas de métodos.", table_cell_style)
        ],
        [
            Paragraph("<b>3. Implementación Modular</b>", table_cell_bold),
            Paragraph("• <code>core</code>: Hilos de adquisición, control de conexión y modo Mock.<br/>• <code>interpretation</code>: Filtros digitales, regresión de calibración, cálculo LOD/LOQ.<br/>• <code>data</code>: Motores de persistencia de sesión e importadores CSV/Excel.<br/>• <code>ui</code>: Interfaz PySide6 (Qt) con graficado de alta tasa (<code>pglive</code>/<code>pyqtgraph</code>).", table_cell_style),
            Paragraph("Código fuente estructurado en paquetes independientes y testeables.", table_cell_style)
        ],
        [
            Paragraph("<b>4. Aseguramiento de Calidad (QA)</b>", table_cell_bold),
            Paragraph("• Construcción de suite de pruebas unitarias e integración con <code>pytest</code>.<br/>• Verificación matemática de modelos de calibración lineal y no lineal.<br/>• Pruebas de estrés y límites de detección con señales estocásticas simuladas.", table_cell_style),
            Paragraph("14 módulos de pruebas automatizadas con validación continua.", table_cell_style)
        ],
        [
            Paragraph("<b>5. Empaquetado y Entrega</b>", table_cell_bold),
            Paragraph("• Congelamiento determinista de dependencias (<code>requirements.txt</code>).<br/>• Preparación para generación de ejecutables portables con <code>PyInstaller</code>.<br/>• Documentación de arquitectura y guías de uso para laboratorio.", table_cell_style),
            Paragraph("Distribución de software lista para ejecución en entornos Windows.", table_cell_style)
        ]
    ]

    phases_table = Table(phases_table_data, colWidths=[80, 272, 180])
    phases_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1E3A8A")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
    ]))
    story.append(phases_table)

    # Forzar salto limpio a Página 2
    story.append(PageBreak())

    # ========================== PÁGINA 2 ==========================
    # 3. Arquitectura del Sistema
    story.append(Paragraph("3. Arquitectura Modular del Sistema", h1_style))
    story.append(Paragraph(
        "El sistema se organiza en capas independientes para maximizar la mantenibilidad y desacoplar el hardware de la lógica visual:",
        body_style
    ))

    arch_table_data = [
        [
            Paragraph("Capa del Sistema", table_header_style),
            Paragraph("Módulos Clave", table_header_style),
            Paragraph("Responsabilidad de Ingeniería", table_header_style)
        ],
        [
            Paragraph("<b>1. Hardware & Core</b>", table_cell_bold),
            Paragraph("<code>device_manager.py</code><br/><code>acquisition.py</code><br/><code>models.py</code>", table_cell_style),
            Paragraph("Gestión de comunicación USB/Serial con el potenciostato. Implementa <code>MockAcquisitionThread</code> para simular el comportamiento físico según la ecuación de Cottrell sin hardware real.", table_cell_style)
        ],
        [
            Paragraph("<b>2. Interpretación Analítica</b>", table_cell_bold),
            Paragraph("<code>filtering.py</code>, <code>calibration.py</code><br/><code>detection_limits.py</code><br/><code>verdict.py</code>", table_cell_style),
            Paragraph("Filtros digitales (Savitzky-Golay, media móvil), extracción de corriente de meseta, cálculo de curvas de calibración (lineal y 4PL) y emisión del veredicto cuantitativo.", table_cell_style)
        ],
        [
            Paragraph("<b>3. Datos y Persistencia</b>", table_cell_bold),
            Paragraph("<code>importers/</code>, <code>exporter.py</code><br/><code>session_store.py</code><br/><code>method_store.py</code>", table_cell_style),
            Paragraph("Persistencia de parámetros experimentales (métodos JSON), historial de ensayos, e importación/exportación fluida a formatos estándar de laboratorio (CSV, Excel .xlsx).", table_cell_style)
        ],
        [
            Paragraph("<b>4. Presentación (UI/UX)</b>", table_cell_bold),
            Paragraph("<code>main_window.py</code><br/><code>live_plot_widget.py</code><br/><code>control_panel.py</code>", table_cell_style),
            Paragraph("Interfaz científica reactiva construida en PySide6 y <code>pglive</code>/<code>pyqtgraph</code>. Disposición de 3 regiones optimizada para monitores de laboratorio con tema claro.", table_cell_style)
        ]
    ]

    arch_table = Table(arch_table_data, colWidths=[110, 142, 280])
    arch_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0284C7")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
    ]))
    story.append(arch_table)
    story.append(Spacer(1, 4))

    # 4. Retos y Decisiones de Ingeniería
    story.append(Paragraph("4. Decisiones Clave y Soluciones de Ingeniería", h1_style))
    decisions = [
        ("Concurrencia y Reactividad:", "La adquisición de datos corre en un hilo de ejecución secundario (<code>QThread</code>), comunicándose con la interfaz gráfica exclusivamente por señales y ranuras (signals/slots) de Qt. Esto evita congelamientos de UI incluso a altas tasas de muestreo."),
        ("Simulación de Hardware (Mocking):", "Permite desarrollo continuo y pruebas en entornos sin potenciostato conectado, modelando el decaimiento exponencial inicial de doble capa y la estabilización faradaica."),
        ("Ergonomía Visual Científica:", "Diseño enfocado en instrumentación de laboratorio: tipografía nítida, controles compactos y paleta clara que evita el deslumbramiento bajo la iluminación típica de mesas de ensayo."),
        ("Robustez Numérica y Unidades:", "Manejo unificado de unidades SI con conversión automática (de pA a mA), garantizando precisión estadística en el ajuste de curvas.")
    ]
    for tit, dsc in decisions:
        story.append(Paragraph(f"• <b>{tit}</b> {dsc}", body_style))

    story.append(Spacer(1, 4))

    # 5. Verificación y QA
    story.append(Paragraph("5. Batería de Pruebas y Aseguramiento de Calidad (QA)", h1_style))
    
    qa_table_data = [
        [
            Paragraph("Componente", table_header_style),
            Paragraph("Módulo de Prueba (pytest)", table_header_style),
            Paragraph("Criterio de Aceptación", table_header_style)
        ],
        [
            Paragraph("Curvas de Calibración", table_cell_bold),
            Paragraph("<code>test_calibration.py</code>", table_cell_style),
            Paragraph("Exactitud de pendiente, intercepto, R² > 0.99 e intervalos de predicción.", table_cell_style)
        ],
        [
            Paragraph("Límites LOD / LOQ", table_cell_bold),
            Paragraph("<code>test_detection_limits.py</code>", table_cell_style),
            Paragraph("Fórmula IUPAC (3.3 * s / S y 10 * s / S) verificada con muestras en blanco.", table_cell_style)
        ],
        [
            Paragraph("Filtros Digitales", table_cell_bold),
            Paragraph("<code>test_filtering.py</code>", table_cell_style),
            Paragraph("Reducción de ruido de alta frecuencia sin alterar la meseta de medición.", table_cell_style)
        ],
        [
            Paragraph("Simulación y Adquisición", table_cell_bold),
            Paragraph("<code>test_acquisition_mock.py</code>", table_cell_style),
            Paragraph("Arranque, detención controlada y entrega estable de paquetes de datos.", table_cell_style)
        ],
        [
            Paragraph("Exportación de Datos", table_cell_bold),
            Paragraph("<code>test_formatting.py</code>, <code>test_exporter.py</code>", table_cell_style),
            Paragraph("Generación fiel de tablas y metadatos en archivos CSV y Excel (.xlsx).", table_cell_style)
        ]
    ]

    qa_table = Table(qa_table_data, colWidths=[120, 150, 262])
    qa_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#334155")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
    ]))
    story.append(qa_table)
    story.append(Spacer(1, 6))

    # 6. Conclusión y Firma
    story.append(Paragraph("6. Conclusión", h1_style))
    story.append(Paragraph(
        "<b>ChronoAmp</b> cumple integralmente con los estándares de ingeniería de software para instrumentación analítica: "
        "alta reactividad, integridad de datos, arquitectura desacoplada y validación formal de cálculos electroquímicos. "
        "El producto constituye una herramienta lista para su implementación y uso productivo.",
        body_style
    ))

    closing_data = [
        [
            Paragraph("<b>Proyecto:</b> <code>chronoamp_app</code><br/><b>Lenguaje:</b> Python 3.10+ / PySide6", table_cell_style),
            Paragraph("<b>Estado:</b> Aprobado para Producción<br/><b>Cobertura:</b> 14 suites automatizadas", table_cell_style),
            Paragraph("<b>Validación de Ingeniería:</b><br/>Arquitectura y Realización Concluida", table_cell_bold)
        ]
    ]
    closing_table = Table(closing_data, colWidths=[177, 177, 178])
    closing_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(closing_table)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully built at: {output_path}")

if __name__ == "__main__":
    output_pdf = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "Informe_Realizacion_ChronoAmp.pdf"
    )
    if len(sys.argv) > 1:
        output_pdf = sys.argv[1]
    build_pdf(output_pdf)
