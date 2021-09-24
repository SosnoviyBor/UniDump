IDEAL
MODEL small
STACK 256

; ==================================== Макроси ====================================
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
; Призначення: запам'ятовування значень регістрів
; ---------------------------------------------------------------------------------
MACRO M_push_all
	push ax
	push bx
	push cx
	push dx
	push bp
	push si
	push di
	ENDM M_push_all

; ---------------------------------------------------------------------------------
; Призначення: повернення значень регістрів
; ---------------------------------------------------------------------------------
MACRO M_pop_all
	pop di
	pop si
	pop bp
	pop dx
	pop cx
	pop bx
	pop ax
	ENDM M_pop_all

DATASEG
msg db "Calculation time!", 10, 13
	db "Type your values and i'll calculate an equation for you", 10, 13
	db "====================", 10, 13
	db "If X > 0, equation will be ax^2+b/x", 10, 13
	db "If X = 0, equation will be a+2b", 10, 13
	db "If X < 0, equation will be ax^2-bx", 10, 13
	db "====================", 10, 13
	db "Variables are allowed only in range from -255 to 255", 10, 13
	db "Division results will be rounded!", 10, 13
	db "I'm not paid enough to program my own floating division algorithm", 10, 13, "$"
	
x_msg db  10, 13, "Enter your X value: ", "$"
a_msg db  10, 13, "Enter your A value: ", "$"
b_msg db  10, 13, "Enter your B value: ", "$"

x_str db 5, 0, 0, 0, 0, 0, 0
a_str db 5, 0, 0, 0, 0, 0, 0
b_str db 5, 0, 0, 0, 0, 0, 0

err_msg db 10, 13, 10, 13, "Wrong input", 10, 13, "$"
result_msg db 10, 13, "Result: ", "$"
minus db "-", "$"
result_str db 0, 0, 0, 0, 0

