def lines(file):                                #一行行读取文件（包括空行）并在文件结束添加一个空行
    for line in file: yield line             #生成器中每yield一个值就会暂停等待下一次调用生成器对象
    yield '\n'                                   #读取最后一行就加一个空行

def blocks(file):                             #block生成器功能：依次输出一个文本块
    block = []
    for line in lines(file):                  #依次取出一行内容
        if line.strip():                         #判断是否为空行
            block.append(line)           #若不是，则会将那一文本块加入block列表
        elif block:                             #若是，则表示已经读完一整段，将其输出
            yield ' '.join(block).strip()   #一段话的不同行需要添加空格分隔开，因为之前都strip过
            block = []




