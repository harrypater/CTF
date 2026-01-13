#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import uncompyle6
import sys
from io import StringIO

def pyc_decompile(pyc_file_path, save_py_path=None):
    """
    纯Python实现 pyc文件反编译为Python源码
    :param pyc_file_path: 待反编译的.pyc文件路径 (必填)
    :param save_py_path: 反编译后.py文件的保存路径 (可选，不传则只返回源码文本)
    :return: 反编译后的Python源码字符串
    """
    try:
        # 创建内存缓冲区，接收反编译的源码
        source_code_io = StringIO()
        # 核心反编译执行：解析pyc，生成源码
        uncompyle6.decompile_file(pyc_file_path, source_code_io)
        # 获取源码文本
        source_code = source_code_io.getvalue()
        
        # 如果传入保存路径，就把源码写入文件
        if save_py_path:
            with open(save_py_path, 'w', encoding='utf-8') as f:
                f.write(source_code)
            print(f"✅ 反编译成功！源码已保存至: {save_py_path}")
        
        return source_code
    
    except FileNotFoundError:
        print(f"❌ 错误：找不到文件 {pyc_file_path}")
        return ""
    except Exception as e:
        print(f"❌ 反编译失败：{str(e)}")
        return ""

# ===================== 调用示例 (重点修改这里) =====================
if __name__ == "__main__":
    # 1. 配置你的pyc文件路径 (PyInstaller解包后的pyc路径)
    PYC_FILE = r"MG.pyc"  # 例：r"main.pyc" / r"D:\exe_extracted\lz77.pyc"
    # 2. 配置反编译后的py文件保存路径
    SAVE_PY_FILE = r"反编译后的源码.py"
    
    # 执行反编译
    decompile_code = pyc_decompile(PYC_FILE, SAVE_PY_FILE)
    
    # 可选：直接打印反编译后的源码
    if decompile_code:
        print("\n======= 反编译后的Python源码 =======")
        print(decompile_code)
        
     
