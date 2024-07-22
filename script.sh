#!/bin/bash

du -ah -Bm $PWD | sort -nr | head -n10
echo "Вывести оставшееся содержимое?Y/N"
read bool
if [ $bool = Y ]; then
    du -h -Bm $PWD | sort -nr | more +10
fi
