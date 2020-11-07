import nsfw


img = 'porn.jpeg'
out = nsfw.classify(img)
print(out)

img = ['porn.jpeg', 'd2.png']
out = nsfw.classify_many(img)
print(out)
