#include "lists.h"

/**
 * reversed - reverses a singly linked list
 *
 * @head: pointer to the first node in list
 *
 * Return: pointer to the first node in the new list
 */

void reversed(listint_t **head)
{
	listint_t *prev = NULL, *prev = NULL, *current = *head;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 *  @head: pointer to a pointer to the first node in the list
 *
 * Return: 1 if true, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reversed(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
