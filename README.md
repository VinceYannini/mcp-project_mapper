# MCP Folder Mapper 🗺️

Un Servidor MCP (Model Context Protocol) ligero, ultrarrápido y seguro diseñado para empoderar a tus Agentes de Inteligencia Artificial (Claude, Cursor, Cline, etc.) con "conciencia espacial". 

**El problema:** Cuando le pides a una IA que lea una carpeta, normalmente se satura leyendo dependencias inútiles (como `node_modules`), agota tu límite de tokens y genera respuestas alucinadas.
**La solución:** Folder Mapper escanea tus directorios bloqueando automáticamente la basura, respetando límites de profundidad y devolviendo a tu IA un mapa JSON limpio y estructurado de tu proyecto.

## 🚀 Características Principales
- **Optimizado para IA:** Filtra automáticamente carpetas pesadas (`node_modules`, `.git`, `venv`, `__pycache__`, `dist`).
- **Seguridad por Diseño (Safe-chroot):** Bloquea intentos de escaneo a la raíz del sistema operativo o carpetas sensibles (`/etc`, `C:\Windows`) para evitar inyecciones de prompts (Prompt Injections).
- **Control de Tokens:** Limita la profundidad de escaneo (`max_depth` configurable) para proteger tu billetera de cobros excesivos por tokens en las APIs.

## ⚙️ Instalación (Plug-and-Play)

### Requisitos previos
- Python 3.10 o superior.
- `uv` (recomendado) o `pip`.

### Para Claude Desktop
Edita tu archivo `claude_desktop_config.json` e inyecta este servidor:

```json
{
  "mcpServers": {
    "folder-mapper": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/RUTA/HACIA/TU/CLON/mcp-project_mapper",
        "mcp-folder-mapper"
      ]
    }
  }
}
```

### Para Cursor IDE / Windsurf
1. Ve a `Settings > Features > MCP` (o la sección MCP de tu editor).
2. Añade un nuevo servidor:
   - **Type:** `command`
   - **Name:** `folder-mapper`
   - **Command:** `uv run --directory /RUTA/HACIA/TU/CLON/mcp-project_mapper mcp-folder-mapper`

## 💬 ¿Cómo lo usa tu IA?
Una vez que el servidor esté activo, tu asistente de IA tendrá acceso a la herramienta interna `map_workspace(path, max_depth)`.
No tienes que programar nada más. Simplemente dile a tu asistente en el chat:
> *"Por favor, mapea la carpeta actual para entender la estructura de mi proyecto."*

---

## 📜 Licencia (Uso Privado y No Comercial)
Este proyecto se distribuye bajo una licencia estricta de **Uso Personal y No Comercial**. 
Queda prohibida su integración, distribución o monetización por parte de corporaciones, agencias, o entidades comerciales sin previa autorización. 
*(Para versiones Enterprise con aislamiento de datos, contactar a Yaco Solutions).*

---
*Diseñado con precisión por **Yaco Solutions***
