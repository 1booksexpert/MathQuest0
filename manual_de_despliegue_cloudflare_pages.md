# Manual de Despliegue Seguro: Cloudflare Pages

Cloudflare ofrece una de las infraestructuras más seguras del mundo contra ataques DDoS y de inyección.

## 1. Preparación del Repositorio
1. Sube el código de tu web app a un repositorio privado en **GitHub** o **GitLab**.

## 2. Configuración en Cloudflare
1. Inicia sesión en el panel de [Cloudflare](https://dash.cloudflare.com/).
2. Ve a **Workers & Pages > Create application > Pages > Connect to Git**.
3. Selecciona tu repositorio de MathQuest.

## 3. Configuración de Compilación
1. **Framework preset**: Selecciona el que uses (React, Vue, o None si es HTML estático).
2. **Build command**: (Ej. `npm run build`).
3. **Build output directory**: (Ej. `dist` o `public`).

## 4. Seguridad de "Por Vida" y Alta Resistencia
Para asegurar el sitio contra ataques:
1. **WAF (Web Application Firewall)**: Activa las reglas gestionadas de Cloudflare para bloquear ataques SQLi y XSS.
2. **DDoS Protection**: Cloudflare Pages incluye protección ilimitada contra DDoS de capa 7 de forma nativa.
3. **DNSSEC**: Actívalo en la pestaña DNS para prevenir el secuestro de dominio.
4. **HSTS**: Fuerza conexiones HTTPS en todo momento.

## 5. Variables de Entorno
Añade tus claves de Supabase (`SUPABASE_URL` y `SUPABASE_ANON_KEY`) en la configuración de la aplicación en Cloudflare para que la app pueda conectarse a la base de datos de forma segura.
