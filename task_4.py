import datetime

# Для примера создадим индекс для коллекции files по полю createdAt, с параметром expireAfterSeconds равным 3600:

db.files.createIndex({"createdAt": 1}, {expireAfterSeconds: 3600})

# Этот индекс позволяет mongoDB удалить запись через час после времени, указанном в поле createdAt

# Поле createdAt заполняется следующим образом при добавлении записи в коллекцию:

db.files.insert({"createdAt": datetime.now(), "logEvent": 2, "logMessage": "Success!"})
