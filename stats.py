def get_num_words(data: str) -> int:
    return len(data.split())

def get_num_chars(data: str) -> dict[str, int]:
    dict = {}
    lis = [ words for words in data.lower().split() ]
    for index,word in enumerate(lis):
        for char in word:
            if dict.get(char) is None:
                dict[char] = 1
            else:
                dict[char] += 1
    return dict

def sort_on(items: dict) -> int:
    return items["num"]

def sort_dict(data: dict[str, int]) -> list[dict]:
    new_dict = [{"char": key , "num": value} for key,value in data.items()] 
    new_dict.sort(reverse=True, key=sort_on)
    return new_dict
