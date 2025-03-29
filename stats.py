def count_words(book_contents):
    return len(book_contents.split())

def count_characters(book_contents):
    counts = {}
    for i in book_contents.lower():
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] = counts[i] + 1
    return counts

'''
   
''' 
def sort_on(dict):
    return dict["num"]

def report_format(counts):
    sorted_list = []
    for key, value in counts.items():
          if key.isalpha() == False:
              continue
          new_dict = {}
          new_dict["name"] = key
          new_dict["num"] = value
          sorted_list.append(new_dict)      
    sorted_list.sort(reverse=True, key=sort_on)    
    return sorted_list    


    # for key, value in counts.items():
    #     print(f"{key}: {value}")
    
    
    # total_words = 0
    # new_words = []
    # book_contents = book_contents.split(" ")
    # for i in book_contents:
    #     if i not in new_words:
    #         new_words.append(i)
    #         total_words += 1
    #     else:
    #         continue
    # return total_words