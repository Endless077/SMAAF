            ; CALL XREFS from fcn.00003610 @ 0x2b80, 0x2b92
┌ 190: fcn.00003290 (int64_t arg1, int64_t arg2);
│           ; arg int64_t arg1 @ rdi
│           ; arg int64_t arg2 @ rsi
│           0x00003290      55             push rbp
│           0x00003291      ba05000000     mov edx, 5
│           0x00003296      4889e5         mov rbp, rsp
│           0x00003299      4155           push r13
│           0x0000329b      4989f5         mov r13, rsi                ; arg2
│           0x0000329e      4889fe         mov rsi, rdi                ; arg1
│           0x000032a1      4154           push r12
│           0x000032a3      4989fc         mov r12, rdi                ; arg1
│           0x000032a6      31ff           xor edi, edi
│           0x000032a8      53             push rbx
│           0x000032a9      4883ec08       sub rsp, 8
│           0x000032ad      e85ef0ffff     call sym.imp.dcgettext
│           0x000032b2      4889c3         mov rbx, rax
│           0x000032b5      4939c4         cmp r12, rax
│       ┌─< 0x000032b8      740e           je 0x32c8
│       │   ; CODE XREFS from fcn.00003290 @ 0x32eb, 0x3349
│     ┌┌──> 0x000032ba      4883c408       add rsp, 8
│     ╎╎│   0x000032be      4889d8         mov rax, rbx
│     ╎╎│   0x000032c1      5b             pop rbx
│     ╎╎│   0x000032c2      415c           pop r12
│     ╎╎│   0x000032c4      415d           pop r13
│     ╎╎│   0x000032c6      5d             pop rbp
│     ╎╎│   0x000032c7      c3             ret
│     ╎╎│   ; CODE XREF from fcn.00003290 @ 0x32b8
│     ╎╎└─> 0x000032c8      bf0e000000     mov edi, 0xe                ; nl_item item
│     ╎╎    0x000032cd      e81ef1ffff     call sym.imp.nl_langinfo    ; char *nl_langinfo(nl_item item)
│     ╎╎    0x000032d2      4885c0         test rax, rax
│     ╎╎┌─< 0x000032d5      7416           je 0x32ed
│     ╎╎│   0x000032d7      803800         cmp byte [rax], 0
│    ┌────< 0x000032da      7411           je 0x32ed
│    │╎╎│   0x000032dc      488d15923200.  lea rdx, str.UTF_8          ; 0x6575 ; "UTF-8"
│    │╎╎│   0x000032e3      4839d0         cmp rax, rdx
│   ┌─────< 0x000032e6      750c           jne 0x32f4
│   ││╎╎│   0x000032e8      4c89eb         mov rbx, r13
│   ││└───< 0x000032eb      ebcd           jmp 0x32ba
│   ││ ╎│   ; CODE XREFS from fcn.00003290 @ 0x32d5, 0x32da
│   │└──└─> 0x000032ed      488d057b3200.  lea rax, str.ASCII          ; 0x656f ; "ASCII"
│   │  ╎    ; CODE XREF from fcn.00003290 @ 0x32e6
│   └─────> 0x000032f4      4c8d057a3200.  lea r8, str.UTF_8           ; 0x6575 ; "UTF-8"
│      ╎┌─< 0x000032fb      eb1e           jmp 0x331b
│      ╎│   ; CODE XREF from fcn.00003290 @ 0x3332
│     ┌───> 0x000032fd      83c720         add edi, 0x20               ; "@"
│     ╎╎│   0x00003300      83c120         add ecx, 0x20               ; "@"
│     ╎╎│   0x00003303      4183f919       cmp r9d, 0x19
│    ┌────< 0x00003307      7706           ja 0x330f
│    │╎╎│   0x00003309      83c620         add esi, 0x20               ; "@"
│    │╎╎│   0x0000330c      83c220         add edx, 0x20               ; "@"
│    │╎╎│   ; CODE XREFS from fcn.00003290 @ 0x3307, 0x3341
│   ┌└────> 0x0000330f      4883c001       add rax, 1
│   ╎ ╎╎│   0x00003313      4983c001       add r8, 1
│   ╎ ╎╎│   0x00003317      38d1           cmp cl, dl
│   ╎┌────< 0x00003319      7528           jne 0x3343
│   ╎│╎╎│   ; CODE XREF from fcn.00003290 @ 0x32fb
│   ╎│╎╎└─> 0x0000331b      0fb638         movzx edi, byte [rax]
│   ╎│╎╎    0x0000331e      410fb630       movzx esi, byte [r8]
│   ╎│╎╎    0x00003322      448d57bf       lea r10d, [rdi - 0x41]
│   ╎│╎╎    0x00003326      89f9           mov ecx, edi
│   ╎│╎╎    0x00003328      448d4ebf       lea r9d, [rsi - 0x41]
│   ╎│╎╎    0x0000332c      89f2           mov edx, esi
│   ╎│╎╎    0x0000332e      4183fa19       cmp r10d, 0x19
│   ╎│└───< 0x00003332      76c9           jbe 0x32fd
│   ╎│ ╎    0x00003334      4183f919       cmp r9d, 0x19
│   ╎│ ╎┌─< 0x00003338      7703           ja 0x333d
│   ╎│ ╎│   0x0000333a      83c620         add esi, 0x20               ; "@"
│   ╎│ ╎│   ; CODE XREF from fcn.00003290 @ 0x3338
│   ╎│ ╎└─> 0x0000333d      89f2           mov edx, esi
│   ╎│ ╎    0x0000333f      85ff           test edi, edi
│   └─────< 0x00003341      75cc           jne 0x330f
│    │ ╎    ; CODE XREF from fcn.00003290 @ 0x3319
│    └────> 0x00003343      39f7           cmp edi, esi
│      ╎    0x00003345      490f44dd       cmove rbx, r13
└      └──< 0x00003349      e96cffffff     jmp 0x32ba
