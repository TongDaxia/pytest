def writeFile(html, filename):
    """
        作用：保存服务器响应文件到本地磁盘文件里
        html: 服务器响应文件
        filename: 本地磁盘文件名
    """
    print ("正在存储" + filename)
    with open(filename, 'wb') as f:
        f.write(html)
    print("-" * 20)