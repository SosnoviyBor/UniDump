; -----------------------------------------
; ЛР №4
; -----------------------------------------
; Архітектура комп'ютера
; Завдання: Дослідження роботи стека МПС в Архітектурі IA-32(x86) y Real Mode
; ВУЗ: КНУУ "КПІ"
; Факультет: ФІОТ
; Курс: 1
; Група: ІТ-03
; -----------------------------------------
; Автори:	Букрєєв М.С.
;			Король К.В.
;			Федяй Б.В.
; Дата: 11/04/2021
; -----------------------------------------

;					І. Заголовок програми
IDEAL
MODEL small
STACK 1024
;					ІІ. Макроси
MACRO M_init		; Макрос для ініціалізації. Його початок
	mov ax, @data	; @data ідентифікатор, що створюються директивою MODEL
	mov ds, ax		; Завантаження початку сегменту даних в регістр DS
	mov es, ax		; Завантаження початку сегменту даних в регістр ES
	ENDM M_init		; Кінець макросу
task_offset equ 32*1
stack_size equ 1022
arr_stack_length equ 16*16*2
bdates_length equ 8*3*2
;					ІІІ. Початок сегменту даних
DATASEG
arr_stack dw 37167, 48596, 55839, 63386, 8462, 55875, 18690, 1688, 3352, 4771, 14729, 11361, 54492, 54234, 38985, 1071
		  dw 20978, 21470, 17482, 15433, 61852, 11505, 47067, 20837, 8527, 15341, 28476, 15205, 13952, 15401, 35945, 17281
		  dw 54285, 30515, 63510, 48005, 21665, 18785, 63361, 13427, 54259, 47587, 15617, 19627, 60442, 55349, 58526, 47029
		  dw 27365, 40245, 64142, 56994, 36311, 20545, 64249, 13262, 32633, 41116, 42096, 34715, 49071, 47584, 25595, 42763
		  dw 33252, 58578, 17503, 64875, 8098, 32634, 31841, 15246, 44478, 63052, 9391, 45386, 13304, 37323, 41091, 65058
		  dw 4155, 14502, 36943, 15487, 15365, 60698, 4758, 57266, 58522, 19380, 51223, 62593, 28472, 26258, 14636, 19656
		  dw 16256, 53891, 3070, 54532, 34473, 48626, 44415, 31231, 16963, 13485, 16544, 34162, 58612, 56006, 63934, 37365
		  dw 4174, 49729, 62804, 26998, 48782, 55916, 30511, 19394, 62445, 19924, 33836, 50275, 6299, 14145, 40889, 65304
		  dw 1915, 21867, 61887, 37125, 46034, 25427, 54631, 32026, 58190, 26427, 42740, 30177, 56930, 20572, 16049, 55036
		  dw 17638, 60729, 80, 21008, 8837, 24393, 12891, 15874, 15579, 44850, 1360, 49199, 62747, 17529, 62021, 37962
		  dw 50358, 24805, 24216, 1695, 31050, 7589, 16430, 13741, 57474, 27088, 31119, 17169, 43595, 14462, 57694, 50811
		  dw 56714, 12999, 41300, 58899, 19431, 11844, 24943, 5899, 64017, 44974, 58650, 20516, 11639, 19890, 48409, 16689
		  dw 22288, 2016, 64331, 51665, 20405, 47615, 50508, 55867, 39646, 6358, 10589, 50221, 53132, 10689, 12152, 36016
		  dw 37657, 34821, 36179, 43149, 2389, 10119, 17162, 19970, 36118, 19467, 19213, 15295, 47026, 1926, 39736, 10127
		  dw 57598, 10374, 41525, 56556, 22959, 26351, 58066, 10395, 21939, 51921, 51050, 11509, 5847, 63439, 30028, 49306
		  dw 16052, 567, 42989, 34743, 12031, 50373, 17605, 60068, 59810, 14777, 60537, 47272, 4580, 19537, 29119, 6200
arr_stack_copy1 dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
				dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
				dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
				dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
				dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
				dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
				dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
				dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
				dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
				dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
				dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
				dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
				dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
				dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
				dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
				dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
bdates dw 30h,32h,30h,39h,32h,30h,30h,32h
	   dw 31h,39h,31h,31h,32h,30h,30h,32h
	   dw 30h,39h,31h,31h,32h,30h,30h,32h
exCode db 0
;					IV. Початок сегменту коду
CODESEG
Start:
	M_init	; Виклик макросу для ініціалізації
	; -----------------------------------------
	; Визначаємо місце, куди ми будем копіювати наш масив
	mov bx, offset arr_stack
	mov di, offset arr_stack_copy1
	mov cx, arr_stack_length
	; Створюємо копію масиву
	COPYINATOR:
		mov ax, [bx]
		mov [di], ax
		
		inc di
		inc di
		inc bx
		inc bx
		dec cx
		dec cx
		jnz COPYINATOR
	; Записуємо копію масива до стеку (через push)
	mov di, offset arr_stack_copy1
	mov cx, arr_stack_length
	STACK_INSERTER:
		push [di]
		
		inc di
		inc di
		dec cx
		dec cx
		jnz STACK_INSERTER
	; Записуємо до стеку дати народження (через базову адресацію)
	; Користуючись TD визначити значення регістру BP до циклу та після нього (завдання 4)
	mov bp, stack_size-task_offset
	mov bx, offset bdates
	mov cx, bdates_length
	BDATE_INSERTER:
		mov ax, [bx]
		mov [bp], ax
	
		dec bp
		dec bp
		inc bx
		inc bx
		dec cx
		dec cx
		jnz BDATE_INSERTER
	; -----------------------------------------
	mov ah, 4ch			; Завантаження числа 01h до регістру AH 
	mov al, [exCode]	; Завантаження значення exCode до регістру AL
	int 21h				; Виклик преривання 21h (AH = 4ch, AL = код виходу - команда виходу із програми)
	end Start