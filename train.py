from ultralytics import YOLO
import os

# ─── CONFIGURACIÓN ───────────────────────────────────────────
DATASET_YAML = "dataset/data.yaml"  
MODELO_BASE  = "yolov8n.pt"            # nano: el más rápido para Codespaces sin GPU
EPOCHS       = 50
BATCH        = 8                       # baja a 4 si te da error de memoria
IMG_SIZE     = 640
# ─────────────────────────────────────────────────────────────

# Verificar que el yaml existe antes de entrenar
if not os.path.exists(DATASET_YAML):
    print(f"❌ No se encontró: {DATASET_YAML}")
    print("📁 Archivos en el directorio actual:")
    for f in os.listdir("."):
        print(f"   {f}")
else:
    print(f"✅ Dataset encontrado: {DATASET_YAML}")

    model = YOLO(MODELO_BASE)

    resultados = model.train(
        data=DATASET_YAML,
        epochs=EPOCHS,
        imgsz=IMG_SIZE,
        batch=BATCH,
        patience=10,
        name="mi_modelo_v2",
        device="cpu",
        workers=2,
    )

    print("\n✅ Entrenamiento terminado")
    print(f"📂 Resultados guardados en: {resultados.save_dir}")