# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...
import room_1 as r1
import room_2 as r2
# TODO здесь ваш код


print("в комннате")
for name in r1.folks:
    print(name)

print("в комннате")
for name in r2.folks:
    print(name)