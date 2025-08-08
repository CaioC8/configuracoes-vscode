import os
import platform
from pathlib import Path
import shutil


def get_settings_path():
    system = platform.system()
    if system == "Windows":
        return Path(os.getenv("APPDATA")) / "Code" / "User" / "settings.json"
    elif system == "Darwin":  # macOS
        return (
            Path.home()
            / "Library"
            / "Application Support"
            / "Code"
            / "User"
            / "settings.json"
        )
    else:  # Linux
        return Path.home() / ".config" / "Code" / "User" / "settings.json"


# Caminhos
settings_path = get_settings_path()
settings_txt_path = Path("settings.txt")
backup_path = Path("previousSettings.txt")

# Verificações
if not settings_path.exists():
    raise FileNotFoundError(f"Arquivo settings.json não encontrado em: {settings_path}")

if not settings_txt_path.exists():
    raise FileNotFoundError(f"Arquivo settings.txt não encontrado na pasta do script.")

# Backup do settings.json atual
shutil.copy(settings_path, backup_path)
print(f"\nBackup criado em: {backup_path}")

# Substitui o conteúdo do settings.json pelo do settings.txt
with open(settings_txt_path, "r", encoding="utf-8") as f:
    new_settings_content = f.read()

with open(settings_path, "w", encoding="utf-8") as f:
    f.write(new_settings_content)

print(f"\nConfigurações do VS Code atualizadas com sucesso usando {settings_txt_path}")
