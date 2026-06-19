from ultralytics import YOLO

# ─── CONFIGURACIÓN ───────────────────────────────────────
MODELO = "runs/detect/mi_modelo_v2/weights/best.pt"
FUENTE  = "Imagenes_Prueba"   # carpeta, imagen o video
CONFIANZA = 0.5                  # umbral de detección (0-1)
# ─────────────────────────────────────────────────────────

model = YOLO(MODELO)

resultados = model.predict(
    source=FUENTE,
    conf=CONFIANZA,
    save=True,        # guarda imágenes con las detecciones
    save_txt=True,    # guarda las coordenadas en .txt
    show_conf=True,   # muestra el porcentaje de confianza
)

print("\n✅ Inferencia terminada")
print(f"📂 Resultados en: runs/detect/predict/")

# Mostrar resumen de detecciones
for r in resultados:
    cajas = len(r.boxes)
    print(f"  {r.path.split('/')[-1]} → {cajas} casco(s) detectado(s)")