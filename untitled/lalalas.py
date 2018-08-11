import vk_api

vk_session = vk_api.VkApi('granj444@mail.ru', 'loveyou')

vk_session.auth()

vk = vk_session.get_api()
print(vk.user.id)
# print(vk.wall.post(message='Hello '))

# print(vk.photos.getAlbums())
print(vk.photos.getAlbumsCount())

photos = vk.photos.getAll()
print(photos)

# 20462871
# 456239450





# <vk_api.vk_api.VkApiMethod object at 0x7f49de77b3c8>
# {'count': 25,
# 'items': [{'id': 178641437, 'thumb_id': 309154513, 'owner_id': 20462871, 'title': 'в месте, вместе',
# 'description': '', 'created': 1376825976, 'updated': 1376828786, 'size': 29, 'thumb_is_last': 1,
# 'privacy_view': ['list1', 'list5', 'list9'], 'privacy_comment': ['all']},
# c
# {'id': 159673502, 'thumb_id': 285930979, 'owner_id': 20462871, 'title': 'Лото - что-ли....', 'description': '', 'created': 1341666790, 'updated': 1341667546, 'size': 34, 'thumb_is_last': 1, 'privacy_view': ['list1', 'list5', 'list9'], 'privacy_comment': ['list13']},
# {'id': 157821412, 'thumb_id': 284058039, 'owner_id': 20462871, 'title': 'первый заплыв на пол дистанции)', 'description': '', 'created': 1338018437, 'updated': 1338019018, 'size': 14, 'thumb_is_last': 1, 'privacy_view': ['list1', 'list5', 'list9'], 'privacy_comment': ['list13']},
# {'id': 156016987, 'thumb_id': 282465600, 'owner_id': 20462871, 'title': 'Д.Р. Анюты', 'description': '', 'created': 1334612623, 'updated': 1334612623, 'size': 18, 'thumb_is_last': 1, 'privacy_view': ['list1', 'list5', 'list9'], 'privacy_comment': ['list13']},
# {'id': 153129613, 'thumb_id': 279060569, 'owner_id': 20462871, 'title': 'Уторник', 'description': '', 'created': 1329660663, 'updated': 1329976393, 'size': 32, 'thumb_is_last': 1, 'privacy_view': [5133718, 5738478, 11157918, 14002040, 17076503, 24487550, 27887407], 'privacy_comment': [5133718, 5738478, 11157918, 14002040, 17076503, 24487550, 27887407]},
# {'id': 148693189, 'thumb_id': 272839927, 'owner_id': 20462871, 'title': 'Новый 12–ый', 'description': '', 'created': 1323774757, 'updated': 1356401092, 'size': 71, 'privacy_view': ['list1', 'list5', 'list9'], 'privacy_comment': ['list13']},
# {'id': 147492648, 'thumb_id': 270811357, 'owner_id': 20462871, 'title': 'без названия', 'description': '', 'created': 1322057626, 'updated': 1322057772, 'size': 7, 'thumb_is_last': 1, 'privacy_view': ['all'], 'privacy_comment': ['all']},
# {'id': 141742472, 'thumb_id': 265434643, 'owner_id': 20462871, 'title': 'чеперы...', 'description': '', 'created': 1314618045, 'updated': 1314666210, 'size': 15, 'thumb_is_last': 1, 'privacy_view': ['all'], 'privacy_comment': ['all']},
# {'id': 137169798, 'thumb_id': 264250787, 'owner_id': 20462871, 'title': 'Наседкено', 'description': 'вот так работать - нельзя))))', 'created': 1308405065, 'updated': 1333779792, 'size': 245, 'privacy_view': ['list1', 'list5', 'list9'], 'privacy_comment': ['list13']},
# {'id': 124096846, 'thumb_id': 199876033, 'owner_id': 20462871, 'title': 'День рождения', 'description': '', 'created': 1293021694, 'updated': 1293022211, 'size': 28, 'thumb_is_last': 1, 'privacy_view': ['list1', 'list5', 'list9'], 'privacy_comment': ['list13']},
# {'id': 122188551, 'thumb_id': 191800076, 'owner_id': 20462871, 'title': 'Ирокинда 2010(2)', 'description': 'продолжение', 'created': 1290552163, 'updated': 1290556045, 'size': 170, 'thumb_is_last': 1, 'privacy_view': ['friends'], 'privacy_comment': ['friends']},
# {'id': 122083237, 'thumb_id': 191594959, 'owner_id': 20462871, 'title': 'Ирокинда 2010(1)', 'description': 'Таки добрался я до фоток!!! Пока не все еще!!!! Но в скором надуюсь... все будет окуенно)))', 'created': 1290429483, 'updated': 1290551936, 'size': 524, 'privacy_view': ['friends'], 'privacy_comment': ['friends']},
# {'id': 122006267, 'thumb_id': 191332445, 'owner_id': 20462871, 'title': 'праздник)', 'description': '', 'created': 1290335744, 'updated': 1290336263, 'size': 7, 'thumb_is_last': 1, 'privacy_view': ['list1', 'list5', 'list9'], 'privacy_comment': ['list13']},
# {'id': 121370124, 'thumb_id': 189833929, 'owner_id': 20462871, 'title': 'Байкал', 'description': 'Это было круто... но фотоаппарат все никак не сможет передать!', 'created': 1289532202, 'updated': 1289535968, 'size': 69, 'privacy_view': ['list1', 'list5', 'list9'], 'privacy_comment': ['list13']},
# {'id': 110067362, 'thumb_id': 163452230, 'owner_id': 20462871, 'title': 'Демы из РФК', 'description': '', 'created': 1273764459, 'updated': 1273766221, 'size': 48, 'thumb_is_last': 1, 'privacy_view': ['all'], 'privacy_comment': ['all']},
# {'id': 108634662, 'thumb_id': 160411647, 'owner_id': 20462871, 'title': 'очередной бессмысленный альбом', 'description': '2010 год...', 'created': 1271660976, 'updated': 1315735914, 'size': 36, 'privacy_view': ['list1', 'list5', 'list9'], 'privacy_comment': ['list13']},
# {'id': 106324947, 'thumb_id': 155738675, 'owner_id': 20462871, 'title': 'жувотные', 'description': '', 'created': 1268291125, 'updated': 1268291189, 'size': 26, 'thumb_is_last': 1, 'privacy_view': ['friends_of_friends'], 'privacy_comment': ['list13']},
# {'id': 106195839, 'thumb_id': 279258001, 'owner_id': 20462871, 'title': 'rest in peace', 'description': 'Памяти Геры', 'created': 1268105976, 'updated': 1330142157, 'size': 50, 'thumb_is_last': 1, 'privacy_view': ['list13'], 'privacy_comment': ['list13']},
# {'id': 105904324, 'thumb_id': 154894546, 'owner_id': 20462871, 'title': '6 лет мечты сбываются)))', 'description': 'Покотушки на борде))) ', 'created': 1267696457, 'updated': 1267697046, 'size': 9, 'thumb_is_last': 1, 'privacy_view': ['list1', 'list5', 'list9'], 'privacy_comment': ['list13']},
# {'id': 105567165, 'thumb_id': 157676537, 'owner_id': 20462871, 'title': 'Психоделика', 'description': '', 'created': 1267199319, 'updated': 1269705318, 'size': 112, 'thumb_is_last': 1, 'privacy_view': ['list13'], 'privacy_comment': ['list13']},
# {'id': 95423195, 'thumb_id': 135551505, 'owner_id': 20462871, 'title': 'Мой питомец', 'description': '', 'created': 1250782072, 'updated': 0, 'size': 6, 'thumb_is_last': 1, 'privacy_view': ['list1', 'list5', 'list9'], 'privacy_comment': ['list13']},
# {'id': 95328410, 'thumb_id': 160740624, 'owner_id': 20462871, 'title': 'Лето 2009', 'description': '', 'created': 1250518644, 'updated': 1271980988, 'size': 66, 'thumb_is_last': 1, 'privacy_view': ['list1', 'list5', 'list9'], 'privacy_comment': ['list13']},
# {'id': 59873557, 'thumb_id': 120259380, 'owner_id': 20462871, 'title': 'просто "ольбом"', 'description': '', 'created': 1228457109, 'updated': 1317517816, 'size': 52, 'thumb_is_last': 1, 'privacy_view': ['list1', 'list5', 'list9'], 'privacy_comment': ['list13']},
# {'id': 119634421, 'thumb_id': 121760982, 'owner_id': 20462871, 'title': 'Я =)', 'description': '', 'created': 1287420434, 'updated': 1376828606, 'size': 55, 'privacy_view': ['list13'], 'privacy_comment': ['all']}]}

