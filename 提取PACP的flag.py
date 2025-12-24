from scapy.all import rdpcap, Raw

# 1. 读取pcap文件（替换为你的ping.pcap实际路径）
pcap_path = "ping.pcap"  # 若文件不在代码同目录，写绝对路径如"D:\ctf\ping.pcap"
packets = rdpcap(pcap_path)

flag = ""

# 2. 遍历每个数据包，安全提取Raw层第一个字节
for packet in packets:
    # 关键：先判断数据包是否包含Raw层，避免索引报错
    if Raw in packet and len(packet[Raw].load) >= 1:
        # 提取负载第一个字节，转成ASCII字符
        flag += chr(packet[Raw].load[0])
    else:
        # 可选：跳过无Raw层/负载为空的数据包，打印提示
        print(f"跳过无Raw层的数据包：{packet.summary()}")

# 3. 输出最终拼接的flag
print("提取到的flag：", flag)
