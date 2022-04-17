# <файл> : <залежності>. Цей фрагмент викликається при команді make
main.bin: lab6.asm lab7.asm

lab6:
# Компіляція в бінарний файл
	nasm -fbin lab6.asm -o main.bin       
# Дозаповнення бінарного файлу нулями, щоб його розмір був достатнім, щоб створити ISO файл 
	truncate main.bin -s 1200k 
	make run

lab7:
# Компіляція в бінарний файл
	nasm -fbin lab7.asm -o main.bin       
# Дозаповнення бінарного файлу нулями, щоб його розмір був достатнім, щоб створити ISO файл 
	truncate main.bin -s 1200k 
	make run

# Очищення поточної директорії. Цей фрагмент викликається по команді make clean
clean: 
	rm main.bin

# Запуск QEMU. Цей фрагмент викликається по команді make run
run: 
	qemu-system-x86_64 -soundhw all main.bin
