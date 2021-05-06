TITLE ЛР_7 
;------------------------------------------------------------------------------
;ЛР  №7
;------------------------------------------------------------------------------
; Архітектура комп'ютера
; Завдання:              Підпрограми
; ВУЗ:                  КНУУ "КПІ"
; Факультет:    ФІОТ
; Курс:                1
; Група:       ІТ-03
;------------------------------------------------------------------------------
; Автор:        Куксюк Іванченко Очкас
; Дата:         18/04/21
;---------------------------------
IDEAL			; Директива - тип Асемблера tasm 
MODEL small		; Директива - тип моделі пам’яті 
STACK 2048		; Директива - розмір стеку 

DATASEG
null db 13,10, '$'

a1 db -1
a2 db 1
a3 db 2
a4 db 2
a5 dw 3

interface_1 db "----Menu from Team 4----",13,10,'$'
interface_2 db "----Press i to count----",13,10,'$'
interface_3 db "----Press O to sound----",13,10,'$'
interface_4 db "----Press p to leave----",13,10,'$'
interface_5 db "------------------------",13,10,'$'
interface_6 db "----Programm  exited----",13,10,'$'

FREQUENCY EQU 20
TIME EQU 3500

input_string db 254

CODESEG
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
mov dl, ah  ;занесення значення для виводу
mov dh, al  ;занесення значення для наступного виводу
mov ah, 02h ;команда виводу байта
int 21h     ;переривання DOS
mov dl, dh  ;вивід наступного значення
int 21h     ;переривання DOS

mov ah,09h      ;команда виводу рядка  
lea dx, [null]  ;вивід пустого рядка
int 21h         ;переривання DOS

ret         ;повернення з процедури
ENDP calc   ;кінець процедури
;---------------------

;Ввід : немає
;Вивід: немає
PROC draw_interface ;Процедура для виводу меню
mov ax,03h      ;команда для очищення консолі
int 10h         ;переривання BIOS
mov ah, 09h     ;команда для виводу на екран
mov dx, offset interface_5
int 21h
mov dx, offset interface_1
int 21h
mov dx, offset interface_5
int 21h
mov dx, offset interface_2
int 21h
mov dx, offset interface_3
int 21h
mov dx, offset interface_4
int 21h
mov dx, offset interface_5
int 21h

ret
ENDP draw_interface
;---------------------

;Ввід : немає
;Вивід: немає
PROC sound
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
 ret
ENDP sound
;---------------------

;Ввід : немає
;Вивід: немає
PROC wait_time ;процедура очікування, простий перебіг за 2 циклами
push cx
mov cx, TIME
loop1:             	  
  PUSH cx	             
  MOV  cx,  TIME
  loop2:
     LOOP loop2
  POP  cx
  LOOP loop1
pop cx
ret
ENDP wait_time  ;кінець процедури очікування
;---------------------

Start:
mov ax, @data   ;
mov ds, ax      ;ініціалізація датасегменту
mov es, ax      ;
mov al,1
out 42h, al     ;ініціалізація таймера

call draw_interface ;виведення меню
ask_cycle:
mov ah, 08h ;команда зчитування з клавіатури
int 21h     ;переривання DOS

cmp al, "i"         ;порівняння вводу та i
je count            ;якщо правильно, то вивести результат
cmp al, "O"         ;порівняння вводу та O
je beep             ;якщо правильно, то beep
cmp al, "p"         ;порівняння вводу та p
je exit             ;якщо правильно, то закрити програму
call draw_interface ;якщо нажато не ту клавішу, оновить меню
jmp ask_cycle       ;повторення головного циклу

count:
call calc       ;запуск процедури обчислення
jmp ask_cycle   ;повернення до зчитування

beep:
call sound      ;запуск процедури звуку
jmp ask_cycle   ;повернення до зчитування

exit:
mov ah, 09h     ;команда для виводу на екран
mov dx, offset interface_6
int 21h
mov ah, 4ch
int 21h

end Start