TITLE ЛР_8 
;------------------------------------------------------------------------------
;ЛР  №8
;------------------------------------------------------------------------------
; Архітектура комп'ютера
; Завдання:             Псевдо-графічний інтерфейс
; ВУЗ:                  КНУУ "КПІ"
; Факультет:    ФІОТ
; Курс:                1
; Група:       ІТ-03
;------------------------------------------------------------------------------
; Автор:        Куксюк Іванченко Очкас
; Дата:         27/04/21
;---------------------------------
IDEAL			; Директива - тип Асемблера tasm 
MODEL small		; Директива - тип моделі пам’яті 
STACK 2048		; Директива - розмір стеку 
DATASEG
MENU DB  '/----------------\'
     DB  '| View creators  |'
     DB  '| Beep           |'
     DB  '| Solve equation |'
     DB  '\----------------/' 

HELP_OUT db ' Arrows up/down, ESC - escape, Enter - choose  '
OUTPUT_SIZE=$-HELP_OUT
CREATORS db ' IT-03 Team-4 Kuksiuk Ivanchenko Ochkas        '
EQUATION db ' ((-1-1)*2*2+3)=                               '
EQUATION_SIZE EQU 16
a1 db -1
a2 db 1
a3 db 2
a4 db 2
a5 dw 3

FREQUENCY EQU 20
TIME EQU 1000

MENU_COLOR EQU 0070h
CURRENT_COLOR EQU 0020h
OUTPUT_COLOR EQU 0020h

SYMBOLS_COUNT EQU 18
TOP_ROW EQU  10
BOTTOM_ROW EQU 14
LEFT_COL EQU 27
OUTPUT_ROW EQU 18
MENU_ITEMS EQU 3
CURRENT_ROW DB 1


CODESEG
MACRO M_pushRegisters   ;макрос для запам'ятовування значень регістрів
push ax
push bx
push cx
push dx
push bp
push si
push di
ENDM M_pushRegisters    ;
;--------------------

MACRO M_popRegisters    ;макрос для повернення значень регістрів
pop di
pop si
pop bp
pop dx
pop cx
pop bx
pop ax
ENDM M_popRegisters     ;
;--------------------

MACRO M_drawOut
mov dh, OUTPUT_ROW   ;початок виведення зверху  
mov dl, 0            ;початок виведення зліва  
mov ax, 1300h        ;функція відображення символів 
mov bx, OUTPUT_COLOR ;колір виводу
mov cx, OUTPUT_SIZE  ;кількість символів для відображення
int 10h              ;виклик переривання BIOS
ENDM M_drawOut

;Ввід : немає
;Вивід: немає
PROC clearScreen;процедура очистки екрану
M_pushRegisters ;
;
mov ax, 0600h   ;функція монотонного залиття екрану
mov bh, 30h     ;колір бекграунду
mov cx, 0       ;відступ зліва
mov dx,184Fh    ;dh, dl - кількість зафарбованих рядків, колонок
int 10h         ;переривання BIOS
;
M_popRegisters  ;
ret
ENDP clearScreen
;--------------------

;Ввід : немає
;Вивід: немає
PROC drawMenu   ;процедура виведення меню
M_pushRegisters
;
mov dh, TOP_ROW       ;початок виведення зверху  
mov dl, LEFT_COL      ;початок виведення зліва  
mov ax, 1300h         ;функція відображення символів 
mov bx, MENU_COLOR    ;колір меню
mov cx, SYMBOLS_COUNT ;кількість символів для відображення
xor si,si             ;вибраний рядок

main_loop_1:          ;
lea bp, [MENU+si]     ;вибір рядка для відображення
int 10h               ;виклик переривання BIOS
inc dh                ;збільшення dh
add si, SYMBOLS_COUNT ;збільшення si
cmp dh, BOTTOM_ROW+1  ;перевірка на кінець меню
jne main_loop_1       ;перевірка на кінець меню
;
M_popRegisters
ret
ENDP drawMenu
;--------------------

;Ввід : немає
;Вивід: немає
PROC drawCurrent
M_pushRegisters
;
call drawMenu
mov dh, [CURRENT_ROW]   ;початок виведення зверху
add dh, TOP_ROW         ;
mov dl, LEFT_COL+1      ;початок виведення зліва  
mov cx, SYMBOLS_COUNT-2 ;кількість символів для відображення
mov al,SYMBOLS_COUNT    ;/
mov bl, [CURRENT_ROW]   ;визначення, який пункт буде обрано
mul bl                  ;
mov si, ax              ;\
mov ax, 1300h           ;функція відображення символів 
mov bx, CURRENT_COLOR   ;колір вибраного пункту
lea bp, [MENU+si+1]     ;вибір рядка для відображення
int 10h                 ;виклик переривання BIOS
;
M_popRegisters
ret
ENDP drawCurrent
;--------------------

