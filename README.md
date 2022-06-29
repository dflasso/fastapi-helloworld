# Get Started
```
python3.9  -m venv .env 
pip install fastapi uvicorn
```

## Up server
```
uvicorn main:app --reload
```

# Documentación
FastAPI también está parado sobre los hombros de OpenAPI, el cual es un conjunto de reglas que permite definir cómo describir, crear y visualizar APIs. Es un conjunto de reglas que permiten decir que una API está bien definida.

OpenAPI necesita de un software, el cual es Swagger, que es un conjunto de softwares que permiten trabajar con APIs. FastAPI funciona sobre un programa de Swagger el cual es Swagger UI, que permite mostrar la API documentada.

Acceder a la documentación interactiva con Swagger UI:
{localhost}/docs

Acceder a la documentación interactiva con Redoc:
{localhost}/redoc

)
