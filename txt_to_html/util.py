def lines(file):                #收集文本文件除空行外的所有行，并在文件结束添加空行
    for line in file: yield line            #生成器中每yield一个值就会暂停等待下一次调用生成器对象
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ' '.join(block).strip()
            block = []



#应加强对生成器的理解
