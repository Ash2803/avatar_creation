from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()

left_cropped_red = red.crop((100, 0, red.width, red.height))
middle_cropped_red = red.crop((50, 0, red.width-50, red.height))

image1 = Image.blend(left_cropped_red, middle_cropped_red, 0.5)

image2 = green.crop((50, 0, green.width-50, green.height))

right_cropped_blue = blue.crop((0, 0, blue.width-100, blue.height))
middle_cropped_blue = blue.crop((50, 0, blue.width-50, blue.height))

image3 = Image.blend(right_cropped_blue, middle_cropped_blue, 0.5)

new_image = Image.merge("RGB", (image1, image2, image3))
new_image.save("final_img.jpg", format="JPEG")

monro_image = Image.open("final_img.jpg")
monro_image.thumbnail((80, 75))
monro_image.save("monro_avatar.jpg", format="JPEG")