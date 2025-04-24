
# Resimden SVG Dosyası Oluşturma

Bu Python projesi, bir resmi alır ve içerisindeki konturları tespit ederek, bu konturları SVG formatına dönüştürür. Elde edilen SVG dosyası, her kontur için ortalama renklerle doldurulmuş şekilde kaydedilir.

## Özellikler
- Giriş olarak herhangi bir resim dosyası alır.
- Resimdeki yüksek kontrastlı alanları tespit etmek için gri tonlama ve eşikleme kullanır.
- Resmin içerisindeki konturları tespit eder ve her birini basitleştirir.
- SVG dosyası oluşturur ve her konturu uygun renklerle doldurur.

## Gereksinimler

- Python 3.x
- `opencv-python` kütüphanesi (cv2 modülü)
- `numpy`
- `svgwrite`
- `tqdm` (isteğe bağlı, ilerleme çubuğu için)

Bu bağımlılıkları yüklemek için aşağıdaki komutu kullanabilirsiniz:

```bash
pip install opencv-python numpy svgwrite tqdm
```

## Kullanım

1. Depoyu indirin veya klonlayın:

    ```bash
    git clone https://github.com/ebubekirbastama/image-to-svg-converter.git
    ```

2. Çalıştırılabilir dosyayı açın:

    ```bash
    cd image-to-svg-converter
    ```

3. Kod dosyasını çalıştırın:

    ```bash
    python resimden_svg_olustur.py
    ```

4. Program sizden bir resim dosyasının yolunu isteyecektir. Örneğin:

    ```bash
    Lütfen resim dosyasının yolunu girin (örneğin: ebs.jpg):
    ```

5. Çalıştırma tamamlandığında, `output.svg` adında bir SVG dosyası oluşturulacaktır.

## Açıklama

- **Gri Tonlama ve Eşikleme**: Resim önce gri tonlamaya çevrilir ve ardından belirli bir eşik değeriyle konturlar tespit edilir.
- **Kontur Basitleştirme**: Tespit edilen her kontur, `cv2.approxPolyDP` fonksiyonu kullanılarak daha basit bir poligon haline getirilir.
- **SVG Dosyası**: Tüm konturlar, SVG formatında renkleriyle birlikte birleştirilerek kaydedilir.

## Çıktı

Kod, işlem tamamlandığında `output.svg` adında bir SVG dosyası oluşturur. Her bir kontur, resmin ortalama rengi ile doldurulmuş olarak görselleştirilir.

## Katkı

Eğer projeye katkı sağlamak isterseniz, lütfen aşağıdaki adımları takip edin:

1. Bu repo'yu forkladıktan sonra kendi özelliklerinizi geliştirin.
2. Değişikliklerinizi commit edin.
3. Pull request gönderin.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır.
