# Hüma için betik dosyalarını çalıştırma
import huma


dosya = "/home/egehan/Masaüstü/Yazılım/huma/main.hb"
komut = f'yurut("{dosya}")'

result, error = huma.run('<stdin>', komut)

if error:
    print(error.as_string())
elif result:
    if len(result.elements) == 1:
        print(repr(result.elements[0]))
    else:
        print(repr(result))

# terminal komutu

# terminal = f"/bin/python3 /home/egehan/Masaüstü/Yazılım/huma/HumaGO.py {komut}"
# print(terminal)