# Estrategia de Monetización: MathQuest

Para que la app sea autosustentable y segura para niños, implementaremos un modelo **Freemium con Enfoque Parental**.

## 1. Modelo de Suscripción (SaaS)
*   **Nivel Gratuito (Fundamentos)**: Acceso a los números 1 al 10 y operaciones básicas.
*   **Plan Premium (Explorador)**: Suscripción mensual/anual que desbloquea niveles avanzados (álgebra, geometría), reportes detallados para tutores y múltiples perfiles de niños.

## 2. Integración de Pagos (Stripe)
1. **Stripe Billing**: Es la opción más segura. No almacenas datos de tarjetas en tus servidores (cumplimiento PCI).
2. **Checkout Seguro**: Utiliza Stripe Checkout para redirigir al padre a una página de pago optimizada y protegida por 3D Secure.

## 3. "Parental Gate" para Compras
Para cumplir con las normativas de protección al menor (COPPA/GDPR Kids):
1. **Verificación de Edad**: Antes de acceder a la pantalla de pago, el adulto debe resolver un desafío matemático complejo (ej. "8 x 7 + 15").
2. **Confirmación por Email**: Envío obligatorio de recibo y notificación de activación de suscripción al correo del tutor.

## 4. Implementación Técnica en Supabase
1. Añade una columna `subscription_status` a la tabla `profiles`.
2. Utiliza **Webhooks de Stripe** para actualizar automáticamente el estado en Supabase cuando un pago se procese correctamente.
