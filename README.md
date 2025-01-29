# Аналіз ефективності алгоритмів сортування

## Опис алгоритмів

1. **Сортування вставками (Insertion Sort)**  
   - Найкращий випадок: O(n) (коли масив уже відсортований)  
   - Найгірший та середній випадок: O(n²)  
   - Підходить для малих масивів або майже відсортованих даних.

2. **Сортування злиттям (Merge Sort)**  
   - Найгірший, середній і найкращий випадки: O(n log n)  
   - Використовує підхід "розділяй і володарюй".  
   - Потребує додаткової пам'яті O(n), оскільки не є сортуванням на місці.

3. **Timsort (вбудований у Python `sorted`)**  
   - Комбінація сортування злиттям та сортування вставками.  
   - Найгірший випадок: O(n log n), найкращий випадок: O(n).  
   - Ефективний для реальних даних, оскільки використовує адаптивні методи.

## Емпіричний аналіз

Було проведено тестування алгоритмів на масивах різного розміру (1000, 5000, 10 000, 50 000, 100 000 елементів). Замір виконано за допомогою модуля `timeit`.

### Основні спостереження:
- **Insertion Sort** швидко працює для малих масивів, але стає непридатним для великих (O(n²)).
- **Merge Sort** завжди працює за O(n log n), проте потребує додаткової пам'яті.
- **Timsort** показує найкращу продуктивність завдяки адаптивності: він використовує сортування вставками для малих підмасивів і злиття для великих.

### Висновки
- `sorted()` у Python (Timsort) є найефективнішим алгоритмом для загального використання, особливо на реальних наборах даних.
- У більшості випадків немає сенсу реалізовувати сортування вручну — використання вбудованих алгоритмів Python гарантує оптимальну швидкість.
- Timsort є надійним вибором через комбінацію ефективності та адаптивності.

**Рекомендація:** Для повсякденного використання варто застосовувати `sorted()` або `.sort()` замість реалізації власних алгоритмів.

