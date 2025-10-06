import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

from capital import Capital
from capitalRoute import CapitalRoute

capital_coords = {
    "CIDAD DE BS AS": (-34.61, -58.38),
    "LA PLATA": (-34.92, -57.95),
    "SFDV DE CATAMARCA": (-28.47, -65.78),
    "RESISTENCIA": (-27.45, -58.99),
    "RAWSON": (-43.3, -65.1),
    "CORDOBA": (-31.42, -64.18),
    "CORRIENTES": (-27.48, -58.83),
    "PARANA": (-31.73, -60.52),
    "FORMOSA": (-26.18, -58.17),
    "SS DE JUJUY": (-24.18, -65.3),
    "SANTA ROSA": (-36.62, -64.29),
    "LA RIOJA": (-29.41, -66.85),
    "MENDOZA": (-32.89, -68.83),
    "POSADAS": (-27.37, -55.9),
    "NEUQUEN": (-38.95, -68.06),
    "VIEDMA": (-39.02, -67.57),
    "SALTA": (-24.78, -65.41),
    "SAN JUAN": (-31.53, -68.52),
    "SAN LUIS": (-33.3, -66.33),
    "RIO GALLEGOS": (-51.63, -69.23),
    "SANTA FE": (-31.63, -60.7),
    "SGO DEL ESTERO": (-27.79, -64.26),
    "USHUAIA": (-54.8, -68.3),
    "SM DE TUCUMAN": (-26.83, -65.22)
}

# --- FUNCION DE GRAFICO ---
def plot_route_cartopy(capRoute: CapitalRoute) -> None:
    route_names = capRoute.getCapitalNames()
    
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
    ax.plot(lons, lats, '--X', color='crimson', linewidth=1.8, markersize=8, transform=proj)

    # Etiquetar capitales
    for city in route_names:
        lon, lat = capital_coords[city][1], capital_coords[city][0]
        ax.text(lon + 0.3, lat + 0.3, city, fontsize=8, transform=proj)

    ax.set_title(f"Ruta de un Cromosoma - Distancia total: {capRoute.distance:.1f} km", fontsize=10)
    plt.show()