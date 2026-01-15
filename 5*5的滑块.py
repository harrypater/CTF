

erwei=[[x for x in range(10)] for _ in range(10)]

step=1
huakuai_wdith=5
huakuai_height=5

# 原矩阵尺寸
mat_h = len(erwei)    # 矩阵行数
mat_w = len(erwei[0]) # 矩阵列数

# 核心：双重循环实现滑块滑动
print("\n===== 5x5滑块在10x10矩阵上完整滑动 =====")
# 控制滑块的【起始行】，范围：0 ~ mat_h-huakuai_height
for start_row in range(mat_h - huakuai_height + 1):
    # 控制滑块的【起始列】，范围：0 ~ mat_w-slide_w
    for start_col in range(mat_w - huakuai_wdith + 1):
        # 提取当前滑块的5x5数据：切片取值
        slide_window = [
            hang[start_col : start_col+huakuai_wdith] 
            for hang in erwei[start_row : start_row+huakuai_height]
        ]
        
        # 打印当前滑块信息 + 滑块内的数据
        print(f"\n滑块起始位置：行={start_row}, 列={start_col} → 5x5滑块数据：")
        for line in slide_window:
            print(line)

