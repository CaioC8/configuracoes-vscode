from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def create_vscode_settings():
    project_root = get_project_root()
    vscode_dir = project_root / ".vscode"
    vscode_dir.mkdir(exist_ok=True)

    settings_txt_path = Path(__file__).parent / "settings.txt"
    settings_json_path = vscode_dir / "settings.json"

    if not settings_txt_path.exists():
        raise FileNotFoundError(f"Arquivo {settings_txt_path} não encontrado.")

    with open(settings_txt_path, "r", encoding="utf-8") as f:
        new_settings_content = f.read()

    with open(settings_json_path, "w", encoding="utf-8") as f:
        f.write(new_settings_content)

    print(f"\nArquivo criado em: {settings_json_path}")


if __name__ == "__main__":
    create_vscode_settings()
