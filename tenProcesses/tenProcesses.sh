#!/bin/bash

processes=()

mapfile -t processes < <(ps aux --sort=-%cpu | head -10)

for i in {1..10}
do
	mkdir -p "./dir$i"
	touch "./dir$i/file$i.txt"
	echo "${processes[i]}" > ./dir$1/file$1.txt
done
