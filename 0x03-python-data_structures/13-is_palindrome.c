#include "lists.h"

/**
 * count_node - counts the number of nodes in the linked list
 * @head: pointer to the head of the linked list
 * Return: returns the number of nodes
*/
int count_node(listint_t **head)
{
	int count = 0;
	listint_t *ptr;

	if (head == NULL)
		return (0);

	ptr = *head;
	while (ptr != NULL)
	{
		count++;
		ptr = ptr->next;
	}
	return (count);
}

/**
 * data_at_node - gets the data at a particular position in a linked list
 * @head: pointer to the head of the linked list
 * @pos: index of data to retrieve
 * Return: returns the data at the position
*/
int data_at_node(listint_t **head, int pos)
{
	listint_t *ptr = NULL;
	int count = 0;

	if (head == NULL)
		return (0);
	ptr = *head;
	while (ptr != NULL && count != pos - 1)
	{
		count++;
		ptr = ptr->next;
	}
	return (ptr->n);
}

/**
 * is_palindrome - function to check if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: returns 0 if it is not a palindrome or 1
*/
int is_palindrome(listint_t **head)
{
	int cnt = 0, i, j;

	cnt = count_node(head);

	for (i = 1, j = cnt; i < cnt; i++, j--)
	{
		if (data_at_node(head, i) != data_at_node(head, j))
			return (0);
	}
	return (1);
}
