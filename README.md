тест

```
python manage.py fill_db
```

```
python manage.py csu
```
group fixtures -> users/fixtures/

endpoints:

```
users/login/
```
```
users/register/
```
```
materials/
```

Фильтрация по курсу:
```
users/payments/?course=
```
Фильтрация по уроку:
```
users/payments/?lesson=
```
Фильтрация по способу оплаты (например, "cash"):
```
users/payments/?payment_method=cash
```
Сортировка по дате (по убыванию):
```
users/payments/?ordering=-payment_date
```
Сортировка по дате (по возрастанию):
```
users/payments/?ordering=payment_date
```

Подписка на курс
method post
```
materials/subscribe/
```

```
{
    "course_id": "course id"
}
```