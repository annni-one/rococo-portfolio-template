from PIL import Image

# 打开图片
img = Image.open('assets/envelope.png')
img = img.convert('RGBA')

# 把黑色背景变成透明
data = img.getdata()
new_data = []
for item in data:
    # 如果像素接近黑色，就变成透明
    if item[0] < 30 and item[1] < 30 and item[2] < 30:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

img.putdata(new_data)

# 保存为透明PNG
img.save('assets/envelope_transparent.png')
print('背景去除完成，保存为 envelope_transparent.png')
