# rqadviser-consistency
ПО, проверяющее набор требований на противоречия. 

Установить все зависимости из requirements.txt 
Запуск линтеров:
flake8 rqadviser
pylint rqadviser
mypy --package=rqadviser --ignore-missing-imports

Запуск тестов:
pytest --cov=rqadviser
