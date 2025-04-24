import cv2
import numpy as np
import svgwrite
import os
from tqdm import tqdm  # For progress bar

# Kullanıcıdan dosya yolu al
input_file = input("Lütfen resim dosyasının yolunu girin (örneğin: ebs.jpg): ")

# Dosyanın varlığını kontrol et
if not os.path.exists(input_file):
    print(f"❌ {input_file} dosyası bulunamadı. Lütfen geçerli bir dosya yolu girin.")
    exit()

# Resmi oku
image = cv2.imread(input_file)
height, width = image.shape[:2]

# Gri tonlama ve eşik uygulaması
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

# Konturları bul
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# SVG dosyası oluştur
dwg = svgwrite.Drawing("output.svg", size=(width, height))

# Konturlar üzerinde işlem yap
for contour in tqdm(contours, desc="Processing Contours"):
    # Konturu basitleştir
    epsilon = 0.01 * cv2.arcLength(contour, True)  # Bu değeri ayarlayarak kenarları düzleştirebilirsiniz
    simplified_contour = cv2.approxPolyDP(contour, epsilon, True)

    # Kontur için maske oluştur
    mask = np.zeros((height, width), dtype=np.uint8)
    cv2.drawContours(mask, [simplified_contour], -1, 255, -1)

    # Ortalama rengi al
    mean_color = cv2.mean(image, mask=mask)
    r, g, b = int(mean_color[2]), int(mean_color[1]), int(mean_color[0])  # BGR'den RGB'ye

    # SVG path verisini oluştur
    path_data = "M " + " L ".join(f"{pt[0][0]},{pt[0][1]}" for pt in simplified_contour) + " Z"

    # SVG'ye ekle
    dwg.add(dwg.path(d=path_data, fill=svgwrite.rgb(r, g, b), stroke='none'))

# SVG dosyasını kaydet
dwg.save()

print("✅ SVG dosyası başarıyla oluşturuldu: output.svg")
