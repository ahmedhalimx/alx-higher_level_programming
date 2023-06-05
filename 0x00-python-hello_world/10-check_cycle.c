#include "lists.h"

/**
 * check_cycle - checks if a singly linked list contains a cycle in it
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *nodePtr1 = list, *nodePtr2 = list;

	if (!list)
		return (0);

	while (nodePtr1 && nodePtr2 && nodePtr2->next)
	{
		nodePtr1 = nodePtr1->next;
		nodePtr2 = nodePtr2->next->next;
		if (nodePtr1 == nodePtr2)
			return (1);
	}

	return (0);
}
