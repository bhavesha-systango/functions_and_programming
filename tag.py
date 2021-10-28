def tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))

print(tag('img', src ="monet.jpg", alt ="this is image", border =1))

def tag2(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += '{k}="{v}"'.format(k = key, v = str(value))
    result += '>'
    return result

print(tag2('img', src ="monet.jpg", alt ="this is image", border =1))
