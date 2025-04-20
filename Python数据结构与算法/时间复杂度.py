import os

# 打印当前工作目录
print("Current working directory:", os.getcwd())

# 检查文件是否存在
file_path = './File dc them vao.html'
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
        print(html)
else:
    print(f"File not found: {file_path}")