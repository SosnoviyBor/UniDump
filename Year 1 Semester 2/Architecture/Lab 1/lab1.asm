; -----------------------------------------
; ЛР №1
; -----------------------------------------
; Архітектура комп'ютера
; Завдання: основи розробки та налагодження
; ВУЗ: КНУУ "КПІ"
; Факультет: ФІОТ
; Курс: 1
; Група: ІТ-03
; -----------------------------------------
; Автори:	Букрєєв М.С.
;			Король К.В.
;			Федяй Б.В.
; Дата: 11/02/2021
; -----------------------------------------

;					І. Заголовок програми
IDEAL
MODEL small
STACK 256
;					ІІ. Макроси
;					ІІІ. Початок сегменту даних
DATASEG
exCode db 0
message db "Bukreev, Korol, Fedyay", 10, 13, "$"
;					IV. Початок сегменту коду
CODESEG
Start:
;---------------1. Ініціалізація DS та ES----------------
	mov ax, @data	; @data ідентифікатор, що створюються директивою MODEL
	mov ds, ax		; Завантаження початку сегменту даних в регістр DS
	mov es, ax		; Завантаження початку сегменту даних в регістр ES
;---------------2. Вивід на консоль----------------------
	mov dx, offset message	; Пересилання адреси рядка символів message в регістр DX
	mov ah, 09h
	int 21h					; Виклик преривання 21h (09h - команда виводу рядка на консоль)
;---------------3. Зупинка програми----------------------
	mov ah, 01h		; Завантаження числа 01h до регістру AH 
	int 21h			; Виклик преривання 21h (01h - команда очікування натискання будь-якої клавіші)
;---------------4. Вихід із програми---------------------
	mov ah, 4ch			; Завантаження числа 01h до регістру AH 
	mov al, [exCode]	; Завантаження значення exCode до регістру AL
	int 21h				; Виклик преривання 21h (AH = 4ch, AL = код виходу - команда виходу із програми)
	end Start