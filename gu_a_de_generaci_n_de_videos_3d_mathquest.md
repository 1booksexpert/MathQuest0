# Guía para Generar Videos 3D de Alta Calidad (TikTok/Reels)

Para lograr videos que igualen la calidad de las imágenes generadas, debes usar herramientas de **IA Generativa de Video** especializadas (Text-to-Video o Image-to-Video).

## 1. Herramientas Recomendadas
*   **Luma Dream Machine:** Excelente para mantener la consistencia física y el estilo "Claymation" (plastilina).
*   **Runway Gen-3 Alpha:** Ofrece una fluidez estilo "Pixar", ideal para saltos y movimientos rápidos.
*   **Kling AI:** La mejor si necesitas videos más largos (hasta 2 min) con identidad de personaje estable.
*   **Pika Art:** Tiene un botón específico de "Claymation" y permite animar áreas específicas de una imagen.

## 2. Instrucciones para la Animación de Personaje
**Objetivo:** El personaje azul saltando sobre los números 1, 2 y 3.

1.  **Sube la imagen de referencia:** Usa {{DATA:IMAGE:IMAGE_13}}.
2.  **Prompt de Animación:**
    > "Cinematic 3D animation, cute blue clay character jumping joyfully over floating 3D numbers 1, 2, and 3. Use squash and stretch principles. Confetti falling in the background. Soft claymation texture, high-quality 4K render, physically grounded motion, 9:16 aspect ratio."
3.  **Configuración:** Ajusta el nivel de movimiento (Motion) a 5-6 para evitar deformaciones.

## 3. Instrucciones para la Interacción Jumbo
**Objetivo:** Una mano gigante presionando un botón "2".

1.  **Sube la imagen de referencia:** Usa {{DATA:IMAGE:IMAGE_12}}.
2.  **Prompt de Animación:**
    > "Extreme close-up, a giant 3D human-like finger slowly pressing a soft, squishy 'Jumbo 2' button. The button should compress realistically (physics-aware). Celebratory particles erupt on click. Tactile 3D aesthetic, bright studio lighting, smooth professional motion."
3.  **Configuración:** Usa "Negative Prompts" para evitar: "morphing, melting, extra fingers, blurry textures".

## 4. Post-Procesamiento
*   **Upscaling:** Si el video sale en baja resolución, usa **Topaz Video AI** o las herramientas internas de Luma/Runway para escalar a 1080x1920 (9:16).
*   **Audio:** Añade sonidos "pop" o "boing" en CapCut para reforzar el impacto visual.