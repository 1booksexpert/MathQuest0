# Configuración de Tablas Supabase - MathQuest

## 1. Tabla: `profiles` (Perfiles de Usuario/Niño)
Gestiona la información básica del estudiante.

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | `uuid` | PK, vinculada a `auth.users`. |
| `username` | `text` | Nombre del niño/avatar. |
| `current_level` | `int` | Nivel actual de progresión (ej. 1, 2, 3). |
| `total_xp` | `int` | Experiencia total acumulada. |
| `avatar_url` | `text` | URL del avatar seleccionado. |
| `created_at` | `timestamp` | Fecha de registro. |

## 2. Tabla: `progress_logs` (Registro de Hitos)
Registra cada vez que un niño completa una repetición o un nivel.

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | `uuid` | PK. |
| `user_id` | `uuid` | FK -> `profiles.id`. |
| `module_name` | `text` | Ej: "Numeros 1-5", "Suma Basica". |
| `repetition_count` | `int` | Cuántas veces ha completado el ejercicio. |
| `is_mastered` | `boolean` | True si superó el criterio de maestría. |
| `last_attempt` | `timestamp` | Fecha del último éxito. |

## 3. Tabla: `tutor_settings` (Configuración Parental)
Configuración personalizada por el adulto.

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | `uuid` | PK. |
| `tutor_id` | `uuid` | FK -> `auth.users` (el adulto). |
| `child_id` | `uuid` | FK -> `profiles.id`. |
| `daily_goal` | `int` | Minutos o ejercicios meta por día. |
| `difficulty_multiplier` | `float` | Ajuste manual de la velocidad de progresión. |

## 4. Tabla: `leaderboard` (Competencia Global)
Vista optimizada para rankings (puede ser una vista materializada).

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `user_id` | `uuid` | FK -> `profiles.id`. |
| `rank_score` | `int` | Puntaje calculado para el ranking. |
| `country_code` | `text` | Para competencia por regiones. |

## Políticas de Seguridad (RLS)
*   **Usuarios**: Solo pueden leer/escribir su propio `profile`.
*   **Tutores**: Tienen permisos de lectura sobre el `progress_logs` de sus hijos vinculados.
