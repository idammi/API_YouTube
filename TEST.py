import re

status_now = "Найден контент, защищенный авторским правом. Владелец разрешает использовать эти материалы на YouTube."

print(re.findall(fr'(?im)\bВладелец разрешает\S*\b', status_now))

# print(status_now.split(".")[0])