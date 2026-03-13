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

![Texto alternativo](images/uso1.jpg)

A la izquierda, veremos cómo sale que ya tenemos un escaneo activo.

![Texto alternativo](images/uso2.jpg)

Si pinchamos, se nos despliega un listado de escaneos, en este caso pinchamos en el que proceda.

![Texto alternativo](images/uso3.jpg)

Una vez dentro, vemos toda la información que nos proporciona

![Texto alternativo](images/uso4.jpg)

![Texto alternativo](images/uso5.jpg)

![Texto alternativo](images/uso6.jpg)

![Texto alternativo](images/uso7.jpg)


Una vez se complete al 100% el escaneo, ya podemos entrar donde sale la barra y vemos toda la información recopilada:

![Texto alternativo](images/uso8.jpg)

Como vemos, nos indica el nivel de criticidad por colores. Podemos entrar una a una en las diferentes vulnerabilidades y ver más información.

![Texto alternativo](images/uso9.jpg)

![Texto alternativo](images/uso10.jpg)

En este caso nos indica que el servidor SMB (servicio que permite a computadoras en una red compartir archivos, impresoras, puertos serie y comunicaciones entre procesos (IPC)) es vulnerable, y puede ser atacado mediante la técnica man-in-the-middle, la cual ya hemos explotado en alguna máquina de laboratorio.

Por último, decir que podemos hacer nuestros propios script personalizados con python e integrarlos con nessus mediante el uso de las API keys que nos proporciona nessus (en el panel de administrador, mi cuenta, API, generar), aquí vemos un ejemplo:

![Texto alternativo](images/uso11.jpg)

*****

## 4. 📊 Gestión de Hallazgos: Metodología de Priorización

Un error común del analista junior es tratar todas las vulnerabilidades por igual. En este "Arsenal", aplicamos una metodología de triaje basada en el riesgo real, combinando estándares abiertos con inteligencia de amenazas activa.

### 1. El Estándar CVSS (Common Vulnerability Scoring System)

Utilizamos el CVSS v3.1 para medir la severidad teórica de una vulnerabilidad. Este sistema analiza tres grupos de métricas:

**Base**: Características intrínsecas del fallo (¿Es remoto? ¿Requiere privilegios?).

**Temporal**: Estado actual de la vulnerabilidad (¿Existe un exploit público?).

**Environmental**: El impacto específico en nuestra infraestructura.

**Nota técnica**: Un CVSS de 9.8 (Critical) indica que el fallo es explotable de forma remota y sin interacción del usuario, lo que lo convierte en una prioridad inmediata.

### 2. El Factor VPR (Vulnerability Priority Rating)

A diferencia del CVSS, que es estático, el VPR es una métrica dinámica exclusiva de Nessus (Tenable) que utiliza Ciencia de Datos para predecir qué vulnerabilidades tienen más probabilidades de ser explotadas en los próximos 28 días.

**Por qué lo usamos**: El CVSS puede decir que un fallo es "Alto", pero si no hay nadie usándolo en el mundo real, su riesgo práctico es menor. El VPR analiza el panorama de amenazas (Twitter, Dark Web, foros de hackers) para elevar la prioridad de lo que realmente es peligroso hoy.

### 3. Matriz de Decisión para la Remediación

Para estandarizar la respuesta del equipo de seguridad, seguimos esta matriz de prioridad:

| **Prioridad** | **Combinación de métricas** | **Acción inmediata** |
|---------------|-----------------------------|----------------------|
| Ugente (P0) | VSS > 9.0 + VPR Crítico | Parcheo en menos de 24-48 horas |
| Alta (P1) | CVSS > 7.0 + Exploit disponible | Parcheo en el próximo ciclo de mantenimiento |
| Media (P2) | CVSS 4.0 - 6.0 | Monitorización y mitigación mediante controles compensatorios (Firewalls/WAF) |
| Baja (P3) | CVSS < 4.0 o Informacional | Registro en el backlog de endurecimiento (Hardening) |

*****

## 5. Políticas Personalizadas

No debemos quedarnos en la superficie de las políticas por defecto, debemos adaptarlas al tipo de escaneo que buscamos según nuestro objetivo, en este caso supongamos que tenemos como objetivo concreto windows. En el apartado de policies podemos establecer nuevas políticas a nuestro gusto.

![Texto alternativo](images/politicas1.jpg)

En este caso, vamos a hacer un escaneo avanzado

![Texto alternativo](images/politicas2.jpg)

Vamos a ir a la pestaña de plugins

![Texto alternativo](images/politicas3.jpg)

y ahí vamos a dar a deshabilitar todos

![Texto alternativo](images/politicas4.jpg)

y vamos a seleccionar por ejemplo los de windows únicamente

![Texto alternativo](images/politicas5.jpg)

Ahora, si queremos que el servidor no se ralentice, podemos reducir “Max simultaneous checks per host” a 2. Vamos a Settings > performance 

![Texto alternativo](images/politicas6.jpg)

![Texto alternativo](images/politicas7.jpg)

y por último guardamos cambios con

![Texto alternativo](images/politicas8.jpg)

