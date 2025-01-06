#!/bin/bash

logfile="access.log"

total=$(wc -l < "$logfile")

unique_ip=$(awk '{print $1}' "$logfile" | sort | uniq | wc -l)

methods=$(awk '{gsub(/"/, "", $6); print $6}' "$logfile" | sort | uniq -c | awk '{print " " $1 " " $2}')

pop_url=$(awk '{print $7}' "$logfile" | sort | uniq -c | sort -nr | head -n 1 | awk '{print $1 " " $2}')

cat > report.txt <<EOL
Отчет о логе веб-сервера
========================
Общее количество запросов: $total
Количество уникальных IP-адресов: $unique_ip

Количество запросов по методам:
$methods

Самый популярный URL: $pop_url
EOL

