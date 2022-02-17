import os
import re

REGEX = re.compile(r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""")


def task1(file_name='filenames'):
    # в папке test найти все файлы filenames вывести колличество
    path = os.path.abspath('test')
    tree = os.walk(path)
    allfiles = []
    for element in tree:
        allfiles += element[2]
    needed_files = list(filter(lambda x: x.startswith(file_name), allfiles))
    length = len(needed_files)
    print(length)
    return length


def task2():
    # в папке test найти все email адреса записанные в файлы
    path = os.path.abspath('test')
    tree = os.walk(path)
    allfiles = []
    for element in tree:
        for file in element[2]:
            file_path = os.path.join(element[0], file)
            allfiles.append(file_path)
    all_emails = []
    for file in allfiles:
        with open(file) as f:
            content = f.read().replace('\n', ' ')
            if content:
                emails = re.findall(REGEX, content)
                all_emails += emails
#   Now we have list of all emails, then get set of unique emails:
    all_emails = set(all_emails)
    print(f'__________ATTENTION! UNIQUE EMAILS: {all_emails}__________')
    return all_emails







def main():
    task1()
    task2()
    # дополнительно: придумать над механизм оптимизации 2-й задачи (используя threading)

if __name__ == '__main__':
    main()

