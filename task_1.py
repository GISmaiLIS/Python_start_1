def convert_time(duration: int):
    return f' {duration // 86400 % 361} дн. {duration // 3600 % 24} час.' \
        f' {duration // 60 % 60} мин. {duration % 60} сек.'

duration = [51, 153, 4153, 400153]
for element in duration:
    result = convert_time(element)
    print(result)