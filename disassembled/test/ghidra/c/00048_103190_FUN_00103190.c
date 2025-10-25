
bool FUN_00103190(long param_1,long param_2,byte param_3,byte param_4)

{
  long lVar1;
  uint uVar2;
  uint uVar3;
  bool bVar4;
  
  if ((int)(char)param_3 - 0x41U < 0x1a) {
    if ((*(byte *)(param_1 + 7) & 0xdf) != param_3) {
      return false;
    }
  }
  else {
    if (param_3 != *(byte *)(param_1 + 7)) {
      return false;
    }
    if (param_3 == 0) {
      return true;
    }
  }
  if ((int)(char)param_4 - 0x41U < 0x1a) {
    if (param_4 != (*(byte *)(param_1 + 8) & 0xdf)) {
      return false;
    }
  }
  else {
    if (param_4 != *(byte *)(param_1 + 8)) {
      return false;
    }
    if (param_4 == 0) {
      return true;
    }
  }
  bVar4 = true;
  if (param_1 != param_2) {
    lVar1 = 9;
    do {
      uVar2 = (uint)*(byte *)(param_1 + lVar1);
      uVar3 = (uint)*(byte *)(param_2 + lVar1);
      if (uVar2 - 0x41 < 0x1a) {
        uVar2 = uVar2 + 0x20;
        if (uVar3 - 0x41 < 0x1a) {
          uVar3 = uVar3 + 0x20;
        }
      }
      else {
        if (uVar3 - 0x41 < 0x1a) {
          uVar3 = uVar3 + 0x20;
        }
        if (uVar2 == 0) break;
      }
      lVar1 = lVar1 + 1;
    } while ((char)uVar2 == (char)uVar3);
    bVar4 = uVar2 == uVar3;
  }
  return bVar4;
}

