#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check code
 *
 * Rreturn: always 0
 */
int main(void)
{
	listint_t *head;

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 1);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("linked list is a palindrome\n");
	else
	printf("linked list is not a palindrome\n");

	free_listint(head);

	return (0);
}
