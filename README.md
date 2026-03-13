# Analisis-Vulnerabilidades-Nessus
<img width="1024" height="576" alt="image" src="https://github.com/user-attachments/assets/c0f59c97-566e-4bbc-9499-8c834b2b921d" />

## Gestión de Vulnerabilidades de Red: Guía Operativa con Nessus
Este repositorio contiene un recurso técnico diseñado para analistas de seguridad que buscan profesionalizar y estandarizar sus flujos de trabajo en auditorías de infraestructura y redes. El objetivo es proporcionar una guía práctica, útil y orientada a escenarios reales, facilitando la identificación de activos críticos y la gestión de parches.

### 🛠️ El Arsenal del Analista
El recurso se centra en el uso avanzado de Nessus Essentials, integrando metodologías de análisis de red que permiten una visibilidad completa de la superficie de ataque.

### Contenido del Repositorio

* **Guía de Operación Rápida**: Flujo de trabajo desde el descubrimiento de hosts hasta la generación de reportes ejecutivos.

* **CheatSheet de Auditoría**: Diferenciación técnica entre escaneos externos, internos y credencializados.

* **Automatización con API**: Scripting en Python para la extracción masiva de hallazgos y monitorización de tareas.

* **Gestión de Hallazgos**: Metodología para priorizar vulnerabilidades utilizando métricas CVSS y VPR.

* **Instalación**: Guía paso a paso de como descargar e instalar.
  
* **Profundizando un poco**: Personalización de políticas en relación a un objetivo específico.

*****

## 1. Guía de Instalación de Nessus Essentials en Windows
Esta guía detalla el proceso paso a paso para instalar y configurar el escáner de vulnerabilidades Nessus en entornos Windows.

### 📋 Requisitos del Sistema
Antes de comenzar, asegúrate de que tu equipo cumple con los siguientes requisitos mínimos:

**Sistema Operativo**: Windows 10 / 11 o Windows Server 2016/2019/2022 (64-bit).

**Procesador**: 4 núcleos de 2 GHz.

**Memoria RAM**: 4 GB mínimo (se recomiendan 8 GB).

**Espacio en Disco**: 30 GB libres para la base de datos de plugins.

**Navegador**: Chrome, Firefox o Edge (versiones recientes).

### 🛠️ Paso 1: Obtención de la Licencia
Nessus Essentials requiere un código de activación gratuito que se envía por correo electrónico.

Visita la página de registro de Tenable Nessus Essentials.

Introduce tu nombre, apellidos y un correo electrónico válido.

Recibirás un email con el Activation Code. Guárdalo, lo necesitaremos en el Paso 4.

### 📥 Paso 2: Descarga del Instalador
Ve al portal de Descargas de Tenable.

Busca la sección de Windows.

Descarga el archivo ejecutable más reciente (ejemplo: Nessus-10.x.x-x64.msi).

