from scapy.all import rdpcap, Raw


def extract_flag_from_pcap(pcap_file):
    """
    从ping.pcap中提取每个数据包Raw层负载第一个字节，拼接成flag

    Args:
        pcap_file (str): pcap文件路径

    Returns:
        str: 拼接后的flag字符串
    """
    # 读取pcap文件
    packets = rdpcap(pcap_file)
    flag = ''

    # 遍历每个数据包
    for idx, packet in enumerate(packets):
        try:
            # 检查是否包含Raw层
            if Raw in packet:
                load_data = packet[Raw].load
                # 确保load有至少1个字节
                if len(load_data) >= 1:
                    # 提取第一个字节并转换为字符
                    flag += chr(load_data[0])
                else:
                    print(f"警告: 数据包{idx}的Raw层负载为空")
            else:
                print(f"警告: 数据包{idx}无Raw层")
        except Exception as e:
            print(f"错误: 处理数据包{idx}时出错 - {str(e)}")

    return flag


# 主程序执行
if __name__ == "__main__":
    # 替换为你的pcap文件路径
    pcap_path = "ping.pcap"
    flag = extract_flag_from_pcap(pcap_path)
    print("提取到的flag:", flag)
