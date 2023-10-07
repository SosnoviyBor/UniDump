<usize as core::iter::range::Step>::forward_unchecked:
  mov rax, rdi
  add rax, rsi
  ret

core::ptr::drop_in_place<alloc::vec::Vec<i32>>:
  sub rsp, 24
  mov qword ptr [rsp], rdi
  mov rax, qword ptr [rip + <alloc::vec::Vec<T,A> as core::ops::drop::Drop>::drop@GOTPCREL]
  call rax
  jmp .LBB1_3
.LBB1_1:
  mov rdi, qword ptr [rsp]
  mov rax, qword ptr [rip + core::ptr::drop_in_place<alloc::raw_vec::RawVec<i32>>@GOTPCREL]
  call rax
  jmp .LBB1_5
  mov rcx, rax
  mov eax, edx
  mov qword ptr [rsp + 8], rcx
  mov dword ptr [rsp + 16], eax
  jmp .LBB1_1
.LBB1_3:
  mov rdi, qword ptr [rsp]
  call qword ptr [rip + core::ptr::drop_in_place<alloc::raw_vec::RawVec<i32>>@GOTPCREL]
  add rsp, 24
  ret
  mov rax, qword ptr [rip + core::panicking::panic_cannot_unwind@GOTPCREL]
  call rax
  ud2
.LBB1_5:
  mov rdi, qword ptr [rsp + 8]
  call _Unwind_Resume@PLT
  ud2

core::ptr::drop_in_place<alloc::raw_vec::RawVec<i32>>:
  push rax
  call qword ptr [rip + <alloc::raw_vec::RawVec<T,A> as core::ops::drop::Drop>::drop@GOTPCREL]
  pop rax
  ret

core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next:
  push rax
  mov rax, qword ptr [rip + <core::ops::range::Range<T> as core::iter::range::RangeIteratorImpl>::spec_next@GOTPCREL]
  call rax
  pop rcx
  ret

core::slice::<impl [T]>::swap:
  sub rsp, 56
  mov qword ptr [rsp + 8], rdi
  mov qword ptr [rsp + 16], rsi
  mov qword ptr [rsp + 24], rdx
  mov qword ptr [rsp + 32], rcx
  mov qword ptr [rsp + 40], r8
  cmp rdx, rsi
  setb al
  test al, 1
  jne .LBB4_1
  jmp .LBB4_2
.LBB4_1:
  mov rax, qword ptr [rsp + 32]
  mov rcx, qword ptr [rsp + 16]
  mov rdx, qword ptr [rsp + 8]
  mov rsi, qword ptr [rsp + 24]
  shl rsi, 2
  add rdx, rsi
  mov qword ptr [rsp], rdx
  cmp rax, rcx
  setb al
  test al, 1
  jne .LBB4_3
  jmp .LBB4_4
.LBB4_2:
  mov rdx, qword ptr [rsp + 40]
  mov rsi, qword ptr [rsp + 16]
  mov rdi, qword ptr [rsp + 24]
  mov rax, qword ptr [rip + core::panicking::panic_bounds_check@GOTPCREL]
  call rax
  ud2
.LBB4_3:
  mov rax, qword ptr [rsp + 8]
  mov rcx, qword ptr [rsp + 32]
  mov rdx, qword ptr [rsp]
  mov rdi, rcx
  shl rdi, 2
  mov rsi, rax
  add rsi, rdi
  mov edi, dword ptr [rdx]
  mov dword ptr [rsp + 52], edi
  mov esi, dword ptr [rsi]
  mov dword ptr [rdx], esi
  mov edx, dword ptr [rsp + 52]
  mov dword ptr [rax + 4*rcx], edx
  add rsp, 56
  ret
.LBB4_4:
  mov rdx, qword ptr [rsp + 40]
  mov rsi, qword ptr [rsp + 16]
  mov rdi, qword ptr [rsp + 32]
  mov rax, qword ptr [rip + core::panicking::panic_bounds_check@GOTPCREL]
  call rax
  ud2

