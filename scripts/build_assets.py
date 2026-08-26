from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
CV_PATH = ROOT / "Axel-Sanz-CV.pdf"
OG_PATH = ROOT / "og-image.png"


def font_path(name: str) -> Path:
    candidates = [
        Path("C:/Windows/Fonts") / name,
        Path("C:/Users/sanza/AppData/Local/Microsoft/Windows/Fonts") / name,
    ]
    return next((path for path in candidates if path.exists()), candidates[0])


def build_cv() -> None:
    regular = font_path("arial.ttf")
    bold = font_path("arialbd.ttf")
    pdfmetrics.registerFont(TTFont("AxelRegular", str(regular)))
    pdfmetrics.registerFont(TTFont("AxelBold", str(bold)))

    doc = SimpleDocTemplate(
        str(CV_PATH), pagesize=A4, rightMargin=18 * mm, leftMargin=18 * mm,
        topMargin=14 * mm, bottomMargin=14 * mm,
        title="CV - Axel Sanz", author="Axel Sanz",
    )
    styles = getSampleStyleSheet()
    green = colors.HexColor("#168760")
    dark = colors.HexColor("#17202a")
    muted = colors.HexColor("#4d5966")
    name = ParagraphStyle("Name", parent=styles["Title"], fontName="AxelBold", fontSize=25, leading=28, textColor=dark, spaceAfter=2)
    role = ParagraphStyle("Role", parent=styles["Normal"], fontName="AxelBold", fontSize=11, leading=14, textColor=green, spaceAfter=5)
    body = ParagraphStyle("Body", parent=styles["BodyText"], fontName="AxelRegular", fontSize=8.5, leading=11.2, textColor=muted, spaceAfter=4)
    heading = ParagraphStyle("Heading", parent=styles["Heading2"], fontName="AxelBold", fontSize=10, leading=13, textColor=dark, spaceBefore=7, spaceAfter=4, borderColor=green, borderWidth=0, borderPadding=0)
    job = ParagraphStyle("Job", parent=body, fontName="AxelBold", fontSize=9, textColor=dark, spaceAfter=1)

    story = [
        Paragraph("Axel Sanz", name),
        Paragraph("Desarrollador .NET Junior &amp; Data Analyst", role),
        Paragraph("Garín, Buenos Aires · +54 9 11 3877-6066 · sanzaxel12@hotmail.com<br/>linkedin.com/in/axelsanz-dev · github.com/Axelsanz12 · axelsanz12.github.io/AxelSanzdev/", body),
        Paragraph("PERFIL", heading),
        Paragraph("Desarrollador junior Backend/Data, estudiante de la Tecnicatura en Programación en UTN. Combino C#, SQL Server y .NET con más de 10 años de experiencia en planificación, logística y operaciones administrativas. Analizo procesos reales, estructuro datos y construyo soluciones orientadas a resultados.", body),
        Paragraph("EXPERIENCIA", heading),
        Paragraph("Analista de planificación | LOG-IN FARMA | Abr 2026 - Actualidad", job),
        Paragraph("• Planificación y seguimiento integral de operaciones logísticas y productivas.<br/>• Análisis de procesos para mejorar tiempos, recursos y costos.<br/>• Creación de indicadores y reportes en Excel para decisiones operativas.", body),
        Paragraph("Administrativo Sr | CYE Construcciones | Jul 2025 - Feb 2026", job),
        Paragraph("• Gestión de información operativa y administrativa con foco en precisión y control.<br/>• Organización de datos y optimización de procesos con información estructurada.", body),
        Paragraph("PROYECTOS DESTACADOS", heading),
        Paragraph("KioscoApp | C#, WinForms, SQL Server", job),
        Paragraph("Sistema de punto de venta con ABM, control de stock y vencimientos, registro de ventas y reportes en Excel.", body),
        Paragraph("Seguimiento de Ciclos | C#, ASP.NET Web Forms, SQL Server", job),
        Paragraph("Aplicación web que reemplaza planillas dispersas por datos trazables, con indicadores, filtros, roles, validaciones y replanificación por capacidad y SLA.", body),
        Paragraph("FORMACIÓN", heading),
    ]

    education = [
        [Paragraph("Tecnicatura en Programación", job), Paragraph("UTN Facultad Regional General Pacheco | En curso", body)],
        [Paragraph("Front-End JS", job), Paragraph("Talento Tech | Ago 2024 - Dic 2024 | Nota: 9.9/10", body)],
        [Paragraph("C# Nivel 1", job), Paragraph("MaxiPrograma | Feb 2023 - Mar 2023", body)],
        [Paragraph(".NET, POO y SQL", job), Paragraph("MaxiPrograma | Abr 2024 - Jun 2024", body)],
    ]
    table = Table(education, colWidths=[58 * mm, 110 * mm], hAlign="LEFT")
    table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 3), ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
    story.extend([table, Paragraph("HABILIDADES", heading), Paragraph("C# · .NET Framework · ASP.NET Web Forms · WinForms · SQL Server · T-SQL · HTML · CSS · JavaScript · Bootstrap · Git/GitHub · Power BI · Excel avanzado · Arquitectura en capas", body)])
    doc.build(story)


def build_og() -> None:
    image = Image.new("RGB", (1200, 630), "#0b0e13")
    draw = ImageDraw.Draw(image)
    font_bold = font_path("arialbd.ttf")
    font_regular = font_path("arial.ttf")
    draw.ellipse((830, -210, 1390, 350), fill="#10251f")
    draw.rectangle((72, 78, 78, 552), fill="#4fffb0")
    draw.text((112, 100), "AXEL.DEV", font=ImageFont.truetype(str(font_bold), 27), fill="#4fffb0")
    draw.text((108, 195), "Axel Sanz", font=ImageFont.truetype(str(font_bold), 86), fill="#e8eaf0")
    draw.text((112, 305), "Desarrollador .NET Junior", font=ImageFont.truetype(str(font_bold), 44), fill="#e8eaf0")
    draw.text((112, 383), "C#  ·  SQL Server  ·  ASP.NET  ·  Power BI", font=ImageFont.truetype(str(font_regular), 28), fill="#93a0b4")
    draw.text((112, 468), "10+ años en operaciones reales, ahora aplicados a software.", font=ImageFont.truetype(str(font_regular), 25), fill="#4fffb0")
    image.save(OG_PATH, optimize=True)


if __name__ == "__main__":
    build_cv()
    build_og()
    print(CV_PATH)
    print(OG_PATH)
