import regex
import random
def generate_hexa():
    text = ''
    text = text.join([random.choice('2A3B4C5D6E7F8910') for j in range(8)])
    if len((regex.compile(r"\L<name>", name=['AA','BB','CC','DD','EE','FF','AB','BC','CD','DE','EF','00','11', '22', '33', '44', '55','66','77','88','99','12','23','34','45','56','67','78','89'])).findall(text)) != 0:
        return generate_hexa()
    return '0x'+text
output = generate_hexa()
print(output)

#test code for checking repitation of number
def repitation_test():
    List_of_numbers=[]
    while True:
        obj=generate_hexa()
        if obj in List_of_numbers:
            result= {"result_List":List_of_numbers,"repitation_code_no":len(List_of_numbers)}
            return result
        else:
            List_of_numbers.append(obj)
# test_output=repitation_test()
# print(test_output)