; 00h - black
; 10h - blue
; 20h - green
; 30h - light blue
; 40h - red
; 50h - purple
; 60h - brown
; 70h - grey
COLOR_background equ 00h
console_length equ 184Fh
CODESEG
Start:
	M_init
	; Очистка консоли
	mov al, 2
	mov ah, 0
	int 10h
	; Вступительное сообщение
	mov dx, offset msg
	mov ah, 09h
	int 21h

	; Считывание ввода
	call ask_for_input

	; Парсим X стринг
	mov si, offset x_str+2
	mov bh, [si-1]
	call string2dec		; Результат в АХ

	cmp bp, 1
	je x_is_negative	; Х < 0
	cmp ax, 0
	je x_is_zero		; X = 0
	jmp x_is_positive	; X > 0

	x_is_negative:			; Х < 0
		call calc_x_neg		; Вызываем процедуру для подсчета значения
		call print_result	; Вызываем процедуру для вывода результата
		jmp fin

	x_is_zero:				; X = 0
		call calc_x_zero	; Вызываем процедуру для подсчета значения
		call print_result	; Вызываем процедуру для вывода результата
		jmp fin

	x_is_positive:			; X > 0
		call calc_x_pos		; Вызываем процедуру для подсчета значения
		call print_result	; Вызываем процедуру для вывода результата
		jmp fin

	fin:
	M_exit

	; =================================== Процедури ===================================
	; ---------------------------------------------------------------------------------
	; Предназначение: Отправка сообщений и считывание ввода из консоли. Просто упрощение читаемого кода
	; Ввод: ---
	; Вывод: ---
	; ---------------------------------------------------------------------------------
	proc ask_for_input
		M_push_all

		mov dx, offset x_msg
		mov ah, 09h
		int 21h
		mov dx, offset x_str
		mov ah, 0ah
		int 21h

		mov dx, offset a_msg
		mov ah, 09h
		int 21h
		mov dx, offset a_str
		mov ah, 0ah
		int 21h

		mov dx, offset b_msg
		mov ah, 09h
		int 21h
		mov dx, offset b_str
		mov ah, 0ah
		int 21h

		M_pop_all
		ret
	endp ask_for_input

	; ---------------------------------------------------------------------------------
	; Предназначение: Парс стринга в десятичное число
	; Вход:
	; BH <- Длинна стринга (1-3)
	; SI <- Адрес начала стринга
	; Выход:
	; AX <- результат, десятичное число
	; BL <- 0, если число положительное; 1, если число отрицательное
	; ---------------------------------------------------------------------------------
	proc string2dec
		mov ax, 0	; Результат
		mov cx, 0	; Буфер для числа
		mov bp, 0
		Str_parser:
			mov al, [si]	; Считываем чар из стринга

			cmp al, 0dh
			je no_error

			; Проверка на минус
			cmp al, "-"
			jne not_a_minus
			call trim_minus
			jmp Str_parser

			not_a_minus:
			sub al, 30h		; Конвертируем чар в цифру
			
			; Проверяем, цифра ли это
			cmp bl, 0
			jb error
			cmp bl, 9
			ja error

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

		; Искусственное ограничение числа до 255
		; Оно необязательно, но я лучше себя заранее обезопашу от возможных трудностей...
		; ...с 2-байтными регистрами в будущем
		cmp ax, 255d
		jna no_error
		; Ашипка и терминация
		error:
		mov ah, 09h
		mov dx, offset err_msg
		int 21h
		M_exit

		no_error:
		mov ax, cx
		ret
	endp string2dec

	; ---------------------------------------------------------------------------------]
	; Предназначение: отрезание минуса в стринге
	; Вход:
	; SI <- Указатель на минус в стринге
	; Выход:
	; BP <- 1
	; BH <- BH-1
	; ---------------------------------------------------------------------------------
	proc trim_minus
		push ax
		push bx
		push si
		push cx

		mov bx, 4		; Количство желанных итераций
		trimmer:
			mov ax, [si+1]		; Следующее число
			mov [si], ax		; Пишем его на 1 байт назад
			inc si				; Движемся дальше
			dec bx				; Проверка на конец стринга
			jnz trimmer

		pop cx
		pop si
		pop bx
		pop ax
		dec bh		; Длинна стринга уменьшилась на 1
		mov bp, 1	; Число отрицательное
		ret
	endp trim_minus
	
	; ---------------------------------------------------------------------------------
	; Предназначение: подсчитывание переменных по формуле "ax^2 - bx"
	; Ввыод: ---
	; Вывод:
	; АХ <- результат подсчета
	; BP <- 0, если результат положительный; 1, если результат отрицательный
	; ---------------------------------------------------------------------------------
	proc calc_x_neg
		mul ax		; x^2
		push ax		; *Stack will remember it*

		; Парсим А стринг
		mov si, offset a_str+2
		mov bh, [si-1]
		call string2dec

		cmp bp, 1
		je X_NEG_a_neg
		jmp X_NEG_a_pos

		X_NEG_a_neg:
			pop cx		; Возвращаем х^2
			mul cx		; -ax^2
			push ax		; *Stack will remember it*

			; Парсим B стринг
			mov si, offset b_str+2
			mov bh, [si-1]
			call string2dec

			cmp bp, 1
			je X_NEG_a_neg_b_neg
			jmp X_NEG_a_neg_b_pos

			X_NEG_a_neg_b_neg:	; -ax^2 - bx
				mov cx, ax

				; Парсим X стринг
				mov si, offset x_str+2
				mov bh, [si-1]
				call string2dec

				mul cx		; bx
				pop ax		; -ax^2
				add ax, cx	; -ax^2 - bx
				jmp X_NEG_res_neg

			X_NEG_a_neg_b_pos:	; -ax^2 + bx
				mov cx, ax

				; Парсим X стринг
				mov si, offset x_str+2
				mov bh, [si-1]
				call string2dec

				mul cx		; bx
				pop ax		; -ax^2
				sub cx, ax	; -ax^2 + bx
				mov ax, cx
				jb X_NEG_res_neg
				jmp X_NEG_res_pos

		X_NEG_a_pos:
			pop cx		; Возвращаем х^2
			mul cx		; ax^2
			push ax		; *Stack will remember it*

			; Парсим B стринг
			mov si, offset b_str+2
			mov bh, [si-1]
			call string2dec

			cmp bp, 1
			je X_NEG_a_pos_b_neg
			jmp X_NEG_a_pos_b_pos

			X_NEG_a_pos_b_neg:	; ax^2 - bx
				mov cx, ax

				; Парсим X стринг
				mov si, offset x_str+2
				mov bh, [si-1]
				call string2dec

				mul cx		; -bx
				pop ax		; ax^2
				sub ax, cx	; ax^2 - bx
				jb X_NEG_res_neg
				jmp X_NEG_res_pos

			X_NEG_a_pos_b_pos:	; ax^2 + bx
				mov cx, ax

				; Парсим X стринг
				mov si, offset x_str+2
				mov bh, [si-1]
				call string2dec

				mul cx		; bx
				pop ax		; ax^2
				add ax, cx	; -ax^2 - bx
				jmp X_NEG_res_pos

		X_NEG_res_neg:
			neg ax
			mov bp, 1
			jmp X_NEG_end
		X_NEG_res_pos:
			mov bp, 1
			jmp X_NEG_end

		X_NEG_end:
		ret
	endp calc_x_neg

	; ---------------------------------------------------------------------------------
	; Предназначение: подсчитывание переменных по формуле "a + 2b"
	; Ввыод: ---
	; Вывод:
	; АХ <- результат подсчета
	; BP <- 0, если результат положительный; 1, если результат отрицательный
	; ---------------------------------------------------------------------------------
	proc calc_x_zero

		; Парсим А стринг
		mov si, offset a_str+2
		mov bh, [si-1]
		call string2dec
		mov cx, ax

		cmp bp, 1
		je X_ZERO_a_neg
		jmp X_ZERO_a_pos

		; A is stored in CX
		; B is stored in AX
		X_ZERO_a_neg:
			; Парсим B стринг
			mov si, offset b_str+2
			mov bh, [si-1]
			call string2dec

			cmp bp, 1
			je X_ZERO_a_neg_b_neg
			jmp X_ZERO_a_neg_b_pos

			X_ZERO_a_neg_b_neg:		; -a - 2b
				; 2b
				mov dl, 2
				mul dl
				; -a - 2b
				add ax, cx
				jmp X_ZERO_result_neg

			X_ZERO_a_neg_b_pos:		; -a + 2b
				; 2b
				mov dl, 2
				mul dl
				; 2b - a
				sub ax, cx
				jb X_ZERO_result_neg
				jmp X_ZERO_result_pos

		X_ZERO_a_pos:
			; Парсим B стринг
			mov si, offset b_str+2
			mov bh, [si-1]
			call string2dec

			cmp bp, 1
			je X_ZERO_a_pos_b_neg
			jmp X_ZERO_a_pos_b_pos

			X_ZERO_a_pos_b_neg:		; a - 2b
				; 2b
				mov dl, 2
				mul dl
				; a - 2b
				sub cx, ax
				mov ax, cx
				jb X_ZERO_result_neg
				jmp X_ZERO_result_pos

			X_ZERO_a_pos_b_pos:		; a + 2b
				; 2b
				mov dl, 2
				mul dl
				; a + 2b
				add ax, cx
				jmp X_ZERO_result_pos

		X_ZERO_result_neg:
			neg ax
			mov bp, 1
			jmp X_ZERO_end
		X_ZERO_result_pos:
			mov bp, 0
			jmp X_ZERO_end

		X_ZERO_end:
		ret
	endp calc_x_zero

	; ---------------------------------------------------------------------------------
	; ---------------------------------------------------------------------------------
	proc calc_x_pos

		ret
	endp calc_x_pos

	; ---------------------------------------------------------------------------------
	; Предназначение: вывод числа на консоль с учетом его знака
	; Ввод:
	; АХ <- число
	; Вывод: ---
	; ---------------------------------------------------------------------------------
	proc print_result
		call number2string

		cmp bp, 1
		je PRINT_neg
		jmp PRINT_pos

		PRINT_neg:
			mov ah, 09h
			mov dx, offset result_msg
			int 21h
			mov dx, offset minus
			int 21h
			mov dx, offset result_str
			int 21h
			jmp PRINT_end

		PRINT_pos:
			mov ah, 09h
			mov dx, offset result_msg
			int 21h
			mov dx, offset result_str
			int 21h
			jmp PRINT_end

		PRINT_end:
		ret
	endp print_result

	; ---------------------------------------------------------------------------------
	; Предназначение: Парс десятичного числа в стринг
	; Ввод:
	; AX <- Число для парса
	; Вывод: ---
	; ---------------------------------------------------------------------------------
	proc number2string
		mov si, offset result_msg	; Ссылка на начало стрина, в который будут писать результат
		mov bl, 0					; 0 для проверки на последний разряд
		; Парсим)
		Num_parser:
			; Смотрим, в каком разряде вы находимся
			cmp ax, 1000d
			ja four_digit
			cmp ax, 100d
			ja three_digit
			cmp ax, 10d
			ja two_digit
			mov cx, 1d
			mov bl, 1	; Вот мы и на последнем разряде!
			jmp num_continue

			four_digit:
			mov cx, 1000d
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