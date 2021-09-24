IDEAL
MODEL small
STACK 256

; ==================================== Макросы ====================================
; ---------------------------------------------------------------------------------
; Призначення: ініціалізація програми
; ---------------------------------------------------------------------------------
MACRO M_init		; Макрос для ініціалізації. Його початок
	mov ax, @data	; @data ідентифікатор, що створюються директивою MODEL
	mov ds, ax		; Завантаження початку сегменту даних в регістр DS
	mov es, ax		; Завантаження початку сегменту даних в регістр ES
	ENDM M_init		; Кінець макросу

; ---------------------------------------------------------------------------------
; Призначення: вихід із програми (із кодом 0)
; ---------------------------------------------------------------------------------
MACRO M_exit
	mov ah, 4ch
	mov al, 0
	int 21h
	ENDM M_exit

; ---------------------------------------------------------------------------------
; Предназначение: считать в зависимости от знака (регистра BL) перед числом
; Вход:
; AX <- число
; BL <- 0, если число положительное; 1, если число отрицательное
; Выход:
; AX <- результат
; ---------------------------------------------------------------------------------
MACRO M_calculate
	cmp bl, 0
	je positive
	jmp negative

	positive:
		sub ax, task
		jb negative_result
		push ax

		mov ah, 09h
		mov dx, offset spacer
		int 21h

		pop ax
		jmp calculate_end

		negative_result:
			push ax

			mov ah, 09h
			mov dx, offset spacer
			int 21h
			mov ah, 09h
			mov dx, offset minus
			int 21h

			pop ax
			neg ax
			jmp calculate_end

	negative:
		add ax, task
		push ax

		mov ah, 09h
		mov dx, offset spacer
		int 21h
		mov dx, offset minus
		int 21h

		pop ax
		jmp calculate_end

	calculate_end:
ENDM M_calculate

DATASEG
digits db 0

; Сегодня мы отнимаем 34 от того, что нам дадут
task equ 34d

msg db "Write any number between -255 and 255: ", "$"
err_msg db 10, 13, 10, 13, "Wrong input", 10, 13, "$"

input_buffer db 5, 0, 0, 0, 0, 0, 0
spacer db 10, 13, "Result: ", "$"
minus db "-", "$"
output_buffer db 0, 0, 0, 0, 0, 0

CODESEG
Start:
	M_init
	; Вступительное сообщение
	mov dx, offset msg
	mov ah, 09h
	int 21h

	; Считывание ввода
	mov dx, offset input_buffer
	mov ah, 0ah
	int 21h							; http://www.codenet.ru/progr/dos/dos_0018.php

	; Парсинг полученного стринга в десятичное число
	mov si, offset input_buffer+2	; Адрес начала стринга
	mov bh, [si-1]					; Длинна стринга
	call string2dec

	; Искусственное ограничение числа до 255
	; Оно необязательно, но я лучше себя заранее обезопашу от возможных трудностей...
	; ...с 2-байтными регистрами в будущем
	cmp ax, 255d
	jna ok_amount	; jump if AX > 255d
	mov ah, 09h
	mov dx, offset err_msg
	int 21h
	M_exit

	ok_amount:
	M_calculate
	; Парсинг десятичного числа в стринг
	mov si, offset output_buffer
	call number2string

	; Вывод этого стринга и отступа перед ним
	mov ah, 09h
	mov dx, offset output_buffer
	int 21h

	M_exit

; =================================== Процедуры ===================================
; ---------------------------------------------------------------------------------
; Предназначение: Парс стринга в десятичное число
; Вход:
; BH <- Длинна стринга (1-3)
; SI <- Адрес начала стринга
; Выход:
; AX <- Результат, десятичное число
; BL <- 0, если число положительное; 1, если число отрицательное
; ---------------------------------------------------------------------------------
proc string2dec
	mov ax, 0	; Результат
	mov cx, 0	; Буфер для числа
	mov bl, 0
	Str_parser:
		mov al, [si]	; Считываем чар из стринга

		; Проверка на минус
		cmp al, "-"
		jne not_a_minus
		call trim_minus
		jmp Str_parser

		not_a_minus:
		sub al, 30h		; Конвертируем чар в цифру
		call validate	; Проверяем, цифра ли это

		; Увеличиваем число в зависимости от его разряда
		cmp bh, 3
		je mul_by_100
		cmp bh, 2
		je mul_by_10
		jmp str_continue

		mul_by_100:
		mov dx, 10d
		mul dx
		mul_by_10:
		mov dx, 10d
		mul dx

		str_continue:
		add cx, ax	; Сохраняем число в буфер
		inc si		; Двигаем указатель на следующий чар
		dec bh		; BH == 0 : Конец
		jnz Str_parser	; BH != 0 : Повтор
	mov ax, cx
	ret
	endp string2dec

; ---------------------------------------------------------------------------------
; Предназначение: Проверка, является ли цифра на самом деле цифрой
; Вход:
; AL <- Возможно цифра
; Выход: ---
; ---------------------------------------------------------------------------------
proc validate 
	push dx

	cmp al, 0
	jb validate_error
	cmp al, 9
	ja validate_error
	jmp ok
	
	validate_error:
		mov ah, 09h
		mov dx, offset err_msg
		int 21h
		M_exit

	ok:
	pop dx
	ret
	endp validate

; ---------------------------------------------------------------------------------]
; Предназначение: отрезание минуса в стринге
; Вход: ---
; Выход:
; BL <- 1
; ---------------------------------------------------------------------------------
proc trim_minus
	push si
	push bx
	push ax

	mov si, offset input_buffer+2	; Получаем адрес минуса
	mov bx, 4						; Количство желанных итераций
	trimmer:
		mov ax, [si+1]		; Следующее число
		mov [si], ax		; Пишем его на 1 байт назад
		inc si				; Движемся дальше
		dec bx				; Проверка на конец стринга
		jnz trimmer

	pop ax
	pop bx
	pop si

	dec bh
	mov bl, 1
	ret
endp trim_minus

; ---------------------------------------------------------------------------------
; Предназначение: Парс десятичного числа в стринг
; Ввод:
; AX <- Число для парса
; SI <- Ссылка на начало стринга
; Вывод: ---
; ---------------------------------------------------------------------------------
proc number2string
	mov bl, 0	; 0 для проверки на последний разряд
	; Парсим)
	Num_parser:
		; Смотрим, в каком разряде вы находимся
		cmp ax, 100d
		ja three_digit
		cmp ax, 10d
		ja two_digit
		mov cx, 1d
		mov bl, 1	; Вот мы и на последнем разряде!
		jmp num_continue

		three_digit:
		mov cx, 100d
		jmp num_continue
		two_digit:
		mov cx, 10d
		jmp num_continue

		num_continue:
		; Получаем нашу цифру, делением с остатком
		; AX <- Делимое, потом результат деления с остатком
		; CX <- Делитель
		; DX <- Остаток
		mov dx, 0
		div cx
		cmp ax, 0
		
		; Заносим цифру в стринг
		add ax, 30h
		mov [si], ax
		; Повторить BL раз
		mov ax, dx
		inc si
		cmp bl, 1
		jne Num_parser
	; В конце дописываем доллар, чтобы прерывание для вывода знало, где кончается строка
	mov [si], "$"
	ret
	endp number2string


	end Start