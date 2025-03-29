# 📌 Scraper de Ofertas de Mercado Libre

Este proyecto es una aplicación web que permite obtener y visualizar **ofertas de Mercado Libre** en Perú. Se incluyen dos modos de scraping:

1. **Scrapeo de la página principal** (Extrae las primeras ofertas visibles).
2. **Scrapeo de ofertas con rango de páginas** (Permite definir cuántas páginas analizar).

Los datos obtenidos se muestran en una tabla interactiva con **filtros dinámicos** para ordenar por **precio antes, precio actual, diferencia, descuento y cupones disponibles**.

---

## 🚀 Tecnologías utilizadas

- **Python** (Para el scraping con `requests` y `BeautifulSoup`).
- **Flask** (Para la aplicación web).
- **HTML, CSS y JavaScript** (Interfaz interactiva con filtros y estilos modernos).

---

### 📌 Página Principal
Aquí el usuario elige entre dos modos de scraping:
- ✅ Scrapeo de la página principal.
- ✅ Scrapeo de ofertas con un rango de páginas.

![Página Principal](https://raw.githubusercontent.com/FernandoCruz1999/Examen-Final---Fernando-Cruz/refs/heads/main/screenshots/Pagina%20Principal.png)

---

### 📊 Página de Resultados
Muestra la lista de ofertas con su **nombre, precio antes, precio actual y diferencia de precio**.

![Página de Resultados | Página principal](https://raw.githubusercontent.com/FernandoCruz1999/Examen-Final---Fernando-Cruz/refs/heads/main/screenshots/Pagina%20Resultado.png)

![Página de Resultados | Página múltiple](https://raw.githubusercontent.com/FernandoCruz1999/Examen-Final---Fernando-Cruz/refs/heads/main/screenshots/Pagina%20Resultado%20Multiple.png)

---

## ⚙️ Instalación y Uso

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/FernandoCruz1999/Examen-Final---Fernando-Cruz
cd Examen-Final---Fernando-Cruz
```
### 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar la aplicación

```bash
python app.py
```

Abrir el navegador en la dirección http://127.0.0.1:5000
