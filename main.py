import time
from create_datasets import generate_datasets
from sorting import heap_sort, merge_sort, numpy_sort, quick_sort

def run_experiments():

    my_datasets = generate_datasets()
    algorithms = {
        "Numpy Sort": numpy_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort,
        "Merge Sort": merge_sort
    }

    print("\nBẮT ĐẦU CHẠY THỬ NGHIỆM...")
    print(f"{'Thuật toán':<15} | {'Loại dữ liệu':<20} | {'Thời gian (mili giây)'}")
    print("-" * 55)

    for name, func in algorithms.items():
        for data_name, data_array in my_datasets.items():
            
            test_array = data_array.copy() 
            
            start_time = time.perf_counter() 
            func(test_array)
            end_time = time.perf_counter()
            
            duration = int((end_time - start_time) * 1000) 
            
            print(f"{name:<15} | {data_name:<20} | {duration}")

if __name__ == "__main__":
    run_experiments()