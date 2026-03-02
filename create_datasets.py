import random

def generate_datasets(size=1_000_000, seed=42):
    random.seed(seed) 
    datasets = {}
    
    # Dãy số nguyên tăng dần
    print("Đang tạo dãy số nguyên tăng dần...")
    datasets['int_ascending'] = list(range(size))
    
    # Dãy số thực giảm dần
    print("Đang tạo dãy số thực giảm dần...")
    datasets['float_descending'] = [float(x) for x in range(size, 0, -1)]
    
    # 4 dãy số nguyên ngẫu nhiên
    for i in range(1, 5):
        print(f"Đang tạo dãy số nguyên ngẫu nhiên{i}...")
        datasets[f'int_random_{i}'] = [random.randint(0, size * 10) for _ in range(size)]
        
    # 4 dãy số thực ngẫu nhiên
    for i in range(1, 5):
        print(f"Đang tạo dãy số thực ngẫu nhiên{i}...")
        datasets[f'float_random_{i}'] = [random.uniform(0.0, float(size * 10)) for _ in range(size)]
        
    print("Đã tạo xong:>!")
    return datasets