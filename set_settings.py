from pathlib import Path


def get_project_root(n: int) -> Path:
    """
    Retorna o caminho do diretório 'n' níveis acima do diretório onde está este script.

    Parâmetros:
        n (int): Quantos níveis subir em relação à pasta do script.
                 - 0 → pasta onde está o script
                 - 1 → diretório pai da pasta onde está o script
                 - 2 → pai do pai, e assim por diante.

    Exemplo:
        Se o script estiver em /home/user/projeto/configuracoes-vscode/set_settings.py:
        n=0 → /home/user/projeto/configuracoes-vscode
        n=1 → /home/user/projeto
        n=2 → /home/user
    """
    return Path(__file__).resolve().parents[n]


def create_vscode_settings():
    project_root = get_project_root(1)  # Mude o valor conforme necessário
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
