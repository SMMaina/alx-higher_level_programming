#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @d: intger
 * @next: ptr to next node
 * Description: a singly linked list
 */
typedef struct listint_s
{
	int d;
	struct listint_s *next;
} listint;

size_t print_listint(const listint *h);
listint *add_nodeint(listint **head, const int n);
void free_listint(listint *head);
int check_cycle(listint *list);

#endif
