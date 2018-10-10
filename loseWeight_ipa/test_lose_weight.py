import tinify


tinify.key = "pQSYJusBRv86PZ81yYfu4GX53oUnS1cA" # AppKey
fromFilePath = "/Users/happiness/Downloads/1/2e6a95eef01f3a29b883b2e59425bc315c607c14.jpg" # 源路径
toFilePath = "/Users/happiness/Downloads/1/22222.jpg " # 输出路径


# source = tinify.from_file(fromFilePath)
# source.to_file(toFilePath)

img = open(fromFilePath,'rb')
print(img)


source_data = img.read()
print(source_data)
result_data = tinify.from_buffer(source_data).to_buffer()


# with open(fromFilePath, 'rb') as source:
#     source_data = source.read()
#     result_data = tinify.from_buffer(source_data).to_buffer()