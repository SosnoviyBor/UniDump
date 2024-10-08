[org 0x7c00] ; Початок BOOT сектора
[bits 16]



; Виводимо меню у консоль
call draw_ui

ask_for_input:
; Зчитуємо символ, введений із клавіатури (AL <- input)
	mov ah, 0
	int 0x16
	call draw_ui

; Перевірка вводу
	cmp al, "q"
	je q_pressed
	cmp al, "W"
	je W_pressed
	cmp al, "e"
	je e_pressed
	jmp ask_for_input

q_pressed:
	; Обчислення прикладу
	call calculate
	jmp ask_for_input

W_pressed:
	; Пищання у колонки
	call do_noise
	jmp ask_for_input

e_pressed:
	; Вихід із програми
	mov si, ui_end
	call printf

	jmp $

; =================================== Процедури ===================================
; ----------------------------------------------------------------------------------
; Призначення: вивід текстовоїстроки у консоль
; Вхід: 
; 	SI - зміщення, по якому знаходиться початок рядка для друку
; Вихід: ---
; ----------------------------------------------------------------------------------
printf:
	pusha

	; Записуємо в AL поточний символ по зміщенню SI
	print_loop:
		mov al, [si]
		cmp al, "$"
		jne print_char		; Якщо це ще не кінець рядка
		jmp printf_end

	print_char:
		mov ah, 0x0e
		int 0x10			; Друкуємо символ, що знаходиться в AL
		add si, 1 			; Переходимо до наступного символа в рядку
		jmp print_loop

	printf_end:
	popa
	ret
	
; ---------------------------------------------------------------------------------
; Призначення: вивід інтерфейсу
; Вхід: ---
; Вихід: ---
; ---------------------------------------------------------------------------------
draw_ui:
	pusha

	; Очищаємо консоль
	mov ax,03h
	int 10h
	; Виводимo текст у консоль
	mov si, ui
	call printf

	popa
	ret

; ---------------------------------------------------------------------------------
; Призначення: обчислення виразу, та його виводу на екран
; Вхід: ---
; Вихід: ---
; ---------------------------------------------------------------------------------
calculate:

	; Підготовка декоративного тексту
	mov si, equation
	call printf

	; Обнулюємо регістр АХ. Це не обов'язково, але про всяк випадок хай буде
	mov ax, 0

	; a1 + a2
	mov ax, a1
	mov dx, a2
	neg ax
	sub dx, ax
	mov ax, dx
	; (a1 + a2) * a3
	mov bx, a3
	imul bx
	; (a1 + a2) * a3 / a4
	mov bx, a4
	idiv bx
	; (a1 + a2) * a3 / a4 + a5
	mov dx, a5
	neg ax
	sub dx, ax
	mov ax, dx

	; Перевіряємо, чи від'ємний наш результат
	cmp ax, 0
	jge number_printer
	; Підготовка даних до виводу, якщо результат від'ємний
	minus_printer:
		neg ax
		push ax

		mov al, "-"
		mov ah, 0eh
		int 0x10

		pop ax

	; Вивід результату у консоль
	number_printer:
	; Конвертуємо результат у ASCII код нашого числа
	add al, 30h
	; Виводимо число (AL) у консоль
	mov ah, 0eh
	int 0x10
	ret

; ---------------------------------------------------------------------------------
; Призначення: програш звуку
; Вхід:
; frequency <- частота звуку
; duration <- тривалість звуку
; Вихід:
; Максимально противний звук із колонок. Наслоджуйтесь
; ---------------------------------------------------------------------------------
do_noise:
	; Виводимо у консоль індикатор наявності звуку
	mov si, standby
	call printf

	; Зберігаємо початковий стан динаміка
	in al, 61h
	push ax

	or al, 00000011B	; Зміна стану на включений динамік (режим керування мікросхемою таймера)
	out 61h, al			; Занесення стану
	mov al, 10110110b
	out 0x43, al
	mov al, frequency	; Встановлюємо частоту (1.19МГц / frequency)
	out 42h, al			; Вмикаємо таймер, що буде подавати імпульси на динамік за заданою частотою
	call pause			; Виклик процедури очікування, під час виконання котрої в нас буде створюватись звук

	; Повертаємо початковий стан динаміка
	pop ax
	out 61h, al

	; Повертаємо звичайний інтерфейс
	call draw_ui
	ret

; ---------------------------------------------------------------------------------
; Призначення: очікування
; Вхід: ---
; Вихід: ---
; ---------------------------------------------------------------------------------
pause:
	push cx

	; Робимо duration^2 ітерацій циклу та сподіваємось, що це займе приблизно 1 секунду
	; Eкспериментальним методом було доведено, що виконання duration^2 ітерацій циклу займає приблизно 1 секунду
	mov cx, duration
	loop1:
		push cx
		mov cx, duration
		loop2:
			loop loop2
			pop cx
		loop loop1

	pop cx
	ret



; ================================ Дані ================================
ui db "Team 1 welcomes you, fellow traveller",13,10
   db 13,10
   db "Press q to calculate a complex equation",13,10
   db "Press W to play an awful noise",13,10
   db "Press e to exit",13,10
   db "------------------------",13,10,'$'
ui_end db "Thanks for using our services!",13,10,'$'

equation db "(a1 + a2) * a3 / a4 + a5",13,10
		 db "a1 = -7",13,10
		 db "a2 = 3",13,10
		 db "a3 = 2",13,10
		 db "a4 = 4",13,10
		 db "a5 = 1",13,10
		 db 13,10
		 db "Result = ", '$'

standby db "Trust me, noise is there", "$"

; Константи
a1 equ -7
a2 equ 3
a3 equ 2
a4 equ 4
a5 equ 1

frequency equ 255
duration equ 5500

; ----------------------------------------------------------------------------------
times 510-($-$$) db 0
dw 0xAA55