alloc::alloc::exchange_malloc:
  sub rsp, 40
  mov qword ptr [rsp + 8], rdi
  mov qword ptr [rsp], rsi
  mov rsi, qword ptr [rsp]
  mov rdx, qword ptr [rsp + 8]
  lea rdi, [rip + .L__unnamed_1]
  xor ecx, ecx
  call alloc::alloc::Global::alloc_impl
  mov qword ptr [rsp + 24], rdx
  mov qword ptr [rsp + 16], rax
  mov rdx, qword ptr [rsp + 16]
  xor eax, eax
  mov ecx, 1
  cmp rdx, 0
  cmove rax, rcx
  cmp rax, 0
  jne .LBB5_2
  mov rax, qword ptr [rsp + 16]
  mov qword ptr [rsp + 32], rax
  mov rax, qword ptr [rsp + 32]
  add rsp, 40
  ret
.LBB5_2:
  mov rdi, qword ptr [rsp]
  mov rsi, qword ptr [rsp + 8]
  mov rax, qword ptr [rip + alloc::alloc::handle_alloc_error@GOTPCREL]
  call rax
  ud2

alloc::alloc::Global::alloc_impl:
  sub rsp, 280
  mov al, cl
  mov byte ptr [rsp + 23], al
  mov qword ptr [rsp + 32], rsi
  mov qword ptr [rsp + 40], rdx
  mov rax, qword ptr [rsp + 40]
  mov qword ptr [rsp + 24], rax
  cmp rax, 0
  jne .LBB6_2
  mov rax, qword ptr [rsp + 32]
  mov qword ptr [rsp + 168], rax
  mov rax, qword ptr [rsp + 168]
  mov qword ptr [rsp + 80], rax
  mov rax, qword ptr [rsp + 80]
  mov qword ptr [rsp + 192], rax
  mov qword ptr [rsp + 200], 0
  mov rcx, qword ptr [rsp + 192]
  mov rax, qword ptr [rsp + 200]
  mov qword ptr [rsp + 176], rcx
  mov qword ptr [rsp + 184], rax
  mov rcx, qword ptr [rsp + 176]
  mov rax, qword ptr [rsp + 184]
  mov qword ptr [rsp + 64], rcx
  mov qword ptr [rsp + 72], rax
  mov rcx, qword ptr [rsp + 64]
  mov rax, qword ptr [rsp + 72]
  mov qword ptr [rsp + 48], rcx
  mov qword ptr [rsp + 56], rax
  jmp .LBB6_3
.LBB6_2:
  mov al, byte ptr [rsp + 23]
  test al, 1
  jne .LBB6_5
  jmp .LBB6_4
.LBB6_3:
  mov rax, qword ptr [rsp + 48]
  mov rdx, qword ptr [rsp + 56]
  add rsp, 280
  ret
.LBB6_4:
  mov rcx, qword ptr [rsp + 32]
  mov rax, qword ptr [rsp + 40]
  mov qword ptr [rsp + 112], rcx
  mov qword ptr [rsp + 120], rax
  mov rax, qword ptr [rip + __rust_no_alloc_shim_is_unstable@GOTPCREL]
  mov al, byte ptr [rax]
  mov byte ptr [rsp + 279], al
  mov rdi, qword ptr [rsp + 120]
  mov rax, qword ptr [rsp + 112]
  mov qword ptr [rsp + 216], rax
  mov rsi, qword ptr [rsp + 216]
  call qword ptr [rip + __rust_alloc@GOTPCREL]
  mov qword ptr [rsp + 88], rax
  jmp .LBB6_6
.LBB6_5:
  mov rcx, qword ptr [rsp + 32]
  mov rax, qword ptr [rsp + 40]
  mov qword ptr [rsp + 96], rcx
  mov qword ptr [rsp + 104], rax
  mov rdi, qword ptr [rsp + 104]
  mov rax, qword ptr [rsp + 96]
  mov qword ptr [rsp + 208], rax
  mov rsi, qword ptr [rsp + 208]
  call qword ptr [rip + __rust_alloc_zeroed@GOTPCREL]
  mov qword ptr [rsp + 88], rax
.LBB6_6:
  mov rax, qword ptr [rsp + 88]
  mov qword ptr [rsp + 8], rax
  mov qword ptr [rsp + 232], rax
  mov rax, qword ptr [rsp + 232]
  cmp rax, 0
  sete al
  xor al, -1
  test al, 1
  jne .LBB6_8
  mov qword ptr [rsp + 144], 0
  jmp .LBB6_9
