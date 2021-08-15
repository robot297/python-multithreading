import threading
import time
import concurrent.futures

from dictionary import *

if __name__ == "__main__":
    big_list = ['hello'] * 100000
    print(len(big_list))
    master_dictionary = {}

    start = time.time()
    # threads = []
    # for item in range(0, len(big_list)):
    #     # thread = threading.Thread(target=dictionary_writer, args=[item, big_list[item]])
    #     thread = threading.Thread(target=file_writer, args=[item, big_list[item]])
    #     threads.append(thread)
    #     thread.start()

    # for thread in threads:
    #     thread.join()

    for item in range(0, len(big_list)):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(dictionary_writer, item, big_list[item])
            master_dictionary.update(future.result())

    dictionary_file_writer(master_dictionary)
    print(f'{start - time.time()}')
