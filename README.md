тест

```
python manage.py fill_db
```

endpoints:

Фильтрация по курсу:
```
/payments/?course=
```
Фильтрация по уроку:
```
/payments/?lesson=
```
Фильтрация по способу оплаты (например, "cash"):
```
/payments/?payment_method=cash
```
Сортировка по дате (по убыванию):
```
/payments/?ordering=-payment_date
```
Сортировка по дате (по возрастанию):
```
/payments/?ordering=payment_date
```