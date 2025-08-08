# Scripts para instalar extensões no VScode e definir novas configurações no settings.json

## Como usar

### Instalar Extensões

- Crie um arquivo **"extensions.txt"** com as extensoes que você quer instalar.

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

- Crie um arquivo **"settings.txt"** com as configurações no formato de json válido.

- Com o **"settings.txt"** pronto, execute no terminal:

```bash
python set_settings.py
```

> Quando executado, além de trocar o conteúdo de settings.json, será criado um arquivo **"previousSettings.txt"** com o conteúdo antigo de settings.json, servindo como um backup.

## Pré-requisitos

- [Python](https://www.python.org/downloads) instalado.
