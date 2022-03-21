#Autor: Anna Maria Geiger
#Firma: ODE - office for digital engineering
#Datum: 21.03.1997

import fitz # PyMuPDF
import io
from PIL import Image

# Dateinname; Wichtig! muss im selben Ordner liegen
file = "Prüfbericht ASFINAG  S31_08044_Sept 2011.pdf"
# Datei oeffnen
pdf_file = fitz.open(file)

# iterate ueeber die Seiten
for page_index in range(len(pdf_file)):
    # Seite laden
    page = pdf_file[page_index]
    image_list = page.getImageList()
    # Anzahl der Bilder printen
    if image_list:
        print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
    else:
        print("[!] No images found on page", page_index)
    for image_index, img in enumerate(page.getImageList(), start=1):
        # XREF der Bilder
        xref = img[0]
        # extrahiere die image bytes
        base_image = pdf_file.extractImage(xref)
        image_bytes = base_image["image"]
        # Bilderformat
        image_ext = base_image["ext"]
        # load it to PIL
        image = Image.open(io.BytesIO(image_bytes))
        # abspeichern
        image.save(open(f"image{page_index+1}_{image_index}.{image_ext}", "wb"))