.LBB6_8:
  mov rax, qword ptr [rsp + 8]
  mov qword ptr [rsp + 224], rax
  mov rax, qword ptr [rsp + 224]
  mov qword ptr [rsp + 144], rax
.LBB6_9:
  mov rdx, qword ptr [rsp + 144]
  mov eax, 1
  xor ecx, ecx
  cmp rdx, 0
  cmove rax, rcx
  cmp rax, 0
  jne .LBB6_11
  mov qword ptr [rsp + 136], 0
  jmp .LBB6_12
.LBB6_11:
  mov rax, qword ptr [rsp + 144]
  mov qword ptr [rsp + 136], rax
.LBB6_12:
  mov rdx, qword ptr [rsp + 136]
  xor eax, eax
  mov ecx, 1
  cmp rdx, 0
  cmove rax, rcx
  cmp rax, 0
  jne .LBB6_14
  mov rax, qword ptr [rsp + 136]
  mov qword ptr [rsp + 128], rax
  jmp .LBB6_15
.LBB6_14:
  mov qword ptr [rsp + 128], 0
.LBB6_15:
  mov rdx, qword ptr [rsp + 128]
  xor eax, eax
  mov ecx, 1
  cmp rdx, 0
  cmove rax, rcx
  cmp rax, 0
  jne .LBB6_17
  mov rax, qword ptr [rsp + 24]
  mov rcx, qword ptr [rsp + 128]
  mov qword ptr [rsp + 256], rcx
  mov qword ptr [rsp + 264], rax
  mov rcx, qword ptr [rsp + 256]
  mov rax, qword ptr [rsp + 264]
  mov qword ptr [rsp + 240], rcx
  mov qword ptr [rsp + 248], rax
  mov rcx, qword ptr [rsp + 240]
  mov rax, qword ptr [rsp + 248]
  mov qword ptr [rsp + 152], rcx
  mov qword ptr [rsp + 160], rax
  mov rcx, qword ptr [rsp + 152]
  mov rax, qword ptr [rsp + 160]
  mov qword ptr [rsp + 48], rcx
  mov qword ptr [rsp + 56], rax
  jmp .LBB6_3
.LBB6_17:
  mov qword ptr [rsp + 48], 0
  jmp .LBB6_3

alloc::slice::<impl [T]>::into_vec:
  push rax
  mov rax, rdi
  mov qword ptr [rsp], rax
  call qword ptr [rip + alloc::slice::hack::into_vec@GOTPCREL]
  mov rax, qword ptr [rsp]
  pop rcx
  ret

alloc::slice::hack::into_vec:
  mov rax, rdi
  mov qword ptr [rsp - 96], rsi
  mov qword ptr [rsp - 88], rdx
  mov rsi, qword ptr [rsp - 96]
  mov rcx, qword ptr [rsp - 88]
  mov qword ptr [rsp - 64], rsi
  mov qword ptr [rsp - 56], rcx
  mov rsi, qword ptr [rsp - 64]
  mov rcx, qword ptr [rsp - 56]
  mov qword ptr [rsp - 48], rsi
  mov qword ptr [rsp - 40], rcx
  mov rsi, qword ptr [rsp - 48]
  mov rcx, qword ptr [rsp - 40]
  mov qword ptr [rsp - 80], rsi
  mov qword ptr [rsp - 72], rcx
  mov rsi, qword ptr [rsp - 80]
  mov rcx, qword ptr [rsp - 72]
  mov qword ptr [rsp - 112], rsi
  mov qword ptr [rsp - 104], rcx
  mov rsi, qword ptr [rsp - 112]
  mov rcx, qword ptr [rsp - 104]
  mov qword ptr [rsp - 128], rsi
  mov qword ptr [rsp - 120], rcx
  mov rcx, qword ptr [rsp - 128]
  mov qword ptr [rsp - 8], rcx
  mov rcx, qword ptr [rsp - 8]
  mov qword ptr [rsp - 16], rcx
  mov rcx, qword ptr [rsp - 16]
  mov qword ptr [rsp - 32], rcx
  mov qword ptr [rsp - 24], rdx
  mov rsi, qword ptr [rsp - 32]
  mov rcx, qword ptr [rsp - 24]
  mov qword ptr [rdi], rsi
  mov qword ptr [rdi + 8], rcx
  mov qword ptr [rdi + 16], rdx
  ret

