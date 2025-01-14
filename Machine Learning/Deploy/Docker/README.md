# Instruções para instalar

## Ubuntu
- [Docker Engine](https://docs.docker.com/engine/install/ubuntu/#set-up-the-repository)
- [Docker Desktop](https://docs.docker.com/desktop/install/ubuntu/)

Se usando Windows, utilizar o WSL2 (Windows Subsystem for Linux). Veja as instruções de instalação [neste link](https://learn.microsoft.com/pt-br/windows/wsl/install) (tutorial Microsoft) ou [deste link](v) (tutorial Linux).


# Procedimento

## Testar se Docker está funcionando
```
docker run hello-world
```

## Criar imagem Docker
```
docker build -t fastapi-app .
docker run --name insurance_project -d -p 8000:8000 fastapi-app
```
