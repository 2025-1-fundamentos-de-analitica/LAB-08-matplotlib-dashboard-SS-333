# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """

    # Crear el directorio de salida si no existe
    output_dir = "docs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Cargar los datos
    df = pd.read_csv("files/input/shipping-data.csv", sep=",")

    # --- Gráfico 1: Warehouse_block ---
    plt.figure(figsize=(6, 4))
    df['Warehouse_block'].value_counts().sort_index().plot(kind='bar', color='skyblue')
    plt.title('Distribución por Bloque de Almacén')
    plt.xlabel('Bloque de Almacén')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'shipping_per_warehouse.png'))
    plt.close()

    # --- Gráfico 2: Mode_of_Shipment ---
    plt.figure(figsize=(6, 4))
    df['Mode_of_Shipment'].value_counts().plot(kind='bar', color='lightgreen')
    plt.title('Distribución por Modo de Envío')
    plt.xlabel('Modo de Envío')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'mode_of_shipment.png'))
    plt.close()

    # --- Gráfico 3: Customer_rating ---
    plt.figure(figsize=(6, 4))
    df['Customer_rating'].value_counts().sort_index().plot(kind='bar', color='salmon')
    plt.title('Distribución de Calificación del Cliente')
    plt.xlabel('Calificación')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'average_customer_rating.png'))
    plt.close()

    # --- Gráfico 4: Weight_in_gms ---
    plt.figure(figsize=(6, 4))
    plt.hist(df['Weight_in_gms'], bins=20, color='gold', edgecolor='black')
    plt.title('Distribución del Peso en Gramos')
    plt.xlabel('Peso (gms)')
    plt.ylabel('Frecuencia')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'weight_distribution.png'))
    plt.close()

    # --- Generar el archivo HTML ---
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dashboard de Envíos</title>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            h1 {{ text-align: center; }}
            .grid-container {{
                display: grid;
                grid-template-columns: auto auto;
                padding: 10px;
                gap: 20px;
            }}
            .grid-item {{
                border: 1px solid #ccc;
                padding: 20px;
                text-align: center;
            }}
            img {{
                max-width: 100%;
                height: auto;
            }}
        </style>
    </head>
    <body>
        <h1>Dashboard de Análisis de Envíos</h1>
        <div class="grid-container">
            <div class="grid-item"><img src="shipping_per_warehouse.png" alt="Gráfico 1"></div>
            <div class="grid-item"><img src="mode_of_shipment.png" alt="Gráfico 2"></div>
            <div class="grid-item"><img src="average_customer_rating.png" alt="Gráfico 3"></div>
            <div class="grid-item"><img src="weight_distribution.png" alt="Gráfico 4"></div>
        </div>
    </body>
    </html>
    """
    
    with open(os.path.join(output_dir, 'index.html'), 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    pregunta_01()