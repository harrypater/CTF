import uncompyle6
from io import StringIO


def decompile_pyc(pyc_path, output_py_path):
    """
    反编译 PYC 文件到指定 .py 文件
    :param pyc_path: PYC 文件路径
    :param output_py_path: 输出的 PY 文件路径
    """
    # 创建字符串缓冲区接收反编译结果
    buf = StringIO()
    # 反编译 PYC
    uncompyle6.decompile_file(pyc_path, buf)
    # 写入文件

    with open(output_py_path, "w", encoding="utf-8") as f:
        f.write(buf.getvalue())
    print(f"反编译完成，结果已保存到 {output_py_path}")



# 调用示例
decompile_pyc("test.pyc", "test_decompiled.py")
