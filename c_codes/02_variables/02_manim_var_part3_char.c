  char myChar = 'A';
  printf("\nCHAR: char\n");
  printf("Use '%%c, myChar' to print 'myChar' content ");
  printf("into a string.\n");

  printf("myChar = %c\n", myChar);

  printf("Use '%%d, myChar' to print 'myChar' numeric value ");
  printf("into a string.\n");

  printf("myChar = %d\t(ASCII code)\n", myChar);
  printf("Use arithmetic to change character\n");
  printf("myChar + 1 = %d (ASCII) => myChar + 1 = %c (char)\n",
	 myChar + 1, myChar + 1);

  return 0;
}
