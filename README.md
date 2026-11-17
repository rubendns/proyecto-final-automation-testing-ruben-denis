# Proyecto Final - Automation Testing

## Descripción

Proyecto de automatización de pruebas desarrollado como entrega final del curso de QA Automation de Talento Tech.

El objetivo es validar funcionalidades de una aplicación web y servicios API mediante pruebas automatizadas con Python y Pytest.

## Tecnologías utilizadas

- Python
- Pytest
- Selenium WebDriver
- Requests
- Pytest-HTML
- Git y GitHub

## Aplicaciones utilizadas

**Pruebas UI:** [SauceDemo](https://www.saucedemo.com/)

**Pruebas API:** [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

## Casos de prueba

### Pruebas UI

1. Inicio de sesión válido.
2. Inicio de sesión inválido.
3. Visualización de productos.
4. Agregar un producto al carrito.
5. Completar una compra.

### Pruebas API

1. GET: consultar una publicación.
2. POST: crear publicaciones utilizando datos CSV.
3. DELETE: eliminar una publicación de forma simulada.

## Estructura del proyecto

```text
proyecto-final-automation-testing/
├── pages/          # Page Object Model
├── tests/
│   ├── ui/         # Pruebas Selenium
│   ├── api/        # Pruebas Requests
│   └── conftest.py # Fixtures y capturas
├── data/           # Datos JSON y CSV
├── utils/          # Configuración de logging
├── reports/        # Reportes HTML
├── screenshots/    # Capturas ante fallos
├── logs/           # Registros de ejecución
├── pytest.ini
├── requirements.txt
└── README.md
```

## Instalación

Clonar el repositorio:

```powershell
git clone URL_DEL_REPOSITORIO
cd proyecto-final-automation-testing
```

Crear el entorno virtual:

```powershell
python -m venv .venv
```

Activarlo en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```powershell
python -m pip install -r requirements.txt
```

## Ejecución de pruebas

Ejecutar todas las pruebas:

```powershell
python -m pytest -v
```

Ejecutar solamente las pruebas UI:

```powershell
python -m pytest tests/ui -v
```

Ejecutar solamente las pruebas API:

```powershell
python -m pytest tests/api -v
```

## Reportes y evidencias

Al ejecutar Pytest se genera automáticamente el reporte:

`reports/reporte.html`

El reporte incluye los resultados de las pruebas y las capturas adjuntas cuando falla una prueba UI.

Las capturas también se guardan en `screenshots/`, con el nombre del test y la fecha de ejecución.

Los mensajes de logging se almacenan en:

`logs/ejecucion.log`

## Resultados

Última ejecución completa verificada:

**10 pruebas aprobadas (10 passed).**

## Autor

Ruben Denis
