def single_root_words(root_world, *other_words, ):
    same_word = []
    for i in other_words:
        if root_world.lower() in i.lower() or i.lower() in root_world.lower():
            same_word.append(i)
    return same_word


#result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(result2)