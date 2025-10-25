            ; CALL XREFS from fcn.00003610 @ 0x4f07, 0x4f5a
┌ 102: fcn.000035a0 (int64_t arg1);
│           ; arg int64_t arg1 @ rdi
│           0x000035a0      55             push rbp
│           0x000035a1      4889e5         mov rbp, rsp
│           0x000035a4      4155           push r13
│           0x000035a6      4154           push r12
│           0x000035a8      53             push rbx
│           0x000035a9      4889fb         mov rbx, rdi                ; arg1
│           0x000035ac      4883ec08       sub rsp, 8
│           0x000035b0      e81bedffff     call sym.imp.__fpending
│           0x000035b5      448b23         mov r12d, dword [rbx]
│           0x000035b8      4889df         mov rdi, rbx
│           0x000035bb      4989c5         mov r13, rax
│           0x000035be      4183e420       and r12d, 0x20              ; "@"
│           0x000035c2      e8b9feffff     call fcn.00003480
│           0x000035c7      4585e4         test r12d, r12d
│       ┌─< 0x000035ca      7524           jne 0x35f0
│       │   0x000035cc      85c0           test eax, eax
│      ┌──< 0x000035ce      7415           je 0x35e5
│      ││   0x000035d0      4d85ed         test r13, r13
│     ┌───< 0x000035d3      752a           jne 0x35ff
│     │││   0x000035d5      e8c6ecffff     call sym.imp.__errno_location
│     │││   0x000035da      833809         cmp dword [rax], 9
│     │││   0x000035dd      0f95c0         setne al
│     │││   0x000035e0      0fb6c0         movzx eax, al
│     │││   0x000035e3      f7d8           neg eax
│     │││   ; CODE XREFS from fcn.000035a0 @ 0x35ce, 0x3604
│    ┌─└──> 0x000035e5      4883c408       add rsp, 8
│    ╎│ │   0x000035e9      5b             pop rbx
│    ╎│ │   0x000035ea      415c           pop r12
│    ╎│ │   0x000035ec      415d           pop r13
│    ╎│ │   0x000035ee      5d             pop rbp
│    ╎│ │   ; DATA XREF from fcn.00003610 @ 0x2fd6
│    ╎│ │   0x000035ef      c3             ret
│    ╎│ │   ; CODE XREF from fcn.000035a0 @ 0x35ca
│    ╎│ └─> 0x000035f0      85c0           test eax, eax
│    ╎│ ┌─< 0x000035f2      750b           jne 0x35ff
│    ╎│ │   0x000035f4      e8a7ecffff     call sym.imp.__errno_location
│    ╎│ │   0x000035f9      c70000000000   mov dword [rax], 0
│    ╎│ │   ; CODE XREFS from fcn.000035a0 @ 0x35d3, 0x35f2
│    ╎└─└─> 0x000035ff      b8ffffffff     mov eax, 0xffffffff         ; -1
└    └────< 0x00003604      ebdf           jmp 0x35e5
