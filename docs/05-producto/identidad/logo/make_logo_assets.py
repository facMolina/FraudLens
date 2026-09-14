#!/usr/bin/env python3
"""Reconstruye los assets oficiales del logo de FraudLens a partir de la geometria
exacta extraida del pptx (Propuesta_de_Identidad_Visual_-_FraudLens.pptx, slide 14).

Grilla 3x3 en viewBox 100x100: columnas/filas en 22, 50, 78.
Dot regular r=8. Anomalia (columna 78, fila 22) r=12.
Fuente: Arimo Bold en el deck -> se usa Liberation Sans Bold (metric-compatible)
porque Arimo no esta instalada en este entorno.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT_DIR, exist_ok=True)

SS = 4  # supersampling factor para anti-aliasing

# Grid en unidades del viewBox 100x100
GRID = [22, 50, 78]
ANOMALY_POS = (78, 22)
R_REGULAR = 8
R_ANOMALY = 12

PALETTES = {
    "claro": {"regular": "#6B21A8", "anomalia": "#9333EA", "texto": "#0D0D10"},
    "oscuro": {"regular": "#7E22CE", "anomalia": "#C084FC", "texto": "#FFFFFF"},
}
BLANCO = "#FFFFFF"

FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def draw_isotipo(size_px, color_regular, color_anomalia, margin_frac=0.06):
    """Dibuja el isotipo (grilla 3x3 con anomalia) centrado, RGBA transparente."""
    ss_size = size_px * SS
    img = Image.new("RGBA", (ss_size, ss_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # viewBox logico 0-100, con margen para que no quede pegado al borde
    vb = 100
    margin = vb * margin_frac
    scale = ss_size / (vb + 2 * margin)

    def to_px(x, y):
        return ((x + margin) * scale, (y + margin) * scale)

    for cx in GRID:
        for cy in GRID:
            r = R_ANOMALY if (cx, cy) == ANOMALY_POS else R_REGULAR
            color = color_anomalia if (cx, cy) == ANOMALY_POS else color_regular
            x0, y0 = to_px(cx - r, cy - r)
            x1, y1 = to_px(cx + r, cy + r)
            draw.ellipse([x0, y0, x1, y1], fill=color)

    return img.resize((size_px, size_px), Image.LANCZOS)


def draw_logo_completo(icon_px, color_regular, color_anomalia, color_texto, out_path):
    """Isotipo + wordmark 'FraudLens' en horizontal, RGBA transparente."""
    icon = draw_isotipo(icon_px, color_regular, color_anomalia)

    font_size = int(icon_px * 0.62)
    font = ImageFont.truetype(FONT_BOLD, font_size)

    # Medir el texto con un canvas temporal
    tmp = Image.new("RGBA", (10, 10))
    tmp_draw = ImageDraw.Draw(tmp)
    bbox = tmp_draw.textbbox((0, 0), "FraudLens", font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    gap = int(icon_px * 0.28)
    pad = int(icon_px * 0.08)
    canvas_w = pad * 2 + icon_px + gap + text_w
    canvas_h = pad * 2 + max(icon_px, text_h)

    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    canvas.paste(icon, (pad, (canvas_h - icon_px) // 2), icon)

    draw = ImageDraw.Draw(canvas)
    text_x = pad + icon_px + gap - bbox[0]
    text_y = (canvas_h - text_h) // 2 - bbox[1]
    draw.text((text_x, text_y), "FraudLens", font=font, fill=color_texto)

    canvas.save(out_path)
    print("Guardado:", out_path, canvas.size)


def draw_favicon(size_px, out_path):
    """Icono en modo oscuro sobre cuadrado redondeado, replica el mockup del deck."""
    ss_size = size_px * SS
    img = Image.new("RGBA", (ss_size, ss_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    radius = int(ss_size * 0.102)
    border = max(1, int(ss_size * 0.012))
    draw.rounded_rectangle(
        [0, 0, ss_size - 1, ss_size - 1],
        radius=radius,
        fill="#17171B",
        outline="#7E22CE",
        width=border,
    )

    icon_scale = 0.5
    icon_px = int(ss_size * icon_scale)
    icon = draw_isotipo(icon_px, "#7E22CE", "#C084FC")
    # redimensiona el icono ya generado (a resolucion final) hacia arriba para pegarlo en el supersample
    icon_up = icon.resize((icon_px, icon_px), Image.LANCZOS)
    offset = ((ss_size - icon_px) // 2, (ss_size - icon_px) // 2)
    img.paste(icon_up, offset, icon_up)

    final = img.resize((size_px, size_px), Image.LANCZOS)
    final.save(out_path)
    print("Guardado:", out_path, final.size)


if __name__ == "__main__":
    # Isotipo solo, 3 variaciones
    draw_isotipo(1024, PALETTES["claro"]["regular"], PALETTES["claro"]["anomalia"]).save(
        f"{OUT_DIR}/isotipo-modo-claro.png"
    )
    draw_isotipo(1024, PALETTES["oscuro"]["regular"], PALETTES["oscuro"]["anomalia"]).save(
        f"{OUT_DIR}/isotipo-modo-oscuro.png"
    )
    draw_isotipo(1024, BLANCO, BLANCO).save(f"{OUT_DIR}/isotipo-monocromo-blanco.png")
    print("Isotipos guardados")

    # Logo completo (isotipo + wordmark), 2 variaciones
    draw_logo_completo(
        320,
        PALETTES["claro"]["regular"],
        PALETTES["claro"]["anomalia"],
        PALETTES["claro"]["texto"],
        f"{OUT_DIR}/logo-completo-modo-claro.png",
    )
    draw_logo_completo(
        320,
        PALETTES["oscuro"]["regular"],
        PALETTES["oscuro"]["anomalia"],
        PALETTES["oscuro"]["texto"],
        f"{OUT_DIR}/logo-completo-modo-oscuro.png",
    )

    # Favicon / app icon
    draw_favicon(512, f"{OUT_DIR}/favicon.png")