;Ввід : немає
;Вивід: немає
PROC inputChecker
M_pushRegisters
;
input_loop_1:
mov ah, 10h     ;функція зчитування з клавіатури
int 16h
cmp ah, 50h     ;стрілка вверх
je arrow_up
cmp ah, 48h     ;стрілка вниз
je arrow_down
cmp al, 0Dh     ;Enter
je enter_
cmp al, 1Bh     ;ESC
je escape
jmp input_loop_1; повторення циклу
;
arrow_down:
mov al, [CURRENT_ROW] ;вибір рядка
cmp al, 1             ;перевірка на максимум
je input_loop_1       ;вихід, якщо максимум
dec al
mov [CURRENT_ROW], al ;Зміна теперішнього рядка
call drawCurrent      ;Виведення на екран теперішнього рядка
jmp input_loop_1

arrow_up:
mov al, [CURRENT_ROW] ;вибір рядка
cmp al, MENU_ITEMS    ;перевірка на максимум
je input_loop_1       ;вихід, якщо максимум
inc al
mov [CURRENT_ROW], al ;Зміна теперішнього рядка
call drawCurrent      ;Виведення на екран теперішнього рядка
jmp input_loop_1

enter_:
call procChooser      ;виклик процедури виклику процедур
jmp input_loop_1

escape:               ;Вихід з программи
mov ah, 4Ch
int 21h
M_popRegisters
ret
ENDP inputChecker
;--------------------

;Ввід : немає
;Вивід: немає
PROC procChooser        ;процедура виклику потрібної процедури
M_pushRegisters
;
mov al, [CURRENT_ROW]   ;Перевірка вибранного рядка
cmp al, 1
je item_1
cmp al, 2
je item_2
cmp al, 3
je item_3

item_1:             ;Перший пункт меню
lea bp, [CREATORS]
M_drawOut 
jmp proc_chooser_end

item_2:             ;Другий пункт меню
call sound
jmp proc_chooser_end

item_3:             ;Третій пункт меню
call calc
jmp proc_chooser_end

proc_chooser_end:
;
M_popRegisters
ret
ENDP procChooser

;Ввід : немає
;Вивід: немає
PROC sound
M_pushRegisters
;
in al, 61h       ;одержуємо стан динаміка
push ax          ;зберігаємо стан динаміка
or al, 00000011B ;зміна стану на включений динамік
out 61h, al      ;занесення стану
mov al, FREQUENCY;виставляємо частоту
out 42h, al      ;вмикаємо таймер, що буде подавати імпульси на динамік за заданою частотою
call wait_time   ;виклик процедури очікування
pop ax           ;повернення стану динаміка
and al, 11111100B;зміна стану на виключений динамік
out 61h, al      ;занесення стану
;
M_popRegisters
ret
ENDP sound
;---------------------

;Ввід : немає
;Вивід: немає
PROC wait_time ;процедура очікування, простий перебіг за 2 циклами
M_pushRegisters
;
mov cx, TIME
loop1:             	  
  PUSH cx	             
  MOV  cx,  TIME
  loop2:
     LOOP loop2
  POP  cx
  LOOP loop1
;
M_popRegisters
ret
ENDP wait_time  ;кінець процедури очікування
;---------------------

;Ввід : немає
;Вивід: немає
PROC calc       ;процедура обчислення виразу, та його виводу на екран
mov al, [a1]    ;запис а1 до al
mov ah, [a2]    ;запис а2 до bh
sub al, ah      ;al - ah, результат в al
mov ah, [a3]    ;запис а3 до ah
imul ah         ;ah * al, результат в ax
mov ah, [a4]    ;запис а4 до bx
imul ah         ;ah * al, результат в ax
mov bx, [a5]    ;запис а5 до bx
add ax, bx      ;ax + bx, результат в ax

mov bx, ax      ;заносимо значення ax до bx
neg bx          ;змінюємо знак в регістрі bx
cmp ax, bx      ;порівнюємо значення в ax та bx
jb outer        ;якщо значення нижче(FF-від'ємне, але вище ніж 01-додатнє) пропускаємо minus

minus:      ;
    mov ax, bx  ;беремо додатнє значення    
    mov ah, '-' ;запис знака "-"
    jmp outer   ;вихід
outer:      ;

add al, 30h ;щоб вивід був в ASCII
mov [EQUATION+EQUATION_SIZE], ah  ;занесення значення для виводу
mov [EQUATION+EQUATION_SIZE+1], al  ;занесення значення для виводу
lea bp, [EQUATION]
M_drawOut 

ret
ENDP calc   ;кінець процедури
;---------------------

Start:
mov ax, @data   ;
mov ds, ax      ;ініціалізація датасегменту
mov es, ax      ;
mov al,1
out 42h, al     ;ініціалізація таймера

call clearScreen  ;Виклик очистки екрану
call drawMenu     ;Виклик выдображення меню
call drawCurrent  ;Виклик виведення теперышнього вибраного рядка
lea bp, [HELP_OUT];Виведення помічного тексту
M_drawOut
call inputChecker;Виклик зчитування з клавіатури та обробок

mov ah, 4ch
int 21h
end Start