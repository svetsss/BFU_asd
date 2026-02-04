#сортировки с разбиение на части во временные файлы и сливание позже
#в каждой кучи наим value потом закидывание в файл

import heapq
import os


def merge_files(output_file: str, temp_files: list[str], path: str):
    heap_array = []
    temp_files = [open(temp_file, "r", encoding="utf-8") for temp_file in temp_files]

    with open(output_file, "w", encoding="utf-8") as output:
        for i in range(len(temp_files)):
            element = temp_files[i].readline().strip()
            if element:
                heapq.heappush(heap_array, (int(element), i))

        while heap_array:
            value, file_idx = heapq.heappop(heap_array)
            output.write(f"{value}\n")

            element = temp_files[file_idx].readline().strip()
            if element: 
                heapq.heappush(heap_array, (int(element), file_idx))

    for temp_file in temp_files:
        temp_file.close()


def create_initial_runs(input_file: str, run_size: int, path: str):
    temp_files: list[str] = []

    if not os.path.exists(path):
        os.makedirs(path)

    with open(input_file, "r", encoding="utf-8") as input:
        temp_files_counter = 0

        while True:
            data = []
            for _ in range(run_size):
                line = input.readline()
                if not line:
                    break
                line = line.strip()
                if line == "":
                    continue
                data.append(int(line))

            if not data:
                break

            data.sort()

            run_path = os.path.join(path, f"f_{temp_files_counter}.txt")
            with open(run_path, "w", encoding="utf-8") as output:
                output.write("\n".join(str(i) for i in data) + "\n")

            temp_files.append(run_path)
            temp_files_counter += 1

    return temp_files


def external_multiphase_sort(run_size: int, base_dir: str = r"tests/data_12/"):
    input_file = os.path.join(base_dir, "input.txt")
    output_file = os.path.join(base_dir, "output.txt")
    temp_dir = os.path.join(base_dir, "Temp_files_linear")

    print("External multiphase sort", input_file)

    temp_files = create_initial_runs(input_file, run_size, temp_dir)
    merge_files(output_file, temp_files, temp_dir)


external_multiphase_sort(run_size=1000)