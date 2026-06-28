# 🚀 Impulsa PIE - Plataforma de Gestión Educativa

Plataforma B2B desarrollada en Django orientada a optimizar la gestión técnica, normativa y pedagógica de los Programas de Integración Escolar (PIE) en Chile. 

## ⚙️ Stack Tecnológico
* **Backend:** Python 3, Django 5.x
* **Frontend:** HTML5, Tailwind CSS, JavaScript nativo
* **Base de Datos:** SQLite3 (Desarrollo) / Soporte preparado para PostgreSQL
* **Arquitectura:** MVT (Model-View-Template)

## 📌 Características Principales
* **Catálogo Dinámico:** Gestión de servicios (Asesorías, Auditorías) desde el panel de administración.
* **Auto-Registro Seguro:** Sistema de creación de cuentas públicas con prevención de escalada de privilegios y validación de correos únicos.
* **Motor de Agendamiento:** Interfaz transaccional con validación de fechas (bloqueo automático de fines de semana y feriados) y selección de bloques horarios.
* **Perfiles Extendidos:** Integración del modelo `User` nativo de Django con metadata de negocio (Institución educativa, roles) mediante relaciones `OneToOne`.

## 🛠️ Instalación y Despliegue Local

1. Clonar el repositorio:
```bash
git clone [https://github.com/MauricioSec/impulsa-pie.git](https://github.com/MauricioSec/impulsa-pie.git)