#include <stdio.h>
#include <stdlib.h>

int lenString(char* pChar);
int max2int(int n1, int n2);
int maxInt(int n1, int n2, int n3, int n4);
void copyStr(char* source, char* target);
char** createMenu(int nbLines,
		  int* chars,
		  char* menuTitle,
		  char* option1,
		  char* option2,
		  char* option3);
void dispMenu(char** menu, int nbLines);
void launchTerminal();
void git4macOSandUnix();
void SSH4macOSandUnix();
  
int main()
{

  printf("Program starting...\n");
  char menuTitle[] = "What do you want to do?";
  int lenTitle = lenString(menuTitle);
  //printf("%s\t%d characters\n", menuTitle, lenTitle);
  
  char option1[] = "1) How to launch a terminal?";
  int lenOpt1 = lenString(option1);
  //printf("%s\t%d characters\n", option1, lenOpt1);
  
  char option2[] = "2) How to set up git on macOS or Unix?";
  int lenOpt2 = lenString(option2);
  //printf("%s\t%d characters\n", option2, lenOpt2);
  
  char option3[] = "3) How to set up SSH connection to GitHub?";
  int lenOpt3 = lenString(option3);
  //printf("%s\t%d characters\n", option3, lenOpt3);  

  int maxLen = maxInt(lenTitle, lenOpt1, lenOpt2, lenOpt3);
  int menuLengths[] = {lenTitle, lenOpt1, lenOpt2, lenOpt3};
  printf("MaxLen = %d\n", maxLen);

  char** menu = createMenu(4,
			   menuLengths,
			   menuTitle,
			   option1,
			   option2,
			   option3);
  
  int choice = 0;
  while (choice != 1 && choice != 2 && choice != 3)
  {
    dispMenu(menu, 4);
    printf("Your choice: ");
    scanf("%d", &choice);
    switch(choice)
    {
      case 1:
	launchTerminal();
	break;
      case 2:
	git4macOSandUnix();
	break;
      case 3:
	SSH4macOSandUnix();
	break;
      default:
	printf("Wrong choice choose a number between 1 and 3\n");
	break;
    }
    printf("Something else? \n1) No\t 0) Yes\nYour choice: ");
    scanf("%d", &choice);
  }

  
  return 0;
}

int lenString(char* pChar)
{
  int i = 0;
  while( *(pChar + i) != '\0' ) i++;
  return i;
}

int max2int(int n1, int n2)
{
  if (n1 > n2) return n1;
  else return n2;
}
  
int maxInt(int n1, int n2, int n3, int n4)
{
  int m1 = max2int(n1, n2);
  int m2 = max2int(n3, n4);
  int M = max2int(m1, m2);
  return M;
}

void copyStr(char* source, char* target)
{
  int index = 0;
  while ( *(source + index) != '\0' )
  {
    *(target + index) = *(source + index);
    index++;
  }
}

char** createMenu(int nbLines,
		  int* chars,
		  char* menuTitle,
		  char* option1,
		  char* option2,
		  char* option3)
{
  char** menu;
  menu = malloc( sizeof(*menu) * nbLines );
  if ( menu )
  {
    for (size_t r = 0; r < nbLines; r++)
    {
      menu[r] = malloc( sizeof (*menu[r]) * chars[r] );
    }
  }
  
  copyStr(menuTitle,  *menu);
  copyStr(option1,  *(menu + 1) );
  copyStr(option2,  *(menu + 2) );
  copyStr(option3, *(menu + 3) );
  
  return menu;  
}

void dispMenu(char** menu, int nbLines)
{
  for (int i = 0; i < nbLines; i++) printf("%s\n", *(menu + i));
}

void launchTerminal()
{
  getchar();
  char step1[] = "Step 1: Open a terminal (command line)";
  printf("%s\n", step1);
  getchar();
  printf("Step 2: Type cd ~ \n");
  getchar();
  char step3[] = "Step 3: Check your location:";
  char pwd[] = "with pwd (Print Working Directory)"; 
  printf("%s\n\tType: \"%s\"", step3, pwd);
  getchar();
}

