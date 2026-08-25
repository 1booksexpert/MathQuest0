# Manual de Configuración de Supabase para MathQuest

Este manual detalla los pasos para configurar la infraestructura de datos, autenticación y seguridad en Supabase.

## 1. Creación del Proyecto
1. Ve a [supabase.com](https://supabase.com/) y crea una cuenta.
2. Haz clic en **"New Project"**.
3. Selecciona tu organización y asigna un nombre (ej. `MathQuest-Prod`).
4. Genera una contraseña segura para la base de datos y guárdala.
5. Selecciona la región más cercana a tus usuarios principales.

## 2. Configuración de la Base de Datos (SQL Editor)
Copia y ejecuta el siguiente script en el **SQL Editor** para crear las tablas definidas en el diseño:

```sql
-- Tabla de Perfiles
CREATE TABLE profiles (
  id UUID REFERENCES auth.users ON DELETE CASCADE PRIMARY KEY,
  username TEXT UNIQUE,
  current_level INT DEFAULT 1,
  total_xp INT DEFAULT 0,
  avatar_url TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW())
);

-- Tabla de Registro de Progreso
CREATE TABLE progress_logs (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
  module_name TEXT NOT NULL,
  repetition_count INT DEFAULT 1,
  is_mastered BOOLEAN DEFAULT FALSE,
  last_attempt TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW())
);

-- Tabla de Configuración de Tutores
CREATE TABLE tutor_settings (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  tutor_id UUID REFERENCES auth.users(id),
  child_id UUID REFERENCES profiles(id),
  daily_goal INT DEFAULT 3,
  difficulty_multiplier FLOAT DEFAULT 1.0
);
```

## 3. Políticas de Seguridad (RLS)
Para garantizar la seguridad, activa Row Level Security (RLS) en todas las tablas:

1. Ve a **Authentication > Policies**.
2. Para `profiles`: Crea una política que permita `SELECT` y `UPDATE` solo si `auth.uid() = id`.
3. Para `progress_logs`: Los tutores deben poder leer los logs de sus `child_id` vinculados en `tutor_settings`.

## 4. Autenticación
1. Ve a **Authentication > Providers**.
2. Habilita **Email/Password**.
3. (Opcional) Configura proveedores sociales (Google/Apple) para facilitar el acceso a los padres.
