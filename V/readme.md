# Минумы функций
## 7.1b
Написал алоритм, чтобы убедится что в точке он дает действительно минимум, на не значение на конце отрезка, взял производную в этой точке... Экстремум в 0.0, в -3.0 экстремума нет

## 7.6c
Устал писать каждый раз заново функции, сделал библиотеку MyMath
Реализовал наискорейший спуск. Забавно, что его сходимость довольно сильно зависит от точности бинарного поиска: при точности бинпоиска 10^(-8) для точности 10^(-4) наискорейшего спуска алгоритм не сходится. Однако если подкрутить в бинпоиске точность до минус 10, все ок. Работает вроде быстро, для алгоритма без np.sum в каждой строчке)
