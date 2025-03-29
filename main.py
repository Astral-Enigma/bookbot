from stats import count_words
from stats import count_characters
from stats import report_format
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents   

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    book_contents = get_book_text(sys.argv[1])
    # print(book_contents)
    num_words = count_words(book_contents)
    print("====BOOKBOT====")
    print("")
    print("Analyzing book found at" + " " + sys.argv[1])
    print("")
    print("---Word Count---")
    print("")  
    print(f"Found {num_words} total words")
    print("")
    print("---Character Count---")
    print("")
    num_chars = count_characters(book_contents)
    # print(str(num_chars))
    report_chars = report_format(num_chars)
    for i in report_chars:
        print(i["name"]+ ":" + " " + str(i["num"]))
    # for i in report_chars:
    #     print(i)
          

if __name__=="__main__":
    main()