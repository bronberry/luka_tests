Следует использовать поле fuction, для рутинга на определенную функцию, таким образом наш запрос к сервису может отслиживать на
какую именно функцию адрессуется вызов, например
```
baseurl = 'localhost:8000/api/Datalore'
```
В FastAPI:
```
router = APIRouter(prefix='/Datalore')
app.include_router(add_router.router)

@app.get()
async def webhook_wrapper(function: dict):
    if function is None/False:
        send_error
    elif function == 'func1':
        do_something_and_return
    elif function == 'func2':
        do_something_ELSE_and_return
    ....
```
Реализация рутинга в Django в функциональном стиле отличаться будет малозначительно, указал тут самый простой пример. 

Также можно реализовать FSM (Finite-State-Machine) если требуется контроль того к какой функции изначально и далее было обращение.