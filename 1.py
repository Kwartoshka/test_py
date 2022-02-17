MAX_PAGES = 10000000


def black_box(page: int):
    if page <= 575757:
        return True
    else:
        return False


def find_last_page(min=0, page=MAX_PAGES, max = MAX_PAGES):
    if black_box(page):
        if not black_box(page+1):
            result = page
        else:
            min = page
            page = int(min + (max - min) / 2)
            result = find_last_page(min, page, max)

    else:
        max = page
        page = int(max - (max - min) / 2)
        result = find_last_page(min, page, max)
    return result



def main():
    """
    Вам дали книгу, конкретное количество страниц вам не сообщили,
    но оно точно не превышает 10 000 000.
    
    Вам необходимо вычислить номер последней страницы.
    Книгу открывать нельзя - вместо этого вам выдали черный ящик, чтобы слегка усложнить задачу.
    Черному ящику (функция black_box) можно сообщить предполагаемый номер последней страницы,
    а в ответ узнать, есть ли эта страница в книге.
    
    Уточнение:
        !!!!!!!!!!!!!!!! black_box возвращает True, если страница последняя  NOT LAST!!! IN the book
        !!!!!!!!!!!!!!!! возвращает False, если страница не последняя. NOT LAST!!! NOT IN the book
    
    31  `
    Важно: написать наиболее эффективный алгоритм (по числу итераций)
    """
    print(find_last_page())

if __name__ == '__main__':
    main()

