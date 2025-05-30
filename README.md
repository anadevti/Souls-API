# Souls API

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?logo=fastapi&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Uma **REST API** construída com [FastAPI](https://fastapi.tiangolo.com/) que disponibiliza, de forma rápida e totalmente documentada, informações sobre os jogos da _FromSoftware_ — _Demon’s Souls_, trilogia _Dark Souls_, _Bloodborne_, _Sekiro_ e _Elden Ring_.

> **Objetivo** — Servir de boiler‑plate para APIs em Python, além de funcionar como _playground_ para estudos de arquitetura, conteinerização e boas práticas.
> Vale ressaltar que este projeto ainda está em andamento e irá ser finalizado!

---

## 🛠️ Stack & dependências

* **Python 3.11**
* **FastAPI** + **Uvicorn** (ASGI)
* **Pydantic** para validação de dados
* **Docker** & **Docker Compose** para orquestração
* **PostgreSQL** como datastore

As dependências estão listadas em [`requirements.txt`](requirements.txt).

---

## 🚀 Rodando localmente

### Pré‑requisitos

* Python 3.11+ e `pip`
* Docker + Docker Compose

### Clonando o repositório

```bash
$ git clone https://github.com/anadevti/Souls-API.git
$ cd Souls-API
```

### Ambiente virtual

```bash
$ python -m venv .venv
$ source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\Activate.ps1  # Windows PowerShell
$ pip install -r requirements.txt
$ uvicorn main:app --reload
```

## 📜 Licença

Distribuído sob a licença **MIT**.

---

## 🙏 Agradecimentos Especiais

* Comunidade Souls ❤
* [FastAPI](https://fastapi.tiangolo.com/) & [Pydantic](https://docs.pydantic.dev/)

---

> "Prepare to API, Tarnished." 🗡️
