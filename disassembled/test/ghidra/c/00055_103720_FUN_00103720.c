
ulong FUN_00103720(undefined1 *param_1,ulong param_2,char *param_3,int param_4,uint param_5,
                  long param_6,char *param_7,char *param_8)

{
  byte *pbVar1;
  bool bVar2;
  bool bVar3;
  bool bVar4;
  bool bVar5;
  bool bVar6;
  bool bVar7;
  bool bVar8;
  char cVar9;
  int iVar10;
  int iVar11;
  size_t sVar12;
  ushort **ppuVar13;
  ulong uVar14;
  ulong uVar15;
  long lVar16;
  byte *pbVar17;
  uint uVar18;
  ulong uVar19;
  byte bVar20;
  ulong uVar21;
  uint *puVar22;
  ulong uVar23;
  long in_FS_OFFSET;
  bool bVar24;
  bool bVar25;
  bool bVar26;
  bool bVar27;
  bool bVar28;
  bool bVar29;
  ulong local_d0;
  uint local_c4;
  char *local_c0;
  long local_88;
  ulong local_80;
  bool local_68;
  int local_64;
  ulong local_60;
  wint_t local_4c;
  mbstate_t local_48;
  long local_40;
  
  uVar23 = 0xffffffffffffffff;
  local_40 = *(long *)(in_FS_OFFSET + 0x28);
  local_c4 = param_5;
  local_88 = param_6;
  local_64 = param_4;
LAB_00103770:
  sVar12 = __ctype_get_mb_cur_max();
  uVar18 = local_c4 & 2;
  bVar25 = uVar18 != 0;
  switch(local_64) {
  case 0:
    bVar8 = true;
    local_68 = false;
    bVar5 = false;
    local_d0 = 0;
    bVar25 = false;
    bVar6 = false;
    local_80 = 0;
    local_c0 = (char *)0x0;
    local_60 = 0;
    break;
  case 1:
    goto LAB_00104015;
  case 2:
    bVar5 = false;
    bVar8 = true;
    uVar21 = 0;
    local_68 = false;
    bVar6 = false;
    local_d0 = param_2;
    goto LAB_00104aa7;
  case 3:
    bVar6 = true;
    goto LAB_00104030;
  case 4:
    bVar8 = true;
    if (uVar18 == 0) {
      bVar5 = false;
      local_68 = false;
      local_d0 = 0;
      bVar6 = true;
      uVar19 = param_2;
      goto LAB_00103efc;
    }
LAB_00104015:
    bVar6 = false;
LAB_00104030:
    bVar8 = true;
    bVar25 = true;
    bVar5 = false;
    local_68 = false;
    local_d0 = 0;
    local_80 = 1;
    local_c0 = "\'";
    local_60 = 0;
    local_64 = 2;
    break;
  case 5:
    if (uVar18 == 0) {
      if (param_2 != 0) {
        *param_1 = 0x22;
      }
      bVar8 = true;
      local_68 = false;
      bVar5 = false;
      local_d0 = 0;
      bVar25 = false;
      bVar6 = true;
      local_80 = 1;
      local_c0 = "\"";
      local_60 = 1;
    }
    else {
      bVar8 = true;
      local_68 = false;
      bVar5 = false;
      local_d0 = 0;
      bVar25 = true;
      bVar6 = true;
      local_80 = 1;
      local_c0 = "\"";
      local_60 = 0;
    }
    break;
  case 6:
    bVar8 = true;
    local_68 = false;
    bVar5 = false;
    local_d0 = 0;
    bVar25 = true;
    bVar6 = true;
    local_80 = 1;
    local_c0 = "\"";
    local_60 = 0;
    local_64 = 5;
    break;
  case 7:
    bVar8 = true;
    local_68 = false;
    bVar5 = false;
    local_d0 = 0;
    bVar25 = false;
    bVar6 = true;
    local_80 = 0;
    local_c0 = (char *)0x0;
    local_60 = 0;
    break;
  case 8:
  case 9:
  case 10:
    if (local_64 != 10) {
      param_7 = (char *)dcgettext(0,&DAT_001065b0,5);
      if (param_7 == "`") {
        param_7 = (char *)FUN_00103350(&DAT_001065b0,local_64);
      }
      param_8 = (char *)dcgettext(0,&DAT_00106584,5);
      if (param_8 == "\'") {
        param_8 = (char *)FUN_00103350(&DAT_00106584,local_64);
      }
    }
    local_60 = 0;
    if ((uVar18 == 0) && (cVar9 = *param_7, cVar9 != '\0')) {
      local_60 = 0;
      do {
        if (local_60 < param_2) {
          param_1[local_60] = cVar9;
        }
        local_60 = local_60 + 1;
        cVar9 = param_7[local_60];
      } while (cVar9 != '\0');
    }
    local_80 = strlen(param_8);
    bVar8 = true;
    local_68 = false;
    bVar5 = false;
    local_d0 = 0;
    bVar6 = true;
    local_c0 = param_8;
    break;
  default:
                    /* WARNING: Subroutine does not return */
    abort();
  }
LAB_00103888:
  uVar19 = 0;
  bVar2 = local_68;
LAB_00103890:
  bVar26 = uVar19 != uVar23;
  if (uVar23 == 0xffffffffffffffff) {
    bVar26 = param_3[uVar19] != '\0';
  }
  bVar28 = bVar6;
  if (!bVar26) goto LAB_00104769;
  bVar7 = (bool)(local_64 != 2 & bVar6);
  pbVar1 = (byte *)(param_3 + uVar19);
  bVar24 = (bool)(local_80 != 0 & bVar7);
  iVar11 = local_64;
  bVar29 = bVar5;
  bVar3 = bVar24;
  if (bVar24) {
    if ((uVar23 == 0xffffffffffffffff) && (1 < local_80)) {
      uVar23 = strlen(param_3);
    }
    if ((uVar23 < local_80 + uVar19) || (iVar10 = memcmp(pbVar1,local_c0,local_80), iVar10 != 0)) {
      bVar20 = *pbVar1;
      uVar21 = (ulong)bVar20;
      if ('?' < (char)bVar20) {
        if ('z' < (char)bVar20) {
          if (bVar20 == 0x7d) {
            bVar24 = false;
          }
          else {
            if ('}' < (char)bVar20) {
              bVar3 = false;
              if (bVar20 == 0x7e) goto LAB_00104c19;
              bVar24 = false;
              bVar20 = 0x7f;
              goto switchD_0010390d_caseD_1;
            }
            bVar24 = false;
            if (bVar20 != 0x7b) {
              uVar21 = 0x7c;
              goto switchD_0010419a_caseD_21;
            }
          }
          goto LAB_0010450e;
        }
        if (bVar20 != 0x40) {
          uVar14 = 1L << (bVar20 + 0xbf & 0x3f);
          if ((uVar14 & 0x3ffffff53ffffff) != 0) {
            bVar3 = false;
            goto LAB_00103941;
          }
          if ((uVar14 & 0xa4000000) == 0) goto LAB_0010456d;
          goto switchD_001042f2_caseD_21;
        }
switchD_001042f2_caseD_1:
        bVar24 = false;
        goto switchD_0010390d_caseD_1;
      }
      switch(uVar21) {
      case 0:
        goto switchD_001042f2_caseD_0;
      default:
        goto switchD_001042f2_caseD_1;
      case 7:
        bVar27 = false;
        bVar4 = false;
        bVar20 = 0x61;
        break;
      case 8:
        bVar27 = false;
        bVar4 = false;
        bVar20 = 0x62;
        break;
      case 9:
        bVar27 = false;
        bVar24 = false;
        uVar21 = 9;
        bVar20 = 0x74;
        goto joined_r0x00103c8f;
      case 10:
        bVar27 = false;
        bVar24 = false;
        uVar21 = 10;
        bVar20 = 0x6e;
        goto joined_r0x00103c8f;
      case 0xb:
        bVar27 = false;
        bVar4 = false;
        bVar20 = 0x76;
        break;
      case 0xc:
        bVar27 = false;
        bVar4 = false;
        bVar20 = 0x66;
        break;
      case 0xd:
        bVar27 = false;
        bVar24 = false;
        uVar21 = 0xd;
        bVar20 = 0x72;
        goto joined_r0x00103c8f;
      case 0x20:
        uVar21 = 0x20;
        bVar20 = 0x20;
        bVar3 = false;
        if ((bool)(bVar7 | bVar25)) goto LAB_00103941;
        bVar28 = false;
        bVar4 = bVar24;
        goto LAB_00103a18;
      case 0x21:
      case 0x22:
      case 0x24:
      case 0x26:
      case 0x28:
      case 0x29:
      case 0x2a:
      case 0x3b:
      case 0x3c:
      case 0x3d:
      case 0x3e:
switchD_001042f2_caseD_21:
        bVar24 = false;
        goto switchD_0010419a_caseD_21;
      case 0x23:
        bVar24 = false;
        uVar21 = 0x23;
        goto LAB_00103e48;
      case 0x25:
      case 0x2b:
      case 0x2c:
      case 0x2d:
      case 0x2e:
      case 0x2f:
      case 0x30:
      case 0x31:
      case 0x32:
      case 0x33:
      case 0x34:
      case 0x35:
      case 0x36:
      case 0x37:
      case 0x38:
      case 0x39:
      case 0x3a:
        bVar3 = false;
        if ((bool)(bVar7 | bVar25)) goto LAB_00103941;
        bVar28 = false;
        bVar4 = bVar24;
        goto LAB_00103a18;
      case 0x27:
        uVar21 = 0x27;
        bVar20 = 0x27;
        bVar3 = false;
        bVar2 = bVar24;
        if ((bool)(bVar7 | bVar25)) goto LAB_00103941;
        bVar28 = false;
        bVar4 = bVar24;
        goto LAB_00103a18;
      case 0x3f:
        bVar3 = false;
        if (local_64 == 5) goto LAB_00103cd6;
        goto LAB_001043e0;
      }
      goto joined_r0x00103ca1;
    }
    if (!bVar25) {
      bVar20 = *pbVar1;
      uVar21 = (ulong)bVar20;
      if ('?' < (char)bVar20) {
        if ('z' < (char)bVar20) {
          if (bVar20 != 0x7d) {
            if ('}' < (char)bVar20) {
              if (bVar20 != 0x7e) goto LAB_0010459f;
LAB_00104c19:
              if (uVar19 == 0) {
                uVar21 = 0x7e;
                bVar20 = 0x7e;
                if (!(bool)(bVar7 | bVar25)) {
                  bVar28 = false;
                  bVar4 = bVar24;
                  goto LAB_00103a18;
                }
                goto LAB_00103941;
              }
              bVar4 = false;
              bVar26 = false;
              uVar21 = 0x7e;
              goto LAB_00103943;
            }
            if (bVar20 != 0x7b) {
              uVar21 = 0x7c;
              goto switchD_0010419a_caseD_21;
            }
          }
          goto LAB_0010450e;
        }
        if (bVar20 == 0x40) goto switchD_0010390d_caseD_1;
        uVar14 = 1L << (bVar20 + 0xbf & 0x3f);
        if ((uVar14 & 0x3ffffff53ffffff) != 0) goto LAB_00103941;
        if ((uVar14 & 0xa4000000) != 0) goto switchD_0010419a_caseD_21;
LAB_0010486d:
        if (!bVar6) goto switchD_0010419a_caseD_21;
        bVar4 = false;
        bVar20 = 0x5c;
        goto LAB_001039c0;
      }
      switch(uVar21) {
      case 0:
        goto LAB_001041e0;
      default:
        goto switchD_0010390d_caseD_1;
      case 7:
        bVar27 = false;
        bVar4 = false;
        bVar20 = 0x61;
        break;
      case 8:
        bVar27 = false;
        bVar4 = false;
        bVar20 = 0x62;
        break;
      case 9:
        bVar27 = false;
        uVar21 = 9;
        bVar20 = 0x74;
        goto joined_r0x00103c8f;
      case 10:
        bVar27 = false;
        uVar21 = 10;
        bVar20 = 0x6e;
        goto joined_r0x00103c8f;
      case 0xb:
        bVar27 = false;
        bVar4 = false;
        bVar20 = 0x76;
        break;
      case 0xc:
        bVar27 = false;
        bVar4 = false;
        bVar20 = 0x66;
        break;
      case 0xd:
        bVar27 = false;
        uVar21 = 0xd;
        bVar20 = 0x72;
        goto joined_r0x00103c8f;
      case 0x20:
        uVar21 = 0x20;
        bVar20 = 0x20;
        if (!bVar7) {
          bVar28 = false;
          bVar4 = bVar24;
          goto LAB_00103a18;
        }
        goto LAB_00103941;
      case 0x21:
      case 0x22:
      case 0x24:
      case 0x26:
      case 0x28:
      case 0x29:
      case 0x2a:
      case 0x3b:
      case 0x3c:
      case 0x3d:
      case 0x3e:
        goto switchD_0010419a_caseD_21;
      case 0x23:
        goto switchD_0010390d_caseD_23;
      case 0x25:
      case 0x2b:
      case 0x2c:
      case 0x2d:
      case 0x2e:
      case 0x2f:
      case 0x30:
      case 0x31:
      case 0x32:
      case 0x33:
      case 0x34:
      case 0x35:
      case 0x36:
      case 0x37:
      case 0x38:
      case 0x39:
      case 0x3a:
        if (bVar7) goto LAB_00103941;
        bVar28 = false;
        bVar4 = bVar24;
        goto LAB_00103a18;
      case 0x27:
        uVar21 = 0x27;
        bVar20 = 0x27;
        bVar2 = bVar24;
        if (bVar7) goto LAB_00103941;
        bVar28 = false;
        bVar4 = bVar24;
        goto LAB_00103a18;
      case 0x3f:
        goto switchD_0010419a_caseD_3f;
      }
      goto LAB_00103979;
    }
    goto LAB_00103c66;
  }
  bVar20 = *pbVar1;
  uVar21 = (ulong)bVar20;
  if ('?' < (char)bVar20) {
    if ('z' < (char)bVar20) {
      if (bVar20 != 0x7d) {
        if ((char)bVar20 < '~') {
          if (bVar20 != 0x7b) {
            bVar26 = false;
            uVar21 = 0x7c;
            goto LAB_00103c3b;
          }
          goto LAB_0010450e;
        }
        if (bVar20 == 0x7e) goto LAB_00103e48;
LAB_0010459f:
        bVar20 = 0x7f;
        goto joined_r0x001045a7;
      }
LAB_0010450e:
      if (uVar23 == 0xffffffffffffffff) {
        if (param_3[1] == '\0') goto LAB_00103e48;
      }
      else if (uVar23 == 1) {
LAB_00103e48:
        if (uVar19 == 0) goto LAB_00103c3b;
      }
      goto switchD_0010419a_caseD_21;
    }
    if (bVar20 == 0x40) goto switchD_0010390d_caseD_1;
    uVar14 = 1L << (bVar20 + 0xbf & 0x3f);
    if ((uVar14 & 0x3ffffff53ffffff) != 0) goto switchD_0010390d_caseD_25;
    if ((uVar14 & 0xa4000000) != 0) goto switchD_0010390d_caseD_21;
    if (local_64 == 2) {
      if (bVar25) goto LAB_00103c56;
    }
    else {
LAB_0010456d:
      bVar24 = (bool)(bVar6 & bVar25);
      if (!bVar24) goto LAB_0010486d;
      if (local_80 == 0) goto LAB_00103c66;
    }
    uVar19 = uVar19 + 1;
    bVar4 = false;
    bVar20 = 0x5c;
    goto LAB_00103a32;
  }
  switch(uVar21) {
  case 0:
    if (bVar6) {
switchD_001042f2_caseD_0:
      if (!bVar25) {
        bVar28 = (bool)(local_64 == 2 & (bVar5 ^ 1U));
        bVar24 = bVar28;
        if (bVar28) {
          if (local_60 < param_2) {
            param_1[local_60] = 0x27;
          }
          if (local_60 + 1 < param_2) {
            param_1[local_60 + 1] = 0x24;
          }
          if (local_60 + 2 < param_2) {
            param_1[local_60 + 2] = 0x27;
          }
          uVar21 = local_60 + 3;
          local_60 = local_60 + 4;
          bVar29 = bVar28;
          if (uVar21 < param_2) {
            param_1[uVar21] = 0x5c;
            bVar26 = false;
            bVar20 = 0x30;
          }
          else {
            bVar26 = false;
            bVar20 = 0x30;
          }
          goto LAB_00103a28;
        }
LAB_001041e0:
        uVar14 = local_60 + 1;
        if (local_60 < param_2) {
          param_1[local_60] = 0x5c;
        }
        bVar3 = bVar24;
        if (!bVar7) {
          bVar20 = 0x30;
          local_60 = uVar14;
          bVar28 = bVar26;
          bVar4 = false;
          goto LAB_00103a18;
        }
        if ((uVar19 + 1 < uVar23) && ((byte)(param_3[uVar19 + 1] - 0x30U) < 10)) {
          if (uVar14 < param_2) {
            param_1[uVar14] = 0x30;
          }
          if (local_60 + 2 < param_2) {
            param_1[local_60 + 2] = 0x30;
          }
          uVar14 = local_60 + 3;
        }
        uVar21 = 0x30;
        bVar4 = false;
        local_60 = uVar14;
        goto LAB_00103943;
      }
      iVar11 = 4;
      if (local_64 != 2) {
        iVar11 = local_64;
      }
      goto LAB_00103c66;
    }
    if ((local_c4 & 1) == 0) {
      bVar24 = false;
      uVar21 = 0;
      bVar20 = 0;
      bVar3 = false;
      if ((bool)(bVar7 | bVar25)) goto LAB_00103941;
      bVar28 = false;
      bVar4 = bVar24;
      goto LAB_00103a18;
    }
    uVar19 = uVar19 + 1;
    goto LAB_00103890;
  default:
switchD_0010390d_caseD_1:
joined_r0x001045a7:
    if (sVar12 != 1) {
      local_48.__count = 0;
      local_48.__value = (_union_27)0x0;
      if (uVar23 == 0xffffffffffffffff) {
        uVar23 = strlen(param_3);
      }
      uVar14 = 0;
      bVar4 = bVar26;
LAB_0010466f:
      uVar21 = uVar19 + uVar14;
      pbVar1 = (byte *)(param_3 + uVar21);
      if (pbVar1 == (byte *)0x0) {
        puVar22 = (uint *)0x0;
        lVar16 = 1;
        pbVar17 = (byte *)0x106623;
        bVar3 = bVar26;
      }
      else {
        puVar22 = &local_4c;
        lVar16 = uVar23 - uVar21;
        pbVar17 = pbVar1;
        bVar3 = lVar16 != 0;
      }
      uVar15 = mbrtoc32(puVar22,pbVar17,lVar16,&local_48);
      if ((uVar15 < 0xfffffffffffffffe) || (!bVar3)) {
        if (uVar15 == 0) goto LAB_001048ed;
        if (uVar15 == 0xffffffffffffffff) goto LAB_00104753;
        if (uVar15 == 0xfffffffffffffffe) goto joined_r0x0010473a;
        if (uVar15 != 0xfffffffffffffffd) {
          if ((local_64 == 2) && (bVar25)) {
            if (uVar15 == 1) goto LAB_00104c7c;
            pbVar17 = (byte *)(param_3 + uVar21 + 1);
            do {
              if (((byte)(*pbVar17 - 0x5b) < 0x22) &&
                 ((0x20000002bU >> ((ulong)(*pbVar17 - 0x5b) & 0x3f) & 1) != 0)) {
                local_64 = 2;
                goto LAB_00103c56;
              }
              pbVar17 = pbVar17 + 1;
            } while (pbVar1 + uVar15 != pbVar17);
          }
          goto LAB_001048b7;
        }
LAB_001048ba:
        iVar11 = iswprint(local_4c);
        if (iVar11 == 0) {
          bVar4 = false;
        }
        iVar11 = mbsinit(&local_48);
        if (iVar11 != 0) goto LAB_001048ed;
        goto LAB_0010466f;
      }
      cVar9 = FUN_00103610();
      if (cVar9 == '\0') {
        if ((puVar22 == (uint *)0x0) || ((*puVar22 = (uint)*pbVar17, local_64 == 2 && (bVar25)))) {
LAB_00104c7c:
          uVar14 = uVar14 + 1;
        }
        else {
          uVar15 = 1;
LAB_001048b7:
          uVar14 = uVar14 + uVar15;
        }
        goto LAB_001048ba;
      }
      if (uVar15 != 0xffffffffffffffff) {
joined_r0x0010473a:
        while ((uVar21 < uVar23 && (param_3[uVar21] != '\0'))) {
          uVar14 = uVar14 + 1;
          uVar21 = uVar19 + uVar14;
        }
      }
LAB_00104753:
      bVar4 = false;
      bVar27 = bVar6;
      goto LAB_0010475a;
    }
    ppuVar13 = __ctype_b_loc();
    bVar26 = (*(byte *)((long)*ppuVar13 + (ulong)bVar20 * 2 + 1) & 0x40) == 0;
    uVar14 = 1;
    bVar27 = (bool)(bVar26 & bVar6);
    bVar26 = !bVar26;
    goto LAB_00103ad9;
  case 7:
    bVar27 = local_64 == 2;
    uVar21 = 7;
    bVar20 = 0x61;
    break;
  case 8:
    bVar27 = local_64 == 2;
    uVar21 = 8;
    bVar20 = 0x62;
    break;
  case 9:
    uVar21 = 9;
    bVar20 = 0x74;
    goto LAB_00103e6a;
  case 10:
    uVar21 = 10;
    bVar20 = 0x6e;
    goto LAB_00103e6a;
  case 0xb:
    bVar27 = local_64 == 2;
    uVar21 = 0xb;
    bVar20 = 0x76;
    break;
  case 0xc:
    bVar27 = local_64 == 2;
    uVar21 = 0xc;
    bVar20 = 0x66;
    break;
  case 0xd:
    uVar21 = 0xd;
    bVar20 = 0x72;
LAB_00103e6a:
    bVar27 = local_64 == 2;
    bVar24 = (bool)(bVar25 & bVar27);
    if (bVar24) goto LAB_00103c4f;
    break;
  case 0x20:
    uVar21 = 0x20;
    goto LAB_00103c3b;
  case 0x21:
  case 0x22:
  case 0x24:
  case 0x26:
  case 0x28:
  case 0x29:
  case 0x2a:
  case 0x3b:
  case 0x3c:
  case 0x3d:
  case 0x3e:
switchD_0010390d_caseD_21:
    bVar26 = false;
LAB_00103c3b:
    bVar3 = bVar24;
    if ((local_64 != 2) || (!bVar25)) goto switchD_0010390d_caseD_25;
    goto LAB_00103c4f;
  case 0x23:
switchD_0010390d_caseD_23:
    uVar21 = 0x23;
    goto LAB_00103e48;
  case 0x25:
  case 0x2b:
  case 0x2c:
  case 0x2d:
  case 0x2e:
  case 0x2f:
  case 0x30:
  case 0x31:
  case 0x32:
  case 0x33:
  case 0x34:
  case 0x35:
  case 0x36:
  case 0x37:
  case 0x38:
  case 0x39:
  case 0x3a:
    goto switchD_0010390d_caseD_25;
  case 0x27:
    uVar21 = 0x27;
    bVar2 = bVar26;
    if (local_64 != 2) goto switchD_0010390d_caseD_25;
    if (!bVar25) {
      if ((param_2 == 0) || (uVar21 = 0, uVar14 = param_2, local_d0 != 0)) {
        if (local_60 < param_2) {
          param_1[local_60] = 0x27;
        }
        if (local_60 + 1 < param_2) {
          param_1[local_60 + 1] = 0x5c;
        }
        uVar21 = param_2;
        uVar14 = local_d0;
        if (local_60 + 2 < param_2) {
          param_1[local_60 + 2] = 0x27;
        }
      }
      bVar28 = false;
      bVar20 = 0x27;
      local_60 = local_60 + 3;
      param_2 = uVar21;
      local_d0 = uVar14;
      bVar29 = false;
      goto LAB_00103a28;
    }
    goto LAB_00103c56;
  case 0x3f:
    if (local_64 == 2) {
      if (!bVar25) {
        bVar26 = false;
        bVar28 = false;
        bVar20 = 0x3f;
        goto LAB_00103a28;
      }
      goto LAB_00103c56;
    }
switchD_0010419a_caseD_3f:
    if (local_64 != 5) {
LAB_001043e0:
      bVar24 = false;
      uVar21 = 0x3f;
      bVar20 = 0x3f;
      if ((bool)(bVar7 | bVar25)) goto LAB_00103941;
      bVar28 = false;
      bVar4 = bVar24;
      goto LAB_00103a18;
    }
LAB_00103cd6:
    if ((local_c4 & 4) == 0) goto LAB_001043e0;
    uVar14 = uVar19 + 2;
    bVar26 = false;
    uVar21 = 0x3f;
    if ((uVar23 <= uVar14) || (param_3[uVar19 + 1] != '?')) goto switchD_0010390d_caseD_25;
    bVar20 = param_3[uVar14];
    uVar21 = (ulong)bVar20;
    bVar24 = bVar26;
    if ((bVar20 < 0x3f) && (bVar24 = (0x7000a38200000000U >> (uVar21 & 0x3f) & 1) != 0, bVar24)) {
      if (!bVar25) {
        if (local_60 < param_2) {
          param_1[local_60] = 0x3f;
        }
        if (local_60 + 1 < param_2) {
          param_1[local_60 + 1] = 0x22;
        }
        if (local_60 + 2 < param_2) {
          param_1[local_60 + 2] = 0x22;
        }
        if (local_60 + 3 < param_2) {
          param_1[local_60 + 3] = 0x3f;
        }
        local_60 = local_60 + 4;
        bVar24 = false;
        uVar19 = uVar14;
        if (bVar7) goto LAB_00103941;
        bVar28 = false;
        bVar4 = false;
        goto LAB_00103a18;
      }
      goto LAB_00103c66;
    }
    uVar21 = 0x3f;
    bVar20 = 0x3f;
    if ((bool)(bVar7 | bVar25)) goto LAB_00103941;
    bVar28 = false;
    bVar4 = bVar24;
    goto LAB_00103a18;
  }
joined_r0x00103c8f:
  if (!bVar6) {
switchD_0010419a_caseD_21:
    bVar26 = false;
    bVar3 = bVar24;
    goto switchD_0010390d_caseD_25;
  }
  bVar4 = false;
  goto joined_r0x00103ca1;
LAB_00104e28:
  local_64 = 5;
  param_2 = local_d0;
  goto LAB_00103770;
LAB_001048ed:
  bVar27 = (bool)((bVar4 ^ 1U) & bVar6);
LAB_0010475a:
  bVar26 = bVar4;
  if (1 < uVar14) {
LAB_00103ae8:
    uVar14 = uVar19 + uVar14;
    bVar26 = false;
    uVar21 = uVar19;
    do {
      if (bVar27) {
        bVar28 = local_64 == 2;
        if (bVar25) goto LAB_00103c56;
        bVar28 = (bool)(bVar28 & (bVar29 ^ 1U));
        if (bVar28) {
          if (local_60 < param_2) {
            param_1[local_60] = 0x27;
          }
          if (local_60 + 1 < param_2) {
            param_1[local_60 + 1] = 0x24;
          }
          if (local_60 + 2 < param_2) {
            param_1[local_60 + 2] = 0x27;
          }
          local_60 = local_60 + 3;
          bVar29 = bVar28;
        }
        if (local_60 < param_2) {
          param_1[local_60] = 0x5c;
        }
        if (local_60 + 1 < param_2) {
          param_1[local_60 + 1] = (bVar20 >> 6) + 0x30;
        }
        if (local_60 + 2 < param_2) {
          param_1[local_60 + 2] = (bVar20 >> 3 & 7) + 0x30;
        }
        uVar19 = uVar21 + 1;
        local_60 = local_60 + 3;
        bVar20 = (bVar20 & 7) + 0x30;
        bVar26 = bVar27;
        if (uVar14 <= uVar19) goto LAB_001039d7;
      }
      else {
        bVar5 = (bool)((bVar26 ^ 1U) & bVar29);
        if (bVar24) {
          if (local_60 < param_2) {
            param_1[local_60] = 0x5c;
          }
          local_60 = local_60 + 1;
        }
        uVar19 = uVar21 + 1;
        if (uVar14 <= uVar19) goto LAB_00103a32;
        if (bVar5) {
          if (local_60 < param_2) {
            param_1[local_60] = 0x27;
          }
          if (local_60 + 1 < param_2) {
            param_1[local_60 + 1] = 0x27;
          }
          local_60 = local_60 + 2;
          bVar24 = false;
          bVar29 = false;
        }
        else {
          bVar24 = false;
        }
      }
      uVar21 = uVar21 + 1;
      if (local_60 < param_2) {
        param_1[local_60] = bVar20;
      }
      bVar20 = param_3[uVar21];
      local_60 = local_60 + 1;
    } while( true );
  }
LAB_00103ad9:
  uVar21 = (ulong)bVar20;
  bVar3 = bVar24;
  if (bVar27) {
    bVar4 = false;
    bVar27 = bVar6;
    goto LAB_00103ae8;
  }
switchD_0010390d_caseD_25:
  bVar20 = (byte)uVar21;
  bVar28 = (bool)(bVar7 | bVar25);
  bVar4 = bVar26;
  bVar24 = bVar26;
  if ((bool)(bVar7 | bVar25)) {
LAB_00103941:
    bVar26 = false;
    bVar4 = bVar24;
LAB_00103943:
    bVar20 = (byte)uVar21;
    bVar28 = bVar26;
    if ((local_88 == 0) || ((*(uint *)(local_88 + (uVar21 >> 5) * 4) >> (bVar20 & 0x1f) & 1) == 0))
    goto LAB_00103a18;
    bVar27 = local_64 == 2;
  }
  else {
LAB_00103a18:
    bVar26 = bVar4;
    bVar27 = local_64 == 2;
    bVar4 = bVar26;
    if (!bVar3) {
LAB_00103a28:
      uVar19 = uVar19 + 1;
      bVar5 = (bool)((bVar28 ^ 1U) & bVar29);
      bVar4 = bVar26;
LAB_00103a32:
      if (bVar5) {
        if (local_60 < param_2) {
          param_1[local_60] = 0x27;
        }
        if (local_60 + 1 < param_2) {
          param_1[local_60 + 1] = 0x27;
        }
        local_60 = local_60 + 2;
        bVar29 = false;
      }
      goto LAB_001039d7;
    }
  }
joined_r0x00103ca1:
  if (bVar25) {
    bVar28 = (bool)(bVar6 & bVar27);
    goto LAB_00103c56;
  }
LAB_00103979:
  bVar27 = (bool)((bVar5 ^ 1U) & bVar27);
  if (bVar27) {
    if (local_60 < param_2) {
      param_1[local_60] = 0x27;
    }
    if (local_60 + 1 < param_2) {
      param_1[local_60 + 1] = 0x24;
    }
    if (local_60 + 2 < param_2) {
      param_1[local_60 + 2] = 0x27;
    }
    local_60 = local_60 + 3;
    bVar5 = bVar27;
  }
LAB_001039c0:
  if (local_60 < param_2) {
    param_1[local_60] = 0x5c;
  }
  local_60 = local_60 + 1;
  uVar19 = uVar19 + 1;
  bVar29 = bVar5;
LAB_001039d7:
  bVar5 = bVar29;
  if (local_60 < param_2) {
    param_1[local_60] = bVar20;
  }
  local_60 = local_60 + 1;
  if (!bVar4) {
    bVar8 = false;
  }
  goto LAB_00103890;
LAB_00104769:
  bVar26 = local_64 == 2;
  bVar29 = local_60 == 0;
  if (bVar29 && bVar26) {
    if (bVar25) {
LAB_00103c4f:
      local_64 = 2;
LAB_00103c56:
      iVar11 = 4;
      if (!bVar28) {
        iVar11 = local_64;
      }
LAB_00103c66:
      local_64 = iVar11;
      local_c4 = local_c4 & 0xfffffffd;
      local_88 = 0;
      goto LAB_00103770;
    }
    if (bVar2) {
      if (bVar8) goto LAB_00104e28;
      local_68 = local_d0 != 0 && param_2 == 0;
      uVar19 = local_d0;
      if (local_d0 != 0 && param_2 == 0) {
LAB_00103efc:
        if (uVar19 != 0) {
          *param_1 = 0x27;
        }
        bVar25 = false;
        local_80 = 1;
        local_c0 = "\'";
        local_60 = 1;
        local_64 = 2;
        param_2 = uVar19;
        goto LAB_00103888;
      }
      local_60 = 0;
      bVar25 = bVar2;
    }
    else {
      local_60 = 0;
      bVar25 = bVar29 && bVar26;
    }
  }
  else {
    bVar25 = (bool)(bVar25 ^ 1);
    if (((bool)(bVar26 & bVar25)) && (bVar25 = (bool)(bVar26 & bVar25), bVar2)) {
      if (bVar8) goto LAB_00104e28;
      local_68 = param_2 == 0 && local_d0 != 0;
      bVar25 = bVar2;
      if (param_2 == 0 && local_d0 != 0) {
        uVar21 = local_d0;
        bVar25 = bVar8;
        bVar8 = false;
LAB_00104aa7:
        local_64 = 2;
        local_60 = 0;
        local_c0 = "\'";
        local_80 = 1;
        uVar19 = local_d0;
        param_2 = local_d0;
        local_d0 = uVar21;
        if (bVar25) goto LAB_00103888;
        goto LAB_00103efc;
      }
    }
  }
  uVar23 = local_60;
  if (((local_c0 != (char *)0x0) && (bVar25)) && (cVar9 = *local_c0, cVar9 != '\0')) {
    do {
      if (uVar23 < param_2) {
        param_1[uVar23] = cVar9;
      }
      uVar23 = uVar23 + 1;
      cVar9 = local_c0[uVar23 - local_60];
    } while (cVar9 != '\0');
  }
  if (uVar23 < param_2) {
    param_1[uVar23] = 0;
  }
  if (local_40 == *(long *)(in_FS_OFFSET + 0x28)) {
    return uVar23;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

