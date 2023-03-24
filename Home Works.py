# y = int(input())
# if y % 4 == 0 and y % 100 != 0:
#    print("Так")
# elif y % 400 == 0:
#    print("Так")
# else:
#    print("Ні")
# favoritegame = input("Моя улюблена гра: Half-Life 2")
# favoritebook = input("Моя улюблена книга: Володар Перстнів")
# favoritefile = input("Мій улюблений фільм: Залізна людина")
# print()
#list = ["hello", "world", "say", "to"]

#list.append("west")

#list.insert(int(len(list) / 2), "middle")

#print([x for x in list if "w" in x and "d" in x])

#new_list = [x for x in list if "t" in x]

#print(new_list)
def a(str1, str2):
    return str1 + str2
def b(list1):
    return len(list1)
if __name__ == '__main__':
    print(a('Hello world!','Denis'))
    print(b([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
