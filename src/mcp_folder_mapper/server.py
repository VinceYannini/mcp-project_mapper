from mcp.server.fastmcp import FastMCP
from mcp_folder_mapper.mapper import map_directory
import os

# Inicializar FastMCP server
mcp = FastMCP("FolderMapper")

@mcp.tool()
def map_workspace(path: str, max_depth: int = 3, calculate_hash: bool = False) -> str:
    """
    Escanea y mapea un directorio local para obtener su estructura jerárquica.
    Filtra automáticamente carpetas como node_modules o .git para ahorrar tokens.
    
    Args:
        path: La ruta absoluta al directorio que deseas mapear.
        max_depth: Profundidad máxima del escaneo (por defecto 3, máximo 5 para evitar sobrecarga de tokens).
        calculate_hash: Si es True, calcula el hash MD5 de los archivos (más lento).
    """
    
    # Validaciones de seguridad básicas
    if max_depth > 5:
        max_depth = 5
        
    target_path = os.path.abspath(path)
    
    # Seguridad: Evitar escaneos de la raíz del sistema o rutas sensibles
    sensitive_paths = ['/', '/etc', '/var', '/usr', '/bin', '/sys', 'C:\\', 'C:\\Windows']
    if target_path in sensitive_paths:
        return "ERROR DE SEGURIDAD: Escaneo de rutas del sistema bloqueado por protección."

    if not os.path.exists(target_path):
        return f"ERROR: La ruta {target_path} no existe."
        
    if not os.path.isdir(target_path):
        return f"ERROR: La ruta {target_path} no es un directorio válido."
        
    try:
        import json
        result = map_directory(target_path, calculate_hash=calculate_hash, max_depth=max_depth)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"ERROR mapeando el directorio: {str(e)}"

def main():
    # Ejecutar en modo stdio (el estándar para clientes MCP como Cursor/Claude Desktop)
    mcp.run(transport='stdio')
