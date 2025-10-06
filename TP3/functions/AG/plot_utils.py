import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

from capital import Capital
from capitalRoute import CapitalRoute

capital_coords = {
    "Buenos Aires": (-34.61, -58.38),
    "Catamarca": (-28.47, -65.78),
    "Chaco": (-27.45, -58.99),
    "Chubut": (-43.3, -65.1),
    "Córdoba": (-31.42, -64.18),
    "Corrientes": (-27.48, -58.83),
    "Entre Ríos": (-31.73, -60.52),
    "Formosa": (-26.18, -58.17),
    "Jujuy": (-24.18, -65.3),
    "La Pampa": (-36.62, -64.29),
    "La Rioja": (-29.41, -66.85),
    "Mendoza": (-32.89, -68.83),
    "Misiones": (-27.37, -55.9),
    "Neuquén": (-38.95, -68.06),
    "Río Negro": (-39.02, -67.57),
    "Salta": (-24.78, -65.41),
    "San Juan": (-31.53, -68.52),
    "San Luis": (-33.3, -66.33),
    "Santa Cruz": (-51.63, -69.23),
    "Santa Fe": (-31.63, -60.7),
    "Santiago del Estero": (-27.79, -64.26),
    "Tierra del Fuego": (-54.8, -68.3),
    "Tucumán": (-26.83, -65.22)
}

route = [
    "Buenos Aires",
    "Santa Fe",
    "Córdoba",
    "San Luis",
    "Mendoza",
    "San Juan",
    "La Rioja",
    "Catamarca",
    "Tucumán",
    "Salta",
    "Jujuy",
    "Formosa",
    "Chaco",
    "Corrientes",
    "Misiones",
    "Entre Ríos",
    "La Pampa",
    "Neuquén",
    "Río Negro",
    "Chubut",
    "Santa Cruz",
    "Tierra del Fuego",
    "Buenos Aires"  # cierra el ciclo
]

# --- FUNCION DE GRAFICO ---
def plot_route_cartopy() -> None:
    route_names = route # capRoute.getCapitalNames()
    lats = [capital_coords[c][0] for c in route_names]
    lons = [capital_coords[c][1] for c in route_names]

    # Proyección geográfica (plana)
    proj = ccrs.PlateCarree()

    fig, ax = plt.subplots(figsize=(8, 10), subplot_kw={"projection": proj})
    ax.set_extent([-73, -53, -56, -21])  # Extensión aproximada del mapa de Argentina

    # Agregar elementos de fondo (mapa base)
    ax.add_feature(cfeature.LAND, facecolor="lightgray")
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=":")
    ax.add_feature(cfeature.LAKES, alpha=0.5)
    ax.add_feature(cfeature.RIVERS, alpha=0.5)

    # Dibujar la ruta
    ax.plot(lons, lats, '-o', color='crimson', linewidth=1.8, markersize=5, transform=proj)

    # Etiquetar capitales
    for city in route_names:
        lon, lat = capital_coords[city][1], capital_coords[city][0]
        ax.text(lon + 0.3, lat + 0.3, city, fontsize=8, transform=proj)

    # ax.set_title(f"Ruta de un Cromosoma - Distancia total: {capRoute.distance:.1f} km", fontsize=10)
    plt.show()