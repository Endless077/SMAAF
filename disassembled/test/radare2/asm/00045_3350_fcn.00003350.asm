            ; CALL XREFS from fcn.00003610 @ 0x4d91, 0x4dac
┌ 229: fcn.00003350 (int64_t arg1, uint32_t arg2);
│           ; arg int64_t arg1 @ rdi
│           ; arg uint32_t arg2 @ rsi
│           0x00003350      55             push rbp
│           0x00003351      4889e5         mov rbp, rsp
│           0x00003354      4154           push r12
│           0x00003356      4189f4         mov r12d, esi               ; arg2
│           0x00003359      53             push rbx
│           0x0000335a      4889fb         mov rbx, rdi                ; arg1
│           0x0000335d      bf0e000000     mov edi, 0xe                ; nl_item item
│           0x00003362      e889f0ffff     call sym.imp.nl_langinfo    ; char *nl_langinfo(nl_item item)
│           0x00003367      4885c0         test rax, rax
│       ┌─< 0x0000336a      7463           je 0x33cf
│       │   0x0000336c      4889c7         mov rdi, rax
│       │   0x0000336f      0fb600         movzx eax, byte [rax]
│       │   0x00003372      84c0           test al, al
│      ┌──< 0x00003374      7459           je 0x33cf
│      ││   0x00003376      83e0df         and eax, 0xffffffdf         ; 4294967263
│      ││   0x00003379      3c55           cmp al, 0x55
│     ┌───< 0x0000337b      7543           jne 0x33c0
│     │││   0x0000337d      0fb64701       movzx eax, byte [rdi + 1]
│     │││   0x00003381      83e0df         and eax, 0xffffffdf         ; 4294967263
│     │││   0x00003384      3c54           cmp al, 0x54
│    ┌────< 0x00003386      7547           jne 0x33cf
│    ││││   0x00003388      0fb64702       movzx eax, byte [rdi + 2]
│    ││││   0x0000338c      83e0df         and eax, 0xffffffdf         ; 4294967263
│    ││││   0x0000338f      3c46           cmp al, 0x46
│   ┌─────< 0x00003391      753c           jne 0x33cf
│   │││││   0x00003393      807f032d       cmp byte [rdi + 3], 0x2d
│  ┌──────< 0x00003397      7536           jne 0x33cf
│  ││││││   0x00003399      807f0438       cmp byte [rdi + 4], 0x38
│ ┌───────< 0x0000339d      7530           jne 0x33cf
│ │││││││   0x0000339f      807f0500       cmp byte [rdi + 5], 0
│ ────────< 0x000033a3      752a           jne 0x33cf
│ │││││││   0x000033a5      803b60         cmp byte [rbx], 0x60
│ │││││││   0x000033a8      488d05cc3100.  lea rax, [0x0000657b]       ; "\u2019"
│ │││││││   0x000033af      488d15d43100.  lea rdx, [0x0000658a]       ; "\u2018"
│ │││││││   0x000033b6      5b             pop rbx
│ │││││││   0x000033b7      480f44c2       cmove rax, rdx
│ │││││││   0x000033bb      415c           pop r12
│ │││││││   0x000033bd      5d             pop rbp
│ │││││││   0x000033be      c3             ret
..
│ │││││││   ; CODE XREF from fcn.00003350 @ 0x337b
│ ││││└───> 0x000033c0      3c47           cmp al, 0x47
│ ││││┌───< 0x000033c2      750b           jne 0x33cf
│ │││││││   0x000033c4      0fb64701       movzx eax, byte [rdi + 1]
│ │││││││   0x000033c8      83e0df         and eax, 0xffffffdf         ; 4294967263
│ │││││││   0x000033cb      3c42           cmp al, 0x42
│ ────────< 0x000033cd      7421           je 0x33f0
│ │││││││   ; XREFS: CODE 0x0000336a  CODE 0x00003374  CODE 0x00003386  
│ │││││││   ; XREFS: CODE 0x00003391  CODE 0x00003397  CODE 0x0000339d  
│ │││││││   ; XREFS: CODE 0x000033a3  CODE 0x000033c2  CODE 0x000033f4  
│ │││││││   ; XREFS: CODE 0x000033fa  CODE 0x00003400  CODE 0x00003406  
│ │││││││   ; XREFS: CODE 0x0000340c  CODE 0x00003420  
│ └└└└└└└─> 0x000033cf      4183fc09       cmp r12d, 9
│           0x000033d3      488d05aa3100.  lea rax, [0x00006584]       ; "'"
│           0x000033da      488d15a13100.  lea rdx, [0x00006582]       ; u"\"'\u07a1e\u80e2\x98\u4247\u3831\u33300\u656d\u6f6d\u7972\u6520\u6878\u7561\u7473\u6465\u2500s\u4f50\u4953X`\u7277\u7469\u2065\u7265\u6f72r\u4e47\u2055\u6f63\u6572\u7475\u6c69s\u6365\u6f68\u2500\u2073\u2528\u2973\u2520\u0a73\u2800\u2943\u5700\u6972\u7474\u6e65\u6220\u2079\u7325\u0a2e\u5700\u6972\u7474\u6e65\u6220\u2079\u7325\u6120"
│           0x000033e1      5b             pop rbx
│           0x000033e2      480f44c2       cmove rax, rdx
│           0x000033e6      415c           pop r12
│           0x000033e8      5d             pop rbp
│           0x000033e9      c3             ret
..
│           ; CODE XREF from fcn.00003350 @ 0x33cd
│ ────────> 0x000033f0      807f0231       cmp byte [rdi + 2], 0x31
│ ────────< 0x000033f4      75d9           jne 0x33cf
│           0x000033f6      807f0338       cmp byte [rdi + 3], 0x38
│ ────────< 0x000033fa      75d3           jne 0x33cf
│           0x000033fc      807f0430       cmp byte [rdi + 4], 0x30
│ ────────< 0x00003400      75cd           jne 0x33cf
│           0x00003402      807f0533       cmp byte [rdi + 5], 0x33
│ ────────< 0x00003406      75c7           jne 0x33cf
│           0x00003408      807f0630       cmp byte [rdi + 6], 0x30
│ ────────< 0x0000340c      75c1           jne 0x33cf
│           0x0000340e      31c9           xor ecx, ecx
│           0x00003410      31d2           xor edx, edx
│           0x00003412      488d35753100.  lea rsi, str.GB18030        ; 0x658e ; "GB18030"
│           0x00003419      e872fdffff     call fcn.00003190
│           0x0000341e      85c0           test eax, eax
│ ────────< 0x00003420      74ad           je 0x33cf
│           0x00003422      803b60         cmp byte [rbx], 0x60
│           0x00003425      488d05533100.  lea rax, [0x0000657f]
│           0x0000342c      488d15533100.  lea rdx, [0x00006586]
│           0x00003433      5b             pop rbx
│           0x00003434      480f44c2       cmove rax, rdx
│           0x00003438      415c           pop r12
│           0x0000343a      5d             pop rbp
└           0x0000343b      c3             ret
