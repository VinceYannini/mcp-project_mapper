# MCP Folder Mapper

Un Servidor MCP (Model Context Protocol) ligero y rápido para agentes de Inteligencia Artificial.
Permite a cualquier agente de IA mapear e indexar directorios locales sin reventar sus límites de tokens.

## Características
- **Optimizado para IA:** Filtra automáticamente carpetas basura (`node_modules`, `.git`, `venv`, `__pycache__`).
- **Seguro por Defecto:** Bloquea intentos de escaneo a la raíz del sistema o carpetas sensibles (`/etc`, `C:\Windows`).
- **Límites Inteligentes:** Tiene una profundidad máxima (max_depth) configurable (pero limitada a 5) para evitar desbordar el contexto del LLM.

## Instalación para Claude Desktop / Cursor

### Requisitos
- Python 3.10+
- `uv` o `pip`

### 1. Claude Desktop
Abre tu archivo `claude_desktop_config.json` y agrega:

```json
{
  "mcpServers": {
    "folder-mapper": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/ruta/absoluta/a/mcp-folder-mapper",
        "mcp-folder-mapper"
      ]
    }
  }
}
```

### 2. Cursor IDE
Ve a `Settings > Features > MCP`.
Añade un nuevo servidor:
- **Type:** command
- **Name:** folder-mapper
- **Command:** `uv run --directory /ruta/absoluta/a/mcp-folder-mapper mcp-folder-mapper`

## Uso (Para IAs)
Una vez conectado, tendrás acceso a la herramienta `map_workspace(path, max_depth, calculate_hash)`.
Simplemente pide a tu asistente: *"Mapea la carpeta actual para entender el proyecto"*.

---
*Desarrollado por [Yaco Solutions]*