void git4macOSandUnix()
{
  printf("\nLaunching Terminal Instructions...\n\n");
  launchTerminal(); /* Steps 1 to 3 */
  
  printf("\nGit Configuration...\n\n");
  char checkGitVersion[] = "Step 4: Check your git version";
  printf("%s\n\tType: \"git --version\"\n", checkGitVersion);
  
  printf("\nIs your version greater or equal than 2.32? \n0) No\t1) Yes : ");
  int version = 0;
  scanf("%d", &version);
  if (version != 1) printf("Go visit https://git-scm.com/\n");

  getchar();
  printf("\n");
  
  char gitConfigUser[] = "git config --global user.";
  
  char setupName[] = "Step 5: Set up your name";
  char configName[] = "name \"your_name\"";
  printf("%s\n\t%s%s\n", setupName, gitConfigUser, configName);
  getchar();

  char setupEmail[] = "Step 6: Set up your email";
  char configEmail[] = "email \"your@email.com\"";
  printf("%s\n\t%s%s\n", setupEmail, gitConfigUser, configEmail);
  getchar();

  char checkName[] = "Step 7: Check your name" ;
  printf("%s\n\t%sname\n", checkName, gitConfigUser);
  getchar();
  char checkEmail[] = "Step 8: Check your email\n";
  printf("%s\n\t%semail\n", checkEmail, gitConfigUser);
  getchar();

  char configDone[] = "Minimal Git configuration done!";
  printf("\n%s\n", configDone);
}

void SSH4macOSandUnix()
{
  launchTerminal(); /* Steps 1 to 3 */
  
  char makeSSHDir[] = "Step 4: Create a .ssh directory";
  printf("%s\n\tType: \"mkdir .ssh\"\n", makeSSHDir);
  getchar();
  
  char moveIntoDir[] = "Step 5: Move into your new .ssh directory";
  printf("%s\n\tType: \"cd .ssh\"\n", moveIntoDir);
  getchar();
  
  char createSSHkey[] = "Step 6: Create SSH key pair";
  char SSHkeygen[] = "ssh-keygen -t rsa -C";
  printf("%s\n\tType: %s \"your@email.com\"\n",
	 createSSHkey, SSHkeygen);
  getchar();
  
  char defaultLoc[] = "Use default location";
  char hackerConfig[] = "unless you want to dig into hacker's config";
  printf("%s...\n\t...%s...\n", defaultLoc, hackerConfig);
  getchar();
  
  char passPhrase[] = "Step 7: Be sure to save your passprhase";
  printf("%s!\n", passPhrase);
  getchar();
  
  char addKey2SSH[] = "Step 8: Add your key to the SSH agent";
  char sshAdd[] = "ssh-add --apple-use-keychain ~/.ssh/id_rsa";
  printf("%s\n\tType: %s\n", addKey2SSH, sshAdd);
  getchar();
  
  char copyFromTerm[] = "Step 9: You need to copy the key from the Terminal";
  char pbcopy[] = "pbcopy < ~/.ssh/id_rsa.pub";
  printf("%s\n\tType: %s\n", copyFromTerm, pbcopy);
  getchar();
  
  char GitHubSettings[] = "Step 10: Go to GitHub and click \"Settings\"";
  printf("%s\n", GitHubSettings);
  getchar();
  
  printf("Step 11: On the left sidebar click SSH and GPG keys\n");
  getchar();

  printf("Step 12: In the top right corner, click New SSH Key\n");
  getchar();

  printf("Step 13: Name your key (\"CPGE Computer\" for instance\n");
  getchar();

  char keySection[] = "Step 14: In the key section, paste the key ";
  printf("%syou copied in step 9\n", keySection);
  getchar();

  char back2Term[] = "Step 15: Go back to the command line";
  char sshT[] = "ssh -T git@github.com";
  char ensureConnection[] = "to ensure your computer is connected";
  printf("%s\n\tType: \"%s\" \n\t%s to GitHub\n",
	 back2Term, sshT, ensureConnection);
  getchar();

  printf("Step 16: Ignore the message and type \"yes\"\n");
}
