
long FUN_00103290(long param_1,long param_2)

{
  long lVar1;
  char *pcVar2;
  byte bVar3;
  uint uVar4;
  uint uVar5;
  byte *pbVar6;
  
  lVar1 = dcgettext(0,param_1,5);
  if (param_1 == lVar1) {
    pcVar2 = nl_langinfo(0xe);
    if (((byte *)pcVar2 == (byte *)0x0) || (*pcVar2 == 0)) {
      pcVar2 = "ASCII";
    }
    else if (pcVar2 == &DAT_00106575) {
      return param_2;
    }
    pbVar6 = &DAT_00106575;
    do {
      bVar3 = *pcVar2;
      uVar5 = (uint)bVar3;
      uVar4 = (uint)*pbVar6;
      if (uVar5 - 0x41 < 0x1a) {
        uVar5 = uVar5 + 0x20;
        bVar3 = bVar3 + 0x20;
        if (uVar4 - 0x41 < 0x1a) {
          uVar4 = uVar4 + 0x20;
        }
      }
      else {
        if (uVar4 - 0x41 < 0x1a) {
          uVar4 = uVar4 + 0x20;
        }
        if (uVar5 == 0) break;
      }
      pcVar2 = (char *)((byte *)pcVar2 + 1);
      pbVar6 = pbVar6 + 1;
    } while (bVar3 == (byte)uVar4);
    if (uVar5 == uVar4) {
      lVar1 = param_2;
    }
  }
  return lVar1;
}

