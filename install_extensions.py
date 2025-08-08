import subprocess
import shutil
import sys
from pathlib import Path

EXT_FILE = Path("extensions.txt")

if not EXT_FILE.exists():
    sys.exit(f"ERRO: Arquivo '{EXT_FILE}' não encontrado.")

if not shutil.which("code"):
    sys.exit(
        "ERRO: O comando 'code' não está no PATH. Ative-o no VS Code antes de rodar o script."
    )

with EXT_FILE.open(encoding="utf-8") as f:
    extensions = [
        line.strip() for line in f if line.strip() and not line.startswith("#")
    ]

if not extensions:
    sys.exit("ERRO: Nenhuma extensão válida encontrada no arquivo.")

for ext in extensions:
    print(f"\nInstalando: {ext}")
    result = subprocess.run(f"code --install-extension {ext} --force", shell=True)
    if result.returncode != 0:
        print(f"Falha ao instalar: {ext}")

print("\nTodas as extensões do arquivo foram processadas.")
