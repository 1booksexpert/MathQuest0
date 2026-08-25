# Informe Técnico de Implementación: MathQuest

Este informe proporciona una descripción exhaustiva del ecosistema **MathQuest**, detallando su arquitectura, lógica de funcionamiento y la infraestructura necesaria para su despliegue global.

---

## 1. Visión General del Producto
**MathQuest** es una plataforma educativa multiplataforma (Web, Android, Desktop) diseñada para enseñar matemáticas a niños desde los niveles más básicos (párvulos) hasta niveles avanzados, utilizando la metodología **CPA (Concreto-Pictórico-Abstracto)**.

### Experiencia del Usuario
- **Niño (Estudiante):** Interfaz táctil de alta visibilidad, refuerzo positivo visual (caras sonrientes notorias), ciclo de 3 repeticiones para maestría y progresión bloqueada basada en el éxito.
- **Tutor (Padre/Educador):** Acceso protegido por "Parental Gate", panel de justificación pedagógica, seguimiento de progreso detallado y gestión de suscripciones.

---

## 2. Arquitectura de Frontend
El frontend se divide en tres interfaces principales diseñadas para ser consistentes visualmente bajo el sistema **Luminous Equation** (estética 3D Claymation).

### Tecnologías Core
- **Framework:** React / Next.js (recomendado para SEO y rendimiento).
- **Estilos:** Tailwind CSS con tokens de diseño personalizados (Colores: `#007bff` primary, superficies suaves).
- **Animaciones:** Framer Motion para transiciones de UI y CSS/JS para efectos de partículas.
- **Gráficos 3D:** Three.js para escenas interactivas de pre-renderizado.

### Módulos Críticos
1.  **Dashboard del Estudiante:** Punto de entrada con mapa de niveles y "Trophy Case".
2.  **Motor de Gameplay:** Interfaz "Jumbo" con botones de gran tamaño para accesibilidad visual y motriz.
3.  **Parental Control Center:** Área administrativa para tutores con visualización de datos de `progress_logs`.

---

## 3. Arquitectura de Backend y Datos (BaaS)
Para garantizar costo cero inicial y alta escalabilidad, se utiliza **Supabase** como núcleo del backend.

### Base de Datos (PostgreSQL)
Tablas configuradas con **Row Level Security (RLS)**:
- **`profiles`:** Almacena XP, nivel actual y metadatos del niño.
- **`progress_logs`:** Registro de cada hito de aprendizaje (repeticiones, fallos, éxitos).
- **`tutor_settings`:** Vinculación entre el adulto y el niño, configuración de metas diarias.
- **`leaderboard`:** Vista materializada para el ranking global por XP.

### Autenticación
- **Email/Password:** Principalmente para tutores.
- **OAuth (Google/Apple):** Para agilizar el onboarding.
- **Sincronización:** Uso de `supabase-js` para persistencia en tiempo real entre dispositivos.

---

## 4. Estrategia de Despliegue y Hosting
Se ha seleccionado un modelo de **Hospedaje de Alta Capacidad** (Vercel o Netlify) para mitigar el agotamiento de créditos por activos pesados.

### Infraestructura
- **Hosting Web:** Vercel/Netlify conectado a un repositorio de GitHub (CI/CD automático).
- **Edge Network:** Distribución global de activos (videos/imágenes) para baja latencia.
- **Seguridad:**
    - **SSL/TLS:** Cifrado automático.
    - **Firewall (WAF):** Protección contra inyecciones SQL y ataques XSS.
    - **DDoS Protection:** Capa de protección nativa del proveedor de hosting.

---

## 5. Monetización e Integración de Pagos
Modelo **Freemium** basado en suscripciones SaaS gestionado a través de **Stripe**.

- **Pasarela:** Stripe Billing & Checkout (Cumplimiento PCI).
- **Seguridad Parental:** El acceso a la compra requiere resolver un reto matemático complejo (Parental Gate).
- **Webhooks:** Sincronización automática; Stripe informa a Supabase para actualizar el `subscription_status` del perfil.

---

## 6. Producción de Activos Multimedia (Videos 3D)
Para Reels/TikTok y marketing, el flujo de producción sugerido es:
1.  **IA de Video:** Luma Dream Machine o Runway Gen-3 utilizando las imágenes de referencia generadas ({{DATA:IMAGE:IMAGE_18}}, {{DATA:IMAGE:IMAGE_19}}).
2.  **Consistencia:** Instrucciones de prompt centradas en "Claymation", "Soft Lighting" y "Tactile textures".

---

## 7. Datos que no debes olvidar (Checklist de Implementación)
- [ ] **Cumplimiento Legal:** Asegurar que los términos de uso mencionen COPPA/GDPR Kids para el manejo de datos de menores.
- [ ] **Offline Mode:** Implementar Service Workers para que la app funcione (al menos en niveles básicos) sin conexión a internet.
- [ ] **Analíticas Éticas:** Evitar rastreo invasivo de niños; medir solo hitos de aprendizaje, no comportamiento publicitario.
- [ ] **Internacionalización (i18n):** Preparar la estructura de archivos para traducir el contenido a múltiples idiomas desde el día 1.
- [ ] **Escalabilidad de DB:** Monitorear el tamaño de `progress_logs`, ya que con miles de usuarios y repeticiones, esta tabla crecerá exponencialmente.

---
**Preparado para la Fase de Desarrollo V1.0**