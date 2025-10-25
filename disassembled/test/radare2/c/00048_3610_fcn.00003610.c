int fcn.00003610 (int esi, int edx) {
    loc_0x24c0:
        // CODE XREFS from fcn.00003610 @ 0x3797, 0x37b3
        sym.imp.abort  () // [16] -r-x section size 12626 named .text
        0x000024c5
        no
        // DATA XREF from entry0 @ 0x3028
        endbr6
        push  (rbp)
        rbp = rsp
        push  (r15)
        push  (r14)
        r14d = 1
        push  (r13)
        push  (r12)
        r12d = edi
        rdi = rip + 0x4134 // str.POSIXLY_CORRECT
        // 0x6624 // "POSIXLY_CORRECT" // const char *name
        push  (rbx)
        rbx = rsi
        rsp -= 0xa8
        rax = qword fs:[0x28] // elf_shdr
        qword [var_38h_2] = rax
        eax = 0
        sym.imp.getenv  ()
        // char *getenv("POSIXLY_CORRECT")
        r15 = rax
        var = rax & rax
        if  (!var) goto loc_0x2539 // likely
            
    loc_0x2539:
        // CODE XREFS from fcn.00003610 @ 0x2515, 0x251e
        eax = r14d
        r13 = qword [rbx]
        eax &= 1
        byte [var_b8h] = al
        var = r13 & r13
        if  (!var) goto loc_0x2c46 // unlikely
            
    loc_0x2c46:
        // CODE XREF from fcn.00003610 @ 0x254b
        rax = qword [reloc.stderr] // [0x8ff8:8]=0
        edx = 0x37    // '7' // size_t nitems
        esi = 1       // size_t size
        rdi = rip + 0x3cda // str.A_NULL_argv_0__was_passed_through_an_exec_system_call._n
        // 0x6938 // "A NULL argv[0] was passed through an exec system call.\n" // const void *ptr
        rcx = qword [rax] // FILE *stream
        sym.imp.fwrite  ()
        // size_t fwrite(0x61204c4c554e2041, ?, ?, ?)
        sym.imp.abort  ()
         // do {
    loc_0x2c6b:
        // CODE XREF from fcn.00003610 @ 0x261a
        edx = 5       // (pstr 0x00000101) " "
        rsi = rip + 0x3cf9 // str.Usage:__s__SHORT_OPTION_...__STRING_..._n__or:___s_LONG_OPTION_n
        // 0x6970 // "Usage: %s [SHORT-OPTION]... [STRING]...\n  or:  %s LONG-OPTION\n"
        edi = 0
        sym.imp.dcgettext  ()
        rcx = r13
        rdx = r13
        edi = 2
        rsi = rax
        eax = 0
        sym.imp.__printf_chk  ()
        rbx = qword [reloc.stdout] // [0x8fc8:8]=0
        edx = 5       // (pstr 0x00000101) " "
        edi = 0
        rsi = rip + 0x3d08 // str.Echo_the_STRING_s__to_standard_output._n_n___n_____________do_not_output_the_trailing_newline_n
        // 0x69b0 // "Echo the STRING(s) to standard output.\n\n  -n             do not output the trailing newline\n"
        r12 = qword [rbx]
        sym.imp.dcgettext  ()
        rdi = rax
        rsi = r12
        sym.imp.fputs_unlocked  ()
        r12 = qword [rbx]
        edx = 5       // (pstr 0x00000101) " "
        edi = 0
        rsi = rip + 0x3d44 // str.___e_____________enable_interpretation_of_backslash_escapes_n___E_____________disable_interpretation_of_backslash_escapes__default__n
        // 0x6a10 // "  -e             enable interpretation of backslash escapes\n  -E             disable interpretation of backslash escapes (default)\n"
        sym.imp.dcgettext  ()
        rsi = r12
        rdi = rax
        sym.imp.fputs_unlocked  ()
        r12 = qword [rbx]
        edx = 5       // (pstr 0x00000101) " "
        edi = 0
        rsi = rip + 0x3dab // str.________help________display_this_help_and_exit_n
        // 0x6a98 // "      --help        display this help and exit\n"
        sym.imp.dcgettext  ()
        rsi = r12
        rdi = rax
        sym.imp.fputs_unlocked  ()
        r12 = qword [rbx]
        edx = 5       // (pstr 0x00000101) " "
        edi = 0
        rsi = rip + 0x3dba // str.________version_____output_version_information_and_exit_n
        // 0x6ac8 // "      --version     output version information and exit\n"
        sym.imp.dcgettext  () // "\u0201"
        rsi = r12
        rdi = rax
        sym.imp.fputs_unlocked  ()
        r12 = qword [rbx]
        edx = 5       // (pstr 0x00000101) " "
        edi = 0
        rsi = rip + 0x3dd9 // str._nIf__e_is_in_effect__the_following_sequences_are_recognized:_n_n
        // 0x6b08 // "\nIf -e is in effect, the following sequences are recognized:\n\n"
        sym.imp.dcgettext  ()
        rsi = r12
        rdi = rax
        sym.imp.fputs_unlocked  ()
        r12 = qword [rbx]
        edx = 5       // (pstr 0x00000101) " "
        edi = 0
        rsi = rip + 0x3df8 // str.________backslash_n___a______alert__BEL__n___b______backspace_n__c______produce_no_further_output_n__e______escape_n___f______form_feed_n___n______new_line_n___r______carriage_return_n___t______horizontal_tab_n___v______vertical_tab_n
        // 0x6b48 // "  \\      backslash\n  \a      alert (BEL)\n  \b      backspace\n  \c      produce no further output\n  \e      escape\n  \f      form feed\n  \n      new line\n  \r      carriage return\n  \t      horizontal tab\n  \v      vertical tab\n"
        sym.imp.dcgettext  ()
        rsi = r12
        rdi = rax
        sym.imp.fputs_unlocked  ()
        r12 = qword [rbx]
        edx = 5       // (pstr 0x00000101) " "
        edi = 0
        rsi = rip + 0x3ebf // str.__0NNN___byte_with_octal_value_NNN__1_to_3_digits__n__xHH____byte_with_hexadecimal_value_HH__1_to_2_digits__n
        // 0x6c30 // "  \0NNN   byte with octal value NNN (1 to 3 digits)\n  \xHH    byte with hexadecimal value HH (1 to 2 digits)\n"
        sym.imp.dcgettext  ()
        rsi = r12
        r12 = rip + 0x384c // str.echo
        // 0x65cc // "echo"
        rdi = rax
        sym.imp.fputs_unlocked  ()
        edx = 5       // (pstr 0x00000101) " "
        rsi = rip + 0x3f0c // str._nNOTE:_your_shell_may_have_its_own_version_of__s__which_usually_supersedes_nthe_version_described_here.__Please_refer_to_your_shells_documentation_nfor_details_about_the_options_it_supports._n
        // 0x6ca0 // "\nNOTE: your shell may have its own version of %s, which usually supersedes\nthe version described here.  Please refer to your shell's documentation\nfor details about the options it supports.\n"
        edi = 0
        sym.imp.dcgettext  ()
        rdx = r12     // "echo" str.echo
        edi = 2
        rsi = rax
        eax = 0
        sym.imp.__printf_chk  ()
        r13 = qword [rbx]
        edx = 5       // (pstr 0x00000101) " "
        edi = 0
        rsi = rip + 0x3fa2 // str._nNOTE:_printf_1__is_a_preferred_alternative__nwhich_does_not_have_issues_outputting_option_like_strings._n
        // 0x6d60 // "\nNOTE: printf(1) is a preferred alternative,\nwhich does not have issues outputting option-like strings.\n"
        sym.imp.dcgettext  ()
        rsi = r13
        r13 = var_b0h
        rdi = rax
        sym.imp.fputs_unlocked  ()
        rax = rip + 0x3891 // str.test_invocation
        // 0x666d // "test invocation"
        rcx = rip + 0x3888 // "["
        // 0x666b
        // DATA XREF from fcn.00003610 @ 0x37c6
        xmm2 = rax
        xmm0 = rcx
        rax = rip + 0x3889 // str.Multi_call_invocation
        // 0x667d // "Multi-call invocation"
        punpcklqdq xmm0,mm2
        xmm3 = rax
        rax = rip + 0x388f // str.sha224sum
        // 0x6693 // "sha224sum"
        xmmword [var_b0h] = xmm0
        xmm0 = qword [section..data.rel.ro] // [0x8c88:8]=0x65c2 "coreutils"
        punpcklqdq xmm0,mm3
        xmmword [ps] = xmm0
        xmm0 = rax
        rax = rip + 0x3832 // str.sha2_utilities
        // 0x665c // "sha2 utilities"
        xmm1 = rax
        rax = rip + 0x3867 // str.sha256sum
        // 0x669d // "sha256sum"
        punpcklqdq xmm0,mm1
        xmmword [n] = xmm0
        xmm0 = rax
        rax = rip + 0x385a // str.sha384sum
        // 0x66a7 // "sha384sum"
        punpcklqdq xmm0,mm1
        xmmword [var_80h_2] = xmm0
        xmm0 = rax
        rax = rip + 0x3850 // str.sha512sum
        // 0x66b1 // "sha512sum"
        punpcklqdq xmm0,mm1
        xmmword [var_70h_2] = xmm0
        xmm0 = rax
        punpcklqdq xmm0,mm1
        xmmword [var_60h] = xmm0
        xmm0 ^= xmm0
        xmmword [var_50h] = xmm0
        goto loc_0x2e90
         // } while (?);
         // } while (?);
         // } while (?);
        }
        return eax;
        goto loc_0x2517
    loc_0x2520:
        rdi = qword [rbx + 8] // const char *s1
        rsi = rip + 0x4109 // "-n"
        // 0x6634 // const char *s2
        r14d = 0
        sym.imp.strcmp  ()
        // int strcmp(-1, "-n")
        var = eax & eax
        r14b = e
    loc_0x00002566: // orphan
             r8 = rax + 1
             rax = r8
             qword [s1] = r8
             rax -= r13
             var = rax - 6
             if  (var <= 0) goto loc_0x25a1 // likely

    loc_0x0000257d: // orphan
         rdi = rcx - 6            // const char *s1
         edx = 7                  // size_t n
         rsi = rip + 0x40aa       // str._.libs_
                                  // 0x6637 // "/.libs/" // const char *s2
         qword [var_c8h] = rcx
         sym.imp.strncmp  ()
                                  // int strncmp("", "/.libs/", ?)
         var = eax & eax
         if  (!var) goto loc_0x2809 // likely

    loc_0x000025a1: // orphan
         // CODE XREFS from fcn.00003610 @ 0x2564, 0x257b, 0x282a, 0x2845
         rax = qword [reloc.program_invocation_name] // [0x8fd8:8]=0
         rsi = rip + 0x4074       // 0x6623 // const char *locale
         edi = 6                  // int category
         qword [0x00009020] = r13 // [0x9020:8]=0
         qword [rax] = r13
         sym.imp.setlocale  ()
                                  // char *setlocale(0, "")
         rsi = rip + 0x4079       // str._usr_share_locale
                                  // 0x6643 // "/usr/share/locale" // char *dirname
         rdi = rip + 0x3ff1       // "coreutils"
                                  // 0x65c2 // char *domainname
         sym.imp.bindtextdomain  ()
                                  // char *bindtextdomain("coreutils", "/usr/share/locale")
         rdi = rip + 0x3fe5       // "coreutils"
                                  // 0x65c2 // char *domainname
         sym.imp.textdomain  ()
                                  // char *textdomain("coreutils")
         rdi = rip + 0x2907       // 0x4ef0
         fcn.00005600  ()
         var = r12d - 2
         if  (var) goto loc_0x26ec // likely

    loc_0x000025f8: // orphan
         var = byte [var_b8h] - 0
         if  (!var) goto loc_0x26ec // likely

    loc_0x00002605: // orphan
         r12 = qword [rbx + 8]
         rsi = rip + 0x4045       // str.__help
                                  // 0x6655 // "--help" // const char *s2
         rdi = r12                // const char *s1
         sym.imp.strcmp  ()
                                  // int strcmp(-1, "--help")
         var = eax & eax
         if  (!var) goto loc_0x2c6b // likely

    loc_0x00002620: // orphan
         rsi = rip + 0x40ca       // str.__version
                                  // 0x66f1 // "--version" // const char *s2
         rdi = r12                // const char *s1
         sym.imp.strcmp  ()
                                  // int strcmp(-1, "--version")
         var = eax & eax
         if  (!var) goto loc_0x2b76 // likely

    loc_0x00002637: // orphan
         r13 = rbx + 8
         r12d = 1
         var = r14d & r14d
         if  (var) goto loc_0x2709 // unlikely

    loc_0x0000264a: // orphan
         // CODE XREF from fcn.00003610 @ 0x26f7
         r14d = 1
         var = r15 & r15
         if  (!var) goto loc_0x2a8a // likely

    loc_0x00002659: // orphan
         // CODE XREFS from fcn.00003610 @ 0x2bd0, 0x2bdf
         var = r12d & r12d
         if  (var <= 0) goto loc_0x27bd // likely

    loc_0x00002662: // orphan
         // CODE XREFS from fcn.00003610 @ 0x2a7b, 0x2a84
         r12d = r12d
         rax = r13 + r12*8
         r12 = rip + 0x3d9b       // 0x640c
         qword [var_b8h] = rax

    loc_0x00002678: // orphan
         // CODE XREFS from fcn.00003610 @ 0x2a67, 0x2b71
         r15 = qword [r13]
         goto loc_0x26a9

    loc_0x00002680: // orphan
         // CODE XREF from fcn.00003610 @ 0x26bc
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r8d = dl
         r15 = rax

    loc_0x0000268e: // orphan
         // XREFS: CODE 0x00002877  CODE 0x000028b2  CODE 0x0000292c  
         // XREFS: CODE 0x00002946  CODE 0x00002960  CODE 0x0000297a  
         // XREFS: CODE 0x00002994  CODE 0x000029ae  CODE 0x000029c8  
         // XREFS: CODE 0x000029e2  CODE 0x00002b0b  CODE 0x00002b1f  
         // XREFS: CODE 0x00002b33  CODE 0x00002b4d  CODE 0x00002b62  
         // XREFS: CODE 0x00002c3c  
         rdi = qword [rbx]
         rax = qword [rdi + 0x28] // elf_shdr
         var = rax - qword [rdi + 0x30]
         jae 0x2a18               // unlikely

    loc_0x0000269f: // orphan
         // CODE XREF from fcn.00003610 @ 0x2a0b
         rsi = rax + 1
         qword [rdi + 0x28] = rsi
         byte [rax] = dl

    loc_0x000026a9: // orphan
         // CODE XREF from fcn.00003610 @ 0x267c
         edx = byte [r15]
         rax = r15 + 1
         var = dl & dl
         if  (!var) goto loc_0x2a30 // likely

    loc_0x000026b9: // orphan
         // CODE XREF from fcn.00003610 @ 0x2a2a
         var = dl - 0x5c
         if  (var) goto loc_0x2680 // likely

    loc_0x000026be: // orphan
         r9d = byte [r15 + 1]
         var = r9b & r9b
         if  (!var) goto loc_0x29f0 // likely

    loc_0x000026cc: // orphan
         eax = r9 - 0x30
         r10 = r15 + 2
         esi = r9d
         var = al - 0x48
         if  (((unsigned) var) > 0) goto case.0x26e9.56 // case.default.0x26e9 // likely

    loc_0x000026df: // orphan
         eax = al
         rax = dword [r12 + rax*4]
         rax += r12
         goto loc_rax             // switch table (73 cases) at 0x640c

    loc_0x000026ec: // orphan
         // CODE XREFS from fcn.00003610 @ 0x25f2, 0x25ff
         r12d -= 1
         r13 = rbx + 8
         var = r14d & r14d
         if  (!var) goto loc_0x264a // likely

    loc_0x000026fd: // orphan
         r14d = r12d
         var = r12d & r12d
         if  (var <= 0) goto loc_0x27c2 // likely

    loc_0x00002709: // orphan
         // CODE XREF from fcn.00003610 @ 0x2644
         r9 = 0x20100000001       // 2203318222849
         var = r15 & r15
         r12d = r14d
         r14d = 1
         r11b = ne
         r10d = 0

    loc_0x00002726: // orphan
         // CODE XREF from fcn.00003610 @ 0x27b7
         r8 = qword [r13]
         var = byte [r8] - 0x2d
         if  (var) goto loc_0x2bcd // likely

    loc_0x00002734: // orphan
         esi = byte [r8 + 1]
         var = sil & sil
         if  (!var) goto loc_0x2bcd // likely

    loc_0x00002742: // orphan
         rdx = r8 + 2
         eax = esi
         

    loc_0x00002750: // orphan
         // CODE XREF from fcn.00003610 @ 0x2775
         eax -= 0x45
         var = al - 0x29
         if  (((unsigned) var) > 0) goto 0x2a78 // likely

    loc_0x0000275b: // orphan
         bt r9,ax
         setb dil
         var = dil & dil
         if  (!var) goto loc_0x2a78 // likely

    loc_0x0000276c: // orphan
         eax = byte [rdx]
         rdx += 1
         var = al & al
         if  (var) goto loc_0x2750 // unlikely

    loc_0x00002777: // orphan
         rax = r8 + 1
         edx = 0
         goto loc_0x2790

    loc_0x00002780: // orphan
         // CODE XREF from fcn.00003610 @ 0x27a2
         var = sil - 0x45
         if  (!var) r10d = edx

    loc_0x00002788: // orphan
         // CODE XREF from fcn.00003610 @ 0x2a73
         esi = byte [rax]
         var = sil & sil
         if  (!var) goto loc_0x27af // likely

    loc_0x00002790: // orphan
         // CODE XREFS from fcn.00003610 @ 0x277d, 0x27ad
         rax += 1
         var = sil - 0x65
         if  (!var) goto loc_0x2a70 // unlikely

    loc_0x0000279e: // orphan
         var = sil - 0x6e
         if  (var) goto loc_0x2780 // likely

    loc_0x000027a4: // orphan
         esi = byte [rax]
         r14d = 0
         var = sil & sil
         if  (var) goto loc_0x2790 // unlikely

    loc_0x000027af: // orphan
         // CODE XREF from fcn.00003610 @ 0x278e
         r13 += 8
         r12d -= 1
         if  (var) goto loc_0x2726 // likely

    loc_0x000027bd: // orphan
         // CODE XREFS from fcn.00003610 @ 0x265c, 0x2a3e, 0x2a8d, 0x2ac6
         var = r14b & r14b
         if  (!var) goto loc_0x27e5 // case.0x26e9.99 // likely

    loc_0x000027c2: // orphan
         // CODE XREF from fcn.00003610 @ 0x2703
         rax = qword [reloc.stdout] // [0x8fc8:8]=0
         rdi = qword [rax]
         rax = qword [rdi + 0x28]
         var = rax - qword [rdi + 0x30]
         jae 0x2c1e               // unlikely

    loc_0x000027da: // orphan
         rdx = rax + 1
         qword [rdi + 0x28] = rdx
         // DATA XREF from fcn.00003610 @ 0x38fb
         byte [rax] = 0xa

    loc_0x000027e5: // orphan
         // CODE XREFS from fcn.00003610 @ 0x26e9, 0x27c0, 0x2bc8, 0x2c28
         rax = qword [var_38h_2]
         rax -= qword fs:[0x28]
         if  (var) goto loc_0x2c41 // likely

    loc_0x000027f8: // orphan
         rsp = var_28h
         eax = 0                  // (pstr 0x00000000) "\n" // (pstr 0x00000000) "\n"
         rbx = pop  ()
         r12 = pop  ()
         r13 = pop  ()
         r14 = pop  ()
         r15 = pop  ()            // (cstr 0x00000000) "\n" rsp
         rbp = pop  ()            // (cstr 0x00000000) "\n"
         re

    loc_0x00002809: // orphan
         // CODE XREF from fcn.00003610 @ 0x259b
         rdi = qword [s1]         // const char *s1 // (pstr 0x00000000) "\n"
         edx = 3                  // size_t n // (pstr 0x00000000) "\n"
         rsi = rip + 0x3e23       // "lt-"
                                  // 0x663f // const char *s2
         sym.imp.strncmp  ()
                                  // int strncmp("", "lt-", ?)
         r13 = qword [s1]         // (pstr 0x00000000) "\n"
         var = eax & eax          // (pstr 0x00000000) "\n" // (pstr 0x00000000) "\n"
         if  (var) goto loc_0x25a1 // unlikely

    loc_0x00002830: // orphan
         rcx = qword [var_c8h]
         rax = qword [reloc.program_invocation_short_name] // [0x8fe8:8]=0
         r13 = rcx + 4            // (pstr 0x00000000) "\n"
         qword [rax] = r13
         goto loc_0x25a1

    loc_0x0000284a: // orphan
         // CODE XREFS from fcn.00003610 @ 0x26d9, 0x26e9, 0x28e9
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r8d = r9b
         rdi = qword [rbx]
         rax = qword [rdi + 0x28]
         var = rax - qword [rdi + 0x30]
         jae 0x2be4               // unlikely

    loc_0x00002866: // orphan
         rdx = rax + 1
         qword [rdi + 0x28] = rdx
         byte [rax] = 0x5c        // '\\'
                                  // [0x5c:1]=0

    loc_0x00002871: // orphan
         // CODE XREF from fcn.00003610 @ 0x2c19
         edx = r9d
         r15 = r10
         goto loc_0x268e

    loc_0x0000287c: // orphan
         // CODE XREF from fcn.00003610 @ 0x26e9
         esi = byte [r15 + 2]
         eax = rsi - 0x30
         var = al - 7             // (pstr 0x00000000) "\" // (pstr 0x00000000) "\" // (pstr 0x00000000) "\"
         if  (((unsigned) var) > 0) goto 0x2b10 // likely

    loc_0x0000288c: // orphan
         r10 = r15 + 3            // (pstr 0x00000000) "\"

    loc_0x00002890: // orphan
         // CODE XREF from fcn.00003610 @ 0x26e9
         eax = byte [r10]         // (pstr 0x00000000) "\"
         edx = rsi - 0x30
         esi = rax - 0x30         // (pstr 0x00000000) "\"
         var = sil - 7            // (pstr 0x00000000) "\"
         if  (((unsigned) var) <= 0) goto 0x2ae5 // unlikely

    loc_0x000028a4: // orphan
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r8d = dl
         r15 = r10
         goto loc_0x268e

    loc_0x000028b7: // orphan
         // CODE XREF from fcn.00003610 @ 0x26e9
         qword [var_c8h] = r10
         ebx = byte [r15 + 2]
         byte [s1] = r9b
         sym.imp.__ctype_b_loc  ()
         r9d = byte [s1]
         r10 = qword [var_c8h]
         rsi = qword [rax]        // (pstr 0x00000000) "\"
         eax = bl
         var = byte [rsi + rax*2 + 1] & 0x10 // (pstr 0x00000000) "\" // (pstr 0x00000000) "\"
         if  (!var) goto loc_0x284a // case.default.0x26e9 // likely

    loc_0x000028ef: // orphan
         edi = bl
         fcn.00003100  ()         // fcn.00003100(0x0)
         r8d = byte [r15 + 3]
         edx = eax
         rdi = r8
         var = byte [rsi + r8*2 + 1] & 0x10 // (pstr 0x00000000) "\" // (pstr 0x00000000) "\"
         // DATA XREF from fcn.00003610 @ 0x25e2
         if  (!var) goto loc_0x2b24 // likely

    loc_0x0000290d: // orphan
         r8d = eax
         r15 += 4                 // (pstr 0x00000000) "\"
         // DATA XREF from fcn.00003610 @ 0x379d
         fcn.00003100  ()         // fcn.00003100(0x0)
         r8d <<<= 4               // (pstr 0x00000000) "\" // (pstr 0x00000000) "\"
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         edx = r8 + rax
         r8d = dl
         goto loc_0x268e

    loc_0x00002931: // orphan
         // CODE XREF from fcn.00003610 @ 0x26e9
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r15 = r10
         r8d = 0xb                // (pstr 0x00000000) "\"
         edx = 0xb                // (pstr 0x00000000) "\"
         goto loc_0x268e

    loc_0x0000294b: // orphan
         // CODE XREF from fcn.00003610 @ 0x26e9
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r15 = r10
         r8d = 9                  // (pstr 0x00000000) "\"
         edx = 9                  // (pstr 0x00000000) "\"
         goto loc_0x268e

    loc_0x00002965: // orphan
         // CODE XREF from fcn.00003610 @ 0x26e9
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r15 = r10
         r8d = 0xd
         edx = 0xd
         goto loc_0x268e

    loc_0x0000297f: // orphan
         // CODE XREF from fcn.00003610 @ 0x26e9
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r15 = r10
         r8d = 0xa                // (pstr 0x00000000) "\"
         edx = 0xa                // (pstr 0x00000000) "\"
         goto loc_0x268e

    loc_0x00002999: // orphan
         // CODE XREF from fcn.00003610 @ 0x26e9
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r15 = r10
         r8d = 0xc                // (pstr 0x00000000) "\"
         edx = 0xc                // (pstr 0x00000000) "\"
         goto loc_0x268e

    loc_0x000029b3: // orphan
         // CODE XREF from fcn.00003610 @ 0x26e9
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r15 = r10
         r8d = 0x1b               // (pstr 0x00000000) "\"
         edx = 0x1b               // (pstr 0x00000000) "\"
         goto loc_0x268e

    loc_0x000029cd: // orphan
         // CODE XREF from fcn.00003610 @ 0x26e9
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r15 = r10
         r8d = 8                  // (pstr 0x00000000) "\"
         edx = 8                  // (pstr 0x00000000) "\"
         goto loc_0x268e

    loc_0x000029f0: // orphan
         // CODE XREF from fcn.00003610 @ 0x26c6
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r15 = rax
         r8d = 0x5c               // '\\' // (pstr 0x00000000) "\"
         rdi = qword [rbx]        // (pstr 0x00000000) "\"
         rax = qword [rdi + 0x28]
         var = rax - qword [rdi + 0x30] // (pstr 0x00000000) "\"
         if  (((unsigned) var) < 0) goto 0x269f // unlikely

    loc_0x00002a11: // orphan
         

    loc_0x00002a18: // orphan
         // CODE XREF from fcn.00003610 @ 0x2699
         esi = r8d
         sym.imp.__overflow  ()
         edx = byte [r15]         // (pstr 0x00000000) "\"
         rax = r15 + 1            // (pstr 0x00000000) "\"
         var = dl & dl            // (pstr 0x00000000) "\"
         if  (var) goto loc_0x26b9 // likely

    loc_0x00002a30: // orphan
         // CODE XREF from fcn.00003610 @ 0x26b3
         rax = qword [var_b8h]
         r13 += 8                 // (pstr 0x00000000) "\"
         var = r13 - rax
         if  (!var) goto loc_0x27bd // unlikely

    loc_0x00002a44: // orphan
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         rdi = qword [rbx]        // (pstr 0x00000000) "\"
         rax = qword [rdi + 0x28]
         var = rax - qword [rdi + 0x30] // (pstr 0x00000000) "\"
         jae 0x2b67               // likely

    loc_0x00002a5c: // orphan
         rdx = rax + 1            // (pstr 0x00000000) "\"
         qword [rdi + 0x28] = rdx
         byte [rax] = 0x20        // [0x20:1]=64 // "@"
         goto loc_0x2678

    loc_0x00002a70: // orphan
         // CODE XREF from fcn.00003610 @ 0x2798
         r10d = edi
         goto loc_0x2788

    loc_0x00002a78: // orphan
         // CODE XREFS from fcn.00003610 @ 0x2755, 0x2766
         var = r11b & r11b        // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (var) goto loc_0x2662 // unlikely

    loc_0x00002a81: // orphan
         var = r10b & r10b        // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (var) goto loc_0x2662 // unlikely

    loc_0x00002a8a: // orphan
         // CODE XREF from fcn.00003610 @ 0x2653
         var = r12d & r12d        // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (var <= 0) goto loc_0x27bd // likely

    loc_0x00002a93: // orphan
         // CODE XREF from fcn.00003610 @ 0x2bd9
         r12d = r12d
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r12 = r13 + r12*8
         goto loc_0x2ab3

    loc_0x00002aa8: // orphan
         // CODE XREF from fcn.00003610 @ 0x2ad7
         rdx = rax + 1            // (pstr 0x00000000) " "
         qword [rdi + 0x28] = rdx
         byte [rax] = 0x20        // [0x20:1]=64 // "@"

    loc_0x00002ab3: // orphan
         // CODE XREFS from fcn.00003610 @ 0x2aa2, 0x2ae3
         rdi = qword [r13]
         rsi = qword [rbx]
         r13 += 8                 // (pstr 0x00000000) " "
         sym.imp.fputs_unlocked  ()
         var = r13 - r12
         if  (!var) goto loc_0x27bd // unlikely

    loc_0x00002acc: // orphan
         rdi = qword [rbx]
         rax = qword [rdi + 0x28] // elf_phdr
         var = rax - qword [rdi + 0x30] // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (((unsigned) var) < 0) goto 0x2aa8 // unlikely

    loc_0x00002ad9: // orphan
         esi = 0x20               // "@"
         sym.imp.__overflow  ()
         goto loc_0x2ab3

    loc_0x00002ae5: // orphan
         // CODE XREF from fcn.00003610 @ 0x289e
         edx = rax + rdx*8 - 0x30
         eax = byte [r10 + 1]
         eax -= 0x30              // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         var = al - 7             // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (((unsigned) var) > 0) goto 0x2c2d // likely

    loc_0x00002af9: // orphan
         edx = rax + rdx*8
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r15 = r10 + 2            // (pstr 0x00000000) " "
         r8d = dl
         goto loc_0x268e

    loc_0x00002b10: // orphan
         // CODE XREF from fcn.00003610 @ 0x2886
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r15 = r10
         r8d = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         edx = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         goto loc_0x268e

    loc_0x00002b24: // orphan
         // CODE XREF from fcn.00003610 @ 0x2907
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r15 += 3                 // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         r8d = al
         goto loc_0x268e

    loc_0x00002b38: // orphan
         // CODE XREF from fcn.00003610 @ 0x26e9
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r15 = r10
         r8d = 7                  // (pstr 0x00000000) " "
         edx = 7                  // (pstr 0x00000000) " "
         goto loc_0x268e

    loc_0x00002b52: // orphan
         // CODE XREF from fcn.00003610 @ 0x26e9
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r15 = r10
         r8d = 0x5c               // '\\' // (pstr 0x00000000) " "
         goto loc_0x268e

    loc_0x00002b67: // orphan
         // CODE XREF from fcn.00003610 @ 0x2a56
         esi = 0x20               // "@"
         sym.imp.__overflow  ()
         goto loc_0x2678

    loc_0x00002b76: // orphan
         // CODE XREF from fcn.00003610 @ 0x2631
         rdi = rip + 0x3b7e       // str.Chet_Ramey
                                  // 0x66fb // "Chet Ramey"
         rsi = rdi                // "Chet Ramey" str.Chet_Ramey
         fcn.00003290  ()         // fcn.00003290(0x66fb, 0x66fb)
         rdi = rip + 0x3b7a       // str.Brian_Fox
                                  // 0x6706 // "Brian Fox"
         rsi = rdi                // "Brian Fox" str.Brian_Fox
         rbx = rax
         fcn.00003290  ()         // fcn.00003290(0x6706, 0x6706)
         rcx = rip + 0x3b72       // "9.4"
                                  // 0x6710
         r9 = rbx
         rdx = rip + 0x3a16       // str.GNU_coreutils
                                  // 0x65be // "GNU coreutils"
         r8 = rax
         push  (rax)              // (pstr 0x00000000) " "
         rax = qword [reloc.stdout] // [0x8fc8:8]=0
         rsi = rip + 0x3a12       // str.echo
                                  // 0x65cc // "echo"
         push  (0)
         rdi = qword [rax]
         eax = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         fcn.00004f80  ()         // fcn.00004f80(0x20, 0x65cc, 0x65be, 0x6710, 0x0, 0x0, 0x0, 0x0, -1, -1)
         rdx = pop  ()
         rcx = pop  ()            // (pstr 0x00000000) " "
         goto loc_0x27e5          // case.0x26e9.99 // case.0x26e9.99(0x20, 0x65cc, 0x2bc6, 0x0)

    loc_0x00002bcd: // orphan
         // CODE XREFS from fcn.00003610 @ 0x272e, 0x273c
         var = r11b & r11b        // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (var) goto loc_0x2659 // unlikely

    loc_0x00002bd6: // orphan
         var = r10b & r10b        // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x2a93 // likely

    loc_0x00002bdf: // orphan
         goto loc_0x2659

    loc_0x00002be4: // orphan
         // CODE XREF from fcn.00003610 @ 0x2860
         esi = 0x5c               // '\\' // (pstr 0x00000000) " "
         qword [s2] = r10
         dword [var_c8h] = r8d
         byte [s1] = r9b
         sym.imp.__overflow  ()
         r9d = byte [s1]
         r8d = dword [var_c8h]
         r10 = qword [s2]
         goto loc_0x2871

    loc_0x00002c1e: // orphan
         // CODE XREF from fcn.00003610 @ 0x27d4
         esi = 0xa                // (pstr 0x00000000) " "
         sym.imp.__overflow  ()
         goto loc_0x27e5          // case.0x26e9.99 // case.0x26e9.99(0x0, 0xa, 0x0, 0x0)

    loc_0x00002c2d: // orphan
         // CODE XREF from fcn.00003610 @ 0x2af3
         rbx = qword [reloc.stdout] // [0x8fc8:8]=0
         r15 = r10 + 1            // (pstr 0x00000000) " "
         r8d = dl
         goto loc_0x268e

    loc_0x00002c41: // orphan
         // CODE XREF from fcn.00003610 @ 0x27f2
         sym.imp.__stack_chk_fail  ()

    loc_0x00002e80: // orphan
         // CODE XREF from fcn.00003610 @ 0x2e97
         rdi = r12                // const char *s1
         sym.imp.strcmp  ()
                                  // int strcmp(-1, -1)
         var = eax & eax          // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x2e99 // likely

    loc_0x00002e8c: // orphan
         r13 += 0x10

    loc_0x00002e90: // orphan
         // CODE XREF from fcn.00003610 @ 0x2e7e
         rsi = qword [r13]
         var = rsi & rsi
         if  (var) goto loc_0x2e80 // likely

    loc_0x00002e99: // orphan
         // CODE XREF from fcn.00003610 @ 0x2e8a
         r14 = qword [r13 + 8]
         edx = 5                  // (pstr 0x00000000) " "
         rsi = rip + 0x3812       // str._n_s_online_help:___s__n
                                  // 0x66bb // "\n%s online help: <%s>\n"
         edi = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         var = r14 & r14          // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x2f6d // likely

    loc_0x00002eb4: // orphan
         sym.imp.dcgettext  ()
         r13 = rip + 0x3f10       // str.https:__www.gnu.org_software_coreutils_
                                  // 0x6dd0 // "https://www.gnu.org/software/coreutils/"
         edi = 2                  // (pstr 0x00000000) " "
         rdx = rip + 0x36f2       // str.GNU_coreutils
                                  // 0x65be // "GNU coreutils"
         rsi = rax
         rcx = r13                // "https://www.gnu.org/software/coreutils/" str.https:__www.gnu.org_software_coreutils_
         eax = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         sym.imp.__printf_chk  ()
         esi = 0                  // const char *locale // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         edi = 5                  // int category // (pstr 0x00000000) " "
         sym.imp.setlocale  ()    // (pstr 0x00000000) " "
                                  // char *setlocale(0, -1)
         var = rax & rax          // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x2f06 // likely

    loc_0x00002eea: // orphan
         // CODE XREF from fcn.00003610 @ 0x2fa8
         edx = 3                  // size_t n // (pstr 0x00000000) " "
         rsi = rip + 0x37dc       // "en_"
                                  // 0x66d2 // const char *s2
         rdi = rax                // const char *s1
         sym.imp.strncmp  ()
                                  // int strncmp(-1, "en_", ?)
         var = eax & eax          // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (var) goto loc_0x2fe9 // unlikely

    loc_0x00002f06: // orphan
         // CODE XREFS from fcn.00003610 @ 0x2ee8, 0x300a
         edx = 5                  // (pstr 0x00000000) " "
         rsi = rip + 0x37c4       // str.Full_documentation___s_s__n
                                  // 0x66d6 // "Full documentation <%s%s>\n"
         // DATA XREF from fcn.00003100 @ 0x3107
         edi = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         sym.imp.dcgettext  ()
         rcx = r12
         rdx = r13
         edi = 2                  // (pstr 0x00000000) " "
         rsi = rax
         eax = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         rbx = rip + 0x36f3       // 0x6623
         sym.imp.__printf_chk  ()
         var = r14 - r12          // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x2fd6 // likely

    loc_0x00002f3e: // orphan
         // CODE XREF from fcn.00003610 @ 0x2fe4
         edx = 5                  // (pstr 0x00000000) " "
         rsi = rip + 0x3ef6       // str.or_available_locally_via:_info__coreutils___s_s_n
                                  // 0x6e40 // "or available locally via: info '(coreutils) %s%s'\n"
         edi = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         sym.imp.dcgettext  ()
         edi = 2                  // (pstr 0x00000000) " "
         rcx = rbx
         rdx = r14
         rsi = rax
         eax = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         sym.imp.__printf_chk  ()
         edi = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         sym.imp.exit  ()

    loc_0x00002f6d: // orphan
         // CODE XREF from fcn.00003610 @ 0x2eae
         sym.imp.dcgettext  ()
         r13 = rip + 0x3e57       // str.https:__www.gnu.org_software_coreutils_
                                  // 0x6dd0 // "https://www.gnu.org/software/coreutils/"
         rdx = rip + 0x363e       // str.GNU_coreutils
                                  // 0x65be // "GNU coreutils"
         edi = 2                  // (pstr 0x00000000) " "
         rsi = rax
         rcx = r13                // "https://www.gnu.org/software/coreutils/" str.https:__www.gnu.org_software_coreutils_
         r14 = rip + 0x363a       // str.echo
                                  // 0x65cc // "echo"
         eax = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         sym.imp.__printf_chk  ()
         esi = 0                  // const char *locale // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         edi = 5                  // int category // (pstr 0x00000000) " "
         sym.imp.setlocale  ()
                                  // char *setlocale(0, -1)
         var = rax & rax          // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (var) goto loc_0x2eea // unlikely

    loc_0x00002fae: // orphan
         edx = 5                  // (pstr 0x00000000) " "
         rsi = rip + 0x371c       // str.Full_documentation___s_s__n
                                  // 0x66d6 // "Full documentation <%s%s>\n"
         edi = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         sym.imp.dcgettext  ()
         rcx = r12
         rdx = r13
         edi = 2                  // (pstr 0x00000000) " "
         rsi = rax
         eax = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         sym.imp.__printf_chk  ()

    loc_0x00002fd6: // orphan
         // CODE XREF from fcn.00003610 @ 0x2f38
         r14 = rip + 0x35ef       // str.echo
                                  // 0x65cc // "echo"
         rbx = rip + 0x36a3       // " invocation"
                                  // 0x6687
         goto loc_0x2f3e

    loc_0x00002fe9: // orphan
         // CODE XREF from fcn.00003610 @ 0x2f00
         rbx = qword [rbx]
         edi = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         edx = 5                  // (pstr 0x00000000) " "
         rsi = rip + 0x3dfe       // str.Report_any_translation_bugs_to__https:__translationproject.org_team___n
                                  // 0x6df8 // "Report any translation bugs to <https://translationproject.org/team/>\n"
         sym.imp.dcgettext  ()
         rdi = rax
         rsi = rbx
         sym.imp.fputs_unlocked  ()
         goto loc_0x2f06

    loc_0x00003610: // orphan
           // CALL XREF from fcn.00003610 @ 0x46d6
         push  (rbp)
         esi = 0                  // const char *locale // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         edi = 0                  // int category // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         rbp = rsp
         push  (rbx)              // (pstr 0x00000000) " "
         rsp -= 0x118             // (cstr 0x00000000) " " // (pstr 0x00000000) " "
         rax = qword fs:[0x28]    // (pstr 0x00000000) " "
         qword [var_18h] = rax
         eax = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         sym.imp.setlocale  ()    // (cstr 0x00000000) " "
                                  // char *setlocale(-1, -1)
         var = rax & rax          // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x364c // likely

    loc_0x00003639: // orphan
         rdi = rax                // const char *s
         rbx = rax
         sym.imp.strlen  ()
                                  // size_t strlen(-1)
         var = rax - 0x100        // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (((unsigned) var) <= 0) goto 0x3670 // likely

    loc_0x0000364c: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3637, 0x36b7
         eax = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "

    loc_0x0000364e: // orphan
         // CODE XREF from fcn.00003610 @ 0x36ae
         rdx = qword [var_18h]
         rdx -= qword fs:[0x28]
         if  (var) goto loc_0x371a // likely

    loc_0x00003661: // orphan
         rbx = qword [var_8h]     // "H="
         leav                     // (cstr 0x00000000) " " rsp // (cstr 0x00000000) " "
         re

    loc_0x00003670: // orphan
         // CODE XREF from fcn.00003610 @ 0x364a
         r8 = var_120h            // (cstr 0x00000000) " "
         rax += 1                 // (pstr 0x00000000) " "
         rdi = r8                 // (cstr 0x00000000) " "
         var = eax - 8            // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         jae 0x3700               // unlikely

    loc_0x00003683: // orphan
         edx = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         var = al & 4             // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (var) goto loc_0x36f0 // unlikely

    loc_0x00003689: // orphan
         // CODE XREF from fcn.00003610 @ 0x3712
         var = al & 2             // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (var) goto loc_0x36d8 // unlikely

    loc_0x0000368d: // orphan
         // CODE XREF from fcn.00003610 @ 0x36fb
         var = al & 1             // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (var) goto loc_0x36c0 // unlikely

    loc_0x00003691: // orphan
         // CODE XREF from fcn.00003610 @ 0x36e6
         var = byte [var_120h] - 0x43 // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x36b0 // unlikely

    loc_0x0000369a: // orphan
         // CODE XREFS from fcn.00003610 @ 0x36b9, 0x36ce
         rsi = rip + 0x2f09       // str.POSIX
                                  // 0x65aa // "POSIX" // const char *s2
         rdi = r8                 // const char *s1
         sym.imp.strcmp  ()       // (pstr 0x00003644) "H="
                                  // int strcmp(-1, "POSIX")
         var = eax & eax          // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         al = ne
         goto loc_0x364e

    loc_0x000036b0: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3698, 0x36d0
         var = byte [var_11fh] - 0 // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x364c // likely

    loc_0x000036b9: // orphan
         goto loc_0x369a

    loc_0x000036c0: // orphan
         // CODE XREFS from fcn.00003610 @ 0x368f, 0x36e8
         eax = byte [rbx + rdx]
         byte [rdi + rdx] = al
         var = byte [var_120h] - 0x43 // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (var) goto loc_0x369a // likely

    loc_0x000036d0: // orphan
         goto loc_0x36b0

    loc_0x000036d8: // orphan
         // CODE XREFS from fcn.00003610 @ 0x368b, 0x36fd
         ecx = word [rbx + rdx]
         word [rdi + rdx] = cx
         rdx += 2                 // (pstr 0x00000000) " "
         var = al & 1             // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x3691 // likely

    loc_0x000036e8: // orphan
         goto loc_0x36c0

    loc_0x000036f0: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3687, 0x3718
         edx = dword [rbx]
         // DATA XREF from fcn.00003610 @ 0x2ec5
         dword [rdi] = edx
         edx = 4                  // (pstr 0x00000000) " "
         var = al & 2             // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x368d // likely

    loc_0x000036fd: // orphan
         goto loc_0x36d8

    loc_0x00003700: // orphan
         // CODE XREF from fcn.00003610 @ 0x3681
         ecx = eax
         rsi = rbx
         edx = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         ecx >>>= 3               // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         rep movsq qword [rdi],word ptr [rsi]
         rbx = rsi
         var = al & 4             // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x3689 // likely

    loc_0x00003718: // orphan
         goto loc_0x36f0

    loc_0x0000371a: // orphan
         // CODE XREF from fcn.00003610 @ 0x365b
         sym.imp.__stack_chk_fail  ()
         no
         push  (rbp)
         r11 = rsi
         rbp = rsp
         push  (r15)              // (pstr 0x00000000) " "
         push  (r14)
         push  (r13)              // (cstr 0x00000000) " "
         push  (r12)              // (cstr 0x00000000) " "
         push  (rbx)              // (cstr 0x00000000) " "
         rsp -= 0xc8              // (cstr 0x00000000) " " // (pstr 0x00000000) " "
         qword [var_80h] = r9
         r14 = qword [var_10h]
         r9 = 0xffffffffffffffff
         qword [var_70h] = rdx
         r15 = qword [var_18h_2]
         dword [var_bch] = r8d
         r13 = r14
         r14 = r9
         r9 = rdi
         rax = qword fs:[0x28]    // (pstr 0x00000000) " "
         qword [var_38h] = rax
         eax = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         dword [var_5ch] = ecx

    loc_0x00003770: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3c75, 0x4e36
         qword [var_68h] = r11
         qword [var_58h] = r9
         sym.imp.__ctype_get_mb_cur_max  ()
         ebx = dword [var_bch]
         qword [var_d0h] = rax
         eax = dword [var_5ch]
         ebx &= 2                 // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         byte [var_5dh] = ne
         var = eax - 0xa          // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (((unsigned) var) > 0) goto section..text // unlikely

    loc_0x0000379d: // orphan
         rsi = rip + 0x2914       // 0x60b8
         r9 = qword [var_70h_2]
         r11 = qword [var_80h_2]
         rax = dword [rsi + rax*4]
         rax += rsi               // case.0x37b3.0 // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         goto loc_rax             // switch table (11 cases) at 0x60b8 // case.0x37b3.0

    loc_0x000037c0: // orphan
         // CODE XREF from fcn.00003610 @ 0x37b3
         var = dword [var_5ch_3] - 0xa // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         // DATA XREF from fcn.00003610 @ 0x2f0b
         if  (!var) goto loc_0x382a // unlikely

    loc_0x000037c6: // orphan
         r12 = rip + 0x2de3       // "`"
                                  // 0x65b0
         edi = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         edx = 5                  // (pstr 0x00000000) " "
         qword [var_80h_2] = r11
         rsi = r12                // "`"
         qword [var_70h_2] = r9
         sym.imp.dcgettext  ()
         r9 = qword [var_70h_2]
         r11 = qword [var_80h_2]
         var = rax - r12          // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         r13 = rax
         if  (!var) goto loc_0x4da6 // unlikely

    loc_0x000037f8: // orphan
         // CODE XREF from fcn.00003610 @ 0x4dbc
         r12 = rip + 0x2d85       // "'"
                                  // 0x6584
         edi = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         edx = 5                  // (pstr 0x00000000) " "
         qword [var_80h_2] = r11
         rsi = r12                // "'"
         qword [var_70h_2] = r9
         sym.imp.dcgettext  ()
         r9 = qword [var_70h_2]
         r11 = qword [var_80h_2]
         var = rax - r12          // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         r15 = rax
         if  (!var) goto loc_0x4d8b // unlikely

    loc_0x0000382a: // orphan
         // CODE XREFS from fcn.00003610 @ 0x37c4, 0x4da1
         qword [var_70h_2] = 0
         // DATA XREF from fcn.00003610 @ 0x2e23
         var = ebx & ebx          // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x4cce // likely

    loc_0x0000383a: // orphan
         // CODE XREFS from fcn.00003610 @ 0x4cd5, 0x4cfb
         rdi = r15                // const char *s
         qword [var_90h_2] = r11
         qword [ps] = r9
         sym.imp.strlen  ()
                                  // size_t strlen(-1)
         // DATA XREF from fcn.00003610 @ 0x2e5a
         byte [var_80h_2] = 1
         r9 = qword [ps]
         qword [n] = rax
         r11 = qword [var_90h_2]
         qword [s2] = r15
         byte [var_78h] = 0
         byte [var_5eh_2] = 0
         qword [var_c8h_2] = 0
         byte [var_5fh_2] = 1
         

    loc_0x00003888: // orphan
         // XREFS: DATA 0x00002ddc  CODE 0x00003ed6  CODE 0x00003f31  
         // XREFS: CODE 0x00003f70  CODE 0x00003fc3  CODE 0x0000400c  
         // XREFS: CODE 0x00004055  CODE 0x00004af1  CODE 0x00004d3d  
         ebx = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         

    loc_0x00003890: // orphan
         // CODE XREFS from fcn.00003610 @ 0x39fb, 0x4b41
         var = rbx - r14          // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         r10b = ne
         var = r14 - 0xffffffffffffffff // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (var) goto loc_0x38a9 // likely

    loc_0x0000389d: // orphan
         rax = qword [s]
         var = byte [rax + rbx] - 0
         r10b = ne                // (pstr 0x00000000) " "

    loc_0x000038a9: // orphan
         // CODE XREF from fcn.00003610 @ 0x389b
         var = r10b & r10b        // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x4769 // likely

    loc_0x000038b2: // orphan
         var = dword [var_5ch_3] - 2 // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         rdi = qword [s]
         al = ne                  // (pstr 0x00000000) " "
         al &= byte [var_5fh_2]   // (pstr 0x00000000) " "
         var = qword [n] - 0      // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         r8d = eax                // (pstr 0x00000000) " "
         al = ne
         rcx = rdi + rbx
         al &= r8b                // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         r12d = eax
         if  (var) goto loc_0x4080 // unlikely

    loc_0x000038db: // orphan
         esi = byte [rcx]
         var = sil - 0x3f         // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (var > 0) goto loc_0x4490 // unlikely

    loc_0x000038e8: // orphan
         var = sil & sil          // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         js case.0x419a.1         // unlikely

    loc_0x000038f1: // orphan
         var = sil - 0x3f         // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (((unsigned) var) > 0) goto case.0x419a.1 // unlikely

    loc_0x000038fb: // orphan
         rdi = rip + 0x27e2       // 0x60e4
         eax = sil
         rax = dword [rdi + rax*4]
         rax += rdi               // case.0x390d.0 // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         goto loc_rax             // switch table (64 cases) at 0x60e4 // case.0x390d.0

    loc_0x00003910: // orphan
         // CODE XREF from fcn.00003610 @ 0x390d
         var = dword [var_5ch_3] - 2 // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         esi = 0xc                // (pstr 0x00000000) " "
         eax = 0x66               // 'f'
         dl = e
         

    loc_0x00003928: // orphan
         // XREFS: CODE 0x00003cbd  CODE 0x00003e0a  CODE 0x00003e79  
         // XREFS: CODE 0x000041c0  CODE 0x0000423f  CODE 0x00004287  
         // XREFS: CODE 0x000043ac  CODE 0x00004428  CODE 0x0000444b  
         var = byte [var_5fh_2] - 0
         if  (var) goto loc_0x3c98 // likely

    loc_0x00003932: // orphan
         // XREFS: CODE 0x00003c8f  CODE 0x00003e4b  CODE 0x0000419a  
         // XREFS: CODE 0x00004313  CODE 0x0000451c  CODE 0x000047d0  
         // XREFS: CODE 0x00004802  CODE 0x00004867  CODE 0x00004871  
         // XREFS: CODE 0x00004c55  
         r10d = 0                 // (pstr 0x00000000) " " // (pstr 0x00000000) " "

    loc_0x00003935: // orphan
         // XREFS: CODE 0x0000390d  CODE 0x00003adb  CODE 0x00003c3f  
         // XREFS: CODE 0x00003c49  CODE 0x00003cf2  CODE 0x00003d01  
         // XREFS: CODE 0x00003dad  CODE 0x000044b8  
         eax = r8d
         al |= byte [var_5dh_3]   // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x3a18 // likely

    loc_0x00003941: // orphan
         // XREFS: CODE 0x00003d92  CODE 0x00003e34  CODE 0x000041a9  
         // XREFS: CODE 0x00004261  CODE 0x000042ad  CODE 0x00004304  
         // XREFS: CODE 0x000043ee  CODE 0x0000440e  CODE 0x0000447f  
         // XREFS: CODE 0x00004bf8  CODE 0x00004c2f  CODE 0x00004dd9  
         eax = 0                  // (pstr 0x00000000) " " // (pstr 0x00000000) " "

    loc_0x00003943: // orphan
         // CODE XREFS from fcn.00003610 @ 0x422e, 0x4c77
         rcx = qword [var_80h_3]
         var = rcx & rcx          // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x3a18 // likely

    loc_0x00003950: // orphan
         edx = esi
         dl >>>= 5                // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         edx = dl
         edx = dword [rcx + rdx*4]
         ecx = esi
         edx >>>= cl
         edx &= 1                 // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x3a18 // likely

    loc_0x00003968: // orphan
         var = dword [var_5ch_3] - 2 // (pstr 0x00000000) " " // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         dl = e

    loc_0x0000396f: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3a22, 0x43c8, 0x4437, 0x445a, 0x4469
         var = byte [var_5dh_3] - 0 // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (var) goto loc_0x3ca7 // unlikely

    loc_0x00003979: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3ca1, 0x41cf, 0x424e, 0x4276, 0x4296
         eax = byte [var_5eh_2]
         eax ^= 1                 // (pstr 0x00000000) " "
         al &= dl                 // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         if  (!var) goto loc_0x39c0 // likely

    loc_0x00003984: // orphan
         rdi = qword [var_70h_2]
         var = rdi - r11          // (pstr 0x00000000) " " // (pstr 0x00000000) " "
         jae 0x3992               // likely

    loc_0x0000398d: // orphan
         byte [r9 + rdi] = 0x27   // '''
                                  // [0x27:1]=0

    loc_0x00003992: // orphan
         // CODE XREF from fcn.00003610 @ 0x398b
         rcx = qword [var_70h_2]
         rdx = rcx + 1            // (pstr 0x00000000) "'"
         var = rdx - r11
         jae 0x39a5               // likely

    loc_0x0000399f: // orphan
         byte [r9 + rcx + 1] = 0x24 // '$'
                                  // [0x24:1]=0

    loc_0x000039a5: // orphan
         // CODE XREF from fcn.00003610 @ 0x399d
         rdi = qword [var_70h_2]
         rdx = rdi + 2            // (pstr 0x00000000) "'$"
         var = rdx - r11
         jae 0x39b8               // likely

    loc_0x000039b2: // orphan
         byte [r9 + rdi + 2] = 0x27 // '''
                                  // [0x27:1]=0

    loc_0x000039b8: // orphan
         // CODE XREF from fcn.00003610 @ 0x39b0
         qword [var_70h_2] += 3
         byte [var_5eh_2] = al

    loc_0x000039c0: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3982, 0x487f
         rax = qword [var_70h_2]  // (pstr 0x00000000) "'$'"
         var = rax - r11
         jae 0x39ce               // likely

    loc_0x000039c9: // orphan
         byte [r9 + rax] = 0x5c   // '\\'
                                  // [0x5c:1]=0

    loc_0x000039ce: // orphan
         // CODE XREF from fcn.00003610 @ 0x39c7
         qword [var_70h_2] += 1
         rbx += 1

    loc_0x000039d7: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3a34, 0x3a60, 0x4bbf
         rax = qword [var_70h_2]  // (pstr 0x00000000) "\$'"
         var = rax - r11
         jae 0x39e4               // likely

    loc_0x000039e0: // orphan
         byte [r9 + rax] = sil

    loc_0x000039e4: // orphan
         // CODE XREF from fcn.00003610 @ 0x39de
         eax = byte [var_80h_2]
         qword [var_70h_2] += 1
         edi = 0
         var = r10b & r10b
         if  (!var) eax = edi
         byte [var_80h_2] = al
         goto loc_0x3890

    loc_0x00003a00: // orphan
         // CODE XREF from fcn.00003610 @ 0x41f1
         qword [var_70h_2] = rcx
         r12d = eax
         esi = 0x30               // '0'
         eax = r10d
         r10d = 0
         // DATA XREF from fcn.00003610 @ 0x2bb3
         

    loc_0x00003a18: // orphan
         // XREFS: CODE 0x0000393b  CODE 0x0000394a  CODE 0x00003962  
         // XREFS: CODE 0x00003d98  CODE 0x00003e3a  CODE 0x000041af  
         // XREFS: CODE 0x00004267  CODE 0x000042b3  CODE 0x0000430a  
         // XREFS: CODE 0x000043f4  CODE 0x00004414  CODE 0x00004485  
         // XREFS: CODE 0x00004c35  CODE 0x00004ddf  
         var = dword [var_5ch_3] - 2
         dl = e
         var = r12b & r12b
         if  (var) goto loc_0x396f // unlikely

    loc_0x00003a28: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3df4, 0x4398, 0x4824, 0x4c08
         eax ^= 1
         rbx += 1
         al &= byte [var_5eh_2]

    loc_0x00003a32: // orphan
         // CODE XREFS from fcn.00003610 @ 0x44ed, 0x4b6b
         var = al & al
         if  (!var) goto loc_0x39d7 // likely

    loc_0x00003a36: // orphan
         rax = qword [var_70h_2]
         var = rax - r11
         jae 0x3a44               // likely

    loc_0x00003a3f: // orphan
         byte [r9 + rax] = 0x27   // '''
                                  // [0x27:1]=0

    loc_0x00003a44: // orphan
         // CODE XREF from fcn.00003610 @ 0x3a3d
         rcx = qword [var_70h_2]
         rax = rcx + 1
         var = rax - r11
         jae 0x3a57               // likely

    loc_0x00003a51: // orphan
         byte [r9 + rcx + 1] = 0x27 // '''
                                  // [0x27:1]=0

    loc_0x00003a57: // orphan
         // CODE XREF from fcn.00003610 @ 0x3a4f
         qword [var_70h_2] += 2
         byte [var_5eh_2] = 0
         goto loc_0x39d7

    loc_0x00003a68: // orphan
         // CODE XREFS from fcn.00003610 @ 0x42d0, 0x42da, 0x42f2, 0x453e
         r12d = 0
         

    loc_0x00003a70: // orphan
         // XREFS: CODE 0x000038eb  CODE 0x000038f5  CODE 0x0000390d  
         // XREFS: CODE 0x00004178  CODE 0x00004182  CODE 0x0000419a  
         // XREFS: CODE 0x0000449a  CODE 0x0000483e  CODE 0x00004dc9  
         var = qword [var_d0h_3] - 1
         if  (var) goto loc_0x45b0 // likely

    loc_0x00003a7e: // orphan
         // CODE XREF from fcn.00003610 @ 0x45a7
         qword [var_b8h] = r11
         qword [var_b0h] = r9
         byte [var_90h_2] = sil
         byte [ps] = r8b
         sym.imp.__ctype_b_loc  ()
         r8d = byte [ps]
         r9 = qword [var_b0h]
         rdx = rax
         eax = byte [var_90h_2]
         r11 = qword [var_b8h]
         rdx = qword [rdx]
         rsi = rax
         var = byte [rdx + rax*2 + 1] & 0x40
         eax = 1
         r10b = ne
         dl = e
         dl &= byte [var_5fh_2]

    loc_0x00003ad9: // orphan
         // CODE XREF from fcn.00003610 @ 0x4764
         var = dl & dl
         if  (!var) goto loc_0x3935 // case.0x390d.58 // likely

    loc_0x00003ae1: // orphan
         edx = byte [var_5fh_2]
         r10d = 0

    loc_0x00003ae8: // orphan
         // CODE XREF from fcn.00003610 @ 0x475e
         byte [var_b8h] = r10b
         r8 = qword [var_70h_2]
         rcx = rbx + rax
         edi = 0
         qword [ps] = r14
         r10d = byte [var_5eh_2]
         qword [var_90h_2] = r13
         r14 = qword [s]
         qword [var_b0h] = r15
         r13d = byte [var_5dh_3]
         r15d = dword [var_5ch_3]
         goto loc_0x3bd6

    loc_0x00003b28: // orphan
         // CODE XREF from fcn.00003610 @ 0x3bd8
         var = r15d - 2
         al = e
         var = r13b & r13b
         if  (var) goto loc_0x4b70 // unlikely

    loc_0x00003b38: // orphan
         edi = r10d
         edi ^= 1
         al &= dil
         if  (!var) goto loc_0x3b72 // likely

    loc_0x00003b43: // orphan
         var = r8 - r11
         jae 0x3b4d               // likely

    loc_0x00003b48: // orphan
         byte [r9 + r8] = 0x27    // '''
                                  // [0x27:1]=0

    loc_0x00003b4d: // orphan
         // CODE XREF from fcn.00003610 @ 0x3b46
         rdi = r8 + 1
         var = rdi - r11
         jae 0x3b5c               // likely

    loc_0x00003b56: // orphan
         byte [r9 + r8 + 1] = 0x24 // '$'
                                  // [0x24:1]=0

    loc_0x00003b5c: // orphan
         // CODE XREF from fcn.00003610 @ 0x3b54
         rdi = r8 + 2
         var = rdi - r11
         jae 0x3b6b               // likely

    loc_0x00003b65: // orphan
         byte [r9 + r8 + 2] = 0x27 // '''
                                  // [0x27:1]=0

    loc_0x00003b6b: // orphan
         // CODE XREF from fcn.00003610 @ 0x3b63
         r8 += 3                  // (pstr 0x00000000) "'$'"
         r10d = eax

    loc_0x00003b72: // orphan
         // CODE XREFS from fcn.00003610 @ 0x2b97, 0x3b41
         var = r8 - r11
         jae 0x3b7c               // likely

    loc_0x00003b77: // orphan
         byte [r9 + r8] = 0x5c    // '\\'
                                  // [0x5c:1]=0

    loc_0x00003b7c: // orphan
         // CODE XREF from fcn.00003610 @ 0x3b75
         rax = r8 + 1
         var = rax - r11
         jae 0x3b92               // likely

    loc_0x00003b85: // orphan
         eax = esi
         al >>>= 6
         eax += 0x30              // (pstr 0x00000000) "\$'"
         byte [r9 + r8 + 1] = al

    loc_0x00003b92: // orphan
         // CODE XREF from fcn.00003610 @ 0x3b83
         rax = r8 + 2
         var = rax - r11
         jae 0x3bab               // likely

    loc_0x00003b9b: // orphan
         eax = esi
         al >>>= 3
         eax &= 7
         eax += 0x30              // (pstr 0x00000000) "\0'"
         byte [r9 + r8 + 2] = al

    loc_0x00003bab: // orphan
         // CODE XREF from fcn.00003610 @ 0x3b99
         esi &= 7
         rbx += 1
         r8 += 3                  // (pstr 0x00000000) "\00"
         esi += 0x30              // (pstr 0x00000000) "\00"
         var = rbx - rcx
         jae 0x4b9a               // likely

    loc_0x00003bc2: // orphan
         edi = edx

    loc_0x00003bc4: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3c31, 0x4c65
         var = r8 - r11
         jae 0x3bcd               // likely

    loc_0x00003bc9: // orphan
         byte [r9 + r8] = sil

    loc_0x00003bcd: // orphan
         // CODE XREF from fcn.00003610 @ 0x3bc7
         esi = byte [r14 + rbx]
         r8 += 1

    loc_0x00003bd6: // orphan
         // CODE XREF from fcn.00003610 @ 0x3b20
         var = dl & dl
         if  (var) goto loc_0x3b28 // unlikely

    loc_0x00003bde: // orphan
         eax = edi
         eax ^= 1
         eax &= r10d
         var = r12b & r12b
         if  (!var) goto loc_0x3bf9 // likely

    loc_0x00003beb: // orphan
         var = r8 - r11
         jae 0x3bf5               // likely

    loc_0x00003bf0: // orphan
         byte [r9 + r8] = 0x5c    // '\\'
                                  // [0x5c:1]=0

    loc_0x00003bf5: // orphan
         // CODE XREF from fcn.00003610 @ 0x3bee
         r8 += 1

    loc_0x00003bf9: // orphan
         // CODE XREF from fcn.00003610 @ 0x3be9
         rbx += 1
         var = rbx - rcx
         jae 0x4b46               // likely

    loc_0x00003c06: // orphan
         var = al & al
         if  (!var) goto loc_0x4c62 // likely

    loc_0x00003c0e: // orphan
         var = r8 - r11
         jae 0x3c18               // likely

    loc_0x00003c13: // orphan
         byte [r9 + r8] = 0x27    // '''
                                  // [0x27:1]=0

    loc_0x00003c18: // orphan
         // CODE XREF from fcn.00003610 @ 0x3c11
         rax = r8 + 1
         var = rax - r11
         jae 0x3c27               // likely

    loc_0x00003c21: // orphan
         byte [r9 + r8 + 1] = 0x27 // '''
                                  // [0x27:1]=0

    loc_0x00003c27: // orphan
         // CODE XREF from fcn.00003610 @ 0x3c1f
         r8 += 2
         r12d = 0
         r10d = 0
         goto loc_0x3bc4

    loc_0x00003c38: // orphan
         // CODE XREFS from fcn.00003610 @ 0x390d, 0x44c3
         r10d = 0

    loc_0x00003c3b: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3e51, 0x3e5b, 0x4b95
         var = dword [var_5ch_3] - 2
         if  (var) goto loc_0x3935 // case.0x390d.58 // likely

    loc_0x00003c45: // orphan
         var = byte [var_5dh_3] - 0
         if  (!var) goto loc_0x3935 // case.0x390d.58 // likely

    loc_0x00003c4f: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3e7f, 0x4784
         dword [var_5ch_3] = 2

    loc_0x00003c56: // orphan
         // XREFS: CODE 0x00003caa  CODE 0x00003db7  CODE 0x000044d7  
         // XREFS: CODE 0x00004814  CODE 0x000049e9  CODE 0x00004b88  
         var = byte [var_5fh_2] - 0
         eax = 4                  // (pstr 0x00000000) "''0"
         if  (!var) eax = dword [var_5ch_3]
         dword [var_5ch_3] = eax

    loc_0x00003c66: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3d34, 0x4162, 0x4581, 0x4e23
         dword [var_bch_2] &= 0xfffffffd // [0xfffffffd:4]=-1 // 4294967293
         qword [var_80h_3] = 0
         goto loc_0x3770

    loc_0x00003c7a: // orphan
         // CODE XREF from fcn.00003610 @ 0x390d
         var = dword [var_5ch_3] - 2
         esi = 8                  // (pstr 0x00000000) "''0"
         eax = 0x62               // 'b' // (pstr 0x00000000) "''0"
         dl = e
         var = byte [var_5fh_2] - 0
         if  (!var) goto loc_0x3932 // unlikely

    loc_0x00003c95: // orphan
         

    loc_0x00003c98: // orphan
         // CODE XREF from fcn.00003610 @ 0x392c
         r10d = 0
         var = byte [var_5dh_3] - 0
         esi = eax
         if  (!var) goto loc_0x3979 // likely

    loc_0x00003ca7: // orphan
         // CODE XREF from fcn.00003610 @ 0x3973
         byte [var_5fh_2] &= dl
         goto loc_0x3c56

    loc_0x00003cac: // orphan
         // CODE XREF from fcn.00003610 @ 0x390d
         var = dword [var_5ch_3] - 2
         esi = 0xb                // (pstr 0x00000000) "''0"
         eax = 0x76               // 'v'
         dl = e
         goto loc_0x3928

    loc_0x00003cc2: // orphan
         // CODE XREF from fcn.00003610 @ 0x390d
         var = dword [var_5ch_3] - 2
         if  (!var) goto loc_0x4810 // unlikely

    loc_0x00003ccc: // orphan
         // CODE XREF from fcn.00003610 @ 0x419a
         var = dword [var_5ch_3] - 5
         if  (var) goto loc_0x43e0 // likely

    loc_0x00003cd6: // orphan
         // CODE XREF from fcn.00003610 @ 0x43d4
         var = byte [var_bch_2] & 4
         if  (!var) goto loc_0x43e0 // likely

    loc_0x00003ce3: // orphan
         rax = rbx + 2
         r10d = 0
         esi = 0x3f               // '?'
         var = rax - r14
         jae case.0x390d.37       // case.0x390d.58 // likely

    loc_0x00003cf8: // orphan
         rdx = qword [s]
         var = byte [rdx + rbx + 1] - 0x3f
         if  (var) goto loc_0x3935 // case.0x390d.58 // likely

    loc_0x00003d07: // orphan
         esi = byte [rdx + rax]
         var = sil - 0x3e
         if  (((unsigned) var) > 0) goto 0x4dce // unlikely

    loc_0x00003d15: // orphan
         rdx = 0x7000a38200000000 // 8070630310989004800
         bt rdx,si
         setb r10b
         var = r10b & r10b
         if  (!var) goto loc_0x4dce // likely

    loc_0x00003d30: // orphan
         var = byte [var_5dh_3] - 0
         if  (var) goto loc_0x3c66 // unlikely

    loc_0x00003d3a: // orphan
         rbx = qword [var_70h_2]
         var = rbx - r11
         jae 0x3d48               // likely

    loc_0x00003d43: // orphan
         byte [r9 + rbx] = 0x3f   // '?'
                                  // [0x3f:1]=0

    loc_0x00003d48: // orphan
         // CODE XREF from fcn.00003610 @ 0x3d41
         rbx = qword [var_70h_2]
         rdx = rbx + 1            // (pstr 0x00000000) "?'0"
         var = rdx - r11
         jae 0x3d5b               // likely

    loc_0x00003d55: // orphan
         byte [r9 + rbx + 1] = 0x22 // '\"'
                                  // [0x22:1]=0

    loc_0x00003d5b: // orphan
         // CODE XREF from fcn.00003610 @ 0x3d53
         rbx = qword [var_70h_2]
         rdx = rbx + 2            // (pstr 0x00000000) "?\"0"
         var = rdx - r11
         jae 0x3d6e               // likely

    loc_0x00003d68: // orphan
         byte [r9 + rbx + 2] = 0x22 // '\"'
                                  // [0x22:1]=0

    loc_0x00003d6e: // orphan
         // CODE XREF from fcn.00003610 @ 0x3d66
         rbx = qword [var_70h_2]
         rdx = rbx + 3            // (pstr 0x00000000) "?\"\""
         var = rdx - r11
         jae 0x3d81               // likely

    loc_0x00003d7b: // orphan
         byte [r9 + rbx + 3] = 0x3f // '?'
                                  // [0x3f:1]=0

    loc_0x00003d81: // orphan
         // CODE XREF from fcn.00003610 @ 0x3d79
         rbx = rax
         qword [var_70h_2] += 4   // "\"\"?"
         r10d = 0                 // "\"\"?" // "\"\"?"
         eax = r8d
         al |= byte [var_5dh_3]   // "\"\"?" // "\"\"?"
         if  (var) goto loc_0x3941 // unlikely

    loc_0x00003d98: // orphan
         goto loc_0x3a18

    loc_0x00003da0: // orphan
         // CODE XREF from fcn.00003610 @ 0x390d
         var = dword [var_5ch_3] - 2
         byte [var_78h] = r10b
         esi = 0x27               // '''
         if  (var) goto loc_0x3935 // case.0x390d.58 // likely

    loc_0x00003db3: // orphan
         var = byte [var_5dh_3] - 0 // "\"\"?" // "\"\"?"
         if  (var) goto loc_0x3c56 // unlikely

    loc_0x00003dbd: // orphan
         var = r11 & r11          // "\"\"?" // "\"\"?"
         if  (!var) goto loc_0x4af6 // likely

    loc_0x00003dc6: // orphan
         edx = 0                  // "\"\"?" // "\"\"?"
         var = qword [var_c8h_2] - 0 // "\"\"?" // "\"\"?"
         if  (var) goto loc_0x4af6 // unlikely

    loc_0x00003dd6: // orphan
         // CODE XREF from fcn.00003610 @ 0x4b38
         qword [var_c8h_2] = r11
         eax = 0                  // "\"\"?" // "\"\"?"
         r11 = rdx
         esi = 0x27               // '''
         qword [var_70h_2] += 3   // "\"\"?"
         byte [var_78h] = r10b
         byte [var_5eh_2] = 0
         goto loc_0x3a28

    loc_0x00003df9: // orphan
         // CODE XREF from fcn.00003610 @ 0x390d
         var = dword [var_5ch_3] - 2
         esi = 7                  // (pstr 0x00000000) "?\"\"?"
         eax = 0x61               // 'a' // (pstr 0x00000002) "\"?"
         dl = e
         goto loc_0x3928

    loc_0x00003e0f: // orphan
         // CODE XREF from fcn.00003610 @ 0x390d
         var = byte [var_5fh_2] - 0 // "\"\"?" // "\"\"?"
         if  (var) goto loc_0x4320 // unlikely

    loc_0x00003e19: // orphan
         var = byte [var_bch_2] & 1 // "\"\"?" // "\"\"?"
         if  (var) goto loc_0x4b3d // unlikely

    loc_0x00003e26: // orphan
         r12d = 0                 // "\"\"?" // "\"\"?"
         r10d = 0                 // "\"\"?" // "\"\"?"
         esi = 0                  // "\"\"?" // "\"\"?"
         eax = r8d
         al |= byte [var_5dh_3]   // "\"\"?" // "\"\"?"
         if  (var) goto loc_0x3941 // unlikely

    loc_0x00003e3a: // orphan
         goto loc_0x3a18

    loc_0x00003e3f: // orphan
         // CODE XREFS from fcn.00003610 @ 0x390d, 0x419a
         esi = 0x23               // '#' // (pstr 0x00000000) "?\"\"?"
         

    loc_0x00003e48: // orphan
         // CODE XREFS from fcn.00003610 @ 0x43b9, 0x4522, 0x4594, 0x47d6
         var = rbx & rbx          // "\"\"?" // "\"\"?"
         if  (var) goto loc_0x3932 // unlikely

    loc_0x00003e51: // orphan
         goto loc_0x3c3b

    loc_0x00003e56: // orphan
         // CODE XREF from fcn.00003610 @ 0x390d
         esi = 0x20               // "@"
         goto loc_0x3c3b

    loc_0x00003e60: // orphan
         // CODE XREF from fcn.00003610 @ 0x390d
         esi = 9                  // (pstr 0x00000000) "?\"\"?"
         eax = 0x74               // 't' // (pstr 0x00000000) "?\"\"?"

    loc_0x00003e6a: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3e8e, 0x3e9a
         var = dword [var_5ch_3] - 2
         r12d = byte [var_5dh_3]
         dl = e
         r12b &= dl               // "\"\"?" // "\"\"?"
         if  (!var) goto loc_0x3928 // likely

    loc_0x00003e7f: // orphan
         goto loc_0x3c4f

    loc_0x00003e84: // orphan
         // CODE XREF from fcn.00003610 @ 0x390d
         esi = 0xd
         eax = 0x72               // 'r' // (pstr 0x00000000) "?\"\"?"
         goto loc_0x3e6a

    loc_0x00003e90: // orphan
         // CODE XREF from fcn.00003610 @ 0x390d
         esi = 0xa                // (pstr 0x00000000) "?\"\"?"
         eax = 0x6e               // 'n'
         goto loc_0x3e6a

    loc_0x00003e9c: // orphan
         // CODE XREF from fcn.00003610 @ 0x37b3
         byte [var_80h_2] = 1
         byte [var_78h] = 0
         byte [var_5eh_2] = 0
         qword [var_c8h_2] = 0
         byte [var_5dh_3] = 0
         byte [var_5fh_2] = 1
         qword [n] = 0
         qword [s2] = 0
         qword [var_70h_2] = 0
         goto loc_0x3888

    loc_0x00003edb: // orphan
         // CODE XREF from fcn.00003610 @ 0x37b3
         byte [var_80h_2] = 1
         var = ebx & ebx          // "\"\"?" // "\"\"?"
         if  (var) goto loc_0x4015 // unlikely

    loc_0x00003ee7: // orphan
         byte [var_5eh_2] = 0
         eax = 0                  // "\"\"?" // "\"\"?"
         qword [var_c8h_2] = 0
         byte [var_5fh_2] = 1

    loc_0x00003efc: // orphan
         // CODE XREFS from fcn.00003610 @ 0x47be, 0x4edc
         var = r11 & r11          // "\"\"?" // "\"\"?"
         if  (!var) goto loc_0x3f05 // likely

    loc_0x00003f01: // orphan
         byte [r9] = 0x27         // '''
                                  // [0x27:1]=0

    loc_0x00003f05: // orphan
         // CODE XREF from fcn.00003610 @ 0x3eff
         byte [var_78h] = al
         rax = rip + 0x2675       // "'"
                                  // 0x6584
         byte [var_5dh_3] = 0
         qword [n] = 1
         qword [s2] = rax
         qword [var_70h_2] = 1
         dword [var_5ch_3] = 2
         goto loc_0x3888

    loc_0x00003f36: // orphan
         // CODE XREF from fcn.00003610 @ 0x37b3
         byte [var_68h_2] = 1
         byte [var_60h] = 0
         byte [var_5eh] = 0
         qword [var_c8h] = 0
         byte [var_5dh_2] = 0
         byte [var_5fh] = 0
         qword [var_78h] = 0
         qword [var_b8h] = 0
         qword [var_58h_2] = 0
         goto loc_0x3888

    loc_0x00003f75: // orphan
         // CODE XREF from fcn.00003610 @ 0x37b3
         var = ebx & ebx          // "\"\"?" // "\"\"?"
         if  (var) goto loc_0x4d00 // unlikely

    loc_0x00003f7d: // orphan
         var = r11 & r11          // "\"\"?" // "\"\"?"
         if  (!var) goto loc_0x3f86 // likely

    loc_0x00003f82: // orphan
         byte [r9] = 0x22         // '\"'
                                  // [0x22:1]=0

    loc_0x00003f86: // orphan
         // CODE XREF from fcn.00003610 @ 0x3f80
         rax = rip + 0x25f5       // u"\"'\u07a1e\u80e2\x98\u4247\u3831\u33300\u656d\u6f6d\u7972\u6520\u6878\u7561\u7473\u6465\u2500s\u4f50\u4953X`\u7277\u7469\u2065\u7265\u6f72r\u4e47\u2055\u6f63\u6572\u7475\u6c69s\u6365\u6f68\u2500\u2073\u2528\u2973\u2520\u0a73\u2800\u2943\u5700\u6972\u7474\u6e65\u6220\u2079\u7325\u0a2e\u5700\u6972\u7474\u6e65\u6220\u2079\u7325\u6120"
                                  // 0x6582
         byte [var_80h_2] = 1
         byte [var_78h] = 0
         byte [var_5eh_2] = 0
         qword [var_c8h_2] = 0
         byte [var_5dh_3] = 0
         byte [var_5fh_2] = 1
         qword [n] = 1
         qword [s2] = rax
         qword [var_70h_2] = 1
         goto loc_0x3888

    loc_0x00003fc8: // orphan
         // CODE XREF from fcn.00003610 @ 0x37b3
         rax = rip + 0x25b3       // u"\"'\u07a1e\u80e2\x98\u4247\u3831\u33300\u656d\u6f6d\u7972\u6520\u6878\u7561\u7473\u6465\u2500s\u4f50\u4953X`\u7277\u7469\u2065\u7265\u6f72r\u4e47\u2055\u6f63\u6572\u7475\u6c69s\u6365\u6f68\u2500\u2073\u2528\u2973\u2520\u0a73\u2800\u2943\u5700\u6972\u7474\u6e65\u6220\u2079\u7325\u0a2e\u5700\u6972\u7474\u6e65\u6220\u2079\u7325\u6120"
                                  // 0x6582
         byte [var_80h_2] = 1
         byte [var_78h] = 0
         byte [var_5eh_2] = 0
         qword [var_c8h_2] = 0
         byte [var_5dh_3] = 1
         byte [var_5fh_2] = 1
         qword [n] = 1
         qword [s2] = rax
         qword [var_70h_2] = 0
         dword [var_5ch_3] = 5
         goto loc_0x3888

    loc_0x00004011: // orphan
         // CODE XREF from fcn.00003610 @ 0x37b3
         byte [var_80h_2] = 1

    loc_0x00004015: // orphan
         // CODE XREF from fcn.00003610 @ 0x3ee1
         byte [var_78h] = 0
         byte [var_5eh_2] = 0
         qword [var_c8h_2] = 0
         byte [var_5dh_3] = 1
         byte [var_5fh_2] = 0

    loc_0x00004030: // orphan
         // CODE XREF from fcn.00003610 @ 0x4079
         rax = rip + 0x254d       // "'"
                                  // 0x6584
         qword [n] = 1
         qword [s2] = rax
         qword [var_70h_2] = 0
         dword [var_5ch_3] = 2
         goto loc_0x3888

    loc_0x0000405a: // orphan
         // CODE XREF from fcn.00003610 @ 0x37b3
         byte [var_80h_2] = 1
         byte [var_78h] = 0
         byte [var_5eh_2] = 0
         qword [var_c8h_2] = 0
         byte [var_5dh_3] = 1
         byte [var_5fh_2] = 1
         // DATA XREF from fcn.00003610 @ 0x25c3
         goto loc_0x4030

    loc_0x00004080: // orphan
         // CODE XREF from fcn.00003610 @ 0x38d5
         rax = qword [n]          // "\"\"?"
         rdx = rax + rbx          // "\"\"?"
         var = r14 - 0xffffffffffffffff // "\"\"?" // "\"\"?"
         if  (var) goto loc_0x40f2 // likely

    loc_0x0000408e: // orphan
         var = rax - 1            // "\"\"?"
         if  (((unsigned) var) <= 0) goto 0x40f2 // likely

    loc_0x00004094: // orphan
         qword [var_c8h] = r11
         qword [s1] = r9
         qword [var_b8h] = rcx
         byte [var_b0h] = r10b
         qword [var_90h_2] = rdx
         byte [ps] = r8b
         sym.imp.strlen  ()
                                  // size_t strlen(-1)
         r11 = qword [var_c8h]
         // DATA XREFS from fcn.00003610 @ 0x2620, 0x4f40
         r9 = qword [s1]
         rcx = qword [var_b8h]
         r10d = byte [var_b0h]
         r14 = rax
         rdx = qword [var_90h_2]
         r8d = byte [ps]

    loc_0x000040f2: // orphan
         // CODE XREFS from fcn.00003610 @ 0x408c, 0x4092
         var = r14 - rdx          // "\"\"?" // "\"\"?"
         if  (((unsigned) var) < 0) goto 0x42c0 // unlikely

    loc_0x000040fb: // orphan
         rdx = qword [n]          // size_t n // "\"\"?"
         rsi = qword [s2]         // const void *s2 // "'"
         rdi = rcx                // const void *s1
         // DATA XREF from fcn.00003610 @ 0x2524
         qword [s1] = r11
         qword [var_b8h] = r9
         byte [var_b0h] = r10b
         byte [var_90h_2] = r8b
         qword [ps] = rcx
         sym.imp.memcmp  ()
                                  // int memcmp(-1, 0x80e2006507a10027, ?)
         rcx = qword [ps]
         r8d = byte [var_90h_2]
         var = eax & eax          // "\"\"?" // "\"\"?"
         r10d = byte [var_b0h]
         r9 = qword [var_b8h]
         r11 = qword [s1]
         if  (var) goto loc_0x42c0 // unlikely

    loc_0x0000415e: // orphan
         var = byte [var_5dh_3] - 0
         if  (var) goto loc_0x3c66 // likely

    loc_0x00004168: // orphan
         esi = byte [rcx]         // (pstr 0x00000000) "\"\"\"?"
         var = sil - 0x3f         // "\"\"?" // "\"\"?" // "\"\"?"
         if  (var > 0) goto loc_0x4830 // unlikely

    loc_0x00004175: // orphan
         var = sil & sil          // "\"\"?" // "\"\"?"
         js case.0x419a.1         // unlikely

    loc_0x0000417e: // orphan
         var = sil - 0x3f         // "\"\"?" // "\"\"?" // "\"\"?"
         if  (((unsigned) var) > 0) goto case.0x419a.1 // unlikely

    loc_0x00004188: // orphan
         rdx = rip + 0x2055       // 0x61e4
         eax = sil
         rax = dword [rdx + rax*4]
         rax += rdx               // case.0x419a.0 // "\"\"?" // "\"\"?"
         goto loc_rax             // switch table (64 cases) at 0x61e4 // case.0x419a.0

    loc_0x000041a0: // orphan
         // CODE XREF from fcn.00003610 @ 0x419a
         r10d = r12d
         eax = r8d
         al |= byte [var_5dh_3]   // "\"\"?"
         if  (var) goto loc_0x3941 // likely

    loc_0x000041af: // orphan
         goto loc_0x3a18

    loc_0x000041b4: // orphan
         // CODE XREF from fcn.00003610 @ 0x419a
         edx = 0                  // "\"\"?" // "\"\"?"
         esi = 0xa                // (pstr 0x00000000) "\"\"\"?"
         eax = 0x6e               // 'n'
         goto loc_0x3928

    loc_0x000041c5: // orphan
         // CODE XREF from fcn.00003610 @ 0x419a
         edx = 0                  // "\"\"?" // "\"\"?"
         r10d = 0                 // "\"\"?" // "\"\"?"
         esi = 0x61               // 'a' // (pstr 0x00000002) "\"?"
         goto loc_0x3979

    loc_0x000041d4: // orphan
         // CODE XREF from fcn.00003610 @ 0x419a
         rax = qword [var_70h_2]
         rcx = rax + 1            // "\"\"?"
         eax = r12d
         no

    loc_0x000041e0: // orphan
         // CODE XREF from fcn.00003610 @ 0x4342
         rsi = qword [var_70h_2]
         var = rsi - r11          // "\"\"?" // "\"\"?"
         jae 0x41ee               // likely

    loc_0x000041e9: // orphan
         byte [r9 + rsi] = 0x5c   // '\\'
                                  // [0x5c:1]=0

    loc_0x000041ee: // orphan
         // CODE XREF from fcn.00003610 @ 0x41e7
         var = r8b & r8b          // "\"\"?" // "\"\"?"
         if  (!var) goto loc_0x3a00 // likely

    loc_0x000041f7: // orphan
         rdx = rbx + 1            // "\"\"?"
         var = rdx - r14
         jae 0x421c               // likely

    loc_0x00004200: // orphan
         rsi = qword [s]
         esi = byte [rsi + rbx + 1] // (pstr 0x00000000) "\\"\"?"
         edx = rsi - 0x30         // (pstr 0x00000000) "\\"\"?"
         byte [ps] = sil
         var = dl - 9
         if  (((unsigned) var) <= 0) goto 0x4c85 // unlikely

    loc_0x0000421c: // orphan
         // CODE XREFS from fcn.00003610 @ 0x41fe, 0x4caa
         r12d = eax
         qword [var_70h_2] = rcx
         eax = r10d
         esi = 0x30               // '0' // (pstr 0x00000000) "\\"\"?"
         r10d = 0                 // "\"\"?" // "\"\"?"
         goto loc_0x3943

    loc_0x00004233: // orphan
         // CODE XREF from fcn.00003610 @ 0x419a
         edx = 0                  // "\"\"?" // "\"\"?"
         esi = 9                  // (pstr 0x00000000) "\\"\"?"
         eax = 0x74               // 't' // (pstr 0x00000000) "\\"\"?"
         goto loc_0x3928

    loc_0x00004244: // orphan
         // CODE XREF from fcn.00003610 @ 0x419a
         edx = 0                  // "\"\"?" // "\"\"?"
         r10d = 0                 // "\"\"?" // "\"\"?"
         esi = 0x62               // 'b' // (pstr 0x00000000) "\\"\"?"
         goto loc_0x3979

    loc_0x00004253: // orphan
         // CODE XREF from fcn.00003610 @ 0x419a
         r10d = r12d
         esi = 0x20               // "@"
         eax = r8d
         al |= byte [var_5dh_3]   // "\"\"?"
         if  (var) goto loc_0x3941 // likely

    loc_0x00004267: // orphan
         goto loc_0x3a18

    loc_0x0000426c: // orphan
         // CODE XREF from fcn.00003610 @ 0x419a
         edx = 0                  // "\"\"?" // "\"\"?"
         r10d = 0                 // "\"\"?" // "\"\"?"
         esi = 0x76               // 'v'
         goto loc_0x3979

    loc_0x0000427b: // orphan
         // CODE XREF from fcn.00003610 @ 0x419a
         edx = 0                  // "\"\"?" // "\"\"?"
         esi = 0xd
         eax = 0x72               // 'r' // (pstr 0x00000000) "\\"\"?"
         goto loc_0x3928

    loc_0x0000428c: // orphan
         // CODE XREF from fcn.00003610 @ 0x419a
         edx = 0                  // "\"\"?" // "\"\"?"
         r10d = 0                 // "\"\"?" // "\"\"?"
         esi = 0x66               // 'f'
         goto loc_0x3979

    loc_0x0000429b: // orphan
         // CODE XREF from fcn.00003610 @ 0x419a
         byte [var_78h] = r12b
         r10d = r12d
         esi = 0x27               // '''
         eax = r8d
         al |= byte [var_5dh_3]   // "\"\"?"
         if  (var) goto loc_0x3941 // likely

    loc_0x000042b3: // orphan
         goto loc_0x3a18

    loc_0x000042c0: // orphan
         // CODE XREFS from fcn.00003610 @ 0x40f5, 0x4158
         esi = byte [rcx]         // (pstr 0x00000000) "\\"\"?"
         var = sil - 0x3f         // "\"\"?" // "\"\"?"
         if  (var > 0) goto loc_0x4530 // likely

    loc_0x000042cd: // orphan
         var = sil & sil          // "\"\"?" // "\"\"?"
         js case.0x42f2.1         // unlikely

    loc_0x000042d6: // orphan
         var = sil - 0x3f         // "\"\"?" // "\"\"?" // "\"\"?"
         if  (((unsigned) var) > 0) goto case.0x42f2.1 // unlikely

    loc_0x000042e0: // orphan
         rdx = rip + 0x1ffd       // 0x62e4
         eax = sil
         rax = dword [rdx + rax*4]
         rax += rdx               // case.0x42f2.0 // "\"\"?" // "\"\"?"
         goto loc_rax             // switch table (64 cases) at 0x62e4 // case.0x42f2.0

    loc_0x000042f8: // orphan
         // CODE XREF from fcn.00003610 @ 0x42f2
         r10d = r12d
         eax = r8d
         r12d = 0                 // "\"\"?" // "\"\"?"
         al |= byte [var_5dh_3]   // "\"\"?"
         if  (var) goto loc_0x3941 // likely

    loc_0x0000430a: // orphan
         goto loc_0x3a18

    loc_0x00004310: // orphan
         // CODE XREFS from fcn.00003610 @ 0x42f2, 0x4567
         r12d = 0                 // "\"\"?" // "\"\"?"
         goto loc_0x3932          // case.0x419a.62 // case.0x419a.62(0x0, 0x0, 0x0, 0x0)

    loc_0x00004320: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3e13, 0x42f2
         var = byte [var_5dh_3] - 0
         if  (var) goto loc_0x4e12 // likely

    loc_0x0000432a: // orphan
         edx = byte [var_5eh_2]
         var = dword [var_5ch_3] - 2 // "\"\"?" // "\"\"?"
         rsi = qword [var_70h_2]
         al = e                   // "\"\"?"
         edx ^= 1                 // "\"\"?"
         rcx = rsi + 1            // "\"\"?"
         al &= dl                 // "\"\"?"
         if  (!var) goto loc_0x41e0 // unlikely

    loc_0x00004348: // orphan
         var = rsi - r11          // "\"\"?" // "\"\"?"
         jae 0x4352               // likely

    loc_0x0000434d: // orphan
         byte [r9 + rsi] = 0x27   // '''
                                  // [0x27:1]=0

    loc_0x00004352: // orphan
         // CODE XREF from fcn.00003610 @ 0x434b
         var = rcx - r11          // "\"\"?" // "\"\"?"
         jae 0x435c               // likely

    loc_0x00004357: // orphan
         byte [r9 + rcx] = 0x24   // '$'
                                  // [0x24:1]=0

    loc_0x0000435c: // orphan
         // CODE XREF from fcn.00003610 @ 0x4355
         rsi = qword [var_70h_2]
         rdx = rsi + 2
         var = rdx - r11
         jae 0x436f               // likely

    loc_0x00004369: // orphan
         byte [r9 + rsi + 2] = 0x27 // '''
                                  // [0x27:1]=0

    loc_0x0000436f: // orphan
         // CODE XREF from fcn.00003610 @ 0x4367
         rsi = qword [var_70h_2]
         rdx = rsi + 3
         rsi += 4                 // (pstr 0x00000000) "$\"'?"
         qword [var_70h_2] = rsi
         var = rdx - r11          // "\"'?"
         jae 0x4bfd               // likely

    loc_0x00004388: // orphan
         byte [r9 + rdx] = 0x5c   // '\\'
                                  // [0x5c:1]=0
         r10d = 0                 // "\"'?" // "\"'?"
         esi = 0x30               // '0' // (pstr 0x00000000) "\\"'?"
         byte [var_5eh_2] = al
         goto loc_0x3a28

    loc_0x0000439d: // orphan
         // CODE XREF from fcn.00003610 @ 0x42f2
         edx = 0                  // "\"'?" // "\"'?"
         r12d = 0                 // "\"'?" // "\"'?"
         esi = 0xa                // (pstr 0x00000000) "\\"'?"
         eax = 0x6e               // 'n'
         goto loc_0x3928

    loc_0x000043b1: // orphan
         // CODE XREF from fcn.00003610 @ 0x42f2
         r12d = 0                 // "\"'?" // "\"'?"
         esi = 0x23               // '#' // (pstr 0x00000000) "\\"'?"
         goto loc_0x3e48

    loc_0x000043be: // orphan
         // CODE XREF from fcn.00003610 @ 0x42f2
         edx = 0                  // "\"'?" // "\"'?"
         r10d = 0                 // "\"'?" // "\"'?"
         esi = 0x61               // 'a' // (pstr 0x00000002) "'?"
         goto loc_0x396f

    loc_0x000043cd: // orphan
         // CODE XREF from fcn.00003610 @ 0x42f2
         r12d = 0                 // "\"'?" // "\"'?"
         var = dword [var_5ch_3] - 5 // "\"'?" // "\"'?" // "\"'?"
         if  (!var) goto loc_0x3cd6 // unlikely

    loc_0x000043da: // orphan
         

    loc_0x000043e0: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3cd0, 0x3cdd
         r10d = 0                 // "\"'?" // "\"'?"
         esi = 0x3f               // '?'
         eax = r8d
         al |= byte [var_5dh_3]   // "\"'?"
         if  (var) goto loc_0x3941 // likely

    loc_0x000043f4: // orphan
         goto loc_0x3a18

    loc_0x000043f9: // orphan
         // CODE XREF from fcn.00003610 @ 0x42f2
         byte [var_78h] = r12b
         r10d = r12d
         esi = 0x27               // '''
         r12d = 0                 // "\"'?" // "\"'?"
         eax = r8d
         al |= byte [var_5dh_3]   // "\"'?"
         if  (var) goto loc_0x3941 // likely

    loc_0x00004414: // orphan
         goto loc_0x3a18

    loc_0x00004419: // orphan
         // CODE XREF from fcn.00003610 @ 0x42f2
         edx = 0                  // "\"'?" // "\"'?"
         r12d = 0                 // "\"'?" // "\"'?"
         esi = 0xd
         eax = 0x72               // 'r' // (pstr 0x00000000) "\\"'?"
         goto loc_0x3928

    loc_0x0000442d: // orphan
         // CODE XREF from fcn.00003610 @ 0x42f2
         edx = 0                  // "\"'?" // "\"'?"
         r10d = 0                 // "\"'?" // "\"'?"
         esi = 0x66               // 'f'
         goto loc_0x396f

    loc_0x0000443c: // orphan
         // CODE XREF from fcn.00003610 @ 0x42f2
         edx = 0                  // "\"'?" // "\"'?"
         r12d = 0                 // "\"'?" // "\"'?"
         esi = 9                  // (pstr 0x00000000) "\\"'?"
         eax = 0x74               // 't' // (pstr 0x00000000) "\\"'?"
         goto loc_0x3928

    loc_0x00004450: // orphan
         // CODE XREF from fcn.00003610 @ 0x42f2
         edx = 0                  // "\"'?" // "\"'?"
         r10d = 0                 // "\"'?" // "\"'?"
         esi = 0x62               // 'b' // (pstr 0x00000000) "\\"'?"
         goto loc_0x396f

    loc_0x0000445f: // orphan
         // CODE XREF from fcn.00003610 @ 0x42f2
         edx = 0                  // "\"'?" // "\"'?"
         r10d = 0                 // "\"'?" // "\"'?"
         esi = 0x76               // 'v'
         goto loc_0x396f

    loc_0x0000446e: // orphan
         // CODE XREF from fcn.00003610 @ 0x42f2
         r10d = r12d
         esi = 0x20               // "@"
         r12d = 0                 // "\"'?" // "\"'?"
         eax = r8d
         al |= byte [var_5dh_3]   // "\"'?"
         if  (var) goto loc_0x3941 // likely

    loc_0x00004485: // orphan
         goto loc_0x3a18

    loc_0x00004490: // orphan
         // CODE XREF from fcn.00003610 @ 0x38e2
         var = sil - 0x7a         // "\"'?" // "\"'?" // "\"'?"
         if  (var > 0) goto loc_0x44f8 // unlikely

    loc_0x00004496: // orphan
         var = sil - 0x40         // elf_phdr // "\"'?" // "\"'?" // "\"'?"
         if  (!var) goto loc_0x3a70 // unlikely

    loc_0x000044a0: // orphan
         ecx = rsi - 0x41
         eax = 1                  // "\"'?"
         rdx = 0x3ffffff53ffffff
         rax <<<= cl
         var = rax & rdx
         if  (var) goto loc_0x3935 // case.0x390d.58 // likely

    loc_0x000044be: // orphan
         var = eax & 0xa4000000   // "\"'?" // "\"'?"
         if  (var) goto loc_0x3c38 // unlikely

    loc_0x000044c9: // orphan
         var = dword [var_5ch_3] - 2 // "\"'?" // "\"'?"
         if  (var) goto loc_0x456d // unlikely

    loc_0x000044d3: // orphan
         var = byte [var_5dh_3] - 0
         if  (var) goto loc_0x3c56 // likely

    loc_0x000044dd: // orphan
         // CODE XREF from fcn.00003610 @ 0x4587
         eax = byte [var_5eh_2]
         rbx += 1                 // "\"'?"
         r10d = 0                 // "\"'?" // "\"'?"
         esi = 0x5c               // '\\' // (pstr 0x00000000) "\\"'?"
         goto loc_0x3a32

    loc_0x000044f8: // orphan
         // CODE XREF from fcn.00003610 @ 0x4494
         var = sil - 0x7d         // "\"'?" // "\"'?" // "\"'?"
         if  (!var) goto loc_0x450e // unlikely

    loc_0x000044fe: // orphan
         if  (var > 0) goto loc_0x4590 // likely

    loc_0x00004504: // orphan
         var = sil - 0x7b         // "\"'?" // "\"'?" // "\"'?"
         if  (var) goto loc_0x4b8d // likely

    loc_0x0000450e: // orphan
         // CODE XREFS from fcn.00003610 @ 0x44fc, 0x47f7, 0x4c3e, 0x4c4a, 0x4c5d
         var = r14 - 0xffffffffffffffff // "\"'?" // "\"'?"
         if  (!var) goto loc_0x47c8 // unlikely

    loc_0x00004518: // orphan
         var = r14 - 1            // "\"'?"
         if  (var) goto loc_0x3932 // case.0x419a.62 // likely

    loc_0x00004522: // orphan
         goto loc_0x3e48

    loc_0x00004530: // orphan
         // CODE XREF from fcn.00003610 @ 0x42c7
         var = sil - 0x7a         // "\"'?" // "\"'?" // "\"'?"
         if  (var > 0) goto loc_0x47e0 // unlikely

    loc_0x0000453a: // orphan
         var = sil - 0x40         // elf_phdr // "\"'?" // "\"'?" // "\"'?"
         if  (!var) goto loc_0x3a68 // unlikely

    loc_0x00004544: // orphan
         ecx = rsi - 0x41
         eax = 1                  // "\"'?"
         rdx = 0x3ffffff53ffffff
         rax <<<= cl
         var = rax & rdx
         if  (var) goto loc_0x4bf0 // likely

    loc_0x00004562: // orphan
         var = eax & 0xa4000000   // "\"'?" // "\"'?"
         if  (var) goto loc_0x4310 // unlikely

    loc_0x0000456d: // orphan
         // CODE XREF from fcn.00003610 @ 0x44cd
         r12d = byte [var_5fh_2]  // "\"'?"
         r12b &= byte [var_5dh_3] // "\"'?"
         if  (!var) goto loc_0x486d // unlikely

    loc_0x0000457c: // orphan
         var = qword [n] - 0
         if  (!var) goto loc_0x3c66 // unlikely

    loc_0x00004587: // orphan
         goto loc_0x44dd

    loc_0x00004590: // orphan
         // CODE XREF from fcn.00003610 @ 0x44fe
         var = sil - 0x7e         // "\"'?" // "\"'?" // "\"'?" // "\"'?"
         if  (!var) goto loc_0x3e48 // unlikely

    loc_0x0000459a: // orphan
         esi = 0x7f               // '\x7f'

    loc_0x0000459f: // orphan
         // CODE XREF from fcn.00003610 @ 0x4cc9
         var = qword [var_d0h_3] - 1 // "\"'?" // "\"'?" // "\"'?" // "\"'?"
         if  (!var) goto loc_0x3a7e // unlikely

    loc_0x000045ad: // orphan
         

    loc_0x000045b0: // orphan
         // CODE XREF from fcn.00003610 @ 0x3a78
         rax = var_58h_2
         qword [var_58h_2] = 0
         qword [ps] = rax
         var = r14 - 0xffffffffffffffff // "\"'?" // "\"'?"
         if  (var) goto loc_0x461d // likely

    loc_0x000045c9: // orphan
         rdi = qword [s]          // const char *s
         qword [var_c8h] = r11
         qword [s1] = r9
         byte [var_b8h] = sil
         byte [var_b0h] = r10b
         byte [var_90h_2] = r8b
         sym.imp.strlen  ()
                                  // size_t strlen("L\x8b#\xba\x05")
         r11 = qword [var_c8h]
         r9 = qword [s1]
         esi = byte [var_b8h]
         r10d = byte [var_b0h]
         r14 = rax
         r8d = byte [var_90h_2]

    loc_0x0000461d: // orphan
         // CODE XREF from fcn.00003610 @ 0x45c7
         byte [var_90h_2] = r10b
         eax = 0                  // "\"'?" // "\"'?"
         byte [var_beh] = r8b
         qword [var_b8h] = rbx
         byte [var_bdh] = r10b
         byte [var_bfh] = sil
         byte [var_c0h_2] = r12b
         qword [var_c8h] = r9
         qword [var_d8h] = r11
         qword [var_e0h] = r13
         qword [var_e8h] = r15
         qword [s1] = r14
         r14 = rax

    loc_0x0000466f: // orphan
         // CODE XREF from fcn.00003610 @ 0x48e7
         rax = qword [var_b8h]
         rbx = rax + r14
         rax = qword [s]
         r15 = rax + rbx
         r12 = r15
         var = r15 & r15          // "\"'?"
         if  (!var) goto loc_0x4950 // unlikely

    loc_0x0000468e: // orphan
         rdx = qword [s1]
         r13 = wc                 // (cstr 0x00000000) "\\"'?"
         rdx -= rbx               // "\"'?" // "\"'?"
         byte [var_b0h] = ne

    loc_0x000046a3: // orphan
         // CODE XREF from fcn.00003610 @ 0x496c
         rcx = qword [ps]         // (cstr 0x00000000) "\\"'?"
         rsi = r12
         rdi = r13
         sym.imp.mbrtoc32  ()
         rcx = rax
         var = rax - 0xfffffffffffffffd // "\"'?" // "\"'?" // "\"'?"
         if  (((unsigned) var) <= 0) goto 0x4888 // likely

    loc_0x000046c2: // orphan
         var = byte [var_b0h] - 0 // "\"'?" // "\"'?"
         if  (!var) goto loc_0x4888 // likely

    loc_0x000046cf: // orphan
         qword [var_b0h] = rax
         fcn.00003610  ()         // rip
         var = al & al            // "\"'?" // "\"'?"
         if  (!var) goto loc_0x4bc4 // likely

    loc_0x000046e3: // orphan
         rcx = qword [var_b0h]
         rdx = rbx
         rax = r14
         r8d = byte [var_beh]
         rbx = qword [var_b8h]
         esi = byte [var_bfh]
         r14 = qword [s1]
         r12d = byte [var_c0h_2]
         r9 = qword [var_c8h]
         r11 = qword [var_d8h]
         r13 = qword [var_e0h]
         r15 = qword [var_e8h]
         var = rcx - 0xffffffffffffffff // "\"'?" // "\"'?"
         if  (!var) goto loc_0x4753 // unlikely

    loc_0x00004737: // orphan
         // CODE XREF from fcn.00003610 @ 0x4e82
         var = rdx - r14          // "\"'?" // "\"'?"
         jae 0x4753               // likely

    loc_0x0000473c: // orphan
         // CODE XREF from fcn.00003610 @ 0x4751
         rcx = qword [s]
         var = byte [rcx + rdx] - 0
         if  (!var) goto loc_0x4753 // unlikely

    loc_0x00004746: // orphan
         rax += 1                 // "\"'?"
         rdx = rbx + rax          // "\"'?"
         var = rdx - r14
         if  (((unsigned) var) < 0) goto 0x473c // unlikely

    loc_0x00004753: // orphan
         // CODE XREFS from fcn.00003610 @ 0x4735, 0x473a, 0x4744, 0x4d86
         edx = byte [var_5fh_2]   // "\"'?"
         r10d = 0                 // "\"'?" // "\"'?"

    loc_0x0000475a: // orphan
         // CODE XREF from fcn.00003610 @ 0x4942
         var = rax - 1            // "\"'?"
         if  (((unsigned) var) > 0) goto 0x3ae8 // unlikely

    loc_0x00004764: // orphan
         goto loc_0x3ad9

    loc_0x00004769: // orphan
         // CODE XREF from fcn.00003610 @ 0x38ac
         var = dword [wc] - 2     // "\"'?" // "\"'?"
         dl = e                   // "\"'?"
         var = qword [var_58h_2] - 0
         al = e
         al &= dl                 // "\"'?" // "\"'?"
         if  (!var) goto loc_0x49f0 // likely

    loc_0x00004780: // orphan
         var = byte [var_5dh_3] - 0
         if  (var) goto loc_0x3c4f // likely

    loc_0x0000478a: // orphan
         var = byte [var_78h] - 0 // "\"'?" // "\"'?"
         if  (!var) goto loc_0x4e87 // likely

    loc_0x00004794: // orphan
         var = byte [var_80h_2] - 0
         if  (var) goto loc_0x4e28 // likely

    loc_0x0000479e: // orphan
         var = qword [var_c8h_2] - 0 // "\"'?" // "\"'?"
         al = ne
         var = r11 & r11          // "\"'?" // "\"'?"
         dl = e                   // "\"'?"
         al &= dl                 // "\"'?" // "\"'?"
         if  (!var) goto loc_0x4eb9 // likely

    loc_0x000047b7: // orphan
         r11 = qword [var_c8h_2]
         goto loc_0x3efc

    loc_0x000047c8: // orphan
         // CODE XREF from fcn.00003610 @ 0x4512
         rax = qword [s]
         var = byte [rax + 1] - 0 // "\"'?" // "\"'?"
         if  (var) goto loc_0x3932 // case.0x419a.62 // likely

    loc_0x000047d6: // orphan
         goto loc_0x3e48

    loc_0x000047e0: // orphan
         // CODE XREF from fcn.00003610 @ 0x4534
         var = sil - 0x7d         // "\"'?" // "\"'?" // "\"'?"
         if  (!var) goto loc_0x4c5a // unlikely

    loc_0x000047ea: // orphan
         if  (var > 0) goto loc_0x4c0d // likely

    loc_0x000047f0: // orphan
         r12d = 0                 // "\"'?" // "\"'?"
         var = sil - 0x7b         // "\"'?" // "\"'?" // "\"'?"
         if  (!var) goto loc_0x450e // unlikely

    loc_0x000047fd: // orphan
         esi = 0x7c               // '|'
         goto loc_0x3932          // case.0x419a.62 // case.0x419a.62(0x0, 0x7c, 0x0, 0x0)

    loc_0x00004810: // orphan
         // CODE XREF from fcn.00003610 @ 0x3cc6
         var = byte [var_5dh_3] - 0
         if  (var) goto loc_0x3c56 // likely

    loc_0x0000481a: // orphan
         r10d = 0                 // "\"'?" // "\"'?"
         eax = 0                  // "\"'?" // "\"'?"
         esi = 0x3f               // '?'
         goto loc_0x3a28

    loc_0x00004830: // orphan
         // CODE XREF from fcn.00003610 @ 0x416f
         var = sil - 0x7a         // "\"'?" // "\"'?" // "\"'?"
         if  (var > 0) goto loc_0x4c3a // unlikely

    loc_0x0000483a: // orphan
         var = sil - 0x40         // elf_phdr // "\"'?" // "\"'?" // "\"'?"
         if  (!var) goto loc_0x3a70 // unlikely

    loc_0x00004844: // orphan
         ecx = rsi - 0x41
         eax = 1                  // "\"'?"
         rdx = 0x3ffffff53ffffff
         rax <<<= cl
         var = rax & rdx
         if  (var) goto loc_0x4caf // likely

    loc_0x00004862: // orphan
         var = eax & 0xa4000000   // "\"'?" // "\"'?"
         if  (var) goto loc_0x3932 // unlikely

    loc_0x0000486d: // orphan
         // CODE XREF from fcn.00003610 @ 0x4576
         var = byte [var_5fh_2] - 0
         if  (!var) goto loc_0x3932 // unlikely

    loc_0x00004877: // orphan
         r10d = 0                 // "\"'?" // "\"'?"
         esi = 0x5c               // '\\' // (pstr 0x00000000) "\\"'?"
         goto loc_0x39c0

    loc_0x00004888: // orphan
         // CODE XREFS from fcn.00003610 @ 0x46bc, 0x46c9
         var = rcx & rcx          // "\"'?" // "\"'?"
         if  (!var) goto loc_0x48ed // likely

    loc_0x0000488d: // orphan
         var = rcx - 0xffffffffffffffff // "\"'?" // "\"'?"
         if  (!var) goto loc_0x4d42 // unlikely

    loc_0x00004897: // orphan
         var = rcx - 0xfffffffffffffffe // "\"'?" // "\"'?"
         if  (!var) goto loc_0x4e3b // unlikely

    loc_0x000048a1: // orphan
         var = rcx - 0xfffffffffffffffd // "\"'?" // "\"'?" // "\"'?"
         if  (!var) goto loc_0x48ba // unlikely

    loc_0x000048a7: // orphan
         var = dword [var_5ch_3] - 2 // "\"'?" // "\"'?"
         if  (var) goto loc_0x48b7 // unlikely

    loc_0x000048ad: // orphan
         var = byte [var_5dh_3] - 0
         if  (var) goto loc_0x4978 // likely

    loc_0x000048b7: // orphan
         // CODE XREFS from fcn.00003610 @ 0x48ab, 0x499f, 0x4beb
         r14 += rcx               // "\"'?" // "\"'?"

    loc_0x000048ba: // orphan
         // CODE XREFS from fcn.00003610 @ 0x48a5, 0x4c80
         edi = dword [wc]         // wint_t wc
         sym.imp.iswprint  ()
                                  // int iswprint(?)
         ebx = byte [var_90h_2]
         rdi = qword [ps]         // const mbstate_t *ps // (cstr 0x00000000) "\\"'?"
         var = eax & eax          // "\"'?" // "\"'?"
         eax = 0
         if  (!var) ebx = eax
         byte [var_90h_2] = bl
         sym.imp.mbsinit  ()
                                  // int mbsinit(?)
         var = eax & eax          // "\"'?" // "\"'?"
         if  (!var) goto loc_0x466f // likely

    loc_0x000048ed: // orphan
         // CODE XREF from fcn.00003610 @ 0x488b
         r10d = byte [var_90h_2]
         rax = r14
         r8d = byte [var_beh]
         rbx = qword [var_b8h]
         esi = byte [var_bfh]
         edx = r10d
         r14 = qword [s1]
         r12d = byte [var_c0h_2]
         edx ^= 1                 // "\"'?"
         r9 = qword [var_c8h]
         r11 = qword [var_d8h]
         r13 = qword [var_e0h]
         r15 = qword [var_e8h]
         dl &= byte [var_5fh_2]   // "\"'?"
         goto loc_0x475a

    loc_0x00004950: // orphan
         // CODE XREF from fcn.00003610 @ 0x4688
         eax = byte [var_bdh]
         r13d = 0                 // "\"'?" // "\"'?"
         edx = 1                  // "\"'?"
         r12 = rip + 0x1cbd       // 0x6623
         byte [var_b0h] = al
         goto loc_0x46a3

    loc_0x00004978: // orphan
         // CODE XREF from fcn.00003610 @ 0x48b1
         var = rcx - 1            // "\"'?"
         if  (!var) goto loc_0x4c7c // unlikely

    loc_0x00004982: // orphan
         rax = qword [s]
         r8 = r15 + rcx
         rdx = rax + rbx + 1
         goto loc_0x49a5

    loc_0x00004998: // orphan
         // CODE XREFS from fcn.00003610 @ 0x49ad, 0x49bd
         rdx += 1                 // "\"'?"
         var = r8 - rdx           // "\"'?" // "\"'?" // "\"'?" // "\"'?"
         if  (!var) goto loc_0x48b7 // unlikely

    loc_0x000049a5: // orphan
         // CODE XREF from fcn.00003610 @ 0x498f
         eax = byte [rdx]         // (pstr 0x00000000) "\\"'?"
         eax -= 0x5b              // "\"'?"
         var = al - 0x21          // "\"'?" // "\"'?"
         if  (((unsigned) var) > 0) goto 0x4998 // unlikely

    loc_0x000049af: // orphan
         rbx = 0x20000002b        // '+' // 8589934635
         bt rbx,ax                // "\"'?"
         jae 0x4998               // unlikely

    loc_0x000049bf: // orphan
         dword [var_5ch_3] = 2
         r14 = qword [s1]
         r9 = qword [var_c8h]
         r11 = qword [var_d8h]
         r13 = qword [var_e0h]
         r15 = qword [var_e8h]
         goto loc_0x3c56

    loc_0x000049f0: // orphan
         // CODE XREF from fcn.00003610 @ 0x477a
         eax = byte [var_5dh_2]   // "\"'?"
         eax ^= 1                 // "\"'?" // "\"'?"
         dl &= al                 // "\"'?" // "\"'?"
         if  (var) goto loc_0x4a71 // unlikely

    loc_0x000049fb: // orphan
         rdi = r11
         r11 = qword [var_70h_2]  // (pstr 0x00000000) "\\"'?"
         r10 = r9

    loc_0x00004a05: // orphan
         // CODE XREFS from fcn.00003610 @ 0x4e90, 0x4ea1, 0x4eb4, 0x4ec6
         rbx = qword [var_b8h]    // "'"
         var = rbx & rbx          // "\"'?"
         if  (!var) goto loc_0x4a40 // unlikely

    loc_0x00004a11: // orphan
         var = al & al            // "\"'?" // "\"'?"
         if  (!var) goto loc_0x4a40 // likely

    loc_0x00004a15: // orphan
         ecx = byte [rbx]         // (pstr 0x00000000) "\\"'?"
         rax = rbx
         var = cl & cl            // "\"'?"
         if  (!var) goto loc_0x4a40 // unlikely

    loc_0x00004a1f: // orphan
         rdx = r11
         rax -= r11               // "\"'?" // "\"'?"
         rsi = rdi

    loc_0x00004a28: // orphan
         // CODE XREF from fcn.00003610 @ 0x4a3b
         var = rdx - rsi          // "\"'?" // "\"'?"
         jae 0x4a31               // likely

    loc_0x00004a2d: // orphan
         byte [r10 + rdx] = cl

    loc_0x00004a31: // orphan
         // CODE XREF from fcn.00003610 @ 0x4a2b
         rdx += 1                 // "\"'?"
         ecx = byte [rax + rdx]
         var = cl & cl            // "\"'?"
         if  (var) goto loc_0x4a28 // likely

    loc_0x00004a3d: // orphan
         r11 = rdx

    loc_0x00004a40: // orphan
         // CODE XREFS from fcn.00003610 @ 0x4a0f, 0x4a13, 0x4a1d
         var = r11 - rdi          // "\"'?" // "\"'?"
         if  (((unsigned) var) < 0) goto 0x4de4 // unlikely

    loc_0x00004a49: // orphan
         // CODE XREF from fcn.00003610 @ 0x4de9
         rax = qword [var_38h_2]
         rax -= qword fs:[0x28]   // "\"'?" // "\"'?" // "\"'?" // "\"'?"
         if  (var) goto loc_0x4ee1 // likely

    loc_0x00004a5c: // orphan
         rsp += 0xc8
         rax = r11
         rbx = pop  ()
         r12 = pop  ()
         r13 = pop  ()
         r14 = pop  ()
         r15 = pop  ()
         rbp = pop  ()
         re

    loc_0x00004a71: // orphan
         // CODE XREF from fcn.00003610 @ 0x49f9
         var = byte [var_60h] - 0 // "\"'?" // "\"'?"
         if  (!var) goto loc_0x4e95 // likely

    loc_0x00004a7b: // orphan
         var = byte [var_80h_2] - 0
         if  (var) goto loc_0x4e28 // likely

    loc_0x00004a85: // orphan
         var = r11 & r11          // "\"'?" // "\"'?"
         al = e                   // "\"'?"
         var = qword [var_c8h_2] - 0 // "\"'?" // "\"'?"
         dl = ne
         al &= dl                 // "\"'?" // "\"'?"
         if  (!var) goto loc_0x4ea6 // likely

    loc_0x00004a9e: // orphan
         rcx = qword [var_c8h_2]
         edx = 0                  // "\"'?" // "\"'?"

    loc_0x00004aa7: // orphan
         // CODE XREF from fcn.00003610 @ 0x4e0d
         rbx = rip + 0x1ad6       // "'"
                                  // 0x6584
         var = byte [var_80h_2] - 0
         dword [var_5ch_3] = 2
         qword [var_70h_2] = 0
         qword [s2] = rbx
         qword [n] = 1
         if  (!var) goto loc_0x4ecb // unlikely

    loc_0x00004ad6: // orphan
         byte [var_78h] = al
         eax = byte [var_80h_2]   // "\"'?"
         r11 = qword [var_c8h_2]
         byte [var_80h_2] = dl
         qword [var_c8h_2] = rcx
         byte [var_5dh_3] = al
         goto loc_0x3888

    loc_0x00004af6: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3dc0, 0x3dd0
         rax = qword [var_70h_2]
         var = rax - r11          // "\"'?" // "\"'?"
         jae 0x4b04               // likely

    loc_0x00004aff: // orphan
         byte [r9 + rax] = 0x27   // '''
                                  // [0x27:1]=0

    loc_0x00004b04: // orphan
         // CODE XREF from fcn.00003610 @ 0x4afd
         rsi = qword [var_70h_2]
         rax = rsi + 1            // "\"'?"
         var = rax - r11
         jae 0x4b17               // likely

    loc_0x00004b11: // orphan
         byte [r9 + rsi + 1] = 0x5c // '\\'
                                  // [0x5c:1]=0

    loc_0x00004b17: // orphan
         // CODE XREF from fcn.00003610 @ 0x4b0f
         rax = qword [var_70h_2]
         rax += 2
         var = rax - r11
         jae 0x4b2e               // likely

    loc_0x00004b24: // orphan
         rax = qword [var_70h_2]
         byte [r9 + rax + 2] = 0x27 // '''
                                  // [0x27:1]=0

    loc_0x00004b2e: // orphan
         // CODE XREF from fcn.00003610 @ 0x4b22
         rdx = r11
         r11 = qword [var_c8h_2]
         goto loc_0x3dd6

    loc_0x00004b3d: // orphan
         // CODE XREF from fcn.00003610 @ 0x3e20
         rbx += 1                 // "\'?"
         goto loc_0x3890

    loc_0x00004b46: // orphan
         // CODE XREF from fcn.00003610 @ 0x3c00
         byte [var_5eh_2] = r10b
         r14 = qword [ps]         // (cstr 0x00000000) "'\'?"
         qword [var_70h_2] = r8
         r10d = byte [var_b8h]
         r13 = qword [var_90h_2]
         r15 = qword [var_b0h]
         goto loc_0x3a32

    loc_0x00004b70: // orphan
         // CODE XREF from fcn.00003610 @ 0x3b32
         byte [var_5fh_2] = al
         r14 = qword [ps]         // (cstr 0x00000000) "'\'?"
         r13 = qword [var_90h_2]
         r15 = qword [var_b0h]
         goto loc_0x3c56

    loc_0x00004b8d: // orphan
         // CODE XREF from fcn.00003610 @ 0x4508
         r10d = 0                 // "\'?" // "\'?"
         esi = 0x7c               // '|'
         goto loc_0x3c3b

    loc_0x00004b9a: // orphan
         // CODE XREF from fcn.00003610 @ 0x3bbc
         byte [var_5eh_2] = r10b
         r14 = qword [ps]         // (cstr 0x00000000) "'\'?"
         qword [var_70h_2] = r8
         r10d = byte [var_b8h]
         r13 = qword [var_90h_2]
         r15 = qword [var_b0h]
         goto loc_0x39d7

    loc_0x00004bc4: // orphan
         // CODE XREF from fcn.00003610 @ 0x46dd
         var = r13 & r13          // "\'?" // "\'?"
         if  (!var) goto loc_0x4c7c // likely

    loc_0x00004bcd: // orphan
         eax = byte [r12]
         var = dword [var_5ch_3] - 2 // "\'?" // "\'?"
         dword [r13] = eax
         if  (var) goto loc_0x4be6 // unlikely

    loc_0x00004bdc: // orphan
         var = byte [var_5dh_3] - 0
         if  (var) goto loc_0x4c7c // likely

    loc_0x00004be6: // orphan
         // CODE XREF from fcn.00003610 @ 0x4bda
         ecx = 1                  // (pstr 0x00000000) "'"
         goto loc_0x48b7

    loc_0x00004bf0: // orphan
         // CODE XREF from fcn.00003610 @ 0x455c
         eax = 0                  // (pstr 0x00000000) "'" // (pstr 0x00000000) "'"

    loc_0x00004bf2: // orphan
         // CODE XREF from fcn.00003610 @ 0x4cb2
         r10d = r12d
         r12d = eax
         goto loc_0x3941

    loc_0x00004bfd: // orphan
         // CODE XREF from fcn.00003610 @ 0x4382
         byte [var_5eh_2] = al
         r10d = 0                 // (pstr 0x00000000) "'" // (pstr 0x00000000) "'"
         esi = 0x30               // '0' // (pstr 0x00000000) "'"
         goto loc_0x3a28

    loc_0x00004c0d: // orphan
         // CODE XREF from fcn.00003610 @ 0x47ea
         eax = 0                  // (pstr 0x00000000) "'" // (pstr 0x00000000) "'"
         var = sil - 0x7e         // (pstr 0x00000000) "'" // (pstr 0x00000000) "'" // (pstr 0x00000000) "'" // (pstr 0x00000000) "'"
         if  (var) goto loc_0x4dc1 // likely

    loc_0x00004c19: // orphan
         // CODE XREF from fcn.00003610 @ 0x4cbe
         var = rbx & rbx          // (pstr 0x00000000) "'" // (pstr 0x00000000) "'"
         if  (var) goto loc_0x4c6a // unlikely

    loc_0x00004c1e: // orphan
         r10d = r12d
         esi = 0x7e               // '~'
         r12d = eax
         eax = r8d
         al |= byte [var_5dh_3]   // (pstr 0x00000000) "'"
         if  (var) goto loc_0x3941 // likely

    loc_0x00004c35: // orphan
         goto loc_0x3a18

    loc_0x00004c3a: // orphan
         // CODE XREF from fcn.00003610 @ 0x4834
         var = sil - 0x7d         // (pstr 0x00000000) "'" // (pstr 0x00000000) "'" // (pstr 0x00000000) "'"
         if  (!var) goto loc_0x450e // unlikely

    loc_0x00004c44: // orphan
         if  (var > 0) goto loc_0x4cb7 // likely

    loc_0x00004c46: // orphan
         var = sil - 0x7b         // (pstr 0x00000000) "'" // (pstr 0x00000000) "'" // (pstr 0x00000000) "'"
         if  (!var) goto loc_0x450e // unlikely

    loc_0x00004c50: // orphan
         esi = 0x7c               // '|'
         goto loc_0x3932          // case.0x419a.62 // case.0x419a.62(0x0, 0x7c, 0x0, 0x0)

    loc_0x00004c5a: // orphan
         // CODE XREF from fcn.00003610 @ 0x47e4
         r12d = 0                 // (pstr 0x00000000) "'" // (pstr 0x00000000) "'"
         goto loc_0x450e

    loc_0x00004c62: // orphan
         // CODE XREF from fcn.00003610 @ 0x3c08
         r12d = 0                 // (pstr 0x00000000) "'" // (pstr 0x00000000) "'"
         goto loc_0x3bc4

    loc_0x00004c6a: // orphan
         // CODE XREF from fcn.00003610 @ 0x4c1c
         r12d = eax
         r10d = 0                 // (pstr 0x00000000) "'" // (pstr 0x00000000) "'"
         eax = 0                  // (pstr 0x00000000) "'" // (pstr 0x00000000) "'"
         esi = 0x7e               // '~'
         goto loc_0x3943

    loc_0x00004c7c: // orphan
         // CODE XREFS from fcn.00003610 @ 0x497c, 0x4bc7, 0x4be0
         r14 += 1                 // (pstr 0x00000000) "'"
         goto loc_0x48ba

    loc_0x00004c85: // orphan
         // CODE XREF from fcn.00003610 @ 0x4216
         var = rcx - r11          // (pstr 0x00000000) "'" // (pstr 0x00000000) "'"
         jae 0x4c8f               // likely

    loc_0x00004c8a: // orphan
         byte [r9 + rcx] = 0x30   // '0'
                                  // [0x30:1]=0

    loc_0x00004c8f: // orphan
         // CODE XREF from fcn.00003610 @ 0x4c88
         rsi = qword [var_70h_2]
         rdx = rsi + 2            // (pstr 0x00000000) "0"
         var = rdx - r11
         jae 0x4ca2               // likely

    loc_0x00004c9c: // orphan
         byte [r9 + rsi + 2] = 0x30 // '0'
                                  // [0x30:1]=0

    loc_0x00004ca2: // orphan
         // CODE XREF from fcn.00003610 @ 0x4c9a
         rcx = qword [var_70h_2]
         rcx += 3                 // u(pstr 0x00000000) "00"
         goto loc_0x421c

    loc_0x00004caf: // orphan
         // CODE XREF from fcn.00003610 @ 0x485c
         eax = r12d
         goto loc_0x4bf2

    loc_0x00004cb7: // orphan
         // CODE XREF from fcn.00003610 @ 0x4c44
         eax = r12d
         var = sil - 0x7e
         if  (!var) goto loc_0x4c19 // unlikely

    loc_0x00004cc4: // orphan
         esi = 0x7f               // '\x7f'
         goto loc_0x459f

    loc_0x00004cce: // orphan
         // CODE XREF from fcn.00003610 @ 0x3834
         eax = byte [r13]         // u(pstr 0x00000000) "00"
         var = al & al
         if  (!var) goto loc_0x383a // unlikely

    loc_0x00004cdb: // orphan
         r12d = 0
         no

    loc_0x00004ce0: // orphan
         // CODE XREF from fcn.00003610 @ 0x4cf5
         var = r12 - r11
         jae 0x4ce9               // likely

    loc_0x00004ce5: // orphan
         byte [r9 + r12] = al

    loc_0x00004ce9: // orphan
         // CODE XREF from fcn.00003610 @ 0x4ce3
         r12 += 1
         eax = byte [r13 + r12]
         var = al & al
         if  (var) goto loc_0x4ce0 // unlikely

    loc_0x00004cf7: // orphan
         qword [var_70h_2] = r12
         goto loc_0x383a

    loc_0x00004d00: // orphan
         // CODE XREF from fcn.00003610 @ 0x3f77
         rax = rip + 0x187b       // u"\"'\u07a1e\u80e2\x98\u4247\u3831\u33300\u656d\u6f6d\u7972\u6520\u6878\u7561\u7473\u6465\u2500s\u4f50\u4953X`\u7277\u7469\u2065\u7265\u6f72r\u4e47\u2055\u6f63\u6572\u7475\u6c69s\u6365\u6f68\u2500\u2073\u2528\u2973\u2520\u0a73\u2800\u2943\u5700\u6972\u7474\u6e65\u6220\u2079\u7325\u0a2e\u5700\u6972\u7474\u6e65\u6220\u2079\u7325\u6120"
                                  // 0x6582
         byte [var_80h_2] = 1
         byte [var_78h] = 0
         byte [var_5eh_2] = 0
         qword [var_c8h_2] = 0
         byte [var_5dh_3] = 1
         byte [var_5fh_2] = 1
         qword [n] = 1
         qword [s2] = rax
         qword [var_70h_2] = 0
         goto loc_0x3888

    loc_0x00004d42: // orphan
         // CODE XREF from fcn.00003610 @ 0x4891
         rax = r14
         r8d = byte [var_beh]
         rbx = qword [var_b8h]
         esi = byte [var_bfh]
         r14 = qword [s1]
         r12d = byte [var_c0h_2]
         r9 = qword [var_c8h]
         r11 = qword [var_d8h]
         r13 = qword [var_e0h]
         r15 = qword [var_e8h]
         goto loc_0x4753

    loc_0x00004d8b: // orphan
         // CODE XREF from fcn.00003610 @ 0x3824
         esi = dword [var_5ch_3]  // int64_t arg2
         rdi = rax                // int64_t arg1
         fcn.00003350  ()         // fcn.00003350(0x0, 0x2)
         r11 = qword [var_80h_2]
         r9 = qword [var_70h_2]
         r15 = rax
         goto loc_0x382a

    loc_0x00004da6: // orphan
         // CODE XREF from fcn.00003610 @ 0x37f2
         esi = dword [var_5ch_3]  // int64_t arg2
         rdi = rax                // int64_t arg1
         fcn.00003350  ()         // fcn.00003350(0x0, 0x2)
         r11 = qword [var_80h_2]
         r9 = qword [var_70h_2]
         r13 = rax
         goto loc_0x37f8

    loc_0x00004dc1: // orphan
         // CODE XREF from fcn.00003610 @ 0x4c13
         r12d = 0
         esi = 0x7f               // '\x7f'
         goto loc_0x3a70          // case.default.0x390d // case.default.0x390d(0x0, 0x7f, 0x0, 0x0)

    loc_0x00004dce: // orphan
         // CODE XREFS from fcn.00003610 @ 0x3d0f, 0x3d2a
         esi = 0x3f               // '?'
         eax = r8d
         al |= byte [var_5dh_3]
         if  (var) goto loc_0x3941 // likely

    loc_0x00004ddf: // orphan
         goto loc_0x3a18

    loc_0x00004de4: // orphan
         // CODE XREF from fcn.00003610 @ 0x4a43
         byte [r10 + r11] = 0
         goto loc_0x4a49

    loc_0x00004dee: // orphan
         // CODE XREF from fcn.00003610 @ 0x37b3
         eax = byte [var_5dh_3]
         byte [var_5eh_2] = 0
         edx = 1
         ecx = 0
         qword [var_c8h_2] = r11
         byte [var_80h_2] = al
         eax = 0
         byte [var_5fh_2] = 0
         goto loc_0x4aa7

    loc_0x00004e12: // orphan
         // CODE XREF from fcn.00003610 @ 0x4324
         ebx = dword [var_5ch_3]
         eax = 4
         var = ebx - 2
         if  (!zf) eax = ebx
         dword [var_5ch_3] = eax
         goto loc_0x3c66

    loc_0x00004e28: // orphan
         // CODE XREFS from fcn.00003610 @ 0x4798, 0x4a7f
         dword [var_5ch_3] = 5
         r11 = qword [var_c8h_2]
         goto loc_0x3770

    loc_0x00004e3b: // orphan
         // CODE XREF from fcn.00003610 @ 0x489b
         rdx = rbx
         rax = r14
         r8d = byte [var_beh]
         rbx = qword [var_b8h]
         esi = byte [var_bfh]
         r14 = qword [s1]
         r12d = byte [var_c0h_2]
         r9 = qword [var_c8h]
         r11 = qword [var_d8h]
         r13 = qword [var_e0h]
         r15 = qword [var_e8h]
         goto loc_0x4737

    loc_0x00004e87: // orphan
         // CODE XREF from fcn.00003610 @ 0x478e
         rdi = r11
         r10 = r9
         r11d = 0
         goto loc_0x4a05

    loc_0x00004e95: // orphan
         // CODE XREF from fcn.00003610 @ 0x4a75
         rdi = r11
         r10 = r9
         r11 = qword [var_58h_2]
         eax = edx
         goto loc_0x4a05

    loc_0x00004ea6: // orphan
         // CODE XREF from fcn.00003610 @ 0x4a98
         rdi = r11
         eax = byte [var_78h]
         r11 = qword [var_70h_2]
         r10 = r9
         goto loc_0x4a05

    loc_0x00004eb9: // orphan
         // CODE XREF from fcn.00003610 @ 0x47b1
         rdi = r11
         eax = byte [var_78h]
         r10 = r9
         r11d = 0
         goto loc_0x4a05

    loc_0x00004ecb: // orphan
         // CODE XREF from fcn.00003610 @ 0x4ad0
         r11 = qword [var_c8h_2]
         byte [var_80h_2] = dl
         qword [var_c8h_2] = rcx
         goto loc_0x3efc

    loc_0x00004ee1: // orphan
         // CODE XREF from fcn.00003610 @ 0x4a56
         sym.imp.__stack_chk_fail  ()
         
         // DATA XREF from fcn.00003610 @ 0x25e2
         endbr6
         push  (rbp)
         rbp = rsp
         push  (rbx)
         rsp -= 8
         rax = qword [reloc.stdout] // [0x8fc8:8]=0
         rdi = qword [rax]        // int64_t arg1
         fcn.000035a0  ()         // fcn.000035a0(0x300000)
         var = eax & eax
         if  (!var) goto loc_0x4f50 // likely

    loc_0x00004f10: // orphan
         edx = 5
         rsi = rip + str.write_error // 0x65b2 // "write error"
         edi = 0
         sym.imp.dcgettext  ()
         rbx = rax
         sym.imp.__errno_location  ()
         edi = 0                  // int status
         rcx = rbx
         rdx = rip + 0x1670       // "%s"
                                  // 0x65a7 // char *format
         esi = dword [rax]        // int errname
         eax = 0
         sym.imp.error  ()
                                  // void error(-1, -1, "%s")
         edi = dword [0x00009010] // [0x9010:4]=1
         sym.imp._exit  ()
         

    loc_0x00004f50: // orphan
         // CODE XREF from fcn.00003610 @ 0x4f0e
         rax = qword [reloc.stderr] // [0x8ff8:8]=0
         rdi = qword [rax]        // int64_t arg1
         fcn.000035a0  ()         // fcn.000035a0(0x300000)
         var = eax & eax
         if  (var) goto loc_0x4f69 // unlikely

    loc_0x00004f63: // orphan
         rbx = qword [var_8h]
         leav                     // rsp
         re

    loc_0x00004f69: // orphan
         // CODE XREF from fcn.00003610 @ 0x4f61
         edi = dword [0x00009010] // [0x9010:4]=1
         sym.imp._exit  ()
         
         no

}
