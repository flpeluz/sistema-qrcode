import segno
import PIL.Image

# --- CONFIGURAÇÕES ---
# O link do seu site no Render (ou seu-link-final.com)
meu_link_oficial = "https://seu-projeto.onrender.com" 

# Nome do arquivo de logo (certifique-se de que ele está na mesma pasta)
nome_do_logo = "cb.jpg" 

# Nome do arquivo de saída
nome_arquivo_saida = "qrcode_cb.png" 

# --- GERAÇÃO DO QR CODE ---
print(f"Gerando QR Code para: {meu_link_oficial}...")

# 1. Criar o QR Code com nível de erro 'H' (High)
#    Isso é crucial! O nível 'H' permite que até 30% do código seja coberto 
#    pelo logo sem afetar a leitura.
qr = segno.make(meu_link_oficial, error='h')

# 2. Salvar o QR Code temporariamente em memória para podermos manipular
qr.save("temp_qrcode.png", scale=10, dark="#000000", light="#FFFFFF")

# 3. Carregar o QR Code temporário e o Logo usando Pillow
img_qrcode = PIL.Image.open("temp_qrcode.png").convert("RGBA")
img_logo = PIL.Image.open(nome_do_logo).convert("RGBA")

# 4. Calcular o tamanho e posição do logo
#    O ideal é que o logo ocupe cerca de 20% do tamanho total do QR Code.
qrcode_width, qrcode_height = img_qrcode.size
logo_width_max = qrcode_width // 5  # 20% da largura do QR Code

# Redimensionar o logo proporcionalmente
w_percent = (logo_width_max / float(img_logo.size[0]))
h_size = int((float(img_logo.size[1]) * float(w_percent)))
img_logo_resized = img_logo.resize((logo_width_max, h_size), PIL.Image.LANCZOS)

# 5. Calcular a posição central para o logo
x_pos = (qrcode_width - img_logo_resized.size[0]) // 2
y_pos = (qrcode_height - img_logo_resized.size[1]) // 2

# 6. Colar o logo no centro do QR Code
#    Usamos o próprio logo como máscara (o terceiro argumento) para manter a transparência
img_qrcode.paste(img_logo_resized, (x_pos, y_pos), img_logo_resized)

# 7. Salvar o resultado final
img_qrcode.save(nome_arquivo_saida)

# 8. Limpar arquivo temporário
import os
os.remove("temp_qrcode.png")

print(f"Sucesso! QR Code com logo gerado em '{nome_arquivo_saida}'.")
print("Teste a leitura dele agora no seu celular!")