![Captura de pantalla 2026-03-12 080914](https://github.com/user-attachments/assets/c0936050-e6cb-464d-8d4d-811748d92a01)

### ⚙️ Paso 3: Proceso de Instalación
Haz doble clic en el archivo .msi descargado.

Sigue el asistente de instalación:

Haz clic en Next.

![Captura de pantalla 2026-03-12 081015](https://github.com/user-attachments/assets/18f36f9c-ce75-4a05-826d-c8b8192a69fc)

Acepta el acuerdo de licencia (I accept the terms...).

Selecciona la ruta de instalación (por defecto: C:\Program Files\Tenable\Nessus).

Haz clic en Install.

Si el sistema solicita instalar Npcap, acéptalo. Es fundamental para que Nessus pueda "escuchar" el tráfico de red.

Una vez finalizado, haz clic en Finish. El servicio de Nessus se iniciará automáticamente en segundo plano.

![Captura de pantalla 2026-03-12 081037](https://github.com/user-attachments/assets/c922a53a-2ca1-4c69-a76c-43e81656ad93)

### 🌐 Paso 4: Configuración Web Inicial
Nessus se gestiona a través de una interfaz web.

Abre tu navegador y dirígete a: `https://localhost:8834`

![Captura de pantalla 2026-03-12 081150](https://github.com/user-attachments/assets/6eddf708-4cd7-4586-a099-537e8a70436c)

Advertencia de Seguridad: Verás un aviso de "Conexión privada". Esto se debe al certificado SSL local.

Haz clic en Configuración avanzada.

Selecciona Acceder a localhost (sitio no seguro).

![Captura de pantalla 2026-03-12 081241](https://github.com/user-attachments/assets/a44387cf-aac8-47ba-85a0-5631ec3cf5be)

En la pantalla de bienvenida, selecciona Nessus Essentials y presiona Continue.

![Captura de pantalla 2026-03-12 081309](https://github.com/user-attachments/assets/3a09d757-f508-42d9-9620-cd546b667c32)

Activación: * Si ya tienes el código del Paso 1, haz clic en Skip (Omitir) en el formulario de registro.

Introduce tu Activation Code en el campo correspondiente.

Cuenta de Usuario: Crea un nombre de usuario y contraseña para acceder al panel de control de Nessus.

![Captura de pantalla 2026-03-12 081401](https://github.com/user-attachments/assets/b27af0d7-89a4-4028-8804-82f361a8da34)

### ⏳ Paso 5: Descarga de Plugins
Tras configurar la cuenta, Nessus comenzará a descargar y compilar los plugins (las "firmas" de las vulnerabilidades).

**IMPORTANTE**
Este proceso puede tardar entre 20 y 60 minutos dependiendo de tu conexión a internet y la velocidad de tu CPU. No cierres el navegador ni apagues el equipo durante este proceso.

### 🚦 Comandos de Consola Útiles
Si necesitas gestionar el servicio manualmente, abre un Símbolo del Sistema (CMD) o PowerShell como Administrador:

Iniciar el servicio:
`net start "Tenable Nessus"`

Detener el servicio:
`net stop "Tenable Nessus"`

### 🛡️ Próximos Pasos
Una vez que veas el check verde de "Plugins Out to Date" y la interfaz de My Scans, estás listo para realizar tu primer escaneo.

******

## 2. Flujo de Trabajo Profesional (Nessus)

Nessus sigue un flujo de "descubrimiento y auditoría" de red:

**Configuración de Políticas**: Definir si el escaneo será básico, avanzado o con credenciales.

**Host Discovery**: Identificar qué equipos están encendidos en la red.

**Port Scanning**: Ver qué servicios están abiertos (HTTP, SSH, SMB, etc.).

**Detección de Vulnerabilidades**: Comparar los servicios encontrados con la base de datos de Nessus (Plugins).

**Análisis de Resultados**: Priorizar según el CVSS (Common Vulnerability Scoring System).

*****

## 3. CheatSheet: Conceptos y Configuraciones Clave

En Nessus, en lugar de flags de consola, dominamos los Tipos de Escaneo:

| **Concepto Técnico** | **Cuándo usarlo** | **Pro-Tip del Analista** |
|----------------------|-------------------|--------------------------|
| Basic Network Scan   | Escaneo inicial   | Ideal para tener una visión general sin saturar el ancho de banda |
| Advanced Scan        | Ajuste fino       | Permite activar o desactivar grupos de Plugins específicos (ej. solo plugins de Windows) |
| Credentialed Scan    | Auditoría interna | Al darle el usuario/contraseña del PC a Nessus, este detecta programas desactualizados que no se ven desde fuera |
| VPR (Vulnerability Priority Rating) | Al revisar alertas | Prioriza fallos que están siendo explotados ahora mismo en el mundo real, no solo por su teoría |

*****

## 3. Caso de uso

Al entrar al panel de control, vemos como hay un botón de new scan, pulsamos ahí y metemos la dirección ip a escanear, en mi caso localhost.


