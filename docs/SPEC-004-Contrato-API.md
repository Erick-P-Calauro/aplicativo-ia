# SPEC-004 - Contrato de API

Essa especificação busca fixar os contratos de API esperados para a implementação do sistema.

## Endpoints

### 1. Listar usuários

- Rota: `GET /user`
- Auth Required
- Response Code : 200
```json
[
  {
    "id": "uuid",
    "name": "string",
    "photo_path": "string",
    "created_at": "2026-01-01T00:00:00Z"
  }
]
```

### 2. Cadastrar usuário

- Rota: `POST /user/cadastrar`
- Content-Type: `multipart/form-data`
- Body:
  - name (string, obrigatório)
  - photo (file, imagem, obrigatório)
- Response Code : 201
```json
{
  "id": "uuid",
  "name": "string",
  "photo_path": "string",
  "created_at": "2026-01-01T00:00:00Z"
}
```

### 3. Excluir usuário

- Rota : `DELETE /user/{user_id}`
- Auth Required
- Path Param: `user_id` (uuid)
- Response Code : 204.

### 4. Reconhecer faces

- Rota: `POST /face/reconhecer`
- Content-Type: `multipart/form-data`
- Body: 
  - image (file, imagem, obrigatório)
- Response Code (Com faces) : 200
```json
{
  "faces": [
    {
      "box": { "x": 0, "y": 0, "w": 0, "h": 0 },
      "name": "string | Não cadastrado",
      "user_id": "uuid | null",
      "score": 0.0
    }
  ]
}
```
- Response Code (Sem face) : 200
```json
{
  "message": "Nenhuma pessoa encontrada na imagem"
}
```
