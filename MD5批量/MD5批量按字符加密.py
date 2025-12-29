import hashlib
from multiprocessing import Pool

def compute_md5(char):
    md5_flag = hashlib.md5(char.encode())
    return md5_flag.hexdigest()

if __name__ == '__main__':
    with open('flag', 'r') as flag_file:
        content = flag_file.read()
        chars = list(content)
        
        with Pool() as pool:
            md5_results = pool.map(compute_md5, chars)
        
        with open('output', 'w') as output_file:
            for result in md5_results:
                output_file.write(result + '\n')
