def get_all_users (user):
    return {
        'username' : user.username,
        'friends' : list(map(get_all_username,user.friends.all()))
    }

def get_all_username (user):
    return  user.username

def get_all_lessons (lesson):
    return {
        'lessonName' : lesson.name,
        'classesPerWeek' : lesson.classesPerWeek
    }

def get_name_pokemon (pokemon):
    print(pokemon)
    return {'name ':pokemon['name']}