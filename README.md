# Rubber Ducky System Information Gatherer

Este script para Rubber Ducky está diseñado para recolectar información del sistema de manera no intrusiva, sin requerir privilegios de administrador.

## ⚠️ Advertencia Legal

Este script está diseñado únicamente para fines educativos y de prueba en sistemas propios. El uso de este script en sistemas sin autorización explícita es ilegal y no ético.

## 📋 Funcionalidades

El script recolecta la siguiente información del sistema:

- Información del usuario actual
- Perfil de usuario
- Nombre del equipo
- Dominio del usuario
- Información de red
- Servidores DNS
- Tabla ARP
- Tabla de enrutamiento
- Conexiones de red activas
- Carpetas compartidas
- Información del sistema
- Procesos en ejecución
- Software instalado

## 🛠️ Requisitos

- Rubber Ducky o dispositivo compatible
- CircuitPython instalado
- Bibliotecas necesarias:
  - adafruit_hid
  - usb_hid

## 📥 Instalación

1. Asegúrate de tener CircuitPython instalado en tu Rubber Ducky
2. Instala las bibliotecas necesarias:
   ```
   pip install adafruit-circuitpython-hid
   ```

## 🚀 Uso

1. Copia el archivo `GatherInfo.py` a tu Rubber Ducky
2. Renombralo a "code.py"
3. Conecta el Rubber Ducky al sistema objetivo
4. El script se ejecutará automáticamente
5. La información recolectada se guardará en `D:\system_info.txt`

## ⚙️ Funcionamiento

El script realiza las siguientes acciones:

1. Espera 2 segundos para la inicialización
2. Abre PowerShell
3. Ejecuta una serie de comandos para recolectar información
4. Guarda la información en un archivo de texto
5. Cierra PowerShell automáticamente

## 📝 Notas

- El script no requiere privilegios de administrador
- La información se guarda en la unidad D:
- El proceso es silencioso y no muestra ventanas
- El tiempo total de ejecución es aproximadamente 8 segundos

## 🔒 Seguridad

Este script está diseñado para ser utilizado en:
- Pruebas de penetración autorizadas
- Auditorías de seguridad
- Entornos de laboratorio controlados
- Sistemas propios

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles. 
