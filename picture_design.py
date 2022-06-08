from PIL import Image

first_img = Image.open("first.jpg")
second_img = Image.open("second.jpg")
third_img = Image.open("third.jpg")

# Обьединяем каналы в одну картинку
new_image = Image.merge("RGB", (first_img, second_img, third_img))
new_image.save("monro.jpg", format="JPEG")

# Обрезаем первое фото слева на 100
left_cropped_first_img = first_img.crop((100, 0, first_img.width, first_img.height))
left_cropped_first_img.save("first_left.jpg", format="JPEG")

# Обрезаем первое фото по бокам на 50
first_middle_img = first_img.crop((50, 0, first_img.width-50, first_img.height))
first_middle_img.save("first_middle.jpg", format="JPEG")

# Соединяем обрезанные фото
image1 = Image.open("first_left.jpg")
image2 = Image.open("first_middle.jpg")
image3 = Image.blend(image1, image2, 0.5)
image3.save("first_red.jpg", format="JPEG")

# Обрезаем второе фото справа на 100
right_cropped_second_img = second_img.crop((0, 0, first_img.width-100, first_img.height))
right_cropped_second_img.save("second_right.jpg", format="JPEG")

# Обрезаем второе фото по бокам на 50
second_middle_img = second_img.crop((50, 0, second_img.width-50, second_img.height))
second_middle_img.save("second_middle.jpg", format="JPEG")

# Соединяем обрезанные фото
image1 = Image.open("second_right.jpg")
image2 = Image.open("second_middle.jpg")
image3 = Image.blend(image1, image2, 0.5)
image3.save("second_blue.jpg", format="JPEG")

# Обрезаем третье фото по бокам на 50
third_middle_img = third_img.crop((50, 0, third_img.width-50, third_img.height))
third_middle_img.save("third_middle.jpg", format="JPEG")

# Обьединяем все три фото получившиеся в прошлых шагах в одну
image1 = Image.open("first_red.jpg")
image2 = Image.open("second_blue.jpg")
image3 = Image.open("third_middle.jpg")
new_image = Image.merge("RGB", (image1, image2, image3))
new_image.save("final_img.jpg", format="JPEG")

# Обрезаем под аватарку 80х70
monro_image = Image.open("final_img.jpg")
monro_image.thumbnail((80, 75))
monro_image.save("monro_avatar.jpg", format="JPEG")
