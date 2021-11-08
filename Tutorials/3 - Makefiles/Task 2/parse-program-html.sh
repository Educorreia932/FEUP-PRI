#!/bin/bash

courses=$(sed -n '/<table  class="dados" >/,/<\/table>/p' |
    sed -n 's/<td nowrap="nowrap" class="t">\(.*\)<\/td>/\1/p' |
    sed -n '4~5p;3~5p'
)

{
    while read id; do 
        read name; 
        echo -e "$id\t$name";
    done;
} < <(echo "$courses") | sort -t$'\t' -k2
