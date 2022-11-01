import PyPDF2
import os
import timeit


def pdf_read(term, path):
    """
    Функция читает PDF-файлы из заданной директории и выдает названия файлов, в которых обнаружено совпадение с ключевыми словами.
    :param term: Ключевые слова.
    :return: Названия целевых файлов.
    """
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'rb') as f:
            text = PyPDF2.PdfFileReader(f, strict=False)
            for page in range(text.numPages):
                pdf_page = text.getPage(0)
                t = pdf_page.extractText()
            if term in t.lower():
                print(filename)
            else:
                pass


path = input('Введите путь до папки с файлами PDF (в Windows C:\Windows\Folder, в Linux /home/user/Folder, в Mac OS /Users/Folder): ')
term = input('Ключевые слова: ')
print(pdf_read(term, path))

print(f'Скорость выполнения: {timeit.timeit("pdf_read(term, path)", number=0, globals=globals())}')