def replace_chars(string, char1, char2):
    return string.replace(char1, char2)

def main():
    input_string = input("Nhập chuỗi(ko cách): ")
    char1 = input("Nhập chữ cần thay thế: ")
    char2 = input("Nhập chữ muốn thay thế: ")
    result = replace_chars(input_string, char1, char2)
    print("Kết quả:", result)

if __name__ == "__main__":
    main()