alloc::raw_vec::RawVec<T,A>::current_memory:
  mov qword ptr [rsp - 104], rsi
  mov qword ptr [rsp - 96], rdi
  mov qword ptr [rsp - 88], rdi
  xor eax, eax
  test al, 1
  jne .LBB9_2
  mov rax, qword ptr [rsp - 104]
  cmp qword ptr [rax + 8], 0
  sete al
  and al, 1
  mov byte ptr [rsp - 73], al
  jmp .LBB9_3
.LBB9_2:
  mov byte ptr [rsp - 73], 1
.LBB9_3:
  test byte ptr [rsp - 73], 1
  jne .LBB9_5
  mov rax, qword ptr [rsp - 96]
  mov rcx, qword ptr [rsp - 104]
  mov rdx, qword ptr [rcx + 8]
  shl rdx, 2
  mov qword ptr [rsp - 64], rdx
  mov qword ptr [rsp - 72], 4
  mov rcx, qword ptr [rcx]
  mov qword ptr [rsp - 16], rcx
  mov rcx, qword ptr [rsp - 16]
  mov qword ptr [rsp - 8], rcx
  mov rcx, qword ptr [rsp - 8]
  mov qword ptr [rsp - 24], rcx
  mov rcx, qword ptr [rsp - 24]
  mov qword ptr [rsp - 32], rcx
  mov rcx, qword ptr [rsp - 32]
  mov qword ptr [rsp - 56], rcx
  mov rdx, qword ptr [rsp - 72]
  mov rcx, qword ptr [rsp - 64]
  mov qword ptr [rsp - 48], rdx
  mov qword ptr [rsp - 40], rcx
  mov rcx, qword ptr [rsp - 56]
  mov qword ptr [rax], rcx
  mov rcx, qword ptr [rsp - 48]
  mov qword ptr [rax + 8], rcx
  mov rcx, qword ptr [rsp - 40]
  mov qword ptr [rax + 16], rcx
  jmp .LBB9_6
.LBB9_5:
  mov rax, qword ptr [rsp - 96]
  mov qword ptr [rax + 8], 0
.LBB9_6:
  mov rax, qword ptr [rsp - 88]
  ret

<I as core::iter::traits::collect::IntoIterator>::into_iter:
  mov rdx, rsi
  mov rax, rdi
  ret

<alloc::alloc::Global as core::alloc::Allocator>::deallocate:
  sub rsp, 56
  mov qword ptr [rsp + 8], rsi
  mov qword ptr [rsp + 16], rdx
  mov qword ptr [rsp + 24], rcx
  cmp qword ptr [rsp + 24], 0
  jne .LBB11_2
  jmp .LBB11_3
.LBB11_2:
  mov rdi, qword ptr [rsp + 8]
  mov rcx, qword ptr [rsp + 16]
  mov rax, qword ptr [rsp + 24]
  mov qword ptr [rsp + 32], rcx
  mov qword ptr [rsp + 40], rax
  mov rsi, qword ptr [rsp + 40]
  mov rax, qword ptr [rsp + 32]
  mov qword ptr [rsp + 48], rax
  mov rdx, qword ptr [rsp + 48]
  call qword ptr [rip + __rust_dealloc@GOTPCREL]
.LBB11_3:
  add rsp, 56
  ret

<alloc::vec::Vec<T,A> as core::ops::drop::Drop>::drop:
  mov rcx, qword ptr [rdi]
  mov rax, qword ptr [rdi + 16]
  mov qword ptr [rsp - 16], rcx
  mov qword ptr [rsp - 8], rax
  mov rcx, qword ptr [rsp - 16]
  mov rax, qword ptr [rsp - 8]
  mov qword ptr [rsp - 32], rcx
  mov qword ptr [rsp - 24], rax
  ret

<alloc::vec::Vec<T,A> as core::ops::deref::DerefMut>::deref_mut:
  mov rcx, qword ptr [rdi]
  mov rax, qword ptr [rdi + 16]
  mov qword ptr [rsp - 16], rcx
  mov qword ptr [rsp - 8], rax
  mov rcx, qword ptr [rsp - 16]
  mov rax, qword ptr [rsp - 8]
  mov qword ptr [rsp - 32], rcx
  mov qword ptr [rsp - 24], rax
  mov rax, qword ptr [rsp - 32]
  mov rdx, qword ptr [rsp - 24]
  ret

