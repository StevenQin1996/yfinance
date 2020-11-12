def get_key(cache, key, value):
    if type(value) is dict:
        for k, v in value.items():
            get_key(cache, k, v)
    elif type(value) is list:
        for item in value:
            if type(item) is dict:
                for k, v in item.items():
                    get_key(cache, k, v)
    cache.append(key)
    return


keys = []
for key, value in msft.all.items():
    get_key(keys, key, value)
key_candi = set()
for item in keys:
    try:
        temp = int(item)
    except:
        key_candi.add(item)
print(key_candi)