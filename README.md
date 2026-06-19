# Vision-Artificial
# Sistema Inteligente de Detección Automática del Uso de Cascos de Seguridad mediante Visión Artificial y YOLOv8

## Integrantes
Estefhany Betzabe Covarrubias Sánchez - 23310387
Santiago Lomas Pérez - 23310391

## Instrucciones de ejecución
### Requisitos previos
- Python 3.12
- Git
- Entorno virtual (recomendado)

### Pasos
1. Clonar el repositorio:
>git clone https://github.com/usuario/Vision-Artificial.git
>cd Vision-Artificial

2. Crear y activar el entorno virtual:
>python -m venv .venv
>source .venv/bin/activate        # Linux/Mac
>.venv\Scripts\activate           # Windows

3. Instalar las dependencias:
>pip install -r requirements.txt

4. Entrenar el modelo con el dataset incluido:
>python train.py

5. Guarda las imagenes que quieras analizar en la carpeta `Imagenes_Prueba/`.

6. Ejecutar la inferencia sobre imágenes nuevas:
>python inferencia.py

Las imágenes con las detecciones generadas se guardarán en `runs/detect/predict/`.

## Planteamiento del Problema
En los sectores de construcción, manufactura, minería e industrias de alto riesgo, el uso adecuado del equipo de protección personal (EPP) es fundamental para garantizar la seguridad de los trabajadores. Entre estos elementos, el casco de seguridad constituye una de las principales medidas de protección contra impactos, caídas de objetos y accidentes laborales.

Sin embargo, en muchas ocasiones los trabajadores omiten el uso del casco o lo utilizan de manera incorrecta, incrementando significativamente la probabilidad de sufrir lesiones graves. La supervisión manual realizada por personal de seguridad suele ser limitada debido al tamaño de las áreas de trabajo, la cantidad de empleados y la imposibilidad de mantener una vigilancia constante.

Ante esta problemática, surge la necesidad de implementar soluciones tecnológicas capaces de monitorear automáticamente el cumplimiento de las normas de seguridad. La visión artificial y los modelos de detección de objetos basados en inteligencia artificial, como YOLOv8, ofrecen una alternativa eficiente para identificar en tiempo real a trabajadores que utilizan o no utilizan casco de protección, permitiendo generar alertas y mejorar las condiciones de seguridad en el entorno laboral.

## Justificación
La seguridad ocupacional es una prioridad en cualquier entorno industrial. Los accidentes relacionados con la falta de equipo de protección personal generan pérdidas humanas, económicas y operativas para las organizaciones.

La implementación de un sistema automatizado basado en inteligencia artificial permitirá realizar una supervisión continua y precisa del uso de cascos de seguridad sin depender exclusivamente de la observación humana. Además, la utilización de modelos de visión artificial como YOLOv8 posibilita la detección en tiempo real con altos niveles de precisión, contribuyendo a la prevención de accidentes y al cumplimiento de las normativas de seguridad laboral.

Este proyecto también representa una aplicación práctica de técnicas modernas de aprendizaje profundo (Deep Learning), procesamiento de imágenes y detección de objetos, demostrando el potencial de la inteligencia artificial para resolver problemas reales dentro del ámbito industrial.

## Objetivo General
Desarrollar un sistema inteligente basado en visión artificial y el modelo YOLOv8 que permita detectar automáticamente, en tiempo real, si los trabajadores utilizan correctamente el casco de seguridad dentro de entornos laborales de riesgo.

## Objetivos específicos
1.	Recolectar un conjunto de imágenes de trabajadores con y sin casco. 
2.	Etiquetar las imágenes para el entrenamiento del modelo. 
3.	Entrenar un modelo YOLOv8 personalizado. 
4.	Evaluar la precisión del modelo mediante métricas de detección. 
5.	Implementar la detección en imágenes, videos o cámara en tiempo real. 

### Descripción del Flujo

1. **Captura:** Las cámaras IP ubicadas en los accesos a zonas de riesgo capturan
video en tiempo real a 30 fps.

2. **Procesamiento:** Cada frame es procesado por el modelo YOLOv8 entrenado,
ejecutándose en la unidad de cómputo local (Jetson Nano), lo que garantiza baja
latencia sin depender de conexión a internet.

3. **Detección positiva (casco detectado):** El sistema registra el evento en una
bitácora digital con marca de tiempo, el torniquete permite el acceso y el monitor
de seguridad muestra el frame con el bounding box verde.

4. **Detección negativa (sin casco):** El sistema activa una alarma sonora y visual,
bloquea el torniquete e impide el acceso a la zona de riesgo. Simultáneamente,
envía una notificación al supervisor de seguridad vía mensaje o correo electrónico.

5. **Registro y reportes:** Todos los eventos (accesos permitidos y denegados) quedan
almacenados en una base de datos local, permitiendo generar reportes periódicos de
cumplimiento de normas de seguridad para auditorías internas.

### Beneficios del Sistema
- Supervisión continua 24/7 sin depender de personal humano.
- Reducción de accidentes por incumplimiento de EPP.
- Generación automática de registros y reportes de seguridad.
- Escalable a otras zonas de la planta agregando más cámaras.
- Posibilidad de ampliar el modelo para detectar otros elementos de EPP
(chalecos, guantes, lentes de seguridad).