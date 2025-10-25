
void _FINI_0(void)

{
  if (DAT_00109018 == '\0') {
    if (PTR___cxa_finalize_00108ff0 != (undefined *)0x0) {
      __cxa_finalize(PTR_LOOP_00109008);
    }
    FUN_00103040();
    DAT_00109018 = 1;
    return;
  }
  return;
}

