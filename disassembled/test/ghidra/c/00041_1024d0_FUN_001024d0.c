
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined8 FUN_001024d0(int param_1,undefined8 *param_2)

{
  char *__s1;
  long *plVar1;
  byte bVar2;
  FILE *pFVar3;
  bool bVar4;
  bool bVar5;
  undefined *puVar6;
  bool bVar7;
  int iVar8;
  uint uVar9;
  char *pcVar10;
  char *pcVar11;
  byte *pbVar12;
  byte *pbVar13;
  ushort **ppuVar14;
  undefined8 uVar15;
  undefined8 uVar16;
  char *pcVar17;
  byte bVar18;
  long *plVar19;
  char cVar20;
  uint uVar21;
  ushort *puVar22;
  _IO_FILE *p_Var23;
  uint uVar24;
  long *plVar25;
  char **ppcVar26;
  long in_FS_OFFSET;
  bool bVar27;
  char *local_b8 [5];
  char *pcStack_90;
  char *local_88;
  char *pcStack_80;
  char *local_78;
  char *pcStack_70;
  char *local_68;
  char *pcStack_60;
  undefined1 local_58 [16];
  long local_40;
  
  uVar21 = 1;
  local_40 = *(long *)(in_FS_OFFSET + 0x28);
  pcVar10 = getenv("POSIXLY_CORRECT");
  if ((pcVar10 != (char *)0x0) && (uVar21 = 0, 1 < param_1)) {
    iVar8 = strcmp((char *)param_2[1],"-n");
    uVar21 = (uint)(iVar8 == 0);
  }
  pcVar17 = (char *)*param_2;
  if (pcVar17 == (char *)0x0) {
    fwrite("A NULL argv[0] was passed through an exec system call.\n",1,0x37,
           *(FILE **)PTR_stderr_00108ff8);
                    /* WARNING: Subroutine does not return */
    abort();
  }
  pcVar11 = strrchr(pcVar17,0x2f);
  if ((((pcVar11 != (char *)0x0) && (__s1 = pcVar11 + 1, 6 < (long)__s1 - (long)pcVar17)) &&
      (iVar8 = strncmp(pcVar11 + -6,"/.libs/",7), iVar8 == 0)) &&
     (iVar8 = strncmp(__s1,"lt-",3), pcVar17 = __s1, iVar8 == 0)) {
    pcVar17 = pcVar11 + 4;
    *(char **)PTR_program_invocation_short_name_00108fe8 = pcVar17;
  }
  _DAT_00109020 = pcVar17;
  *(char **)PTR_program_invocation_name_00108fd8 = pcVar17;
  setlocale(6,"");
  bindtextdomain("coreutils","/usr/share/locale");
  textdomain("coreutils");
  FUN_00105600(FUN_00104ef0);
  if ((param_1 == 2) && ((char)uVar21 != '\0')) {
    pcVar11 = (char *)param_2[1];
    iVar8 = strcmp(pcVar11,"--help");
    if (iVar8 == 0) {
      uVar15 = dcgettext(0,"Usage: %s [SHORT-OPTION]... [STRING]...\n  or:  %s LONG-OPTION\n",5);
      __printf_chk(2,uVar15,pcVar17,pcVar17);
      puVar6 = PTR_stdout_00108fc8;
      pFVar3 = *(FILE **)PTR_stdout_00108fc8;
      pcVar10 = (char *)dcgettext(0,
                                  "Echo the STRING(s) to standard output.\n\n  -n             do not output the trailing newline\n"
                                  ,5);
      fputs_unlocked(pcVar10,pFVar3);
      pFVar3 = *(FILE **)puVar6;
      pcVar10 = (char *)dcgettext(0,
                                  "  -e             enable interpretation of backslash escapes\n  -E             disable interpretation of backslash escapes (default)\n"
                                  ,5);
      fputs_unlocked(pcVar10,pFVar3);
      pFVar3 = *(FILE **)puVar6;
      pcVar10 = (char *)dcgettext(0,"      --help        display this help and exit\n",5);
      fputs_unlocked(pcVar10,pFVar3);
      pFVar3 = *(FILE **)puVar6;
      pcVar10 = (char *)dcgettext(0,"      --version     output version information and exit\n",5);
      fputs_unlocked(pcVar10,pFVar3);
      pFVar3 = *(FILE **)puVar6;
      pcVar10 = (char *)dcgettext(0,
                                  "\nIf -e is in effect, the following sequences are recognized:\n\n"
                                  ,5);
      fputs_unlocked(pcVar10,pFVar3);
      pFVar3 = *(FILE **)puVar6;
      pcVar10 = (char *)dcgettext(0,
                                  "  \\\\      backslash\n  \\a      alert (BEL)\n  \\b      backspace\n  \\c      produce no further output\n  \\e      escape\n  \\f      form feed\n  \\n      new line\n  \\r      carriage return\n  \\t      horizontal tab\n  \\v      vertical tab\n"
                                  ,5);
      fputs_unlocked(pcVar10,pFVar3);
      pFVar3 = *(FILE **)puVar6;
      pcVar10 = (char *)dcgettext(0,
                                  "  \\0NNN   byte with octal value NNN (1 to 3 digits)\n  \\xHH    byte with hexadecimal value HH (1 to 2 digits)\n"
                                  ,5);
      fputs_unlocked(pcVar10,pFVar3);
      uVar15 = dcgettext(0,
                         "\nNOTE: your shell may have its own version of %s, which usually supersedes\nthe version described here.  Please refer to your shell\'s documentation\nfor details about the options it supports.\n"
                         ,5);
      __printf_chk(2,uVar15,&DAT_001065cc);
      pFVar3 = *(FILE **)puVar6;
      pcVar10 = (char *)dcgettext(0,
                                  "\nNOTE: printf(1) is a preferred alternative,\nwhich does not have issues outputting option-like strings.\n"
                                  ,5);
      ppcVar26 = local_b8;
      fputs_unlocked(pcVar10,pFVar3);
      local_b8[0] = "[";
      local_b8[1] = "test invocation";
      local_b8[2] = PTR_s_coreutils_00108c88;
      local_b8[3] = "Multi-call invocation";
      local_b8[4] = "sha224sum";
      pcStack_90 = "sha2 utilities";
      local_88 = "sha256sum";
      pcStack_80 = "sha2 utilities";
      local_78 = "sha384sum";
      pcStack_70 = "sha2 utilities";
      local_68 = "sha512sum";
      pcStack_60 = "sha2 utilities";
      local_58 = (undefined1  [16])0x0;
      while ((*ppcVar26 != (char *)0x0 && (iVar8 = strcmp("echo",*ppcVar26), iVar8 != 0))) {
        ppcVar26 = ppcVar26 + 2;
      }
      pcVar10 = ppcVar26[1];
      if (pcVar10 == (char *)0x0) {
        uVar15 = dcgettext(0,"\n%s online help: <%s>\n",5);
        pcVar10 = "echo";
        __printf_chk(2,uVar15,"GNU coreutils","https://www.gnu.org/software/coreutils/");
        pcVar17 = setlocale(5,(char *)0x0);
        if (pcVar17 != (char *)0x0) goto LAB_00102eea;
        uVar15 = dcgettext(0,"Full documentation <%s%s>\n",5);
        __printf_chk(2,uVar15,"https://www.gnu.org/software/coreutils/",&DAT_001065cc);
      }
      else {
        uVar15 = dcgettext(0,"\n%s online help: <%s>\n",5);
        __printf_chk(2,uVar15,"GNU coreutils","https://www.gnu.org/software/coreutils/");
        pcVar17 = setlocale(5,(char *)0x0);
        if (pcVar17 != (char *)0x0) {
LAB_00102eea:
          iVar8 = strncmp(pcVar17,"en_",3);
          if (iVar8 != 0) {
            pFVar3 = *(FILE **)puVar6;
            pcVar17 = (char *)dcgettext(0,
                                        "Report any translation bugs to <https://translationproject.org/team/>\n"
                                        ,5);
            fputs_unlocked(pcVar17,pFVar3);
          }
        }
        uVar15 = dcgettext(0,"Full documentation <%s%s>\n",5);
        pcVar17 = "";
        __printf_chk(2,uVar15,"https://www.gnu.org/software/coreutils/",&DAT_001065cc);
        if (pcVar10 != "echo") goto LAB_00102f3e;
      }
      pcVar10 = "echo";
      pcVar17 = " invocation";
LAB_00102f3e:
      uVar15 = dcgettext(0,"or available locally via: info \'(coreutils) %s%s\'\n",5);
      __printf_chk(2,uVar15,pcVar10,pcVar17);
                    /* WARNING: Subroutine does not return */
      exit(0);
    }
    iVar8 = strcmp(pcVar11,"--version");
    if (iVar8 == 0) {
      uVar15 = FUN_00103290("Chet Ramey","Chet Ramey");
      uVar16 = FUN_00103290("Brian Fox","Brian Fox");
      FUN_00104f80(*(undefined8 *)PTR_stdout_00108fc8,&DAT_001065cc,"GNU coreutils",&DAT_00106710,
                   uVar16,uVar15,0,uVar16);
      goto switchD_001026e9_caseD_63;
    }
    uVar24 = 1;
    if (uVar21 != 0) goto LAB_00102709;
LAB_0010264a:
    plVar25 = param_2 + 1;
    bVar4 = true;
    if (pcVar10 == (char *)0x0) {
LAB_00102a8a:
      if (0 < (int)uVar24) {
LAB_00102a93:
        puVar6 = PTR_stdout_00108fc8;
        plVar1 = plVar25 + uVar24;
        while( true ) {
          pcVar10 = (char *)*plVar25;
          plVar25 = plVar25 + 1;
          fputs_unlocked(pcVar10,*(FILE **)puVar6);
          if (plVar25 == plVar1) break;
          p_Var23 = *(_IO_FILE **)puVar6;
          pcVar10 = p_Var23->_IO_write_ptr;
          if (pcVar10 < p_Var23->_IO_write_end) {
            p_Var23->_IO_write_ptr = pcVar10 + 1;
            *pcVar10 = ' ';
          }
          else {
            __overflow(p_Var23,0x20);
          }
        }
      }
    }
    else {
LAB_00102659:
      if (0 < (int)uVar24) {
LAB_00102662:
        plVar1 = plVar25 + uVar24;
        do {
          pbVar13 = (byte *)*plVar25;
LAB_001026a9:
          bVar18 = *pbVar13;
          pbVar12 = pbVar13;
          if (bVar18 != 0) {
            do {
              uVar21 = (uint)bVar18;
              pbVar13 = pbVar12 + 1;
              plVar19 = (long *)PTR_stdout_00108fc8;
              if (bVar18 != 0x5c) goto LAB_0010268e;
              bVar2 = pbVar12[1];
              if (bVar2 == 0) {
                uVar21 = 0x5c;
                p_Var23 = *(_IO_FILE **)PTR_stdout_00108fc8;
                pbVar12 = (byte *)p_Var23->_IO_write_ptr;
                if (pbVar12 < p_Var23->_IO_write_end) goto LAB_0010269f;
              }
              else {
                pbVar13 = pbVar12 + 2;
                switch(bVar2) {
                case 0x30:
                  bVar2 = pbVar12[2];
                  if ((byte)(bVar2 - 0x30) < 8) {
                    pbVar13 = pbVar12 + 3;
                    goto switchD_001026e9_caseD_31;
                  }
                  uVar21 = 0;
                  bVar18 = 0;
                  break;
                case 0x31:
                case 0x32:
                case 0x33:
                case 0x34:
                case 0x35:
                case 0x36:
                case 0x37:
switchD_001026e9_caseD_31:
                  bVar18 = bVar2 - 0x30;
                  if ((byte)(*pbVar13 - 0x30) < 8) {
                    bVar18 = (*pbVar13 - 0x30) + bVar18 * '\b';
                    if ((byte)(pbVar13[1] - 0x30) < 8) {
                      bVar18 = (pbVar13[1] - 0x30) + bVar18 * '\b';
                      pbVar13 = pbVar13 + 2;
                      uVar21 = (uint)bVar18;
                    }
                    else {
                      pbVar13 = pbVar13 + 1;
                      uVar21 = (uint)bVar18;
                    }
                  }
                  else {
                    uVar21 = (uint)bVar18;
                  }
                  break;
                default:
switchD_001026e9_caseD_38:
                  plVar19 = (long *)PTR_stdout_00108fc8;
                  uVar21 = (uint)bVar2;
                  p_Var23 = *(_IO_FILE **)PTR_stdout_00108fc8;
                  pcVar10 = p_Var23->_IO_write_ptr;
                  bVar18 = bVar2;
                  if (pcVar10 < p_Var23->_IO_write_end) {
                    p_Var23->_IO_write_ptr = pcVar10 + 1;
                    *pcVar10 = '\\';
                  }
                  else {
                    __overflow(p_Var23,0x5c);
                  }
                  break;
                case 0x5c:
                  uVar21 = 0x5c;
                  break;
                case 0x61:
                  uVar21 = 7;
                  bVar18 = 7;
                  break;
                case 0x62:
                  uVar21 = 8;
                  bVar18 = 8;
                  break;
                case 99:
                  goto switchD_001026e9_caseD_63;
                case 0x65:
                  uVar21 = 0x1b;
                  bVar18 = 0x1b;
                  break;
                case 0x66:
                  uVar21 = 0xc;
                  bVar18 = 0xc;
                  break;
                case 0x6e:
                  uVar21 = 10;
                  bVar18 = 10;
                  break;
                case 0x72:
                  uVar21 = 0xd;
                  bVar18 = 0xd;
                  break;
                case 0x74:
                  uVar21 = 9;
                  bVar18 = 9;
                  break;
                case 0x76:
                  uVar21 = 0xb;
                  bVar18 = 0xb;
                  break;
                case 0x78:
                  bVar18 = pbVar12[2];
                  ppuVar14 = __ctype_b_loc();
                  puVar22 = *ppuVar14;
                  if ((*(byte *)((long)puVar22 + (ulong)bVar18 * 2 + 1) & 0x10) == 0)
                  goto switchD_001026e9_caseD_38;
                  uVar24 = FUN_00103100(bVar18);
                  if ((*(byte *)((long)puVar22 + (ulong)pbVar12[3] * 2 + 1) & 0x10) == 0) {
                    pbVar13 = pbVar12 + 3;
                    uVar21 = uVar24 & 0xff;
                    plVar19 = (long *)PTR_stdout_00108fc8;
                    bVar18 = (byte)uVar24;
                  }
                  else {
                    pbVar13 = pbVar12 + 4;
                    iVar8 = FUN_00103100((ulong)pbVar12[3]);
                    uVar24 = uVar24 * 0x10 + iVar8;
                    uVar21 = uVar24 & 0xff;
                    plVar19 = (long *)PTR_stdout_00108fc8;
                    bVar18 = (byte)uVar24;
                  }
                }
LAB_0010268e:
                p_Var23 = (_IO_FILE *)*plVar19;
                pbVar12 = (byte *)p_Var23->_IO_write_ptr;
                if (pbVar12 < p_Var23->_IO_write_end) goto LAB_0010269f;
              }
              __overflow(p_Var23,uVar21);
              bVar18 = *pbVar13;
              pbVar12 = pbVar13;
              if (bVar18 == 0) break;
            } while( true );
          }
          plVar25 = plVar25 + 1;
          if (plVar25 == plVar1) break;
          p_Var23 = *(_IO_FILE **)PTR_stdout_00108fc8;
          pcVar10 = p_Var23->_IO_write_ptr;
          if (pcVar10 < p_Var23->_IO_write_end) {
            p_Var23->_IO_write_ptr = pcVar10 + 1;
            *pcVar10 = ' ';
          }
          else {
            __overflow(p_Var23,0x20);
          }
        } while( true );
      }
    }
LAB_001027bd:
    if (!bVar4) goto switchD_001026e9_caseD_63;
  }
  else {
    uVar24 = param_1 - 1;
    if (uVar21 == 0) goto LAB_0010264a;
    uVar21 = uVar24;
    if (0 < (int)uVar24) {
LAB_00102709:
      uVar24 = uVar21;
      plVar25 = param_2 + 1;
      bVar4 = true;
      bVar5 = false;
      do {
        pcVar17 = (char *)*plVar25;
        if ((*pcVar17 != '-') || (uVar21 = (uint)(byte)pcVar17[1], pcVar17[1] == 0)) {
          if ((pcVar10 != (char *)0x0) || (bVar5)) goto LAB_00102659;
          goto LAB_00102a93;
        }
        pbVar13 = (byte *)(pcVar17 + 2);
        uVar9 = uVar21;
        do {
          if ((0x29 < (byte)(uVar9 - 0x45)) ||
             (bVar27 = (0x20100000001U >> ((ulong)(uVar9 - 0x45) & 0x3f) & 1) != 0, !bVar27)) {
            if ((pcVar10 != (char *)0x0) || (bVar5)) goto LAB_00102662;
            goto LAB_00102a8a;
          }
          bVar18 = *pbVar13;
          uVar9 = (uint)bVar18;
          pbVar13 = pbVar13 + 1;
        } while (bVar18 != 0);
        pbVar13 = (byte *)(pcVar17 + 1);
        do {
          while( true ) {
            pbVar13 = pbVar13 + 1;
            cVar20 = (char)uVar21;
            bVar7 = bVar27;
            if (cVar20 != 'e') break;
LAB_00102788:
            bVar5 = bVar7;
            uVar21 = (uint)*pbVar13;
            if (*pbVar13 == 0) goto LAB_001027af;
          }
          if (cVar20 != 'n') {
            bVar7 = bVar5;
            if (cVar20 == 'E') {
              bVar7 = false;
            }
            goto LAB_00102788;
          }
          uVar21 = (uint)*pbVar13;
          bVar4 = false;
        } while (*pbVar13 != 0);
LAB_001027af:
        plVar25 = plVar25 + 1;
        uVar24 = uVar24 - 1;
      } while (uVar24 != 0);
      goto LAB_001027bd;
    }
  }
  p_Var23 = *(_IO_FILE **)PTR_stdout_00108fc8;
  pcVar10 = p_Var23->_IO_write_ptr;
  if (pcVar10 < p_Var23->_IO_write_end) {
    p_Var23->_IO_write_ptr = pcVar10 + 1;
    *pcVar10 = '\n';
  }
  else {
    __overflow(p_Var23,10);
  }
switchD_001026e9_caseD_63:
  if (local_40 == *(long *)(in_FS_OFFSET + 0x28)) {
    return 0;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
LAB_0010269f:
  p_Var23->_IO_write_ptr = (char *)(pbVar12 + 1);
  *pbVar12 = bVar18;
  goto LAB_001026a9;
}

