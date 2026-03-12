.

# 🚀 Guía de Instalación de Nessus Essentials en Windows
Esta guía detalla el proceso paso a paso para instalar y configurar el escáner de vulnerabilidades Nessus en entornos Windows.

## 📋 Requisitos del Sistema
Antes de comenzar, asegúrate de que tu equipo cumple con los siguientes requisitos mínimos:

**Sistema Operativo**: Windows 10 / 11 o Windows Server 2016/2019/2022 (64-bit).

**Procesador**: 4 núcleos de 2 GHz.

**Memoria RAM**: 4 GB mínimo (se recomiendan 8 GB).

**Espacio en Disco**: 30 GB libres para la base de datos de plugins.

**Navegador**: Chrome, Firefox o Edge (versiones recientes).

## 🛠️ Paso 1: Obtención de la Licencia
Nessus Essentials requiere un código de activación gratuito que se envía por correo electrónico.

Visita la página de registro de Tenable Nessus Essentials.

Introduce tu nombre, apellidos y un correo electrónico válido.

Recibirás un email con el Activation Code. Guárdalo, lo necesitaremos en el Paso 4.

## 📥 Paso 2: Descarga del Instalador
Ve al portal de Descargas de Tenable.

Busca la sección de Windows.

Descarga el archivo ejecutable más reciente (ejemplo: Nessus-10.x.x-x64.msi).

![Captura de pantalla 2026-03-12 080914](https://github.com/user-attachments/assets/c0936050-e6cb-464d-8d4d-811748d92a01)

## ⚙️ Paso 3: Proceso de Instalación
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

## 🌐 Paso 4: Configuración Web Inicial
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

## ⏳ Paso 5: Descarga de Plugins
Tras configurar la cuenta, Nessus comenzará a descargar y compilar los plugins (las "firmas" de las vulnerabilidades).

[!IMPORTANT]
Este proceso puede tardar entre 20 y 60 minutos dependiendo de tu conexión a internet y la velocidad de tu CPU. No cierres el navegador ni apagues el equipo durante este proceso.

## 🚦 Comandos de Consola Útiles
Si necesitas gestionar el servicio manualmente, abre un Símbolo del Sistema (CMD) o PowerShell como Administrador:

Iniciar el servicio:
`net start "Tenable Nessus"`

Detener el servicio:
`net stop "Tenable Nessus"`

## 🛡️ Próximos Pasos
Una vez que veas el check verde de "Plugins Out to Date" y la interfaz de My Scans, estás listo para realizar tu primer escaneo.
