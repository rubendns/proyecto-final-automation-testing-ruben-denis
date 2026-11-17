# Proyecto Final - Automation Testing

## Descripción

Proyecto de automatización de pruebas desarrollado como entrega final del curso de **QA Automation de Talento Tech**.

El objetivo es validar funcionalidades de una aplicación web y servicios API mediante pruebas automatizadas con Python y Pytest.

El proyecto implementa pruebas funcionales de interfaz (UI) y API, utilizando Page Object Model (POM), parametrización de datos, reportes HTML, logging e integración continua con GitHub Actions.

## Tecnologías utilizadas

- Python 3.11
- Pytest
- Selenium WebDriver
- Requests
- Pytest-HTML
- Git y GitHub
- GitHub Actions

## Aplicaciones utilizadas

**Pruebas UI:** [SauceDemo](https://www.saucedemo.com/)

**Pruebas API:** [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

## Casos de prueba

### Pruebas UI (5 tests)

1. Inicio de sesión válido.
2. Inicio de sesión inválido.
3. Visualización de productos.
4. Agregar un producto al carrito.
5. Completar una compra exitosamente.

Las pruebas de inicio de sesión utilizan datos externos en formato JSON.

### Pruebas API (5 tests)

1. **GET:** consultar una publicación y validar el código HTTP y los datos JSON.
2. **POST:** crear publicaciones utilizando tres conjuntos de datos de un archivo CSV.
3. **DELETE:** eliminar una publicación de forma simulada y validar la respuesta HTTP.

Las pruebas API utilizan la biblioteca Requests y verifican los códigos de respuesta y el contenido JSON cuando corresponde.

**Total: 10 tests automatizados.**

## Estructura del proyecto

```text
proyecto-final-automation-testing/
├── .github/
│   └── workflows/
│       └── ci.yml          # Integración continua
├── pages/                  # Page Object Model
├── tests/
│   ├── ui/                 # Pruebas Selenium
│   ├── api/                # Pruebas Requests
│   └── conftest.py         # Fixtures y capturas
├── data/                   # Datos JSON y CSV
├── utils/                  # Configuración de logging
├── reports/                # Reportes HTML
├── screenshots/            # Capturas ante fallos
├── logs/                   # Registros de ejecución
├── pytest.ini              # Configuración de Pytest
├── requirements.txt        # Dependencias
└── README.md               # Documentación
```

## Instalación

### 1. Clonar el repositorio

```powershell
git clone https://github.com/rubendns/proyecto-final-automation-testing-ruben-denis.git
cd proyecto-final-automation-testing-ruben-denis
```

### 2. Crear el entorno virtual

```powershell
python -m venv .venv
```

### 3. Activar el entorno virtual en PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

Para ejecutar las pruebas UI es necesario tener Google Chrome instalado.

## Ejecución de pruebas

### Ejecutar todas las pruebas

```powershell
python -m pytest -v
```

### Ejecutar solamente las pruebas UI

```powershell
python -m pytest tests/ui -v
```

### Ejecutar solamente las pruebas API

```powershell
python -m pytest tests/api -v
```

### Ejecutar las pruebas en modo CI (headless)

En PowerShell:

```powershell
$env:CI = "true"
python -m pytest -v
```

En este modo, Chrome se ejecuta sin abrir una ventana gráfica.

Para volver al modo normal en la misma terminal:

```powershell
Remove-Item Env:CI
```

## Reportes y evidencias

Al ejecutar Pytest se genera automáticamente un reporte HTML en:

`reports/reporte.html`

El reporte incluye los resultados de las pruebas, sus tiempos de ejecución y capturas adjuntas cuando falla una prueba UI.

### Capturas automáticas

Cuando falla un test de interfaz, el proyecto guarda una captura en:

`screenshots/`

El nombre del archivo incluye el nombre del test y la fecha y hora de ejecución.

### Logging

Los registros de ejecución se almacenan en:

`logs/ejecucion.log`

Estos registros permiten consultar las acciones realizadas durante las pruebas y facilitar el análisis de errores.

## Integración continua (CI/CD)

El proyecto utiliza **GitHub Actions** para ejecutar automáticamente las pruebas de UI y API.

El workflow se encuentra en:

`.github/workflows/ci.yml`

### ¿Cuándo se ejecuta?

El workflow se activa automáticamente cuando:

- Se realiza un `push` a la rama `main`.
- Se crea o actualiza un Pull Request dirigido a `main`.

### Proceso de ejecución

GitHub Actions realiza los siguientes pasos:

1. Descarga el código del repositorio.
2. Configura Python 3.11 en un entorno Ubuntu.
3. Instala las dependencias desde `requirements.txt`.
4. Ejecuta las pruebas automatizadas con Pytest.
5. Guarda los reportes y las evidencias de ejecución.

Las pruebas UI utilizan Selenium con Google Chrome en modo **headless**, permitiendo su ejecución sin interfaz gráfica.

### Reportes y evidencias en GitHub Actions

Al finalizar cada ejecución, el workflow publica un artifact llamado:

`reporte-automation-testing`

Este artifact contiene los archivos generados durante las pruebas:

- `reports/`: reportes HTML.
- `screenshots/`: capturas de pantalla de pruebas UI fallidas.
- `logs/`: registros de ejecución.

Los archivos pueden descargarse desde la sección **Artifacts** de cada ejecución.

### Consultar los resultados

Los resultados de integración continua pueden consultarse en la pestaña **Actions** del repositorio:

[Ver ejecuciones de GitHub Actions](https://github.com/rubendns/proyecto-final-automation-testing-ruben-denis/actions)

## Resultados

Última ejecución completa verificada:

**10 pruebas aprobadas (10 passed).**

Las pruebas fueron ejecutadas correctamente tanto en el entorno local como en GitHub Actions, incluyendo la ejecución posterior al merge en la rama `main`.

## Control de versiones

El proyecto utiliza Git y GitHub para gestionar el código fuente.

Durante el desarrollo se utilizaron ramas de trabajo y Pull Requests para incorporar nuevas funcionalidades, configurar la integración continua y corregir problemas de sincronización en las pruebas automatizadas.

Repositorio público:

[proyecto-final-automation-testing-ruben-denis](https://github.com/rubendns/proyecto-final-automation-testing-ruben-denis)

## Autor

**Rubén Denis**

Proyecto final del curso de QA Automation - Talento Tech.