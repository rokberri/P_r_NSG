def wirte_to_file(*data):
    f = open('output.txt','a')
    for d in data:
        for el in d:
            f.write(str(el)+' ')
        f.write('\n')
    f.close()
    
def find_T(array:list)->int:
    # [115, 1012, 142, 34, 827]
    start_el = array[1]
    return len(set(array))

def normalize(data)->list: 
    max_el = max(data)
    min_el = min(data)
    normalize_data = list()
    for el in data:
        try:
            normalize_data.append((el - min_el)/(max_el - min_el))
        except ZeroDivisionError:
            normalize_data.append(1 * len(normalize_data))
    return normalize_data

def is_good_sequence(level_of_quality:float,*args)->bool:
    if args[0]>=int(args[1]*0.02):
        res = 0
        norm_args = normalize(args)
        for i in norm_args:
            res += i
        print(res)
        return (res/len(args)+1)>=level_of_quality
    else: return False

def sequence_bit_test(rand_nums)->float:
    """
    Один из статистических тестов NIST
    Частотный побитовый тест
    """
    binary_str = ''
    rand_nums = list(int(el*10000000000000000) for el in rand_nums)
    for el in rand_nums:
        binary_str += bin(el)
    return binary_str.count('1')/len(binary_str)