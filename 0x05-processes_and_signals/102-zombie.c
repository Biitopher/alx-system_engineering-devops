#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - creating while loop
 * @void: nothing
 * Return: 0 on success
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates child process
 *
 * Return: 0 on success
 */

int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{

			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		else if (pid < 0)
		{

			perror("Fork error");
			exit(1);
		}
	}
	infinite_while();
	return (0);
}