<alloc::raw_vec::RawVec<T,A> as core::ops::drop::Drop>::drop:
  sub rsp, 40
  mov rsi, rdi
  mov qword ptr [rsp + 8], rsi
  lea rdi, [rsp + 16]
  call qword ptr [rip + alloc::raw_vec::RawVec<T,A>::current_memory@GOTPCREL]
  mov eax, 1
  xor ecx, ecx
  cmp qword ptr [rsp + 24], 0
  cmove rax, rcx
  cmp rax, 1
  jne .LBB14_2
  mov rdi, qword ptr [rsp + 8]
  mov rsi, qword ptr [rsp + 16]
  mov rdx, qword ptr [rsp + 24]
  mov rcx, qword ptr [rsp + 32]
  call <alloc::alloc::Global as core::alloc::Allocator>::deallocate
.LBB14_2:
  add rsp, 40
  ret

<core::ops::range::Range<T> as core::iter::range::RangeIteratorImpl>::spec_next:
  sub rsp, 40
  mov qword ptr [rsp + 16], rdi
  mov rax, qword ptr [rdi]
  cmp rax, qword ptr [rdi + 8]
  jb .LBB15_2
  mov qword ptr [rsp + 24], 0
  jmp .LBB15_3
.LBB15_2:
  mov rax, qword ptr [rsp + 16]
  mov rdi, qword ptr [rax]
  mov qword ptr [rsp + 8], rdi
  mov esi, 1
  call <usize as core::iter::range::Step>::forward_unchecked
  mov rcx, qword ptr [rsp + 16]
  mov rdx, rax
  mov rax, qword ptr [rsp + 8]
  mov qword ptr [rcx], rdx
  mov qword ptr [rsp + 32], rax
  mov qword ptr [rsp + 24], 1
.LBB15_3:
  mov rax, qword ptr [rsp + 24]
  mov rdx, qword ptr [rsp + 32]
  add rsp, 40
  ret

example::bubble_sort:
  sub rsp, 168
  mov qword ptr [rsp + 48], rdi
  mov qword ptr [rsp + 56], rsi
  cmp rsi, 1
  jbe .LBB16_2
  mov rax, qword ptr [rsp + 56]
  mov rcx, rax
  sub rcx, 1
  mov qword ptr [rsp + 40], rcx
  cmp rax, 1
  setb al
  test al, 1
  jne .LBB16_4
  jmp .LBB16_3
.LBB16_2:
  add rsp, 168
  ret
.LBB16_3:
  mov rax, qword ptr [rsp + 40]
  mov qword ptr [rsp + 64], 0
  mov qword ptr [rsp + 72], rax
  mov rdi, qword ptr [rsp + 64]
  mov rsi, qword ptr [rsp + 72]
  call qword ptr [rip + <I as core::iter::traits::collect::IntoIterator>::into_iter@GOTPCREL]
  mov qword ptr [rsp + 80], rax
  mov qword ptr [rsp + 88], rdx
  jmp .LBB16_5
.LBB16_4:
  lea rdi, [rip + str.0]
  lea rdx, [rip + .L__unnamed_2]
  mov rax, qword ptr [rip + core::panicking::panic@GOTPCREL]
  mov esi, 33
  call rax
  ud2
.LBB16_5:
  mov rax, qword ptr [rip + core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next@GOTPCREL]
  lea rdi, [rsp + 80]
  call rax
  mov qword ptr [rsp + 104], rdx
  mov qword ptr [rsp + 96], rax
  cmp qword ptr [rsp + 96], 0
  je .LBB16_2
  mov rax, qword ptr [rsp + 56]
  mov rcx, qword ptr [rsp + 104]
  mov byte ptr [rsp + 119], 0
  mov rdx, rax
  sub rdx, rcx
  mov qword ptr [rsp + 32], rdx
  cmp rax, rcx
  setb al
  test al, 1
  jne .LBB16_8
  mov rax, qword ptr [rsp + 32]
  mov qword ptr [rsp + 120], 1
  mov qword ptr [rsp + 128], rax
  mov rdi, qword ptr [rsp + 120]
  mov rsi, qword ptr [rsp + 128]
  call qword ptr [rip + <I as core::iter::traits::collect::IntoIterator>::into_iter@GOTPCREL]
  mov qword ptr [rsp + 136], rax
  mov qword ptr [rsp + 144], rdx
  jmp .LBB16_9
