bubbleSort(int*, int):
  push rbp
  mov rbp, rsp
  sub rsp, 32
  mov QWORD PTR [rbp-24], rdi
  mov DWORD PTR [rbp-28], esi
  mov DWORD PTR [rbp-4], 0
  jmp .L2
.L8:
  mov BYTE PTR [rbp-9], 0
  mov DWORD PTR [rbp-8], 0
  jmp .L3
.L5:
  mov eax, DWORD PTR [rbp-8]
  cdqe
  lea rdx, [0+rax*4]
  mov rax, QWORD PTR [rbp-24]
  add rax, rdx
  mov edx, DWORD PTR [rax]
  mov eax, DWORD PTR [rbp-8]
  cdqe
  add rax, 1
  lea rcx, [0+rax*4]
  mov rax, QWORD PTR [rbp-24]
  add rax, rcx
  mov eax, DWORD PTR [rax]
  cmp edx, eax
  jle .L4
  mov eax, DWORD PTR [rbp-8]
  cdqe
  add rax, 1
  lea rdx, [0+rax*4]
  mov rax, QWORD PTR [rbp-24]
  add rdx, rax
  mov eax, DWORD PTR [rbp-8]
  cdqe
  lea rcx, [0+rax*4]
  mov rax, QWORD PTR [rbp-24]
  add rax, rcx
  mov rsi, rdx
  mov rdi, rax
  call std::enable_if<std::__and_<std::__not_<std::__is_tuple_like<int> >, std::is_move_constructible<int>, std::is_move_assignable<int> >::value, void>::type std::swap<int>(int&, int&)
  mov BYTE PTR [rbp-9], 1
.L4:
  add DWORD PTR [rbp-8], 1
.L3:
  mov eax, DWORD PTR [rbp-28]
  sub eax, DWORD PTR [rbp-4]
  sub eax, 1
  cmp DWORD PTR [rbp-8], eax
  jl .L5
  movzx eax, BYTE PTR [rbp-9]
  test eax, eax
  je .L9
  add DWORD PTR [rbp-4], 1
.L2:
  mov eax, DWORD PTR [rbp-28]
  sub eax, 1
  cmp DWORD PTR [rbp-4], eax
  jl .L8
  jmp .L10
.L9:
  nop
.L10:
  nop
  leave
  ret
main:
  push rbp
  mov rbp, rsp
  sub rsp, 32
  mov DWORD PTR [rbp-32], 64
  mov DWORD PTR [rbp-28], 34
  mov DWORD PTR [rbp-24], 25
  mov DWORD PTR [rbp-20], 12
  mov DWORD PTR [rbp-16], 22
  mov DWORD PTR [rbp-12], 11
  mov DWORD PTR [rbp-8], 90
  mov DWORD PTR [rbp-4], 7
  mov edx, DWORD PTR [rbp-4]
  lea rax, [rbp-32]
  mov esi, edx
  mov rdi, rax
  call bubbleSort(int*, int)
  mov eax, 0
  leave
  ret