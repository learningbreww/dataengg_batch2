all_files = ['cat.jpg', 'dog.png', 'report.docx', 'sales.csv']
img_extension=['jpg', 'png']

#convert list ot tuple
tup=tuple(img_extension)

jpg_png=[]
for extension in all_files:
    if extension.endswith(tup):
        jpg_png.append(extension)

print(jpg_png)