.LBB16_8:
  lea rdi, [rip + str.0]
  lea rdx, [rip + .L__unnamed_3]
  mov rax, qword ptr [rip + core::panicking::panic@GOTPCREL]
  mov esi, 33
  call rax
  ud2
.LBB16_9:
  mov rax, qword ptr [rip + core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next@GOTPCREL]
  lea rdi, [rsp + 136]
  call rax
  mov qword ptr [rsp + 160], rdx
  mov qword ptr [rsp + 152], rax
  cmp qword ptr [rsp + 152], 0
  jne .LBB16_11
  mov al, byte ptr [rsp + 119]
  xor al, -1
  test al, 1
  jne .LBB16_2
  jmp .LBB16_5
.LBB16_11:
  mov rax, qword ptr [rsp + 160]
  mov qword ptr [rsp + 16], rax
  mov rcx, rax
  sub rcx, 1
  mov qword ptr [rsp + 24], rcx
  cmp rax, 1
  setb al
  test al, 1
  jne .LBB16_13
  mov rax, qword ptr [rsp + 24]
  mov rcx, qword ptr [rsp + 56]
  cmp rax, rcx
  setb al
  test al, 1
  jne .LBB16_14
  jmp .LBB16_15
.LBB16_13:
  lea rdi, [rip + str.0]
  lea rdx, [rip + .L__unnamed_4]
  mov rax, qword ptr [rip + core::panicking::panic@GOTPCREL]
  mov esi, 33
  call rax
  ud2
.LBB16_14:
  mov rax, qword ptr [rsp + 16]
  mov rcx, qword ptr [rsp + 56]
  mov rdx, qword ptr [rsp + 48]
  mov rsi, qword ptr [rsp + 24]
  shl rsi, 2
  add rdx, rsi
  mov qword ptr [rsp + 8], rdx
  cmp rax, rcx
  setb al
  test al, 1
  jne .LBB16_16
  jmp .LBB16_17
.LBB16_15:
  mov rsi, qword ptr [rsp + 56]
  mov rdi, qword ptr [rsp + 24]
  lea rdx, [rip + .L__unnamed_5]
  mov rax, qword ptr [rip + core::panicking::panic_bounds_check@GOTPCREL]
  call rax
  ud2
.LBB16_16:
  mov rcx, qword ptr [rsp + 48]
  mov rdx, qword ptr [rsp + 16]
  mov rax, qword ptr [rsp + 8]
  mov eax, dword ptr [rax]
  cmp eax, dword ptr [rcx + 4*rdx]
  jg .LBB16_18
  jmp .LBB16_9
.LBB16_17:
  mov rsi, qword ptr [rsp + 56]
  mov rdi, qword ptr [rsp + 16]
  lea rdx, [rip + .L__unnamed_6]
  mov rax, qword ptr [rip + core::panicking::panic_bounds_check@GOTPCREL]
  call rax
  ud2
.LBB16_18:
  mov rax, qword ptr [rsp + 16]
  mov rcx, rax
  sub rcx, 1
  mov qword ptr [rsp], rcx
  cmp rax, 1
  setb al
  test al, 1
  jne .LBB16_20
  mov rcx, qword ptr [rsp + 16]
  mov rdx, qword ptr [rsp]
  mov rsi, qword ptr [rsp + 56]
  mov rdi, qword ptr [rsp + 48]
  lea r8, [rip + .L__unnamed_7]
  call qword ptr [rip + core::slice::<impl [T]>::swap@GOTPCREL]
  mov byte ptr [rsp + 119], 1
  jmp .LBB16_9
.LBB16_20:
  lea rdi, [rip + str.0]
  lea rdx, [rip + .L__unnamed_8]
  mov rax, qword ptr [rip + core::panicking::panic@GOTPCREL]
  mov esi, 33
  call rax
  ud2

