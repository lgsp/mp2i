  int myInt = 2;
  float myFloat = 1.618;
  double myDouble = 1.4142135623;
  char myChar = 'A';

  printf("Use '%%lu', sizeof(myVar) to get the result\n");
  printf("myInt = %d\t\tsizeof(myInt) = %lu\n", myInt, sizeof(myInt));
  printf("myFloat = %f\tsizeof(myFloat) = %lu\n", myFloat, sizeof(myFloat));
  printf("myDouble = %lf\tsizeof(myDouble) = %lu\n", myDouble, sizeof(myDouble));
  printf("myChar = %c\t\tsizeof(myChar) = %lu\n", myChar, sizeof(myChar));
  printf("myChar = %d\t\tsizeof(myChar) = %lu\n", myChar, sizeof(myChar));
  return 0;
}
