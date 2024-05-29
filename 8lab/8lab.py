def z81():
    from PIL import Image

    image = Image.open("123.jpg")

    left = 100
    upper = 50
    right = 300
    lower = 250

    output = image.crop((left, upper, right, lower))

    output.save("image.jpg")