example::main:
  sub rsp, 72
  mov edi, 40
  mov esi, 4
  call alloc::alloc::exchange_malloc
  mov qword ptr [rsp + 24], rax
  and rax, 3
  cmp rax, 0
  sete al
  test al, 1
  jne .LBB17_1
  jmp .LBB17_2
.LBB17_1:
  mov rsi, qword ptr [rsp + 24]
  mov dword ptr [rsi], 7
  mov dword ptr [rsi + 4], 49
  mov dword ptr [rsi + 8], 73
  mov dword ptr [rsi + 12], 58
  mov dword ptr [rsi + 16], 30
  mov dword ptr [rsi + 20], 72
  mov dword ptr [rsi + 24], 44
  mov dword ptr [rsi + 28], 78
  mov dword ptr [rsi + 32], 23
  mov dword ptr [rsi + 36], 9
  mov rax, qword ptr [rip + alloc::slice::<impl [T]>::into_vec@GOTPCREL]
  lea rdi, [rsp + 32]
  mov qword ptr [rsp], rdi
  mov edx, 10
  call rax
  mov rdi, qword ptr [rsp]
  mov rax, qword ptr [rip + <alloc::vec::Vec<T,A> as core::ops::deref::DerefMut>::deref_mut@GOTPCREL]
  call rax
  mov qword ptr [rsp + 8], rdx
  mov qword ptr [rsp + 16], rax
  jmp .LBB17_5
.LBB17_2:
  mov rsi, qword ptr [rsp + 24]
  lea rdx, [rip + .L__unnamed_9]
  mov rax, qword ptr [rip + core::panicking::panic_misaligned_pointer_dereference@GOTPCREL]
  mov edi, 4
  call rax
  ud2
.LBB17_3:
  mov rax, qword ptr [rip + core::ptr::drop_in_place<alloc::vec::Vec<i32>>@GOTPCREL]
  lea rdi, [rsp + 32]
  call rax
  jmp .LBB17_8
  mov rcx, rax
  mov eax, edx
  mov qword ptr [rsp + 56], rcx
  mov dword ptr [rsp + 64], eax
  jmp .LBB17_3
.LBB17_5:
  mov rsi, qword ptr [rsp + 8]
  mov rdi, qword ptr [rsp + 16]
  mov rax, qword ptr [rip + example::bubble_sort@GOTPCREL]
  call rax
  jmp .LBB17_6
.LBB17_6:
  lea rdi, [rsp + 32]
  call qword ptr [rip + core::ptr::drop_in_place<alloc::vec::Vec<i32>>@GOTPCREL]
  add rsp, 72
  ret
  mov rax, qword ptr [rip + core::panicking::panic_cannot_unwind@GOTPCREL]
  call rax
  ud2
.LBB17_8:
  mov rdi, qword ptr [rsp + 56]
  call _Unwind_Resume@PLT
  ud2

.L__unnamed_1:

.L__unnamed_10:
  .ascii "/app/example.rs"

.L__unnamed_2:
  .quad .L__unnamed_10
  .asciz "\017\000\000\000\000\000\000\000\006\000\000\000\021\000\000"

str.0:
  .ascii "attempt to subtract with overflow"

.L__unnamed_3:
  .quad .L__unnamed_10
  .asciz "\017\000\000\000\000\000\000\000\b\000\000\000\025\000\000"

.L__unnamed_4:
  .quad .L__unnamed_10
  .asciz "\017\000\000\000\000\000\000\000\t\000\000\000\026\000\000"

.L__unnamed_5:
  .quad .L__unnamed_10
  .asciz "\017\000\000\000\000\000\000\000\t\000\000\000\020\000\000"

.L__unnamed_6:
  .quad .L__unnamed_10
  .asciz "\017\000\000\000\000\000\000\000\t\000\000\000 \000\000"

.L__unnamed_8:
  .quad .L__unnamed_10
  .asciz "\017\000\000\000\000\000\000\000\n\000\000\000\034\000\000"

.L__unnamed_7:
  .quad .L__unnamed_10
  .asciz "\017\000\000\000\000\000\000\000\n\000\000\000\027\000\000"

.L__unnamed_9:
  .quad .L__unnamed_10
  .asciz "\017\000\000\000\000\000\000\000\024\000\000\000\023\000\000"

DW.ref.rust_eh_personality:
  .quad rust_eh_personality