# ai_defender

مكتبة Python لحماية الهاتف من الاختراق باستخدام الذكاء الاصطناعي.

## المميزات

- فحص الشبكات والروابط والتطبيقات والبورتات.
- التعلم من البيانات لتحسين اكتشاف التهديدات.
- إيقاف الهجمات وقطع الاتصال بالشبكات المشبوهة.

## التثبيت

```bash
pip install .
```

## الاستخدام

```python
from ai_defender import AIDefender

defender = AIDefender()
result = defender.chat("فحص التطبيقات")
print(result)
```
