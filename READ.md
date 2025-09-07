# 📺 Dorama Tracker API

Uma API RESTful feita com **FastAPI** e **SQLAlchemy** para registrar doramas assistidos, seus gêneros, número de episódios e status (como "Assistindo", "Concluído", etc).

---

## 🚀 Tecnologias utilizadas

- **Python 3.11+**
- **FastAPI**
- **SQLAlchemy**
- **SQLite** (pode ser facilmente trocado por PostgreSQL)
- **Uvicorn** (server ASGI para rodar o projeto)

---

## ⚙️ Como rodar o projeto localmente

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/dorama-tracker-api.git
cd dorama-tracker-api
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o servidor
```bash
uvicorn app.main:app --reload
```

Acesse: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para visualizar e testar a API na interface Swagger.

---

## 🔄 Funcionalidades

- [x] Criar doramas
- [x] Listar todos os doramas
- [x] Buscar dorama por ID
- [x] Atualizar dados do dorama
- [x] Deletar dorama

---

## 🗃️ Estrutura de diretórios

```bash
├── app
│   ├── main.py          # Inicialização da aplicação FastAPI
│   ├── routes.py        # Rotas da API (endpoints)
│   ├── models.py        # Modelos SQLAlchemy
│   └── database.py      # Configuração da conexão com SQLite
├── requirements.txt
└── README.md
```

---

## 🧠 Próximos passos (Projeto 3)
- Integração com **frontend em React ou Vue.js** para interface visual do sistema.
- Autenticação de usuário (opcional).
- Exportação de relatórios.

---

## 🙋‍♀️ Desenvolvido por
**Marina Takeda**  
🔗 [LinkedIn](https://www.linkedin.com/in/marinatakeda/)  
🐙 [GitHub](https://github.com/ladymarina08)

---


