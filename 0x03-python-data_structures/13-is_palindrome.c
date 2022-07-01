#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a no is a palindrome
 * @head: ptr to linked list
 *
 * Return: 1 is palindrome, 0 is not one
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int pallist[2048];
	int i = 0, j = 0;

	if (head || (*head))
	{
		while (tmp)
		{
			pallist[i] = tmp->n;
			tmp = tmp->next;
			i++;
		}
		i--;
		for (; j <= i; i--, j++)
		{
			if (pallist[i] != pallist[j])
				return (0);
		}
	}
	return (1);
}
