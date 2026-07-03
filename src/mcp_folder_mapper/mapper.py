import os
import hashlib
from pathlib import Path

EXCLUDE_DIRS = {'.git', 'node_modules', 'venv', '.cache', '__pycache__', '.pytest_cache', 'build', 'dist'}

def get_file_hash(filepath):
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(65536), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except (PermissionError, OSError):
        return None

def map_directory(root_path, calculate_hash=False, max_depth=3, current_depth=0, visited_inodes=None):
    if visited_inodes is None:
        visited_inodes = set()
        
    root = Path(root_path)

    try:
        stat = root.stat()
        if stat.st_ino in visited_inodes:
            return {"name": root.name, "type": "dir", "children": [], "size": 0, "note": "symlink_cycle"}
        visited_inodes.add(stat.st_ino)
    except OSError:
        return {"name": root.name, "type": "dir", "children": [], "size": 0, "note": "unreadable"}

    tree = {"name": root.name, "type": "dir", "children": [], "size": 0}
    
    if current_depth >= max_depth:
        tree["note"] = f"max_depth ({max_depth}) alcanzado"
        return tree

    try:
        entries = sorted(os.scandir(root), key=lambda e: e.name)
        for entry in entries:
            if entry.name in EXCLUDE_DIRS:
                continue
            if entry.name.startswith('.'):
                continue

            try:
                entry_stat = entry.stat(follow_symlinks=False)
            except OSError:
                continue

            if entry.is_dir(follow_symlinks=False):
                child_tree = map_directory(
                    entry.path, 
                    calculate_hash, 
                    max_depth, 
                    current_depth + 1, 
                    visited_inodes
                )
                tree["children"].append(child_tree)
                tree["size"] += child_tree.get("size", 0)
            
            elif entry.is_file(follow_symlinks=False):
                file_size = entry_stat.st_size
                mtime = entry_stat.st_mtime
                
                file_info = {
                    "name": entry.name,
                    "type": "file",
                    "size": file_size,
                    "mtime": mtime
                }

                if calculate_hash:
                    h = get_file_hash(entry.path)
                    if h: file_info["hash"] = h

                tree["children"].append(file_info)
                tree["size"] += file_size

    except PermissionError:
        tree["note"] = "Permission denied"
    
    return tree
