  printf("Division:\t");
  printf("a / b = %d (WARNING! %%d impose int result)\n", a / b);
  printf("WARNING! %%f without float operands gives int\n");
  printf("a / b = %f (WARNING! multiply by 1.0 to get float)\n", a *1.0 / b);

  a = 5;
  b = 3;
  printf("(a, b) = (%d, %d)\n", a, b);

  printf("Modulus:\t");
  printf("a %% b = %d\n", a % b);
