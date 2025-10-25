            ; CALL XREF from fcn.00003350 @ 0x3419
┌ 227: fcn.00003190 (int64_t arg1, int64_t arg2);
│           ; arg int64_t arg1 @ rdi
│           ; arg int64_t arg2 @ rsi
│           0x00003190      4889f8         mov rax, rdi                ; arg1
│           0x00003193      4889f7         mov rdi, rsi                ; arg2
│           0x00003196      0fbef2         movsx esi, dl
│           0x00003199      83ee41         sub esi, 0x41
│           0x0000319c      440fb64007     movzx r8d, byte [rax + 7]
│           ; DATA XREF from fcn.00003350 @ 0x33da
│           0x000031a1      83fe19         cmp esi, 0x19
│       ┌─< 0x000031a4      0f87a6000000   ja 0x3250
│       │   ; DATA XREF from fcn.00003350 @ 0x33d3
│       │   0x000031aa      4183e0df       and r8d, 0xffffffdf         ; 4294967263
│       │   0x000031ae      4138d0         cmp r8b, dl
│      ┌──< 0x000031b1      0f85b9000000   jne 0x3270
│      ││   ; CODE XREF from fcn.00003190 @ 0x325e
│     ┌───> 0x000031b7      0fbed1         movsx edx, cl
│     ╎││   0x000031ba      440fb64008     movzx r8d, byte [rax + 8]
│     ╎││   0x000031bf      83ea41         sub edx, 0x41
│     ╎││   0x000031c2      83fa19         cmp edx, 0x19
│    ┌────< 0x000031c5      0f87ad000000   ja 0x3278
│    │╎││   0x000031cb      4183e0df       and r8d, 0xffffffdf         ; 4294967263
│    │╎││   0x000031cf      4438c1         cmp cl, r8b
│   ┌─────< 0x000031d2      0f8598000000   jne 0x3270
│   ││╎││   ; CODE XREF from fcn.00003190 @ 0x3288
│  ┌──────> 0x000031d8      be01000000     mov esi, 1
│  ╎││╎││   0x000031dd      4839f8         cmp rax, rdi
│ ┌───────< 0x000031e0      7464           je 0x3246
│ │╎││╎││   0x000031e2      ba09000000     mov edx, 9
│ ────────< 0x000031e7      eb24           jmp 0x320d
..
│ │╎││╎││   ; CODE XREF from fcn.00003190 @ 0x3229
│ ────────> 0x000031f0      4183c020       add r8d, 0x20               ; "@"
│ │╎││╎││   0x000031f4      83c620         add esi, 0x20               ; "@"
│ │╎││╎││   0x000031f7      4183fa19       cmp r10d, 0x19
│ ────────< 0x000031fb      7707           ja 0x3204
│ │╎││╎││   0x000031fd      4183c120       add r9d, 0x20               ; "@"
│ │╎││╎││   0x00003201      83c120         add ecx, 0x20               ; "@"
│ │╎││╎││   ; CODE XREFS from fcn.00003190 @ 0x31fb, 0x323b
│ ────────> 0x00003204      4883c201       add rdx, 1
│ │╎││╎││   0x00003208      4038ce         cmp sil, cl
│ ────────< 0x0000320b      7530           jne 0x323d
│ │╎││╎││   ; CODE XREF from fcn.00003190 @ 0x31e7
│ ────────> 0x0000320d      440fb60410     movzx r8d, byte [rax + rdx]
│ │╎││╎││   0x00003212      440fb60c17     movzx r9d, byte [rdi + rdx]
│ │╎││╎││   0x00003217      458d58bf       lea r11d, [r8 - 0x41]
│ │╎││╎││   0x0000321b      4489c6         mov esi, r8d
│ │╎││╎││   0x0000321e      458d51bf       lea r10d, [r9 - 0x41]
│ │╎││╎││   0x00003222      4489c9         mov ecx, r9d
│ │╎││╎││   0x00003225      4183fb19       cmp r11d, 0x19
│ ────────< 0x00003229      76c5           jbe 0x31f0
│ │╎││╎││   0x0000322b      4183fa19       cmp r10d, 0x19
│ ────────< 0x0000322f      7707           ja 0x3238
│ │╎││╎││   0x00003231      4183c120       add r9d, 0x20               ; "@"
│ │╎││╎││   0x00003235      83c120         add ecx, 0x20               ; "@"
│ │╎││╎││   ; CODE XREF from fcn.00003190 @ 0x322f
│ ────────> 0x00003238      4585c0         test r8d, r8d
│ ────────< 0x0000323b      75c7           jne 0x3204
│ │╎││╎││   ; CODE XREF from fcn.00003190 @ 0x320b
│ ────────> 0x0000323d      31f6           xor esi, esi
│ │╎││╎││   0x0000323f      4539c8         cmp r8d, r9d
│ │╎││╎││   0x00003242      400f94c6       sete sil
│ │╎││╎││   ; CODE XREFS from fcn.00003190 @ 0x31e0, 0x3255, 0x327d, 0x3286
│ └───────> 0x00003246      89f0           mov eax, esi
│  ╎││╎││   0x00003248      c3             ret
..
│  ╎││╎││   ; CODE XREF from fcn.00003190 @ 0x31a4
│  ╎││╎│└─> 0x00003250      31f6           xor esi, esi
│  ╎││╎│    0x00003252      4438c2         cmp dl, r8b
│ ────────< 0x00003255      75ef           jne 0x3246
│  ╎││╎│    0x00003257      be01000000     mov esi, 1
│  ╎││╎│    0x0000325c      84d2           test dl, dl
│  ╎││└───< 0x0000325e      0f8553ffffff   jne 0x31b7
│  ╎││ │    0x00003264      89f0           mov eax, esi
│  ╎││ │    0x00003266      c3             ret
..
│  ╎││ │    ; CODE XREFS from fcn.00003190 @ 0x31b1, 0x31d2
│  ╎└──└──> 0x00003270      31f6           xor esi, esi
│  ╎ │      0x00003272      89f0           mov eax, esi
│  ╎ │      0x00003274      c3             ret
..
│  ╎ │      ; CODE XREF from fcn.00003190 @ 0x31c5
│  ╎ └────> 0x00003278      31f6           xor esi, esi
│  ╎        ; DATA XREF from fcn.00003290 @ 0x32f4
│  ╎        0x0000327a      4438c1         cmp cl, r8b
│ ────────< 0x0000327d      75c7           jne 0x3246
│  ╎        0x0000327f      be01000000     mov esi, 1
│  ╎        0x00003284      84c9           test cl, cl
│ ────────< 0x00003286      74be           je 0x3246
└  └──────< 0x00003288      e94bffffff     jmp 0x31d8
