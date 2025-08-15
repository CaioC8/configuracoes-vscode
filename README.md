# Scripts para instalar extensões no VScode e definir novas configurações no settings.json

## Como usar

- Execute:

```bash
git clone https://github.com/CaioC8/configuracoes-vscode.git
```

### Instalar Extensões

- Crie um novo ou altere o arquivo **"extensions.txt"** e coloque as extensoes que você quer instalar.

> Para conseguir o **extensions.txt** mais facilmente, execute no terminal do VScode:
>
> ```bash
> code --list-extensions > extensions.txt
> ```

- Com o **"extensions.txt"** pronto, execute no terminal:

```bash
python install_extensions.py
```

### Definir settings.json

- Crie um novo ou altere o arquivo **"settings.txt"** e coloque as configurações no formato de json válido.

- Com o **"settings.txt"** pronto, execute no terminal:

```bash
python set_settings.py
```

> O set_settings.py vai criar uma pasta **".vscode"** com o arquivo de settings. Para saber como funciona a criação, consulte o código e faça alterações se necessário.

## Pré-requisitos

- [Python](https://www.python.org/downloads) instalado.
